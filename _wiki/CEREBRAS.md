<!-- Recent-IPO / limited-public-history name. No pre-downloaded SEC filings; no BBG consensus.
     Built from corpus (equity calls + briefings) + web (S-1/IPO data). Every datapoint attributed.
     "State of play" used in place of "Current state (latest quarter)" — no standard quarterly history. -->

# CBRS — Cerebras Systems

_Wiki · generated 2026-06-20 · **recent IPO (priced 2026-05-13, first trade 2026-05-14, Nasdaq: CBRS) — limited public disclosure; no pre-IPO SEC filing history, no BBG consensus.** Sources: corpus (`E:\equity_calls_transcripts\Semis\2026-05-06_Cerebras_IPO-UBS.md`, `E:\briefings\2026\2026-05-12-company-specific.md`) + web (S-1/A, press). Master index: [../INDEX.md](../INDEX.md)._

## Snapshot
Cerebras is a wafer-scale AI-compute company built around the **Wafer Scale Engine (WSE)** — it uses an entire silicon wafer as one compute engine rather than dicing it into chips, putting enough on-die SRAM next to compute to hold a model's weights without round-tripping to HBM (UBS/Tim Archer education call, 2026-05-06). The result is a **fast-inference** machine: the niche is the low-latency, lower-right corner of the throughput/latency curve where HBM-based GPUs are weak. It is the only player that spans **from chip to its own inference cloud** — "even Nvidia sells only hardware and software and does not sell tokens from its own cloud" (UBS, 2026-05-06). 2025 revenue $510.0M (+76% Y/Y), split **$358.4M hardware (70%) / $151.6M cloud & other (30%)** (S-1/A via Futurum, TechTimes, 2026-05). Mix is shifting hard toward cloud on the OpenAI ramp.

## At a glance — product · buyer · supplier
| | |
|---|---|
| **Sells (top 3)** | 1) WSE AI accelerators (CS-3/CS-4/CS-5 systems) · 2) Inference cloud (tokens/AI-inference-as-a-service) · 3) Wafer-scale clusters / supercomputers for gov & national labs |
| **Main buyer(s)** | UAE-linked AI builders today (MBZUAI 62% + G42 24% = ~86% of 2025 rev), migrating to OpenAI (~70–80% of rev by 2028E); plus gov/national labs and AWS (CS-3 in AWS cloud) |
| **Key suppliers** | TSMC N5 (single foundry, full-wafer WSE) · advanced packaging; near-term also rents cloud capacity from customer G42 to serve OpenAI |

## Position in the value chain
Cerebras sits between a concentrated TSMC-based supply chain and a concentrated, largely UAE-/OpenAI-driven demand base. It competes against NVIDIA only in the **fast-inference** slice (decode), not broad multi-tenant training/throughput. The two structural tells: a defensible-but-narrow wafer-scale moat vs NVIDIA, and acute **customer concentration** (G42/MBZUAI ~86% of 2025 revenue, migrating to OpenAI ~70-80% by 2028 per UBS, 2026-05-06).

