---
id: ja/domain/legal
type: domain
target_lang: ja
name: 法律文書
description: 法律文書、六法、裁判所書類、法令、判決文、契約条項の翻訳规范
---

# 法律文書 (Legal Documents) — ja-JP

## Reader Model

**読者像：** 法曹関係者（裁判官、弁護士、検察官、司法書士、行政書士、弁理士）、企業法務担当者、法律研究者（比較法学者、国際私法学者）、翻訳認定証明を必要とする契約実務者、外国法事務弁護士。原文の法的効力とニュアンスを完全に保持した翻訳を要求する。具体的な期待と注意点は以下の通り：

- **法的効力と翻訳精度の直結認識**：契約条項の訳文が訴訟で解釈の対象となることを認識しており、「shall」と「may」の一語の誤訳が百万単位の金銭的影響を生む可能性を理解している。
- **用語体系の厳格な一貫性**：一度定義された用語は文書全体で同一表記でなければならない。「当該製品」「本製品」「かかる製品」のゆれは即座に用語体系の崩壊とみなされる。
- **条・項・号の構造的完全性**：原文の階層構造（Article / Section / Paragraph / Subparagraph / Clause）と日本語の「条」「項」「号」「号のイ」の構造が正確にマッピングされているかを最初に確認する。
- **文語調の維持**：「ですます体」への置き換えは文書全体の法的信頼性を喪失させる。法律文書特有の文語調（「…するものとする」「…とみなす」「…を要する」）を維持しなければならない。
- **引用形式の密度と精度**：法条引用（「民法第709条」）、判例引用（「最判昭和48年11月16日民集27巻9号1129頁」）、学説引用の形式を正確に理解した翻訳が求められる。
- **定義済み用語の改変禁止**：定義条項で「本件ソフトウェア」と定義された語を、後段で「かかるソフトウェア」「当該プログラム」等に変更してはならない。
- **英米法と大陸法の架橋**：英米法の概念（consideration, equitable remedy, tort 等）を日本の民法概念でどこまで対応させるかの判断に専門性が求められる。単純な辞書訳では不十分。
- **翻訳証明書の添付形式**：翻訳者としての資格（氏名、住所、日付、署名、「相違ないことを証明する」の文言）が要求される文書があることを認識する。

## Decision Framework

### 法令用語の優先（日本法令外国語訳データベース準拠）
| Condition | Decision | Example |
|-----------|----------|---------|
| JLT（日本法令外国語訳DB）に確立された和訳がある | JLTの訳語を優先。造語や非標準訳を避ける | "shall" → 「するものとする」、JLTでは一貫してこの訳を使用 |
| JLTに未収録の専門法律用語 | 有斐閣「法律用語辞典」、信頼できる法律辞典に従う。民法・刑法等の基本六法の用語体系を参照 | "consideration"（英米法）→ 「約因」（有斐閣）、×「考慮」 |
| 英米法固有の概念（大陸法にない） | カタカナ表記または説明的訳語を使用し、原語を併記。日本の法律概念で無理に代替しない | "trust" → 「信託」（日本にも信託法がある）、"estoppel" → 「エストッペル（禁反言）」 |
| EU法関連用語 | EUの日本語公式訳（EU法公式サイト）またはJLTの対応訳を参照 | "acquis communautaire" → 「EU既存法体系」 |
| 国際私法の用語 | 法の適用に関する通則法の用語体系に従う | "lex loci delicti" → 「不法行為地法」 |
| 新しい法律概念（IT・AI関連） | 経済産業省・デジタル庁のガイドラインの用語を参照。造語は可能な限り避ける | "algorithmic decision-making" → 「アルゴリズムによる意思決定」 |

