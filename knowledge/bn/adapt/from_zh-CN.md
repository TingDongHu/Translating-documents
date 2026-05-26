---
id: bn/adapt/from_zh-CN
type: adapt
target_lang: bn
source_lang: zh-CN
name: Chinese to Bengali Adaptation
description: Target-specific adaptation rules for translating Chinese (Simplified) documents into Bengali
---

## Formality and Address

- **Chinese "您" (formal you) → Bengali আপনি (formal)**
  - Source: "请您确认" → Target: "অনুগ্রহ করে নিশ্চিত করুন" (formal আপনি)
  - Source: "您需要" → Target: "আপনাকে প্রয়োজন"
  - Context: Chinese 您 maps directly to Bengali আপনি — both are formal "you"

- **Chinese "你" (informal you) → Bengali তুমি (informal)**
  - Source: "你可以" → Target: "তুমি পারো" (informal)
  - Note: In formal Bengali translations, always upgrade to আপনি regardless of Chinese register

- **Chinese "贵公司" (your company, honorific) → Bengali আপনার কোম্পানি / সংশ্লিষ্ট কোম্পানি**
  - Source: "贵公司产品" → Target: "আপনার কোম্পানির পণ্য"
  - Note: Chinese honorific "贵" has no direct Bengali equivalent — use আপনার (your) in formal context

- **Chinese "尊敬的" (respected) → Bengali সম্মানিত**
  - Source: "尊敬的先生" → Target: "সম্মানিত মহোদয়"
  - Source: "尊敬的客户" → Target: "সম্মানিত গ্রাহক"

- **Chinese "先生/女士" (Mr./Ms.) → Bengali জনাব / জনাবা**
  - Source: "王先生" → Target: "জনাব ওয়াং"
  - Source: "李女士" → Target: "জনাবা লি"
  - Note: Bengali uses জনাব (Mr.) and জনাবা (Ms./Mrs.) — not transliterations of Chinese titles

- **Chinese "各位" (everyone/everybody) → Bengali সকল / সমস্ত**
  - Source: "各位同事" → Target: "সকল সহকর্মী"
  - Source: "各位领导" → Target: "সমস্ত নেতৃবর্গ"

- **Chinese "同志" (comrade) → Bengali তোয়াদ / সহকর্মী**
  - Source: "同志们" → Target: "সহকর্মীগণ"
  - Note: "তোয়াদ" is the literal equivalent but সহকর্মী is more natural in Bengali

- **Chinese imperative "请" (please) → Bengali অনুগ্রহ করে / দয়া করে**
  - Source: "请查看" → Target: "অনুগ্রহ করে দেখুন"
  - Source: "请联系" → Target: "অনুগ্রহ করে যোগাযোগ করুন"

- **Chinese "谢谢" (thank you) → Bengali ধন্যবাদ**
  - Source: "谢谢合作" → Target: "সহযোগিতার জন্য ধন্যবাদ"

- **Chinese "此致敬礼" (formal letter closing) → Bengali বিশ্বাসী, / সাদর বিনম্র,**
  - Source: "此致敬礼" → Target: "বিশ্বাসী," or "সাদর বিনম্র,"
  - Note: Chinese formal letter closing maps to Bengali formal closing formulas

- **Chinese gender-neutral language → Bengali (Bengali is less gender-marked)**
  - Source: "他/她" (he/she) → Target: "তিনি" (he/she — Bengali তিনি is gender-neutral for respectful third person)
  - Source: "每位员工应检查他的邮箱" → Target: "প্রত্যেক কর্মচারীকে তার ইমেল পরীক্ষা করা উচিত"
  - Note: Bengali তার is gender-neutral for possessive

- **Chinese "他" (he) → Bengali তিনি (formal) / সে (informal)**
  - Source: "他是经理" → Target: "তিনি ব্যবস্থাপক" (formal)
  - Source: "他走了" → Target: "সে চলে গেছে" (informal)
  - Note: Bengali তিনি is respectful and formal; সে is informal

- **Chinese "她" (she) → Bengali তিনি (formal) / সে (informal)**
  - Source: "她是老师" → Target: "তিনি শিক্ষক" (formal)
  - Note: Bengali does not distinguish gender in third-person pronouns

- **Chinese "他们/她们" (they) → Bengali তারা**
  - Source: "他们来了" → Target: "তারা এসেছে"
  - Note: Bengali তারা is gender-neutral for plural third person

- **Chinese "的" (possessive) → Bengali possessive marker র/এর**
  - Source: "我的" → Target: "আমার"
  - Source: "他的" → Target: "তাঁর" (formal) / "তার" (informal)
  - Source: "公司的" → Target: "কোম্পানির"
  - Note: Chinese 的 maps to Bengali possessive marker র (after vowel) or এর