<svg viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI, Arial, sans-serif" font-size="12">
  <rect x="10" y="60" width="170" height="100" rx="8" fill="#eef3fb" stroke="#33557a" stroke-width="1.5"/>
  <text x="95" y="88" text-anchor="middle" font-weight="bold" fill="#1f3a5f">Suppliers</text>
  <text x="95" y="110" text-anchor="middle" fill="#33557a">TSMC N5 wafers</text>
  <text x="95" y="128" text-anchor="middle" fill="#33557a">(wafer-scale)</text>
  <text x="95" y="146" text-anchor="middle" fill="#33557a">advanced packaging</text>

  <rect x="265" y="45" width="190" height="130" rx="8" fill="#e8f6ee" stroke="#2e7d4f" stroke-width="2"/>
  <text x="360" y="78" text-anchor="middle" font-weight="bold" fill="#1d5e38">Cerebras</text>
  <text x="360" y="100" text-anchor="middle" fill="#2e7d4f">Wafer-Scale Engine</text>
  <text x="360" y="118" text-anchor="middle" fill="#2e7d4f">CS-3 / CS-4 / CS-5</text>
  <text x="360" y="136" text-anchor="middle" fill="#2e7d4f">AI accelerators +</text>
  <text x="360" y="154" text-anchor="middle" fill="#2e7d4f">own inference cloud</text>

  <rect x="540" y="60" width="170" height="100" rx="8" fill="#fbf0ee" stroke="#a8442f" stroke-width="1.5"/>
  <text x="625" y="86" text-anchor="middle" font-weight="bold" fill="#7a2c1d">Customers</text>
  <text x="625" y="106" text-anchor="middle" fill="#a8442f">AI inference (OpenAI)</text>
  <text x="625" y="124" text-anchor="middle" fill="#a8442f">G42 / MBZUAI (UAE)</text>
  <text x="625" y="142" text-anchor="middle" fill="#a8442f">gov / national labs, AWS</text>

  <line x1="180" y1="110" x2="262" y2="110" stroke="#555" stroke-width="2" marker-end="url(#arr)"/>
  <line x1="455" y1="110" x2="537" y2="110" stroke="#555" stroke-width="2" marker-end="url(#arr)"/>

  <text x="360" y="200" text-anchor="middle" fill="#888" font-size="11">Niche: fast/low-latency inference vs NVIDIA HBM-GPUs · Risk: G42/MBZUAI + OpenAI concentration</text>

  <defs>
    <marker id="arr" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L7,3 L0,6 Z" fill="#555"/>
    </marker>
  </defs>
</svg>