### 条・項・号・号の構造維持
| Condition | Decision | Example |
|-----------|----------|---------|
| "Article X" | 「第X条」に変換。条レベルの構造は必ず保持 | "Article 5" → 「第5条」 |
| "Section Y" | 「第Y節」に変換。章と条の間の区画 | "Section 2" → 「第2節」 |
| "Paragraph (a)" | 「第a号」または「(a)項」。条約等で用法が分かれるので原文体系に従う | "Paragraph (a)" → 「(a)項」（条約）または「第a号」（国内法） |
| "Subparagraph (i)" | 「(i)」で保持。号の下位区分 | "Subparagraph (i)" → 「(i)」 |
| "Clause 1" または "Item 1" | 「第1号」。号レベル。複数号の列挙は「各号」で総称 | "Items 1 through 5" → 「第1号から第5号まで」 |
| "the preceding paragraph" | 「前項」日本語の定型参照表現 | "pursuant to the preceding paragraph" → 「前項の規定に基づき」 |
| "paragraphs 1 to 3 of Article 10" | 「第10条第1項から第3項まで」引用順序は日本の法制執務慣行に従う | 英語の Article→Paragraph 順を日本語の「条第項」順に並べ替え |
| 構造の省略（編・章・節） | 必要に応じて「第X編第Y章第Z節」も保持。「編」「章」「節」の訳語を固定 | "Book II, Title I, Chapter 3" → 「第二編 第一編 第三章」（民法の構成） |

### 漢語・文語表現の活用
| Condition | Decision | Example |
|-----------|----------|---------|
| 法律文書の文体選択 | 文語調（である体）を厳守。「ですます体」にしない | 全文「である」調で統一。「ですます体」への変換は文書の法的効力の印象を弱める |
| "shall"の基本訳 | 「…するものとする」JIS文書と共通。法律文書での最も頻出する義務表現 | "The Buyer shall pay the Purchase Price." → 「買主は、購入代金を支払うものとする。」 |
| "shall not" | 「…してはならない」禁止表現。強い禁止 | "The Lessee shall not sublease the premises." → 「賃借人は、本物件を転貸してはならない。」 |
| "deem" | 「…とみなす」法律上の擬制を表す定型的表現 | "The notice shall be deemed to have been received." → 「通知は、到達したものとみなす。」 |
| "require" | 「…を要する」「…することを要する」義務・必要性の定型 | "This Agreement requires the consent of both parties." → 「本契約は、両当事者の同意を要する。」 |
| "notwithstanding" | 「…にかかわらず」他の条項に優先することを示す | "Notwithstanding Section 5.1, ..." → 「第5.1項の規定にかかわらず、…」 |
| "subject to" | 「…に従うことを条件として」「…に基づき」優先関係の指示 | "Subject to Section 3, ..." → 「第3条に基づくことを条件として、…」 |
| "without prejudice to" | 「…を害することなく」特定の権利を保持しつつ | "Without prejudice to the generality of the foregoing, ..." → 「前記の一般性を害することなく、…」 |
| "provided that" / "provided, however, that" | 「ただし、…とする」但書の定型。ただし書きの後は主文の例外 | "provided, however, that the total amount shall not exceed..." → 「ただし、総額が…を超えないものとする。」 |
| 文中の「等」の使用 | 例示列挙の「等」は法律文書では多用される。ただし「等」の範囲に注意 | "damages, costs and expenses" → 「損害賠償金、費用及び諸経費等」 |
| 指示語の選択 | 「その」「当該」「同」「前掲」「本件」から適切な語を選択。指示の範囲が不明確な「当該」の濫用に注意 | "the said property" → 「前記財産」or「当該財産」/ "this Agreement" → 「本契約」 |
| "pursuant to" / "in accordance with" | 「…に従い」「…に基づき」「…の定めるところにより」文脈で使い分け | "in accordance with Article 5" → 「第5条の定めるところにより」 |

