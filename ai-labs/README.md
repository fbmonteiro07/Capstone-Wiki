# AI Labs — OpenAI & Anthropic revenue, ARR and P&L

The default **Revenue & sources** tab uses the latest saved Capstone `AI Model.xlsx` calculations, with the workbook timestamp shown on the page. It includes monthly run rates, annual and quarterly revenue, 22 dated news observations with links, and separate model-estimate and forecast labels. `revenue-data.json` is the downloadable data and source ledger.

**Combined system** adds OpenAI and Anthropic for matching months on the selected reporting, net or gross basis. Annual totals use the explicitly labeled workbook basis (OpenAI net + Anthropic gross). A missing component does not become zero.

The six original WFS tabs and `data.json` retain the 11 June 2026 snapshot documented below.

## Automatic refresh

An hourly Codex check reads the official AI Model and rebuilds after a saved-file change. The two companies and the combined system update together. Only validated dashboard HTML and its data download are committed and published; previous model snapshots are retained.

The refresh reads Excel's saved calculated values and does not edit or recalculate the workbook. Invalid selected cells, failed annual tie-outs or mismatched combined totals stop publication. Missing components remain unavailable. News references are retained with their own last-review date; a workbook refresh does not imply new news research.

Runner: `_wiki/_tools/refresh_ai_labs_revenue.py --publish` in the research wiki. `--check` validates a candidate without publication. Repeating a completed run makes no new commit; interrupted publication resumes from its saved state. The local computer, desktop app and network workbook access must be available for the hourly check.

## Original WFS snapshot — 11 June 2026

Página estática com o PnL estimado dos AI labs (estimativas Wells Fargo Securities), extraído do workbook `oAI and Anth.xlsx` em 11-jun-2026.

## Conteúdo

- **index.html** — dashboard com 6 abas:
  - **Overview** — KPIs (valuation, receita, EBIT, gross margin, compute spend 2026E), gráfico de ARR mensal (jan-25 a dez-26) e comparativo anual de P&L 2023-2030
  - **Anthropic Summary** / **OpenAI Summary** — as Summary Views do workbook (Compute & Cost view, P&L summary, Valuation view, notas)
  - **Anthropic PnL** / **OpenAI PnL** — abas completas de PnL da WFS (revenue build, custos de compute treino/inferência, opex, EBIT, com memos das fontes)
  - **ARR Tracker** — build mensal de ARR → receita reconhecida das duas empresas
- **data.json** — dump bruto das 5 abas (texto formatado como exibido no Excel, pt-BR)

## Destaques (2026E, USD)

| | OpenAI | Anthropic |
|---|---|---|
| Valuation (post-money) | $852B | $380B |
| Receita | $30,5B net ($38,8B gross) | $66,9B |
| Gross Margin | 53,7% | 61,9% |
| EBIT ex-SBC | -$31,2B | +$12,4B |
| Compute total | $48,2B | $38,4B |

Valores em USD milhões, formatação pt-BR (ponto = milhar, vírgula = decimal). EBIT exclui SBC; custo de treino 100% despesado no período (framework WFS).