- **Chinese "们" (plural marker) → Bengali plural marker রা/গণ**
  - Source: "我们" → Target: "আমরা"
  - Source: "你们" → Target: "আপনারা" (formal) / "তোমরা" (informal)
  - Source: "他们" → Target: "তারা"
  - Note: Chinese 们 is a suffix. Bengali has separate plural pronouns.

- **Chinese "您们" (formal plural you) → Bengali আপনারা**
  - Source: "您们好" → Target: "আপনাদের নমস্কার"
  - Note: Chinese 您们 is formal plural. Bengali আপনারা covers both formal and plural.

- **Chinese "自己" (self/oneself) → Bengali নিজে**
  - Source: "我自己" → Target: "আমি নিজে"
  - Source: "他自己" → Target: "তিনি নিজে" (formal)
  - Note: Bengali নিজে is gender-neutral

- **Chinese "大家" (everyone) → Bengali সকল / সমস্ত / সবাই**
  - Source: "大家好" → Target: "সকলের জন্য নমস্কার" or "সবাইকে নমস্কার"

## Number and Date Conventions

- **Chinese decimal point (.) → Bengali decimal point (.)** — same, NO change needed
  - Source: "3.14" → Target: "3.14" (both use period as decimal)
  - Important: Chinese uses period as decimal separator, same as Bengali

- **Chinese thousands separator (,) → Indian comma format (lakh/crore grouping)**
  - Source: "12,345,678" → Target: "1,23,45,678" (Indian grouping)
  - Source: "1,000,000" → Target: "10,00,000"
  - Source: "100,000" → Target: "1,00,000"
  - Note: Chinese uses Western grouping (same as English). Bengali uses Indian grouping.

- **Chinese "万" (10,000) → Bengali হাজার (thousand) or লাখ (lakh)**
  - Source: "5万" → Target: "50,000" or "50 হাজার"
  - Note: Chinese 万 = 10,000. Bengali does not have a single word for 10,000. Use 50 হাজার or 0.5 লাখ.

- **Chinese "亿" (100,000,000) → Bengali কোটি (crore)**
  - Source: "5亿" → Target: "5 কোটি" (5,00,00,000)
  - Note: Chinese 亿 = 100 million = Bengali 1 কোটি

- **Chinese "百万" (million) → Bengali মিলিয়ন**
  - Source: "5百万" → Target: "50 লাখ" or "5 মিলিয়ন"
  - Note: Chinese 百万 = 1 million = Bengali 10 লাখ

- **Chinese "十亿" (billion) → Bengali অরব / বিলিয়ন**
  - Source: "5十亿" → Target: "5 অরব" or "5 বিলিয়ন"
  - Note: Chinese 十亿 = 1 billion = Bengali 1 অরব

- **Chinese date format (YYYY年MM月DD日) → Bengali DD/MM/YYYY**
  - Source: "2026年5月27日" → Target: "27/05/2026" or "২৭ মে ২০২৬"
  - Source: "2026-05-27" → Target: "27/05/2026"
  - Note: Chinese date is year-first. Bengali date is day-first. Always reorder.

- **Chinese month names → Bengali month names**
  - Source: "一月" (January) → Target: "জানুয়ারি"
  - Source: "二月" (February) → Target: "ফেব্রুয়ারি"
  - Note: Chinese months are numbered. Bengali months have standard names.

- **Chinese time format (HH:MM) → Bengali 12-hour or 24-hour**
  - Source: "下午2:30" → Target: "বিকাল ২:৩০" or "14:30"
  - Source: "上午10:00" → Target: "সকাল ১০:০০"
  - Note: Chinese uses 上午/下午 (AM/PM). Bengali uses time-of-day terms or 24-hour format.

- **Chinese "元/块" (yuan) → Bengali ইউয়ান / চীনা টাকা**
  - Source: "500元" → Target: "৫০০ ইউয়ান" or "CNY 500"
  - Note: Preserve the Chinese currency unit in Bengali transliteration

- **Chinese "上午/下午" → Bengali time-of-day terms**
  - Source: "上午" → Target: "সকাল" (morning)
  - Source: "下午" → Target: "দুপুর" or "বিকাল" (afternoon/late afternoon)
  - Source: "晚上" → Target: "রাত" (night)
  - Note: Chinese uses 上午 (before noon) and 下午 (after noon). Bengali has more specific time-of-day terms.

- **Chinese "今天/昨天/明天" → Bengali আজ/গতকাল/আগামীকাল**
  - Source: "今天" → Target: "আজ"
  - Source: "昨天" → Target: "গতকাল"
  - Source: "明天" → Target: "আগামীকাল"

- **Chinese "去年/今年/明年" → Bengali গত বছর/এই বছর/আগামী বছর**
  - Source: "去年" → Target: "গত বছর"
  - Source: "今年" → Target: "এই বছর"
  - Source: "明年" → Target: "আগামী বছর"

- **Chinese "星期/周" (week) → Bengali সপ্তাহ**
  - Source: "星期一" → Target: "সোমবার"
  - Source: "下周一" → Target: "আসন্ন সোমবার"
  - Source: "上周五" → Target: "গত শুক্রবার"