### 条件句・接続詞の厳密な訳分け
| Condition | Decision | Example |
|-----------|----------|---------|
| "if"（単純条件） | 「…場合には」「…ときは」条件を表す基本接続詞 | "if the Buyer fails to pay" → 「買主が支払いを怠った場合には」 |
| "where"（事実状況の条件） | 「…場合には」「…において」ifより状況設定的な条件 | "where the amount exceeds..." → 「金額が…を超える場合には」 |
| "when"（時間的契機） | 「…したとき」時間的な順序・契機を示す条件 | "when the Agreement terminates" → 「本契約が終了したとき」 |
| "in the event that" | 「…場合には」「…事態が生じた場合には」フォーマルな条件。ifより形式張った表現 | "In the event that a dispute arises..." → 「紛争が生じた場合には」 |
| "unless"（否定条件） | 「…場合を除き」「…除非して」否定条件の定型 | "unless otherwise agreed in writing" → 「書面による別段の合意がある場合を除き」 |
| "except that"（例外明示） | 「ただし…場合はこの限りでない」但書と類似 | "except that the provisions of Section 3 shall apply" → 「ただし、第3条の規定を適用する場合はこの限りでない」 |
| "whether or not"（選択条件） | 「…の如何にかかわらず」選択を問わない条件 | "whether or not such consent is obtained" → 「かかる同意の有無にかかわらず」 |
| "to the extent that"（範囲限定） | 「…する限りにおいて」適用範囲を限定 | "to the extent permitted by applicable law" → 「適用法令の許容する限りにおいて」 |

### 時制と完了態の日本語的処理
| Condition | Decision | Example |
|-----------|----------|---------|
| 法律文の現在形 | 日本語も現在形で対応。時制を英語に合わせる必要なし | "The Company warrants that..." → 「会社は、…を表明保証する。」 |
| 完了形（has/have + 過去分詞） | 「…した」「…している」で訳す。日本語の完了・状態の表現に置き換え | "the Buyer has paid the deposit" → 「買主が手付金を支払った場合」 |
| 未来形（will） | 「…するものとする」または単なる未来として「…する」。shallと区別 | "This Agreement will become effective on..." → 「本契約は、…から効力を生ずる。」 |
| 仮定法過去（would + 原形） | 「…することとなる」帰結の表現。日本語の仮定は「…場合」でカバー | "the termination would not affect..." → 「解除は…に影響を及ぼさないものとする。」 |
| 現在完了進行形 | 「継続して…している」法律文では比較的まれ。必要な場合のみ明示 | "has been continuously operating" → 「継続して営業している」 |

### 定義条項の一貫性
| Condition | Decision | Example |
|-----------|----------|---------|
| 定義語の翻訳 | 定義条項で確立された訳語を文書全体で一貫使用。別表記に置き換えない | 定義:"Company" → 「会社」。後段で「当社」「同社」「本会社」に変更不可 |
| 定義語の大文字表記 | 日本語訳では大文字・小文字の区別なし。定義であることは文脈で明示 | "the Software" → 「本ソフトウェア」（定義後は「ソフトウェア」とだけでも可だが、定義タグの意識は保持） |
| "means"（定義動詞） | 「…を意味する」「いう」定義を示す基本動詞 | ""Territory" means Japan." → 「「 Territory（地域）」とは、日本をいう。」 |
| "includes"（包含定義） | 「…を含む」定義範囲の拡張的包含 | ""Confidential Information" includes..." → 「「秘密情報」には、…を含む。」 |
| "does not include"（除外定義） | 「…を含まない」明確な除外 | ""Confidential Information" does not include information that..." → 「「秘密情報」には、…に該当する情報を含まない。」 |
| 定義引用の引用符 | 日本語では「」（かぎ括弧）または『』（二重かぎ括弧）で定義語をくくる。英文の引用符(" ")に合わせる必要なし | ""Goods" means..." → 「「商品」とは…をいう。」 |
| 定義再引用時の明示 | 定義語を再引用する場合は文脈で明らかでない限り初出時と同一の引用符表記 | "the "Software" shall be delivered..." → 「「本ソフトウェア」は、…納品されるものとする。」 |

