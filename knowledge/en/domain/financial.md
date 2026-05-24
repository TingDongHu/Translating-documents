---
id: en/domain/financial
type: domain
target_lang: en
name: Financial Documents
description: Translation rules for financial and accounting documents into English
---

## General Principles

- Preserve all numerical values exactly — zero tolerance for rounding or conversion
- Use standard financial terminology in English
- Maintain decimal precision (e.g., 100.00, not 100)
- Format numbers per English conventions after conversion from source locale

## Number Conventions

- Convert source locale decimal/thousand separators to English:
  - Comma decimal → dot decimal (e.g., 100,00 → 100.00)
  - Dot thousands → comma thousands (e.g., 1.234 → 1,234)
  - Space thousands → comma thousands (e.g., 1 234 → 1,234)
- Percentages: 15.5% not 15,5%
- Currency: keep original value, convert formatting only

## Financial Statement Terms

- "资产负债表" → "balance sheet"
- "利润表 / 损益表" → "income statement" / "profit and loss account"
- "营业收入" → "revenue" / "turnover"
- "净利润" → "net income" / "net profit"
- "现金流" → "cash flow"
- "固定资产" → "fixed assets"
- "折旧" → "depreciation"
- "应收账款" → "accounts receivable"
- "应付账款" → "accounts payable"
- "股本" → "share capital"
- "留存收益" → "retained earnings"
- "准备金" → "reserves"

## Tax Terms

- "增值税" → "VAT" (Value Added Tax)
- "含税价" → "price including tax"
- "不含税价" → "price excluding tax" / "net price"
- "企业所得税" → "corporate tax" / "corporate income tax"
- "个人所得税" → "personal income tax"
- "纳税申报表" → "tax return"
- "税收抵免" → "tax credit"
- "发票" → "invoice"
- "收据" → "receipt"

## Invoice Terms

- "发票号码" → "invoice number"
- "订单" → "purchase order"
- "报价单" → "quotation" / "estimate"
- "贷记单" → "credit note"
- "到期日" → "due date" / "maturity date"
- "银行转账" → "bank transfer"