## State of play
- **IPO:** Priced **$185/share on 2026-05-13** (above the lifted $150–160 range, itself raised from $115–125), first trade **2026-05-14** on Nasdaq as **CBRS**; ~$5.55B raised, ~$56B fully-diluted value at pricing; closed first day +68% at ~$331 for a ~$95B market cap (CNBC, Yahoo Finance, 2026-05-13/14; the earlier UBS call referenced a $115–125 range / ~$35–38B post-money, since heavily upsized on ~20x demand — @wallstengine via briefing 2026-05-12). Underwriters: Morgan Stanley, Citi, Barclays, UBS (active) (UBS, 2026-05-06).
- **2025 financials (S-1/A):** Revenue $510.0M (+76% Y/Y; 2024 $290.3M, 2023 $78.7M, 2022 $24.6M). Reported net income **$88M** — but flattered by a **$363.3M non-cash forward-contract gain**; GAAP operating loss ~$146M, non-GAAP net loss ~$76M (EBC, Tom's Hardware, web 2026-05). **Not operationally profitable** ex-accounting gain. Hardware $358.4M / cloud $151.6M.
- **Customer concentration:** **MBZUAI 62% + G42 24% = ~86% of 2025 revenue**, both UAE-linked (S-1/A via TechTimes, 2026-05). G42 share fell from >85% (1H24) on diversification; AWS signed Mar-2026 to deploy CS-3/WSE-3 in its cloud (SiliconANGLE, 2026-03). The 2024 IPO attempt was withdrawn under CFIUS scrutiny of the G42 dependence.
- **OpenAI deal (the swing factor):** ~750MW take-or-pay committed up-front, in three $8B-ish tranches, ~$25B total, initially all-cloud; UBS models cloud → 85–90% of revenue and OpenAI → 70–80% of revenue by 2028. Powers OpenAI's real-time **Codex-Spark** model (>1,000 tokens/sec on Cerebras hardware) (UBS, 2026-05-06; briefing 2026-05-12).
- **UBS model (single broker, IPO education — not consensus):** revenue ~+60% in 2026, ~$2.7B in 2027 (~3x), ~$7B in 2028 (+160%); profitability in 2H27, FCF-positive 2028; long-term targets low-60s GM / low-40s op margin (UBS, 2026-05-06).

## Debate / thesis
- **Bull:** Hard-to-replicate wafer-scale architecture aimed at a large premium fast-inference segment; only chip-to-cloud vertical in AI; >10x faster than NVIDIA and ~4x faster than NVIDIA's post-Groq solution per management; OpenAI take-or-pay underwrites a steep multi-year ramp; upside if OpenAI shifts to hardware sooner or AWS hardware ramps (UBS, 2026-05-06).
- **Bear:** (1) **Concentration** — ~86% UAE-linked in 2025, then ~70–80% OpenAI by 2028; (2) **NVIDIA response** — Jensen calls fast-inference ~20% of the market and bought Groq; NVIDIA can lean on its software platform even if it lags wafer-scale on raw latency; (3) **high-cost / low-flexibility** solution — performance edge narrows on power/footprint, and multi-tenant workloads still favor NVIDIA's platform; (4) **reporting complexity** — Cerebras reports "core revenue" that strips OpenAI cost-plus-3% pass-through (power/rent) and G42/OpenAI warrant contra-revenue, so numbers won't be apples-to-apples vs a neo-cloud; near-term it even **rents cloud capacity from customer G42** to serve OpenAI, pressuring margins/FCF (UBS, 2026-05-06).
- **Token-price tailwind + the trillion-parameter rebuttal (MS):** Morgan Stanley initiated **Overweight** ahead of the first print, framing a sharp tailwind — the price of high-speed tokens has risen a lot (a token "twice as fast costs you about 10 to 12 times as much"), and the low-latency providers (Cerebras, Groq, other privates) have seen **~10x price growth**, which "really opens up the opportunity"; Cerebras is "in the pole position" on a unique architecture. On the key technical knock — that wafer-scale "doesn't scale for large models" — MS notes Cerebras has press-released **running the trillion-parameter Kimmy model** with benchmarks, and the first call is its chance to publicly rebut those concerns; the quarter itself "shouldn't be too much of a surprise" (came public ~quarter-end) (MS "Memory + semicap," 2026-06-22).
- **BofA framing (Vivek Arya):** Cerebras is "very similar to what Groq does" — one of three fast-inference players (Cerebras / Groq / D-Matrix), worth **~10-20% incremental to the market**; the **SRAM reliance limits the size of models** it can run, so it optimizes for speed rather than throughput → a niche, but if the AI market is trillion-plus and this slice is ~10% (~$100bn), Cerebras is doing only a small fraction → a large opportunity. Vivek notes **AMD has an investment in Cerebras** (Andrew Feldman sold SeaMicro to AMD — a prior relationship) and would "not be surprised to see them collaborate" (BofA "AMD recap," 2026-05-06).
- **Supply is the constraint, not demand (UBS/Arcuri):** Arcuri thinks Cerebras can give more color on an **AWS deal** (Amazon using it for training, prefill and decode) on the call, but stresses **"it's not a demand question, it's a supply question"** — Cerebras finalized its TSMC wafer request in February taking into account **only OpenAI** near-term, so he is "pretty confident they were not able to" account for AWS, making meaningful AWS capacity unlikely before **2027 at the earliest** (UBS models AWS only from **2028**) (UBS "Arcuri call," 2026-06-15).
- **Where the Street stands:** No BBG consensus to cite (recent IPO; no estimates file). **MS Overweight** (initiated, 2026-06-22). The only full valuation framework in-corpus is the **UBS IPO education call (2026-05-06)**: at the original range, ~11–12x EV/sales on 2027 and mid-4x on 2028 (≈ neo-cloud level), ~23–25x P/E on 2028 EPS; comp set spans semis (NVDA/AMD) and neo-clouds (CoreWeave). Note this pre-dates the large upsize/pricing, so the realized multiples are richer.

## Catalysts / what to watch
- **First public print as a listed company** (Q1/Q2 2026) — focus on customer-mix disclosure (G42/MBZUAI vs OpenAI), core-vs-GAAP revenue bridge, and cloud build-out cash burn (TECHi, 2026-05). MS expects the first call to be the venue for publicly rebutting the "won't scale to large models" criticism (Kimmy trillion-parameter benchmarks); but cautions that because Cerebras must **satisfy its primary-customer (OpenAI) contract before taking on additional business**, it is "unlikely" to have new customers to announce yet (MS "Memory + semicap," 2026-06-22).
- **OpenAI tranche ramp cadence** and whether it stays all-cloud vs migrates to a CSP partner.
- **AWS hardware ramp** (WSE-3 in AWS, signed Mar-2026) — incremental hardware mix and a concentration-diluting datapoint.
- **Product roadmap:** CS-4 (same chip, better platform/power) ramps early 2027; CS-5 (new core, more SRAM, still N5) in 2028; first N3 part (CS-6) late-2028/2029 — so no near-term N3 contention with NVIDIA (UBS, 2026-05-06).
- **Lock-up expiry** post-IPO.

## Risks
- Revenue concentration (UAE entities now; OpenAI later) — single-counterparty dependence.
- Regulatory/CFIUS sensitivity around UAE ownership and exposure (G42/MBZUAI).
- NVIDIA competitive response in fast inference (post-Groq) compressing the niche.
- Reported "core revenue" excludes pass-through and warrant contra-revenue — comparability and quality-of-earnings risk; reported 2025 profit largely a non-cash accounting gain.
- Capital intensity: building/colocating its own cloud while renting capacity near-term pressures FCF until ~2028.
- TSMC wafer-scale capacity / packaging dependence (single foundry).

## Related themes
- [Custom ASIC / TPU](themes/custom-asic-tpu.md) — Cerebras as a non-GPU, non-merchant accelerator alternative competing for the inference TAM alongside the custom-silicon wave.

## In the inbox (Outlook — recent sell-side flow)
- **UBS IPO-education call** _(2026-05-06)_ + company-specific briefing _(2026-05-12)_: OpenAI ~$25B/750MW take-or-pay underwrites a 3-yr ramp (~$7B 2028E); ~11–12x EV/sales 2027 framework (pre-upsize).
- _Recent IPO ($185, +68% debut 2026-05-13); no BBG consensus; ~86% 2025 revenue UAE-linked (MBZUAI/G42) → concentration the bear._

## Intra-quarter — calls, comentários & relatórios (desde o último print)
_intra-quarter (recent IPO) · May 06 → Jun 22, 2026 · sell-side / expert calls / relatórios entre os earnings. Timeline visual: [timeline.html](timeline.html)._

**Sinal vs gestão** — o posicionamento/guidance da empresa (State of play, IPO recente, sem tabela de evolution) × o que o fluxo intra-quarter está dizendo (✓ confirma · ⚠ nuança · ✗ contesta):

| Tema | Gestão / guidance | Fluxo intra-quarter | Sinal |
|---|---|---|---|
| **Demanda / OpenAI** | OpenAI take-or-pay ~$25B / 750MW em 3 tranches; UBS modela cloud → 85-90% e OpenAI → 70-80% da rev até 2028 | MS (Overweight): preço de tokens high-speed subiu ~10x, "in the pole position"; UBS modela rev ~$7B em 2028 | **✓ confirma** (take-or-pay ancora ramp) |
| **Capacidade / supply** | Ramp multi-ano sustentado por OpenAI; AWS (WSE-3) assinado Mar-2026 | Arcuri: "not a demand question, it's a supply question" — wafer TSMC fechado em fev só com OpenAI; AWS material improvável antes de 2027 | **✗ contesta** (supply trava AWS) |
| **Arquitetura / escala** | >10x mais rápido que NVIDIA; chip-to-cloud vertical único | MS: rodou modelo Kimmy de 1tn-params (rebate o "não escala") — vs BofA (Arya): SRAM limita tamanho do modelo → nicho de ~10-20% | **⚠ nuança** (nicho de velocidade) |
| **Concentração / competição** | G42/MBZUAI ~86% em 2025 → OpenAI ~70-80% em 2028 | BofA (Arya): "very similar to Groq"; Jensen comprou Groq, fast-inference ~20% do mercado | **⚠ nuança** (resposta NVIDIA) |

**Log completo** (todo o fluxo intra-quarter, por data):

| Data | Fonte | Tema | Viés | O que disse |
|---|---|---|---|---|
| 05-06 | UBS · Tim Archer (IPO-education call) | demanda | bull | UBS IPO-education call: OpenAI deal ~US$25B / 750MW take-or-pay across three ~US$8B tranches, initially all-cloud; UBS models cloud → 85-90% of revenue and OpenAI → 70-80% by 2028. Powers the real-time Codex-Spark model (>1,000 tokens/sec). The only vertical chip-to-cloud play in AI; >10x faster than NVIDIA. Model: revenue ~+60% in 2026, ~US$2.7B in 2027, ~US$7B in 2028; FCF-positive 2028. Framework ~11-12x EV/sales 2027 (pre-upsize). |
| 05-06 | BofA · Vivek Arya ('AMD recap') | competicao | mixed | Cerebras is 'very similar to what Groq does' — one of three fast-inference players (Cerebras/Groq/D-Matrix), worth ~10-20% incremental to the market; the SRAM dependence limits model size, optimizing for speed not throughput → a niche. AMD has an investment in Cerebras (Andrew Feldman sold SeaMicro to AMD) and Vivek would 'not be surprised to see them collaborate' (BofA 'AMD recap', 2026-05-06). |
| 05-13 | CBRS (IPO pricing) · web/management | capital | neutral | IPO priced at US$185/share on 2026-05-13 (above the raised range of US$150-160, itself up from US$115-125); first trade 2026-05-14 on the Nasdaq as CBRS; ~US$5.55B raised, ~US$56B fully-diluted at pricing; closed the first day +68% at ~US$331 (~US$95B market cap). Underwriters: Morgan Stanley, Citi, Barclays, UBS (CNBC/Yahoo Finance 2026-05-13/14). |
| 06-15 | UBS · Arcuri ('Arcuri call') | supply | mixed | Arcuri: 'it's not a demand question, it's a supply question' — Cerebras finalized its wafer order with TSMC in February counting only on OpenAI in the near term, so he is 'pretty confident they were not able to' accommodate AWS, making meaningful AWS capacity unlikely before 2027 (UBS models AWS only from 2028) (UBS 'Arcuri call', 2026-06-15). |
| 06-22 | Morgan Stanley · 'Memory + semicap' | valuation | bull | Morgan Stanley initiated Overweight ahead of the first print, with a strong tailwind — high-speed token prices have risen sharply (a token 'twice as fast costs you about 10 to 12 times as much'); low-latency providers saw ~10x price growth. Cerebras is 'in the pole position' on a unique architecture. On the knock that wafer-scale 'doesn't scale for large models', MS notes that Cerebras ran the trillion-parameter Kimmy model with benchmarks; the first call is the chance to rebut that publicly (MS 'Memory + semicap', 2026-06-22). |

**Síntese do quarter:** pós-IPO (precificado $185, +68% no 1º dia), o debate deixou de ser sobre demanda — ancorada pelo take-or-pay de OpenAI e validada pela alta de ~10x no preço de tokens (MS Overweight) — e migrou para *supply e nicho*: Arcuri argumenta que a capacidade TSMC já está comprometida só com OpenAI (AWS improvável antes de 2027), enquanto BofA enquadra a arquitetura SRAM/wafer-scale como um nicho de velocidade de ~10-20% do mercado.

## Sources
- **Equity calls:** `../../equity_calls_transcripts/Semis/2026-05-06_Cerebras_IPO-UBS.md` — UBS investor-education call (Tim Archer), 2026-05-06.
- **Research reports (relatórios bons):**
  - [MS "Memory + semicap" (2026-06-22) — MS Overweight init; ~10x token-price tailwind; Kimmy trillion-param rebuttal; OpenAI-contract gate](../relat%C3%B3rios%20bons/2026_06_22_ms_on_memory_and_semicap_22_jun_26.html)
  - [BofA "AMD recap" (Vivek Arya, 2026-05-06) — Cerebras ~Groq, 10-20% incremental, SRAM/model-size niche; AMD investment/Feldman tie](../relat%C3%B3rios%20bons/2026_05_06_amd_vivek_recap_6_may_2026.html)
  - [UBS "Arcuri call" (2026-06-15) — supply not demand the constraint; AWS unlikely before 2027 (UBS models 2028)](../relat%C3%B3rios%20bons/2026_06_15_ubs_arcuri_15_jun_26.html)
- **Briefings:** [2026-05-12 company-specific](../../briefings/2026/2026-05-12-company-specific.md) — Cerebras IPO upsize, OpenAI/AWS customer flags, Codex-Spark.
- **Web (S-1/IPO, attributed inline):** Futurum S-1 teardown; TechTimes / TheNextWeb (raise + 86% UAE dependence); CNBC + Yahoo Finance (pricing $185, debut +68%); EBC / Tom's Hardware (profitability / accounting gain); SiliconANGLE (AWS deal, 2026-03); SEC EDGAR S-1/A (CIK 0002021728).
- **Filings:** none pre-downloaded (recent IPO); see SEC EDGAR for S-1/A and forthcoming 10-Q.
- **Consensus:** none — no BBG estimates file for this name.