### 契約書の定型条項の翻訳
| Condition | Decision | Example |
|-----------|----------|---------|
| "Representations and Warranties" | 「表明保証」表題は「表明保証条項」。個別に「表明する」「保証する」 | "The Seller represents and warrants that..." → 「売主は、…を表明し、かつ保証する。」 |
| "Indemnification" | 「補償」表題は「補償条項」。"indemnify" → 「補償する」 | "The Seller shall indemnify the Buyer against..." → 「売主は、買主を…から補償するものとする。」 |
| "Limitation of Liability" | 「責任の制限」免責・制限条項 | "Neither party shall be liable for consequential damages." → 「いずれの当事者も、結果的損害について責任を負わないものとする。」 |
| "Force Majeure" | 「不可抗力」表題は「不可抗力条項」 | "No party shall be liable for failure to perform due to Force Majeure." → 「いずれの当事者も、不可抗力による履行遅滞について責任を負わないものとする。」 |
| "Term and Termination" | 「存続期間及び解除」表題の定型 | "This Agreement shall commence on the Effective Date." → 「本契約は、効力発生日から効力を生ずるものとする。」 |
| "Governing Law" | 「準拠法」表題は「準拠法条項」 | "This Agreement shall be governed by the laws of Japan." → 「本契約は、日本法に準拠するものとする。」 |
| "Dispute Resolution" | 「紛争解決」仲裁・裁判管轄の定め | "Any dispute arising out of this Agreement shall be submitted to the Tokyo District Court." → 「本契約に起因する一切の紛争は、東京地方裁判所に提起するものとする。」 |
| "Entire Agreement" | 「完全合意」「本契約の完全性」 | "This Agreement constitutes the entire agreement between the parties." → 「本契約は、当事者間の完全なる合意を構成する。」 |
| "Severability" | 「分離可能性」一部無効の扱い | "If any provision is held invalid, the remaining provisions shall continue in full force." → 「本契約のいずれかの条項が無効と判断された場合でも、その他の条項は完全に効力を存続するものとする。」 |
| "Amendment" | 「変更」「修正」契約変更の手続き | "This Agreement may not be amended except in writing signed by both parties." → 「本契約は、両当事者による署名のある書面によらなければ変更することができない。」 |
| "Assignment" | 「譲渡」契約上の地位の移転 | "Neither party may assign this Agreement without the other party's consent." → 「いずれの当事者も、相手方の同意なく本契約上の地位を譲渡してはならない。」 |
| "Confidentiality" | 「秘密保持」表題は「秘密保持条項」 | "The Receiving Party shall hold the Confidential Information in confidence." → 「受領者は、秘密情報を秘密として保持するものとする。」 |
| "Non-compete" | 「競業避止義務」就業規則やM&A契約で頻出 | "The Seller shall not engage in any competing business for a period of..." → 「売主は、…の期間、競合事業に従事してはならない。」 |
| "Warranty Disclaimer" | 「保証の免責」保証の否認・制限 | "THE SOFTWARE IS PROVIDED 'AS IS' WITHOUT WARRANTY OF ANY KIND." → 「本ソフトウェアは、何らの保証もなく「現状有姿」で提供される。」 |
| "Liquidated Damages" | 「損害賠償の予定」「違約金」 | "The Seller shall pay liquidated damages in the amount of..." → 「売主は、…の額の違約金を支払うものとする。」 |