- **Chinese ordinal numbers (第) → Bengali ordinal suffixes**
  - Source: "第一" → Target: "প্রথম" or "1ম"
  - Source: "第二" → Target: "দ্বিতীয়" or "2য়"
  - Source: "第三" → Target: "তৃতীয়" or "3য়"
  - Note: Chinese 第 is a prefix. Bengali ordinals use suffixes.

- **Chinese "大约/左右" (approximately) → Bengali প্রায় / আনুমানিক**
  - Source: "大约100人" → Target: "প্রায় 100 জন"
  - Source: "100人左右" → Target: "100 জনের আশেপাশে"

- **Chinese "以上/以下" (above/below) → Bengali এর উপরে/এর নীচে**
  - Source: "100以上" → Target: "100 এর উপরে" or "100 বা ততোধিক"
  - Source: "50以下" → Target: "50 এর নীচে" or "50 বা কম"

## Cultural References

- **Chinese idioms (成语) → Bengali idioms of equivalent meaning**
  - Source: "画蛇添足" (draw a snake and add feet — do something unnecessary) → Target: "অতিরিক্ত কাজ করা" (do extra work)
  - Source: "一石二鸟" (kill two birds with one stone) → Target: "এক ঢিলে দুই পাখি" (one stone two birds — similar expression exists in Bengali)
  - Source: "塞翁失马" (blessing in disguise) → Target: "অভাগার ভাগ্য" or use descriptive equivalent
  - Source: "亡羊补牢" (mend the pen after the sheep is lost — better late than never) → Target: "দেরি করলেও ভুল সংশোধন করা ভালো"
  - Source: "守株待兔" (guard a tree stump waiting for a rabbit — wait idly for opportunities) → Target: "অপেক্ষায় থাকা"
  - Note: Do NOT translate Chinese idioms literally — find the Bengali equivalent or use descriptive paraphrase

- **Chinese proverbs → Bengali proverbs**
  - Source: "千里之行，始于足下" (A journey of a thousand miles begins with a single step) → Target: "যাত্রা শুরু হয় প্রথম পদক্ষেপ দিয়ে"
  - Source: "三人行，必有我师" (When three people walk together, one must be my teacher) → Target: "তিন জনের মধ্যে একজন শিক্ষক থাকে"
  - Source: "学无止境" (Learning has no limits) → Target: "জ্ঞানের কোনো সীমা নেই"
  - Note: Some Chinese proverbs have direct Bengali equivalents; others need paraphrase

- **Chinese cultural references → Bengali adaptation**
  - Source: References to Chinese holidays (Spring Festival, Mid-Autumn Festival) → Add brief explanation if context requires
  - Source: References to Chinese business practices → Adapt to Bengali equivalents where possible
  - Note: Preserve cultural references that are understood globally (e.g., "Silicon Valley", "Belt and Road Initiative")

- **Chinese "例如" (for example) → Bengali যেমন**
  - Source: "例如，..." → Target: "যেমন, ..."

- **Chinese "即" (i.e.) → Bengali অর্থাৎ**
  - Source: "即..." → Target: "অর্থাৎ..."

- **Chinese "等等" (etc.) → Bengali ইত্যাদি**
  - Source: "苹果、香蕉等等" → Target: "কলা, আপেল, ইত্যাদি"

- **Chinese " versus" (vs.) → Bengali বনাম**
  - Source: "A versus B" → Target: "A বনাম B"

- **Chinese "和/或" (and/or) → Bengali এবং/অথবা**
  - Source: "和/或" → Target: "এবং/অথবা"

- **Chinese "总之" (in summary) → Bengali সংক্ষেপে**
  - Source: "总之，..." → Target: "সংক্ষেপে, ..."

- **Chinese "另外" (in addition/also) → Bengali এছাড়াও / অন্যদিকে**
  - Source: "另外，..." → Target: "এছাড়াও, ..."

- **Chinese "其实" (actually) → Bengali প্রকৃতপক্ষে**
  - Source: "其实..." → Target: "প্রকৃতপক্ষে..."

- **Chinese "当然" (of course) → Bengali অবশ্যই**
  - Source: "当然..." → Target: "অবশ্যই..."

- **Chinese "可能" (maybe/possibly) → Bengali সম্ভবত / হতে পারে**
  - Source: "可能..." → Target: "সম্ভবত..."

- **Chinese "必须" (must) → Bengali অবশ্য / নির্দিষ্টভাবে**
  - Source: "必须..." → Target: "অবশ্যই..." or "নির্দিষ্টভাবে..."

- **Chinese "应该" (should) → Bengali উচিত / হওয়া উচিত**
  - Source: "应该..." → Target: "...উচিত" or "...হওয়া উচিত"

- **Chinese "可以" (may/can) → Bengali পারেন / করতে পারেন**
  - Source: "你可以..." → Target: "আপনি করতে পারেন..."

