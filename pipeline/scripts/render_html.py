#!/usr/bin/env python3
"""Render translated text back into an HTML document.

Reads an extraction.json (XPath/tag mapping), a translated_merged.txt
(tag -> translated text), and the original HTML, then rebuilds HTML with
translated text inserted at the correct XPath positions.

Usage:
    python pipeline/scripts/render_html.py \
      --template source.html \
      --extraction extraction/extraction.json \
      --translation translation/translated_merged.txt \
      --output translated.html \
      --render-log render_log.json
"""

import argparse
import html as html_module
import json
import re
from html.parser import HTMLParser
from pathlib import Path

# Elements whose direct text content we translate.
TEXT_ELEMENTS = {
    'p', 'div', 'span', 'li',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'td', 'th', 'a', 'button', 'label',
    'textarea',
}

# Elements whose entire content should be preserved as-is.
SKIP_ELEMENTS = {
    'script', 'style', 'code', 'pre',
    'noscript', 'svg', 'math',
}

# Void / self-closing elements (no end tag in HTML).
SELF_CLOSING = {
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
    'link', 'meta', 'param', 'source', 'track', 'wbr',
}

# Pattern for translation file lines: [TAG] text
TAG_RE = re.compile(r'^\[([^\]]+)\]\s?(.*)$')