### 英米法概念の日本語対応
| Condition | Decision | Example |
|-----------|----------|---------|
| "consideration"（約因） | 「約因」または「対価」。英米法契約の成立要件 | "The parties agree that the consideration for this Agreement is..." → 「当事者は、本契約の約因が…であることに合意する。」 |
| "tort"（不法行為） | 「不法行為」日本の民法709条の不法行為に相当 | "claims in contract, tort, or otherwise" → 「契約上の請求、不法行為に基づく請求その他一切の請求」 |
| "equitable remedy"（衡平法上の救済） | 「衡平法上の救済」カタカナ＋説明 | "The parties agree that monetary damages are inadequate and equitable remedies are available." → 「当事者は、金銭損害賠償では不十分であり、衡平法上の救済が利用可能であることに合意する。」 |
| "specific performance"（特定履行） | 「特定履行」英米法の救済手段 | "The Seller agrees that specific performance is an appropriate remedy." → 「売主は、特定履行が適切な救済手段であることに同意する。」 |
| "injunction"（差止命令） | 「差止命令」または「禁止命令」 | "The Company may seek an injunction to prevent unauthorized use." → 「会社は、無許可使用を防止するため差止命令を求めることができる。」 |
| "fiduciary duty"（受託者責任） | 「受託者責任」「信認義務」 | "The director owes a fiduciary duty to the company." → 「取締役は、会社に対して受託者責任を負う。」 |
| "due diligence"（デュー・ディリジェンス） | 「デュー・ディリジェンス（事前調査）」カタカナ＋補足説明 | "The Buyer shall conduct due diligence on the Target Company." → 「買主は、対象会社に対しデュー・ディリジェンス（事前調査）を実施するものとする。」 |
| "material adverse change"（重要悪影響変更） | 「重要悪影響変更（MAC）」M&A契約の定型 | "The Seller shall notify the Buyer of any Material Adverse Change." → 「売主は、重要悪影響変更（MAC）が生じた場合、買主に通知するものとする。」 |

### 判例・裁判例の引用形式
| Condition | Decision | Example |
|-----------|----------|---------|
| 日本の最高裁判決引用 | 日本の判例引用形式（最判年月日・民集頁等）をそのまま保持 | "Supreme Court, 1973.11.16" → 「最判昭和48年11月16日民集27巻9号1129頁」 |
| 英米判例引用 | 判例名（事件名）は原語保持。必要に応じて簡単な事案説明を注記 | "Marbury v. Madison" → 「Marbury v. Madison（マーベリー対マディソン事件）」 |
| EU裁判所判決 | 「事件番号 + 当事者名」の形式を保持 | "Case C-496/18" → 「事件C-496/18」 |
| "holding"（判示） | 「判示」または「判断」裁判所の法的判断 | "The court held that..." → 「裁判所は、…と判示した。」 |
| "obiter dictum"（傍論） | 「傍論」判決理由中の付随的見解 | "This statement is obiter dictum and not binding." → 「この記述は傍論であり、拘束力を有しない。」 |

### コーポレート文書（議事録・定款等）
| Condition | Decision | Example |
|-----------|----------|---------|
| 取締役会議事録 | 「取締役会議事録」の固定訳。開催日時、場所、出席者、議案、決議事項の構成を保持 | "Minutes of the Board of Directors Meeting" → 「取締役会議事録」 |
| "Articles of Incorporation" | 「定款」株式会社の基本定款 | "The Company's Articles of Incorporation provide that..." → 「会社の定款は、…を定めている。」 |
| "resolution" | 「決議」株主総会・取締役会の意思決定 | "adopted by a resolution of the shareholders" → 「株主総会の決議により」 |
| "quorum"（定足数） | 「定足数」会議成立要件 | "The quorum for a meeting shall be one-half of the directors." → 「会議の定足数は、取締役の過半数とする。」 |
| "proxy"（議決権代理行使） | 「議決権の代理行使」「プロキシー」 | "Shareholders may vote by proxy." → 「株主は、代理人により議決権を行使することができる。」 |
| "vote" / "voting" | 「議決権」「投票」 | "Each share carries one vote." → 「1株につき1個の議決権。」 |