- **Chinese "关于" (about/regarding) → Bengali সম্পর্কে / সংক্রান্ত**
  - Source: "关于这个问题" → Target: "এই বিষয় সম্পর্কে"

- **Chinese "根据" (according to) → Bengali অনুযায়ী**
  - Source: "根据规定" → Target: "নিয়ম অনুযায়ী"

- **Chinese "通过" (through/via) → Bengali মাধ্যমে**
  - Source: "通过邮件" → Target: "ইমেলের মাধ্যমে"

- **Chinese "由于" (due to/because) → Bengali কারণে / হয়ে**
  - Source: "由于天气原因" → Target: "আবহাওয়ার কারণে"

- **Chinese "虽然...但是" (although...but) → Bengali যদিও...তবুও**
  - Source: "虽然困难，但是我们完成了" → Target: "যদিও কঠিন ছিল, তবুও আমরা সম্পন্ন করেছি"
  - Note: Chinese uses two-clause structure (虽然...但是). Bengali uses যদিও...তবুও.

- **Chinese "如果...那么" (if...then) → Bengali যদি...তাহলে**
  - Source: "如果下雨，那么活动取消" → Target: "যদি বৃষ্টি হয়, তাহলে অনুষ্ঠান বাতিল"
  - Note: Chinese uses two-clause structure (如果...那么). Bengali uses যদি...তাহলে.

- **Chinese "因为...所以" (because...therefore) → Bengali কারণ...সুতরাং**
  - Source: "因为下雨，所以取消" → Target: "কারণ বৃষ্টি হচ্ছে, সুতরাং বাতিল"
  - Note: Chinese uses two-clause structure (因为...所以). Bengali can use কারণ...সুতরাং or simply যেহেতু...তাই.

## Terminology

- **Technical terms: check for established Bengali equivalents before using Chinese-derived terms**
  - Source: "互联网" (internet) → Target: "ইন্টারনেট" (preserve English term, not Chinese transliteration)
  - Source: "计算机" (computer) → Target: "কম্পিউটার" (preserve English term)
  - Source: "软件" (software) → Target: "সফটওয়্যার" (preserve English term)
  - Note: Bengali technical terminology follows English conventions, not Chinese

- **Legal terms: use established Bengali legal terminology**
  - Source: "合同" (contract) → Target: "চুক্তি"
  - Source: "协议" (agreement) → Target: "চুক্তি" or "সমঝোতা"
  - Source: "责任" (liability) → Target: "দায়বদ্ধতা"
  - Note: Bengali legal terms follow South Asian legal traditions, not Chinese

- **Financial terms: use established Bengali financial terminology**
  - Source: "收入" (revenue) → Target: "রাজস্ব"
  - Source: "支出" (expense) → Target: "ব্যয়"
  - Source: "利润" (profit) → Target: "লাভ"
  - Source: "亏损" (loss) → Target: "ক্ষতি"

- **Government terms: use established Bengali administrative terminology**
  - Source: "部长" (minister) → Target: "মন্ত্রী"
  - Source: "秘书长" (secretary-general) → Target: "মহাসচিব"
  - Source: "局长" (director) → Target: "পরিচালক"
  - Note: Bengali government titles follow South Asian administrative traditions

- **Brand names: NEVER translate**
  - Source: "华为" (Huawei) → Target: "Huawei" (preserve)
  - Source: "阿里巴巴" (Alibaba) → Target: "Alibaba" (preserve)
  - Source: "腾讯" (Tencent) → Target: "Tencent" (preserve)

- **Measurement units: convert Chinese units to metric where appropriate**
  - Source: "5里" (Chinese li) → Target: "2.5 কিলোমিটার" (convert to km)
  - Source: "5斤" (Chinese jin) → Target: "2.5 কেজি" (convert to kg)
  - Source: "5亩" (Chinese mu) → Target: "0.33 হেক্টর" (convert to hectares)
  - Note: Bengali uses metric system. Convert Chinese units unless preserving original is necessary.

- **Chinese "公斤" (kilogram) → Bengali কেজি / কিলোগ্রাম**
  - Source: "5公斤" → Target: "5 কেজি"
  - Note: Chinese 公斤 is already metric. Bengali কেজি is the standard term.

- **Chinese "米" (meter) → Bengali মিটার**
  - Source: "100米" → Target: "100 মিটার"

- **Chinese "厘米" (centimeter) → Bengali সেন্টিমিটার / সেমি**
  - Source: "50厘米" → Target: "50 সেন্টিমিটার"

- **Chinese "千米/公里" (kilometer) → Bengali কিলোমিটার / কিমি**
  - Source: "100千米" → Target: "100 কিলোমিটার"

- **Chinese "吨" (ton) → Bengali টন**
  - Source: "5吨" → Target: "5 টন"