# Attributes that carry translatable text.
ATTR_TARGETS = {
    ('img', 'alt'),
    ('input', 'placeholder'),
    ('textarea', 'placeholder'),
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_translations(path):
    """Load translation file into {tag: translated_text} dict."""
    data = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            m = TAG_RE.match(line.rstrip('\n'))
            if m:
                data[m.group(1)] = m.group(2)
    return data


def build_lookups(extraction):
    """Build lookup dicts from extraction data.

    Returns:
        text_lookup: {xpath_with_text_suffix: tag} for TEXT_ELEMENT text nodes.
        attr_lookup: {xpath: {attr_name: tag}} for attribute replacements.
    """
    text_lookup = {}
    attr_lookup = {}
    for para in extraction.get('paragraphs', []):
        tag = para['tag']
        typ = para.get('type', 'body')
        loc = para.get('location', {})
        xpath = loc.get('xpath', '')
        if typ == 'attribute_text':
            attr = loc.get('attr', 'alt')
            if xpath not in attr_lookup:
                attr_lookup[xpath] = {}
            attr_lookup[xpath][attr] = tag
        else:
            # body text: xpath includes /text()[N] suffix
            text_lookup[xpath] = tag
    return text_lookup, attr_lookup


# ---------------------------------------------------------------------------
# HTML Renderer
# ---------------------------------------------------------------------------

class HTMLRenderer(HTMLParser):
    """SAX-style HTML parser that rebuilds HTML with translated text.

    Tracks XPath positions identically to HTMLTextExtractor so that text
    and attribute replacements can be matched to the correct locations.
    """

    def __init__(self, text_lookup, attr_lookup, translations):
        super().__init__(convert_charrefs=True)
        self.text_lookup = text_lookup
        self.attr_lookup = attr_lookup
        self.translations = translations

        # Stack of open elements.  Each entry:
        #   tag             -- element name
        #   full_xpath      -- e.g. "/html[1]/body[1]/p[2]"
        #   text_elem       -- True if in TEXT_ELEMENTS
        #   children        -- dict {tag_name: sibling_count}
        #   fragments       -- list of ('tag', str) or ('text', str)
        #   text_fragment   -- raw text accumulated since last emission
        #   text_index      -- how many /text()[N] entries emitted
        self.stack = []

        # Depth counter for SKIP_ELEMENTS regions.
        self.skip_depth = 0

        # Global output buffer (list of string parts).
        self.output = []

    # -- Internal helpers ---------------------------------------------------

    def _collecting_parent(self):
        """Return the nearest TEXT_ELEMENT ancestor, or None."""
        for elem in reversed(self.stack):
            if elem['text_elem']:
                return elem
        return None

    def _count_sibling(self, tag):
        """Increment sibling count for *tag* under the current parent."""
        if self.stack:
            parent = self.stack[-1]
            n = parent['children'].get(tag, 0) + 1
            parent['children'][tag] = n
            return n
        return 1

    def _push_element(self, tag, sibling_n=None):
        """Push a new open element onto the stack.

        Args:
            tag: Element name.
            sibling_n: Pre-computed sibling index (1-based).  If None,
                       _count_sibling is called automatically.
        """
        parent = self.stack[-1] if self.stack else None
        if parent:
            if sibling_n is not None:
                n = sibling_n
            else:
                n = self._count_sibling(tag)
            comp = f'{tag}[{n}]'
            full = f'{parent["full_xpath"]}/{comp}'
        else:
            comp = f'{tag}[1]'
            full = f'/{comp}'

        self.stack.append({
            'tag': tag,
            'full_xpath': full,
            'text_elem': tag in TEXT_ELEMENTS,
            'children': {},
            'fragments': [],
            'text_fragment': '',
            'text_index': 0,
        })

    def _build_opening_tag(self, tag, attrs):
        """Build an opening tag string, applying attribute translations.

        The caller MUST have already incremented the sibling count via
        _count_sibling so that parent['children'][tag] reflects the
        1-based index of this element.
        """
        parent = self.stack[-1] if self.stack else None
        if parent:
            n = parent['children'].get(tag, 1)
            xpath = f'{parent["full_xpath"]}/{tag}[{n}]'
        else:
            xpath = f'/{tag}[1]'

        attr_replacements = self.attr_lookup.get(xpath, {})

        parts = ['<', tag]
        for name, val in attrs:
            if name in attr_replacements:
                tag_key = attr_replacements[name]
                if tag_key in self.translations:
                    val = self.translations[tag_key]
            safe_val = val.replace('&', '&amp;').replace('"', '&quot;')
            parts.append(f' {name}="{safe_val}"')
        parts.append('>')
        return ''.join(parts)

    def _emit_text(self, elem):
        """Emit accumulated text of a TEXT_ELEMENT, checking for translations.

        This mirrors the extract's _emit_text: it always increments the text
        index (even for empty fragments) to stay in sync, checks for a
        translation match, and adds either the original or translated text
        to the element's fragments.
        """
        elem['text_index'] += 1
        raw = elem['text_fragment']
        elem['text_fragment'] = ''
        if not raw:
            return
        xpath = f'{elem["full_xpath"]}/text()[{elem["text_index"]}]'
        tag_key = self.text_lookup.get(xpath)
        if tag_key and tag_key in self.translations:
            elem['fragments'].append(('text', html_module.escape(self.translations[tag_key])))
        else:
            elem['fragments'].append(('text', html_module.escape(raw)))

    # -- HTMLParser callbacks -----------------------------------------------

    def handle_starttag(self, tag, attrs):
        # --- Skip-mode handling ---
        if self.skip_depth > 0:
            if tag not in SELF_CLOSING:
                self.skip_depth += 1
            raw = self._build_opening_tag(tag, attrs)
            collector = self._collecting_parent()
            if collector:
                collector['fragments'].append(('tag', raw))
            else:
                self.output.append(raw)
            return

        if tag in SKIP_ELEMENTS:
            self.skip_depth = 1
            raw = self._build_opening_tag(tag, attrs)
            collector = self._collecting_parent()
            if collector:
                collector['fragments'].append(('tag', raw))
            else:
                self.output.append(raw)
            return

        # Emit accumulated text from parent TEXT_ELEMENT before ANY child
        # element (void or non-void).  This mirrors the extract's behavior
        # where _emit_text is called before every child start tag.
        if self.stack and self.stack[-1]['text_elem']:
            self._emit_text(self.stack[-1])

        # --- Void / self-closing ---
        if tag in SELF_CLOSING:
            self._count_sibling(tag)
            raw = self._build_opening_tag(tag, attrs)
            collector = self._collecting_parent()
            if collector:
                collector['fragments'].append(('tag', raw))
            else:
                self.output.append(raw)
            return

        # --- Regular element ---
        n = self._count_sibling(tag)
        tag_str = self._build_opening_tag(tag, attrs)
        collector = self._collecting_parent()

        if collector:
            # Inside a TEXT_ELEMENT — add tag to the collector's fragments.
            collector['fragments'].append(('tag', tag_str))
        else:
            self.output.append(tag_str)

        self._push_element(tag, sibling_n=n)

    def handle_endtag(self, tag):
        # --- Skip-mode handling ---
        if self.skip_depth > 0:
            self.skip_depth = max(0, self.skip_depth - 1)
            closing = f'</{tag}>'
            collector = self._collecting_parent()
            if collector:
                collector['fragments'].append(('tag', closing))
            else:
                self.output.append(closing)
            return

        # Find matching element in the stack.
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]['tag'] == tag:
                elem = self.stack[i]
                closing_tag = f'</{tag}>'

                if elem['text_elem']:
                    # TEXT_ELEMENT: emit remaining text, then assemble
                    # all fragments preserving interleaving order.
                    # _emit_text has already checked translations for
                    # each individual text()[N] position, so we do
                    # NOT do a blanket replacement here.
                    self._emit_text(elem)
                    elem['fragments'].append(('tag', closing_tag))
                    parts = [fc for _, fc in elem['fragments']]
                    content = ''.join(parts)

                    # Remove elements and route output.
                    while len(self.stack) > i:
                        self.stack.pop()
                    parent_collector = self._collecting_parent()
                    if parent_collector:
                        parent_collector['fragments'].append(('tag', content))
                    else:
                        self.output.append(content)
                else:
                    # Non-TEXT-ELEMENT: add closing tag, assemble content,
                    # route to parent.
                    if elem['text_fragment']:
                        elem['fragments'].append(('text', elem['text_fragment']))
                        elem['text_fragment'] = ''
                    elem['fragments'].append(('tag', closing_tag))

                    content_parts = []
                    for _, fc in elem['fragments']:
                        content_parts.append(fc)
                    content = ''.join(content_parts)

                    while len(self.stack) > i:
                        self.stack.pop()

                    if self.stack:
                        parent = self.stack[-1]
                        if parent['text_elem']:
                            parent['fragments'].append(('tag', content))
                        else:
                            self.output.append(content)
                    else:
                        self.output.append(content)
                return

    def handle_data(self, data):
        if self.skip_depth > 0 or not self.stack:
            self.output.append(data)
            return

        # If inside a TEXT_ELEMENT (current or ancestor), buffer the text
        # for potential replacement at the TEXT_ELEMENT close.
        collector = self._collecting_parent()
        if collector is not None:
            collector['text_fragment'] += data
        else:
            # No TEXT_ELEMENT in scope — output as structural text.
            # HTML-escape so that &amp; &lt; etc round-trip correctly.
            self.output.append(html_module.escape(data))

    def handle_comment(self, data):
        """Preserve HTML comments verbatim."""
        comment = f'<!--{data}-->'
        collector = self._collecting_parent()
        if collector:
            collector['fragments'].append(('tag', comment))
        else:
            self.output.append(comment)

    def handle_decl(self, decl):
        """Preserve <!DOCTYPE ...> and similar declarations."""
        raw = f'<!{decl}>'
        self.output.append(raw)

    def handle_pi(self, data):
        """Preserve processing instructions (rare in HTML)."""
        raw = f'<?{data}>'
        self.output.append(raw)

    def handle_unknown_decl(self, data):
        """Preserve unknown declarations like <![CDATA[...]]>."""
        raw = f'<![{data}]]>'
        self.output.append(raw)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Render translated text into an HTML template.'
    )
    parser.add_argument('--template', required=True, help='Original HTML source file')
    parser.add_argument('--extraction', required=True, help='extraction.json with XPath mapping')
    parser.add_argument('--translation', required=True, help='translated_merged.txt file')
    parser.add_argument('--output', required=True, help='Output translated HTML file')
    parser.add_argument('--render-log', required=True, help='Path for render_log.json')
    args = parser.parse_args()

    # Load inputs.
    translations = load_translations(args.translation)
    extraction = json.loads(Path(args.extraction).read_text(encoding='utf-8'))
    text_lookup, attr_lookup = build_lookups(extraction)
    template_html = Path(args.template).read_text(encoding='utf-8')

    # Render.
    renderer = HTMLRenderer(text_lookup, attr_lookup, translations)
    renderer.feed(template_html)
    renderer.close()

    output_html = ''.join(renderer.output)

    # Write output.
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(output_html, encoding='utf-8')

    # Build render log.
    report = {
        'logical_tags_applied': 0,
        'missing': [],
        'output_path': str(output_path),
        'layout_warnings': [],
    }
    for para in extraction.get('paragraphs', []):
        tag = para['tag']
        if tag in translations:
            report['logical_tags_applied'] += 1
        else:
            report['missing'].append(tag)

    log_path = Path(args.render_log)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )

    print(f"Applied {report['logical_tags_applied']} logical tags; "
          f"missing {len(report['missing'])}")


if __name__ == '__main__':
    main()