### 訴訟・仲裁関連用語
| Condition | Decision | Example |
|-----------|----------|---------|
| "plaintiff" | 「原告」民事訴訟の当事者 | "The plaintiff filed a complaint." → 「原告は、訴状を提出した。」 |
| "defendant" | 「被告」民事訴訟の当事者 | "The defendant answered the complaint." → 「被告は、答弁書を提出した。」 |
| "complaint"（訴状） | 「訴状」訴訟開始文書 | "The complaint alleges breach of contract." → 「訴状は、契約違反を主張している。」 |
| "answer"（答弁書） | 「答弁書」被告の応答文書 | "The defendant filed an answer." → 「被告は、答弁書を提出した。」 |
| "discovery"（証拠開示） | 「証拠開示」または「ディスカバリー」。英米法独自の制度のため説明を併記 | "During discovery, the parties exchanged documents." → 「証拠開示（ディスカバリー）手続において、当事者は文書を交換した。」 |
| "summary judgment" | 「略式判決」「サマリー・ジャッジメント」 | "The court granted summary judgment in favor of the plaintiff." → 「裁判所は、原告勝訴の略式判決を下した。」 |
| "class action" | 「集団訴訟」「クラス・アクション」 | "A class action was filed against the manufacturer." → 「製造業者に対し集団訴訟（クラス・アクション）が提起された。」 |
| "injunction"（仮処分） | 「仮処分命令」日本の民事保全法に基づく | "The court issued a preliminary injunction." → 「裁判所は、仮の差止命令を発した。」 |

## Standard Conventions

### 日本の法律文書体系

**法令の基本構造（階層順）：**
- 憲法 → 法律 → 政令 → 省令 → 告示・通達
- 翻訳時はこの階層関係を明確に区別して表記する

**日本の六法（基本法体系）：**
| 法令名 | 英語名称 |
|--------|----------|
| 日本国憲法 | Constitution of Japan |
| 民法 | Civil Code |
| 商法 | Commercial Code |
| 会社法 | Companies Act |
| 民事訴訟法 | Code of Civil Procedure |
| 刑法 | Penal Code |
| 刑事訴訟法 | Code of Criminal Procedure |
| 行政事件訴訟法 | Administrative Case Litigation Act |

**法令の引用形式：**
- 正式引用：「民法（明治29年法律第89号）第709条」
- 略式引用：「民法第709条」
- 条・項・号の表記：
  - 第709条（条）
  - 第1項（項：条の下位区分。数字は漢数字が正式）
  - 第1号（号：項の下位区分）
  - 第1号の2（号の：号の下位区分）
- 法文中の引用：「前条」「次条」「同条」「前項」「第何条において準用する第何条」

**法令番号の表記：**
- 「平成11年法律第89号」（元号＋年＋法令種別＋番号）
- 憲法・条約には法令番号なし
- 翻訳時には法令番号を完全保持

**日本の契約書の基本構成：**
1. 表題（「売買契約書」「秘密保持契約書」等）
2. 前文（当事者の表示、契約締結の事実）
3. 定義条項（「第1条（定義）」）
4. 各条項（実体的条項）
5. 終期条項（存続期間、解除、通知）
6. 一般条項（準拠法、合意管轄、完全合意等）
7. 署名欄（締結日、住所、氏名、押印）

**契約書の定型文言：**
| 日本語定型 | 英語相当 | 使用場面 |
|-----------|----------|----------|
| 「…証として本書2通を作成し、各当事者記名押印の上、各自1通を保有する」 | "IN WITNESS WHEREOF, the parties have executed this Agreement" | 契約書末尾の証明文 |
| 「上記の契約の成立を証するため本書を作成する」 | 同上、和文契約の定型 | 同上の和文スタイル |
| 「本契約の履行に関して生じた一切の紛争は…」 | "All disputes arising out of or in connection with this Agreement" | 裁判管轄条項 |
| 「本契約の成立、効力、履行及び解釈に関しては…法を適用する」 | "This Agreement shall be governed by and construed in accordance with..." | 準拠法条項 |

### 法律文書の表記標準

**文体：**
- 文語調（である体）を厳守。会話体・口語体は一切使用しない
- 「ですます体」は契約書・法令では使用禁止。行政手続きの案内文書でのみ許容
- 一文は短く、複数の概念を一文に詰め込まない

**句読点：**
- 横書き：原則「、。」（読点・句点）
- JIS Z 8301に基づく法令・規格文書では「，．」も使用されるが、日本の法律文書は「、。」が標準
- 引用符には「」（かぎ括弧）を使用。二重引用は『』（二重かぎ）
- 括弧は（）を使用。法律文では特に（）内に条項番号を入れる

