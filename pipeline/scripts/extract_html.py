#!/usr/bin/env python3
"""Extract tagged text from HTML files using Python's built-in HTMLParser.

This module walks the HTML DOM tree, extracts visible text from content
elements, assigns [Pnnn] tags, maps each tag to its XPath location, and
writes three standard output files (extraction.json, source_tagged.txt,
extraction_report.json) following the same schema as extract_docx.py.
"""

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path

# Elements whose direct text content we extract and tag.
TEXT_ELEMENTS = {
    'p', 'div', 'span', 'li',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'td', 'th', 'a', 'button', 'label',
    'textarea',
}

# Elements whose entire content subtree should be skipped.
SKIP_ELEMENTS = {
    'script', 'style', 'code', 'pre',
    'noscript', 'svg', 'math',
}

# Void / self-closing elements (no end tag in HTML).
SELF_CLOSING = {
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
    'link', 'meta', 'param', 'source', 'track', 'wbr',
}


class HTMLTextExtractor(HTMLParser):
    """SAX-style HTML parser that collects tagged text paragraphs.

    Uses a stack-based approach to track the current DOM path, sibling
    element counts for accurate XPath generation, and a skip-depth
    counter for elements whose content should be ignored.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.entries = []        # list of extracted paragraph dicts
        self.index = 0           # next Pnnn number
        self.skip_depth = 0      # how deep we are inside a skip region

        # Stack of open elements. Each entry:
        #   tag             -- element name
        #   xpath_component -- eg "p[2]"
        #   full_xpath      -- full path from root, eg "/html[1]/body[1]/p[2]"
        #   text_elem       -- True if this element type is in TEXT_ELEMENTS
        #   text            -- accumulated text content for this node
        #   text_index      -- how many text() children have been emitted
        #   children        -- dict {tag_name: count} of direct children seen
        self.stack = []

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _count_sibling(self, tag):
        """Increment sibling counter for *tag* under the current parent.

        Returns the new count (1-based).
        """
        if self.stack:
            parent = self.stack[-1]
            n = parent['children'].get(tag, 0) + 1
            parent['children'][tag] = n
            return n
        return 1

    def _push_element(self, tag):
        """Record a new open element on the stack."""
        parent = self.stack[-1] if self.stack else None
        if parent:
            n = self._count_sibling(tag)
            comp = f'{tag}[{n}]'
            full = f'{parent["full_xpath"]}/{comp}'
        else:
            comp = f'{tag}[1]'
            full = f'/{comp}'

        self.stack.append({
            'tag': tag,
            'xpath_component': comp,
            'full_xpath': full,
            'text_elem': tag in TEXT_ELEMENTS,
            'text': '',
            'text_index': 0,
            'children': {},
        })

    def _emit_text(self, elem):
        """Emit *elem*'s accumulated text as a new paragraph entry.

        The element's text buffer is cleared after emission.  Nothing is
        emitted if the buffer is empty or whitespace-only.
        """
        raw = elem['text']
        if raw and raw.strip():
            elem['text_index'] += 1
            xpath = f'{elem["full_xpath"]}/text()[{elem["text_index"]}]'
            self.entries.append({
                'tag': f'P{self.index}',
                'type': 'body',
                'text': raw.strip(),
                'location': {'xpath': xpath},
            })
            self.index += 1
        elem['text'] = ''

    def _emit_attribute_text(self, tag, attrs, parent_xpath, count):
        """Emit alt/placeholder text from attrs as paragraph entries.

        Args:
            tag: The element tag name.
            attrs: List of (name, value) tuples from HTMLParser.
            parent_xpath: Full xpath of the parent element (empty for root).
            count: Pre-computed 1-based sibling index for this element.
        """
        for attr_name, attr_value in attrs:
            is_target = (
                (tag == 'img' and attr_name == 'alt')
                or (tag in ('input', 'textarea') and attr_name == 'placeholder')
            )
            if not is_target:
                continue
            if not attr_value or not attr_value.strip():
                continue
            xpath = f'{parent_xpath}/{tag}[{count}]'
            self.entries.append({
                'tag': f'P{self.index}',
                'type': 'attribute_text',
                'text': attr_value.strip(),
                'location': {'xpath': xpath},
            })
            self.index += 1

    # ------------------------------------------------------------------
    # HTMLParser callbacks
    # ------------------------------------------------------------------

    def handle_starttag(self, tag, attrs):
        if self.skip_depth > 0:
            if tag not in SELF_CLOSING:
                self.skip_depth += 1
            return

        if tag in SKIP_ELEMENTS:
            self.skip_depth = 1
            return

        # Emit any accumulated text in the parent before this child.
        if self.stack and self.stack[-1]['text_elem']:
            self._emit_text(self.stack[-1])

        # Compute parent xpath and sibling count for potential attribute
        # emission BEFORE pushing onto the stack (the parent is stack[-1]).
        parent = self.stack[-1] if self.stack else None
        parent_xpath = parent['full_xpath'] if parent else ''

        if tag in SELF_CLOSING:
            count = self._count_sibling(tag)
            self._emit_attribute_text(tag, attrs, parent_xpath, count)
            return

        count = (parent['children'].get(tag, 0) + 1) if parent else 1
        self._emit_attribute_text(tag, attrs, parent_xpath, count)
        self._push_element(tag)

    def handle_endtag(self, tag):
        if not self.stack:
            return

        if self.skip_depth > 0:
            self.skip_depth = max(0, self.skip_depth - 1)
            return

        # Walk the stack from the top down looking for the matching tag.
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]['tag'] == tag:
                # Process elements top-down to the match.
                for j in range(len(self.stack) - 1, i - 1, -1):
                    elem = self.stack[j]
                    if elem['text_elem']:
                        self._emit_text(elem)
                    elif elem['text']:
                        # Transfer non-text-element content to parent.
                        if j > 0:
                            self.stack[j - 1]['text'] += elem['text']
                # Pop processed elements.
                while len(self.stack) > i:
                    self.stack.pop()
                break

    def handle_data(self, data):
        if self.skip_depth > 0 or not self.stack:
            return
        self.stack[-1]['text'] += data


# ------------------------------------------------------------------
# CLI entry point
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Extract tagged text from HTML.'
    )
    parser.add_argument('--source', required=True)
    parser.add_argument('--extraction-output', required=True)
    parser.add_argument('--tagged-output', required=True)
    parser.add_argument('--report-output', required=True)
    args = parser.parse_args()

    source_path = Path(args.source)
    html_content = source_path.read_text(encoding='utf-8')

    extractor = HTMLTextExtractor()
    extractor.feed(html_content)
    extractor.close()

    entries = extractor.entries

    # --- extraction.json ---
    extraction = {'source': args.source, 'paragraphs': entries}
    ext_path = Path(args.extraction_output)
    ext_path.parent.mkdir(parents=True, exist_ok=True)
    ext_path.write_text(
        json.dumps(extraction, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )

    # --- source_tagged.txt ---
    tagged_path = Path(args.tagged_output)
    tagged_path.parent.mkdir(parents=True, exist_ok=True)
    tagged_path.write_text(
        '\n'.join(f"[{e['tag']}] {e['text']}" for e in entries) + '\n',
        encoding='utf-8',
    )

    # --- extraction_report.json ---
    body_count = sum(1 for e in entries if e['type'] == 'body')
    attr_count = sum(1 for e in entries if e['type'] == 'attribute_text')
    report = {
        'paragraph_count': len(entries),
        'body_count': body_count,
        'attribute_text_count': attr_count,
        'warnings': [],
    }
    report_path = Path(args.report_output)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )

    print(f"Extracted {len(entries)} tagged entries from {source_path.name}")


if __name__ == '__main__':
    main()
