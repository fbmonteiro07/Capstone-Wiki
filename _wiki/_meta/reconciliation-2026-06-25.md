# Reconciliation — 2026-06-25 ingest batch

_Post-patch check: each NEW datapoint from today's 6 sources vs **(1) prior wiki comments**, **(2) Capstone house models**, **(3) BBG consensus** (pulled live 2026-06-25 via `E:\bloomberg_api`)._

Sources ingested: BTG/LightCounting (06-25) · Barclays "S-Curve" (06-01) · Bernstein GenAI Handbook (06-22) · JPM Tesla Robotaxi (06-24) · FundaAI Part 2 (06-24) · BofA Vivek "AI 2030" (05-13).

## Where the new data DIVERGES (the alpha)

| Name | New datapoint (this batch) | Prior wiki | Capstone house model | Δ — read |
|---|---|---|---|---|
| **COHR** | BofA CY27/28 EPS **$9.77 / $12.17**, PO $400 NEUTRAL (05-13) | BofA not previously on page; Jefferies/MS more bullish | **EPS PF CY27 $19.21 / CY28 $23.60**, rev CY27 $16.6bn (Jefferies-based, 05-26) | **BBG resolves this: the outlier is OURS, not BofA's.** Street consensus EPS (FY26/27/28) **$5.46 / $8.33 / $11.98**; BofA's $9.77/$12.17 is **in line with Street**; our house **$19.21 ≈ 2× consensus**. Cons PT $386 ≈ BofA $400. **Action: interrogate the house COHR model** (Jefferies 1.6T ramp far above Street). |
| **MRVL** | BofA PO **$200 BUY**, FY28/29 EPS $5.60/$7.80 (05-13) | UBS $120, MS $80 on page (stale) | _(no house model)_ | **BBG flags the page is stale:** live cons PT **$256**, stock **$281** — the $120/$80 on the page are obsolete. BofA $200 is **below** live consensus PT, and its EPS (FY28 $5.60) is **below** Street ($6.92) — so $200 is multiple-light, not a bull outlier. **Action: refresh MRVL targets.** |
| **TSLA** | JPM EPS 26E **$1.90** / 27E **$2.15** / 28E **$3.15**, PO $475 Neutral (06-24) | First PT in corpus (was "no PT") | _(no house model)_ | JPM 26E ≈ cons ($1.87); **JPM out-years BELOW Street** (27E $2.15 vs cons $2.44, -12%; 28E $3.15 vs $3.34) — JPM more cautious on the robotaxi ramp. But **PO $475 > cons $422 > spot $375**. Rev 26E $104.2bn ≈ cons $102.6bn. |
| **AVGO** | BofA ~**$110bn FY27 AI sales** (consensus; flags upside), top pick (05-13) | JPM (on page) **$150bn+ FY27 AI** | **AI rev 2027E $139bn**; EPS PF FY27 $21.07 / FY28 $35.96 | House FY27 EPS $21.07 ≈ cons FY27 **$19.20**; but house FY28 **$35.96 vs cons $25.72 (+40%)** — house bullish on the out-year. Cons PT **$522 vs spot $379 (+38% upside)** — Street very constructive. |
| **GOOG** | FundaAI capex **$180–190bn 2026**; Barclays capex "up significantly" 2027 | Page carried capex-ramp commentary | **Capex 2026E $183bn / 2027E $310bn**; EPS 26E $11.80 / 27E $16.20 | New sell-side **matches house 2026 capex exactly ($183bn)**. EPS: house 27E $16.20 ≈ cons **$15.34** (page's "vs ~$14.5 consensus" was stale). ⚠️ **Revenue basis mismatch** — house 2026 rev $505bn vs BBG `BEST_SALES` $422bn; likely gross-vs-net/TAC basis, verify before trusting the gap. |
| **INTC** | BofA PO **$56 → $96** but **still UNDERPERFORM** (05-13) | Prior BofA $56 (04-24) | _(no house model)_ | PT **+71% yet rating unchanged** — BofA chasing price, not endorsing. Logged to Changelog. |
| **LITE** | BofA PO **$1,100 NEUTRAL** (05-13) | $1,100 already on page (05-06) | **EPS adj 2027E $30.02**, rev $8.1bn | $1,100 = ~37× house 2027E EPS. House very bullish; BofA neutral at a price the house EPS easily supports. |

## Where the new data CONFIRMS prior / house (no action)

| Name | New datapoint | Reconciles with |
|---|---|---|
| **NVDA** | BofA TAM $1.7Tn CY30; PO $320 | PO $320 already on page (05-19). House 2027E rev $661bn (DC $629bn) ≈ BofA bull DC ~$600B. Consistent, house slightly above. |
| **AMD** | BofA $500 BUY | Page already had "$450–500" (05-06). Consistent. |
| **ALAB** | BofA $240 NEUTRAL | Page had $240 (05-06). Consistent. |
| **AMZN** | Barclays AWS op margin 37.7% 1Q (reported actual) | Corroborates infra-margin thesis; not an estimate. No house model on file. |
| **ANTHROPIC** | Series H $965B post; May ARR run-rate >$47B | Page already had $965B + ~$40–47B run-rate. New data = top of prior range. Private → no BBG/house. |
| **OPENAI** | ARR ~$33B; ~$1tn IPO filing | Consistent with prior page direction. Private → no BBG/house. |

## BBG consensus pull (live 2026-06-25)

PT vs new broker PT; EPS = consensus `BEST_EPS` 1FY/2FY/3FY (fiscal). $ = spot.

| Ticker | Spot | Cons PT | New PT (this batch) | Cons EPS 1/2/3FY | Read |
|---|--:|--:|--:|---|---|
| TSLA | 375 | 422 | JPM **475** | 1.87 / 2.44 / 3.34 | PO above Street; JPM EPS below Street out-years |
| MRVL | 281 | **256** | BofA 200 | 4.04 / 6.92 / 9.21 | stock > cons PT > BofA; wiki $120/$80 stale |
| COHR | 407 | 386 | BofA 400 | 5.46 / 8.33 / 11.98 | BofA ≈ Street; **house $19.21 = 2× Street** |
| AVGO | 379 | **522** | (BofA top pick) | 11.55 / 19.20 / 25.72 | +38% upside to cons PT; house FY28 +40% vs Street |
| GOOGL | 344 | 432 | — | 14.28 / 15.34 / 18.40 | house 27E ≈ cons; rev basis to verify |
| LITE | 862 | 1126 | BofA 1100 | 8.16 / 18.07 / 29.14 | BofA ≈ cons PT; house $30 ≈ cons FY28 (1 yr early) |
| ARM | 348 | 284 | BofA 245 | 2.20 / 3.04 / 3.90 | stock > cons PT > BofA |
| INTC | 133 | 99.5 | BofA 96 | 1.08 / 1.56 / 2.38 | **stock > both PTs** — momentum ahead of fundamentals |
| AMD | 533 | 498 | BofA 500 | 7.25 / 13.12 / 17.63 | BofA ≈ cons; stock above both |
| ALAB | 398 | 278 | BofA 240 | 3.01 / 4.37 / 5.58 | **stock 43% > cons PT** — most stretched vs targets |
| NVDA | 196 | 301 | BofA 320 | 9.00 / 12.80 / 14.67 | +54% upside to cons PT; house EPS ≈ cons |

**Cross-cutting reads:**
1. **COHR — our model, not the Street, is the outlier.** Live consensus puts BofA's $9.77 in line; the house $19.21 is ~2× Street. The divergence flag points inward → bridge the house COHR (Jefferies 1.6T ramp) vs consensus.
2. **MRVL targets on the page are stale.** Live cons PT $256 / stock $281 vs the page's UBS $120 / MS $80. Refresh.
3. **Momentum ahead of targets** — ALAB (+43% over cons PT), INTC, ARM, AMD all trade above *both* consensus PT and the new BofA PTs → PTs are lagging the tape on these.
4. **Biggest Street-implied upside** — AVGO (+38% to cons PT) and NVDA (+54%); house sits at/above Street on both.
5. **TSLA** — JPM is the more cautious robotaxi voice (out-year EPS below Street) yet carries an above-consensus PO $475.