**数字表記：**
- 正式な法令文書：漢数字（第一条、第二項、第三号）
- 横書きが増えた現代：算用数字も使用される（第1条、第2項）
- 同一文書内で混在させない。漢数字と算用数字の混用は不可
- 金額は「金1,000,000円」または「金壱百万円」（改ざん防止の大字）
  - 大字（だいじ）：壱、弐、参、肆、伍、陸、漆、捌、玖、拾、百、千、萬
  - 契約書の金員表示では大字が正式

**その/これ/当該の使い分け：**
| 語 | 用法 | 例 |
|----|------|-----|
| その | 一般的指示。指示範囲が広い | 「その場合」 |
| 当該 | 特定的指示。当該文書内で特定されたものを指す | 「当該製品」「当該条項」 |
| 同 | 同一のものを指す。前出の語を受ける | 「同条」「同項」「同号」 |
| 本件 | 当該文書全体の対象を指す | 「本件契約」「本件物件」 |
| 前記 | 前に記述したもの | 「前記のとおり」 |
| 前掲 | 前に掲げたもの（引用文献・条文に使用） | 「前掲注(3)」 |
| いわゆる | 一般に言われるところの | 「いわゆるマネーローンダリング」 |

**条項の参照方式：**
- 「第○条の規定に基づき」
- 「前条の定めるところにより」
- 「同項各号に掲げる場合」
- 「本条の規定は、…場合には適用しない」
- 「第○条の規定は…について準用する」

**翻訳証明書の標準書式（Certificate of Translation）：**
```
翻訳証明書

私は、［氏名］（住所：［住所］）は、英語から日本語への翻訳者として、
別紙の文書が原文の正確な翻訳であることを証明する。

［日付］
［署名］
［氏名］
［資格］（例：公益社団法人日本翻訳者協会会員）
```

### 法律翻訳で注意すべき誤訳事例
| 誤訳例 | 正しい訳 | 誤訳のリスク |
|--------|----------|-------------|
| "shall"を「しなければならない」と一律訳した | 「するものとする」と区別 | 「しなければならない」はmust相当。shallを強制義務化すると契約のニュアンスが変わる |
| "material"を「重要な」と訳した | 「重要な」だが、法律文脈では「重大な」と区別 | material breach（重大な違反）と重要でない違反の区別がつかなくなる |
| "reasonable"を「合理的な」と訳した | 「合理的な」でよいが、日本の「相当性」概念との調整が必要 | 英米法のreasonablenessは日本の「相当性」「合理性」の両方のニュアンスを含む |
| "jointly and severally"を「共同して」のみで訳した | 「連帯して（連帯債務）」 | 連帯責任の意味が欠落 |
| "representations"を「表明」とせず「表現」と訳した | 「表明保証」の「表明」 | 契約上の重要な事実陳述であることが失われる |
| "good faith"を「誠実」と訳した | 「信義誠実（義務）」民法1条2項の「信義則」に基づく | 民法の「信義則」の法的含意が伝わらない |
| "best efforts"を「最善の努力」と訳した | 「最大限の努力」または「善管注意義務」 | 日本法の「善管注意義務」と英米法のbest effortsの差異に注意 |

### 参考文献
- 日本法令外国語訳データベースシステム (https://www.japaneselawtranslation.go.jp/)
- 有斐閣「法律用語辞典」
- 法務省「法令用語に関する通達」
- 「法律文書作成のためのスタイルブック」（商事法務）
- 法制執務研究会「法制執務詳解」
- 「日英契約書の翻訳実務」（商事法務）
- 「英米法辞典」（東京大学出版会）
- 日本公証人連合会「定款作成の手引」
- 法務省民事局「登記六法」
- 最高裁判所「裁判所書類作成要領」
- 「国際契約ハンドブック」（国際商事法研究所）
- 日本仲裁人協会「仲裁判断書作成ガイドライン」
- 日本弁護士連合会「契約書作成ガイドライン」

---

*Document version: 2.0*
*Last updated: 2026-05-25*