- **Chinese "升" (liter) → Bengali লিটার**
  - Source: "10升" → Target: "10 লিটার"

## Administrative and Legal

- **Chinese "应当" (shall/must) → Bengali করতে হবে / করণীয়**
  - Source: "公司应当..." → Target: "কোম্পানি করতে হবে..."
  - Source: "不得" (shall not) → Target: "করতে পারবে না" or "নিষিদ্ধ"
  - Note: Chinese 当 is a strong obligation marker — use Bengali করতে হবে for equivalent force

- **Chinese "兹" (hereby) → Bengali এতদ্বারা**
  - Source: "兹证明" → Target: "এতদ্বারা প্রমাণিত করা হলো"

- **Chinese "本" (this/the present) → Bengali এই / উক্ত**
  - Source: "本合同" → Target: "এই চুক্তি" or "উক্ত চুক্তি"
  - Source: "本文件" → Target: "এই নথি"

- **Chinese "贵" (your, honorific) → Bengali আপনার (your)**
  - Source: "贵方" → Target: "আপনার পক্ষ"
  - Source: "贵公司" → Target: "আপনার কোম্পানি"
  - Note: Chinese "贵" (noble/your) has no Bengali equivalent — use আপনার for formal context

- **Chinese "我方" (our side) → Bengali আমাদের পক্ষ**
  - Source: "我方认为" → Target: "আমাদের পক্ষের মতে"

- **Chinese "鉴于" (whereas/in view of) → Bengali যেহেতু / বিবেচনায় রেখে**
  - Source: "鉴于上述情况" → Target: "উপরের পরিস্থিতি বিবেচনায় রেখে"

- **Chinese "不得" (shall not/must not) → Bengali করা যাবে না / নিষিদ্ধ**
  - Source: "不得转让" → Target: "হস্তান্তর করা যাবে না" or "হস্তান্তর নিষিদ্ধ"

- **Chinese "特此" (hereby/hereupon) → Bengali এতদ্বারা**
  - Source: "特此通知" → Target: "এতদ্বারা জানানো হলো"

- **Chinese "如" (if/as) → Bengali যদি / যেমন**
  - Source: "如遇问题" → Target: "যদি সমস্যা হয়"
  - Note: Chinese 如 has multiple meanings. Choose Bengali equivalent based on context.

- **Chinese "按照" (according to) → Bengali অনুযায়ী**
  - Source: "按照规定" → Target: "নিয়ম অনুযায়ী"

- **Chinese "负责" (be responsible for) → Bengali দায়িত্ব পালন করা / দায়ী থাকা**
  - Source: "负责执行" → Target: "কার্যকর করার দায়িত্ব পালন করা"

- **Chinese "批准" (approve) → Bengali অনুমোদন করা**
  - Source: "已批准" → Target: "অনুমোদিত"

- **Chinese "生效" (take effect) → Bengali কার্যকর হওয়া**
  - Source: "本合同自签署之日起生效" → Target: "এই চুক্তি স্বাক্ষরের তারিখ থেকে কার্যকর"

- **Chinese "终止" (terminate) → Bengali বিলোপ করা / সমাপ্ত করা**
  - Source: "终止合同" → Target: "চুক্তি বিলোপ করা"

- **Chinese "违约" (breach of contract) → Bengali চুক্তি লঙ্ঘন**
  - Source: "违约责任" → Target: "চুক্তি লঙ্ঘনের দায়বদ্ধতা"

- **Chinese "仲裁" (arbitration) → Bengali নির্দিষ্টকরণ / গ্রামীণ বিচার**
  - Source: "仲裁委员会" → Target: "নির্দিষ্টকরণ কমিটি"

- **Chinese "管辖" (jurisdiction) → Bengali এখতিয়ার**
  - Source: "管辖法院" → Target: "এখতিয়ার আদালত"

- **Chinese "保密" (confidentiality) → Bengali গোপনীয়তা**
  - Source: "保密协议" → Target: "গোপনীয়তা চুক্তি"

- **Chinese "不可抗力" (force majeure) → Bengali অপ্রতিরোধ্য শক্তি**
  - Source: "不可抗力条款" → Target: "অপ্রতিরোধ্য শক্তি ধারা"

## Punctuation and Formatting

- **Chinese period (。) → Bengali dari (।) or period (.)**
  - Source: "这是句子。" → Target: "এটি একটি বাক্য।" (dari) or "এটি একটি বাক্য." (period)
  - Note: Chinese uses 。 (full-width period). Bengali uses 。 (dari) or . (period). Choose based on document type.

- **Chinese comma (，) → Bengali comma (,)**
  - Source: "这是，一个测试" → Target: "এটি, একটি পরীক্ষা"
  - Note: Chinese uses ， (full-width comma). Bengali uses , (half-width comma). Convert.

- **Chinese quotation marks ("...") → Bengali same ("...")**
  - Source: "他说"你好"" → Target: "তিনি বললেন \"হ্যালো\""
  - Note: Chinese uses "" (full-width quotation marks). Bengali uses "" (half-width). Convert.

- **Chinese colon (：) → Bengali colon (:)**
  - Source: "如下：" → Target: "নিম্নরূপ:"
  - Note: Chinese uses ： (full-width colon). Bengali uses : (half-width colon). Convert.

- **Chinese semicolon (；) → Bengali semicolon (;)**
  - Source: "第一；第二" → Target: "প্রথম; দ্বিতীয়"
  - Note: Chinese uses ； (full-width semicolon). Bengali uses ; (half-width). Convert.

- **Chinese question mark (？) → Bengali question mark (?)**
  - Source: "这是什么？" → Target: "এটি কী?"
  - Note: Chinese uses ？ (full-width). Bengali uses ? (half-width). Convert.

- **Chinese exclamation mark (！) → Bengali exclamation mark (!)**
  - Source: "太好了！" → Target: "দারুণ!"
  - Note: Chinese uses ！ (full-width). Bengali uses ! (half-width). Convert.

- **Chinese parentheses (（）) → Bengali same ()**
  - Source: "（注释）" → Target: "(টীকা)"
  - Note: Chinese uses （） (full-width). Bengali uses () (half-width). Convert.

- **Chinese dash (——) → Bengali em dash (—)**
  - Source: "这是——一个测试" → Target: "এটি — একটি পরীক্ষা"
  - Note: Chinese uses —— (double em dash). Bengali uses — (single em dash). Convert.

- **Chinese ellipsis (……) → Bengali ellipsis (...)**
  - Source: "等等……" → Target: "ইত্যাদি..."
  - Note: Chinese uses …… (full-width, six dots). Bengali uses ... (three dots). Convert.

- **Chinese bullet points → Bengali same**
  - Bengali uses the same bullet point style as Chinese
  - No conversion needed, but ensure proper spacing

- **Chinese numbered lists → Bengali same**
  - Bengali uses the same numbered list style as Chinese
  - No conversion needed

## SOV/SVO Restructuring

- **Chinese SVO word order → Bengali SOV word order**
  - Source: "我吃饭" (SVO: I eat rice) → Target: "আমি ভাত খাই।" (SOV: I rice eat)
  - Source: "他看书" (SVO: He reads book) → Target: "তিনি বই পড়েন।" (SOV: He book reads)
  - Note: Both Chinese and Bengali can use SOV, but Bengali strictly requires verb-final structure in neutral sentences.

- **Chinese topic-comment structure → Bengali subject-object-verb**
  - Source: "这本书我已经看过了" (Topic-comment: This book I have already read) → Target: "আমি এই বইটি ইতিমধ্যে পড়েছি।" (SOV: I this book already read)
  - Note: Chinese topic-comment structure is more flexible. Bengali requires strict SOV ordering.

- **Chinese postpositions → Bengali postpositions**
  - Both Chinese and Bengali use postpositions, but they differ:
  - Source: "在桌子上" (on the table — Chinese uses 在...上) → Target: "টেবিলের উপরে" (Bengali uses postposition after noun)
  - Note: Bengali postpositions follow the noun directly, similar to Chinese but with different markers.

- **Chinese measure words (量词) → Bengali (remove or adapt)**
  - Source: "一本书" (one [measure word] book) → Target: "একটি বই" (one book — Bengali uses টি/টা as general classifier)
  - Source: "三个人" (three [measure word] person) → Target: "তিন জন ব্যক্তি" (three persons — Bengali uses জন for people)
  - Source: "一张纸" (one [measure word] paper) → Target: "একটি কাগজ"
  - Note: Bengali has classifiers (টি/টা, জন, etc.) but they are less specific than Chinese measure words. Use the appropriate Bengali classifier.

- **Chinese "的" (possessive/attributive) → Bengali possessive constructions**
  - Source: "我的书" (my book) → Target: "আমার বই"
  - Source: "中国的经济" (China's economy) → Target: "চীনের অর্থনীতি"
  - Note: Chinese 的 maps to Bengali possessive marker র/এর

- **Chinese "了" (past tense/completion marker) → Bengali past tense suffixes**
  - Source: "我去了" (I went) → Target: "আমি গেছি" or "আমি গিয়েছি"
  - Source: "他已经走了" (He has already left) → Target: "তিনি ইতিমধ্যে চলে গেছেন"
  - Note: Chinese 了 marks completion. Bengali uses past tense verb forms.

- **Chinese "会" (will/can) → Bengali future tense or ability constructions**
  - Source: "我会来" (I will come) → Target: "আমি আসব"
  - Source: "他会说中文" (He can speak Chinese) → Target: "তিনি চীনা বলতে পারেন"
  - Note: Chinese 会 has multiple meanings. Choose the correct Bengali equivalent based on context.

- **Chinese "能" (can/able to) → Bengali ability constructions**
  - Source: "我能做" (I can do) → Target: "আমি করতে পারি"
  - Source: "不能" (cannot) → Target: "করতে পারি না" or "অসম্ভব"
  - Note: Chinese 能 maps to Bengali পারা (to be able to)

- **Chinese "不" (not) → Bengali negation**
  - Source: "不是" (is not) → Target: "নয়" or "না"
  - Source: "不要" (don't want) → Target: "না চাই" or "দরকার নেই"
  - Note: Chinese 不 is a general negator. Bengali uses different negators based on context.

- **Chinese "吗" (question particle) → Bengali question constructions**
  - Source: "你是学生吗？" (Are you a student?) → Target: "আপনি কি ছাত্র?"
  - Note: Chinese吗 is a yes/no question particle. Bengali uses কি for yes/no questions.

- **Chinese "呢" (question particle for follow-up questions) → Bengali context-dependent**
  - Source: "你呢？" (And you?) → Target: "আপনার কী?" or "আপনি?"
  - Note: Chinese呢 has no direct Bengali equivalent — use contextual translation.

- **Chinese sentence-final particles (啊, 吧, 呢, 嘛) → Bengali (remove or adapt)**
  - Source: "好的啊" (OK, ah) → Target: "ঠিক আছে" (OK — remove particle)
  - Source: "走吧" (Let's go) → Target: "চলুন" (Let's go)
  - Note: Chinese sentence-final particles add mood/tone. Bengali does not have equivalent particles — convey mood through word choice and structure.

- **Chinese "被" (passive marker) → Bengali passive voice**
  - Source: "被拒绝" (was rejected) → Target: "প্রত্যাখ্যাত হয়েছে"
  - Source: "被要求" (was required) → Target: "অনুরোধ করা হয়েছে"
  - Note: Chinese 被 marks passive voice. Bengali uses passive verb constructions with হও (to be).

- **Chinese "把" (object fronting marker) → Bengali object-verb order**
  - Source: "把门关上" (close the door — object fronted) → Target: "দরজাটি বন্ধ করুন" (close the door — SOV)
  - Note: Chinese 把 fronts the object. Bengali naturally places objects before verbs (SOV), so no special marker is needed.

- **Chinese parallel structure (四字成语, etc.) → Bengali natural prose**
  - Source: "改革创新" (reform and innovation — four-character parallel) → Target: "সংস্কার ও উদ্ভাবন" (reform and innovation)
  - Source: "和谐稳定" (harmony and stability) → Target: "সামঞ্জস্য ও স্থিতিশীলতা"
  - Note: Chinese four-character parallel structures are idiomatic. Bengali does not have an equivalent structure — use natural prose.

- **Chinese "是" (to be) → Bengali হওয়া / থাকা**
  - Source: "我是学生" (I am a student) → Target: "আমি ছাত্র"
  - Note: Bengali often omits the copula in present tense. "আমি ছাত্র" (I student) is natural.

- **Chinese "有" (to have) → Bengali আছে / আছন**
  - Source: "我有一个问题" → Target: "আমার একটি প্রশ্ন আছে"
  - Note: Bengali uses possessive + আছে construction, not a verb "to have".

- **Chinese "没有" (don't have/didn't) → Bengali নেই / হয়নি**
  - Source: "我没有时间" → Target: "আমার সময় নেই"
  - Source: "我没有去" → Target: "আমি যাইনি"
  - Note: Chinese 没有 has two meanings: absence (নেই) and past negation (হয়নি).

- **Chinese "在" (at/in/on) → Bengali locative postpositions**
  - Source: "在家里" → Target: "বাড়িতে"
  - Source: "在中国" → Target: "চীনে"
  - Note: Chinese 在 is a preposition. Bengali uses postpositions: -তে, -য়, etc.

- **Chinese "从" (from) → Bengali থেকে / হতে**
  - Source: "从北京来" → Target: "বেইজিং থেকে এসেছে"

- **Chinese "到" (to/until) → Bengali পর্যন্ত / পর্যন্ত**
  - Source: "从1月到3月" → Target: "জানুয়ারি থেকে মার্চ পর্যন্ত"

- **Chinese "和" (and) → Bengali এবং / ও**
  - Source: "A和B" → Target: "A এবং B" or "A ও B"
  - Note: Bengali ও is more formal than এবং.

- **Chinese "或/或者" (or) → Bengali অথবা / অথবা**
  - Source: "A或B" → Target: "A অথবা B"

- **Chinese "但/但是" (but) → Bengali কিন্তু / তবে**
  - Source: "但是..." → Target: "কিন্তু..." or "তবে..."

- **Chinese "而且" (and/moreover) → Bengali এবং / এছাড়াও**
  - Source: "而且..." → Target: "এবং..." or "এছাড়াও..."

- **Chinese "虽然" (although) → Bengali যদিও**
  - Source: "虽然..." → Target: "যদিও..."

- **Chinese "因此/所以" (therefore) → Bengali সুতরাং / তাই**
  - Source: "因此..." → Target: "সুতরাং..."

- **Chinese "例如" (for example) → Bengali যেমন**
  - Source: "例如..." → Target: "যেমন..."

- **Chinese "总之" (in summary) → Bengali সংক্ষেপে**
  - Source: "总之..." → Target: "সংক্ষেপে..."

- **Chinese "另外" (additionally) → Bengali এছাড়াও**
  - Source: "另外..." → Target: "এছাড়াও..."

- **Chinese "其实" (actually) → Bengali প্রকৃতপক্ষে**
  - Source: "其实..." → Target: "প্রকৃতপক্ষে..."

- **Chinese "当然" (of course) → Bengali অবশ্যই**
  - Source: "当然..." → Target: "অবশ্যই..."

- **Chinese "可能" (maybe) → Bengali সম্ভবত**
  - Source: "可能..." → Target: "সম্ভবত..."

- **Chinese "必须" (must) → Bengali অবশ্যই / নির্দিষ্টভাবে**
  - Source: "必须..." → Target: "অবশ্যই..."

- **Chinese "应该" (should) → Bengali উচিত**
  - Source: "应该..." → Target: "...উচিত"

- **Chinese "关于" (about) → Bengali সম্পর্কে**
  - Source: "关于..." → Target: "...সম্পর্কে"

- **Chinese "根据" (according to) → Bengali অনুযায়ী**
  - Source: "根据..." → Target: "...অনুযায়ী"

- **Chinese "通过" (through) → Bengali মাধ্যমে**
  - Source: "通过..." → Target: "...মাধ্যমে"

- **Chinese "由于" (because of) → Bengali কারণে**
  - Source: "由于..." → Target: "...কারণে"

- **Chinese "尽管" (despite) → Bengali সত্ত্বেও**
  - Source: "尽管..." → Target: "...সত্ত্বেও"

- **Chinese "除非" (unless) → Bengali নাহিদে**
  - Source: "除非..." → Target: "নাহিদে..."

- **Chinese "无论" (no matter) → Bengali যাই হোক না কেন**
  - Source: "无论..." → Target: "যাই হোক না কেন..."

- **Chinese "为了" (in order to) → Bengali উদ্দেশ্যে**
  - Source: "为了..." → Target: "...উদ্দেশ্যে"

- **Chinese "以便" (so that) → Bengali যাতে**
  - Source: "以便..." → Target: "যাতে..."

- **Chinese "否则" (otherwise) → Bengali নাহলে**
  - Source: "否则..." → Target: "নাহলে..."

- **Chinese "仍然" (still) → Bengali এখনো / তবুও**
  - Source: "仍然..." → Target: "এখনো..." or "তবুও..."

- **Chinese "已经" (already) → Bengali ইতিমধ্যে**
  - Source: "已经..." → Target: "ইতিমধ্যে..."

- **Chinese "正在" (currently) → Bengali বর্তমানে / এখন**
  - Source: "正在..." → Target: "বর্তমানে..."

- **Chinese "即将" (about to) → Bengali শীঘ্রই / আসন্ন**
  - Source: "即将..." → Target: "শীঘ্রই..."

- **Chinese "始终" (always/from beginning to end) → Bengali সর্বদা / শুরু থেকে শেষ পর্যন্ত**
  - Source: "始终..." → Target: "সর্বদা..." or "শুরু থেকে শেষ পর্যন্ত..."

- **Chinese "通常" (usually) → Bengali সাধারণত**
  - Source: "通常..." → Target: "সাধারণত..."

- **Chinese "竟然" (unexpectedly) → Bengali আশ্চর্যজনকভাবে**
  - Source: "竟然..." → Target: "আশ্চর্যজনকভাবে..."

- **Chinese "究竟" (after all/exactly) → Bengali আসলে / ঠিক**
  - Source: "究竟..." → Target: "আসলে..."

- **Chinese "简直" (simply/virtually) → Bengali সত্যিই / প্রায়**
  - Source: "简直..." → Target: "সত্যিই..."

- **Chinese "反正" (anyway) → Bengali যাই হোক / যেভাবে হোক**
  - Source: "反正..." → Target: "যাই হোক..."

- **Chinese "难道" (could it be that) → Bengali কি সত্যিই**
  - Source: "难道..." → Target: "কি সত্যিই..."

- **Chinese "何必" (why bother) → Bengali কেন প্রয়োজন**
  - Source: "何必..." → Target: "কেন প্রয়োজন..."

- **Chinese "莫非" (could it be that) → Bengali হয়তো**
  - Source: "莫非..." → Target: "হয়তো..."

- **Chinese "罢了" (merely) → Bengali মাত্র / শুধু**
  - Source: "只是...罢了" → Target: "শুধু..."

- **Chinese "而已" (that's all) → Bengali তাই বা**
  - Source: "只是...而已" → Target: "শুধু...তাই বা"
