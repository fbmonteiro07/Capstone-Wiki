# CDNS — Cadence Design Systems

_Wiki · generated 2026-06-19 · sources: `E:\Wiki Felipe\CDNS` · `_equity_calls` · `_briefings\by-ticker\CDNS.md`. Master index: [../INDEX.md](../INDEX.md)._

## Snapshot
Cadence is one half of the EDA duopoly (with Synopsys) — the chip-design software, IP, and hardware-emulation franchise that sits *upstream of every silicon project*: nothing gets taped out without Cadence or SNPS tools. Revenue splits into three categories (FY25 10-K, 2026-02-19): **Core EDA 70%** (Virtuoso custom/analog, Innovus digital implementation, Xcelium/Jasper verification, plus the Palladium emulation / Protium FPGA-prototyping hardware), **Semiconductor IP 14%** (interface/PHY, memory, chiplet subsystems sold into automotive, hyperscale, mobile), and **System Design & Analysis 16%** (PCB/Allegro, multiphysics, the Ansys-adjacent stack post the company's "Intelligent System Design" expansion). The model is overwhelmingly **recurring — 80% of FY25 revenue** recognized over time (time-based software licenses + maintenance + royalties + hardware leases), which is the structural reason the name compounds at a premium multiple. Whole thesis is a toll on rising design complexity: every extra process node, every chiplet/3D-IC stack, and every AI-accelerator startup raises tool intensity per chip, and Cadence is increasingly selling its *own* AI-design layer (Cadence.AI / Verisium / Cerebrus agentic flows) back into that workflow.

## At a glance — product · buyer · supplier
| | |
|---|---|
| **Sells (top 3)** | 1) Core EDA — Virtuoso/Innovus/Xcelium + Palladium emulation (70%) · 2) System Design & Analysis — Allegro PCB/multiphysics (16%) · 3) Semiconductor IP — interface/PHY, memory, chiplet (14%) |
| **Main buyer(s)** | Chip designers & systems companies — hyperscalers building custom ASICs, plus automotive/mobile/HPC; no single customer >10% of revenue |
| **Key suppliers** | Largely software/IP (own R&D); upstream dependency limited to FPGA/components for Palladium/Protium emulation hardware — otherwise — |

## Current state (latest quarter)
**Q1 FY26 (quarter ended 2026-03-31, 10-Q filed 2026-05-01):** Total revenue **$1,474.2M, +18.7% y/y** (vs $1,242.4M). GAAP income from operations $431.3M (**29.3% op margin**), net income $335.7M, **diluted EPS $1.23** (vs $1.00). Recurring/up-front mix was **77%/23%** in the quarter (vs 82%/18% Q1 FY25) — the up-front skew reflects hardware (Palladium Z3/Protium) and IP timing, not deterioration of the franchise. **Backlog (contracted but unsatisfied RPO) $8.0B** as of 2026-03-31, up from $7.8B at FY25 year-end (10-K), of which ~53% converts within 12 months — the visibility cushion buy-side underwrites the multiple on. China bounced back hard: **$189.4M, +36% y/y, ~13% of revenue** (10-Q geography table), a clean recovery from the export-license disruption that dented mid-2025 (see Risks).
- **FY25 full year (10-K):** revenue **$5,296.8M, +14% y/y**; product & maintenance $4,821.6M (+14%), services $475.2M (+11%). GAAP op income $1,492.0M (28.2% margin), net income $1,108.9M, diluted EPS $4.06. Geography FY25: US 44%, China 13%, Other Asia 19%, EMEA 15%, Japan 6%. No single customer >10% of revenue.
- **Demand drivers management frames** (10-K): three AI "horizons" — Infrastructure AI (HPC/AI accelerators for data centers/hyperscalers), Physical AI (autonomous/robotics/SDVs), Life Sciences AI. The hyperscaler custom-silicon wave (every cloud + AI-model builder now designing in-house ASICs) is the cleanest tailwind: more first-time tape-outs = more seat/IP/emulation demand.

## Debate / thesis
- **Bull:** EDA is a structurally advantaged duopoly — mission-critical, deeply embedded, ~80% recurring, near-impossible to rip-and-replace mid-design — that grows *with* design complexity regardless of where the semi cycle sits. AI is a double tailwind: (1) the AI-chip buildout multiplies design starts (every hyperscaler ASIC, every AI-silicon startup needs the full Cadence flow + Palladium emulation), and (2) Cadence sells AI *into* the tools (agentic verification acquired in FY25, VLAB virtual prototyping for SDVs), expanding seat value and ARPU. Backlog $8.0B and 18.7% Q1 growth show the franchise re-accelerating off the 2025 China air-pocket. Briefing data point (firstadopter / Tae Kim, 2026-06-11): **CDNS signed for Intel 14A node IP** — cited by BofA as a foundry-credibility signal in its INTC double-upgrade, and a reminder that Cadence collateral wins regardless of which foundry/customer wins the node war.
- **The buy-side long pitch, framed (Barron's Tech Roundtable, Denny Fish / Janus Henderson, 2025-03-26):** EDA as "one of the most important vertical software industries on the planet," a global CDNS/SNPS duopoly with a TAM that "has expanded materially over time and will likely continue to do so" on hyperscaler custom-silicon plus vertical demand (automotive, aerospace, defense). AI is framed as *enhancing* an already-durable business — "speed to market for design, one of the most complex processes on Earth" — i.e. a name you'd own even without the AI narrative. Valuation angle at the time: both names sat "at the low end of their P/E range over the past several years," with CDNS having traded below ~30x forward earnings "only a couple of times" historically (CDNS $263.41 as of 2025-03-26 per the note's table; pre-dates the 2025 China episode and the subsequent re-rate, treat the multiple frame as directional, not current). Janus's Tony Kim corroborated as a "long-term supporter" of the name.
- **AI-IP / scale-up optionality (MS Scale-up primer, Moore/Marshall, 2025-08-25):** Cadence named among the announced ASIC-side partners for NVIDIA's **NVLink Fusion** (alongside Synopsys, Marvell, Alchip, MediaTek, Astera Labs), which extends NVLink to third-party accelerators/CPUs — a read-through that Cadence's interface-IP franchise is positioned to monetize the custom-silicon-plus-NVLink stack as Fusion adoption scales. MS rates CDNS Overweight in the note.
- **Bear:** premium SaaS-like multiple on a name that is *not* immune to (a) China — 13% of revenue, structurally exposed to export-control escalation and Beijing's drive to build a domestic EDA stack (Empyrean, X-EPIC, Primarius, etc., explicitly named as emerging competitors in the 10-K); and (b) up-front/hardware lumpiness that can compress a quarter (Q1 FY26 up-front mix rose to 23%). The duopoly is mature — SNPS post-Ansys is a larger, broader system-analysis competitor, Siemens EDA is a credible #3, and the TAM math leans on AI design-start growth holding. Valuation leaves no room for a guide-down.
- **Where the sell-side stands:** still thin direct coverage in the inbox. The data points on disk: the **Intel 14A IP sign-up** surfacing via BofA's INTC work (2026-06-11, positive foundry-ecosystem evidence, not a primary CDNS call); a structural **long pitch** from a buy-side PM (Janus's Denny Fish, Barron's 2025-03-26); and an **MS Overweight** stance with NVLink Fusion IP optionality (Scale-up primer, 2025-08-25). No fresh broker rating/PT *change* for CDNS is in the inbox — *do not infer a current Street target from the above; the MS-cited price points predate the 2025 China episode.*

## Catalysts / what to watch
- **Next print: Q2 FY26 earnings** (late Jul 2026, ~7/28 cadence) — watch backlog trajectory off $8.0B, recurring-mix normalization back toward 80%, and any FY26 revenue-guide raise (FY25 grew 14%; Q1 ran 18.7%).
- **China export-control regime** — the BIS license requirement was imposed 2025-05-23 then rescinded 2025-07-02; any reimposition is the single biggest swing factor on the 13% China line.
- **AI-design monetization** — uptake of agentic verification + Cadence.AI/Cerebrus; Palladium Z3 / Protium emulation refresh cycle (hardware drives the up-front line).
- **NVLink Fusion ecosystem traction** — adoption of Fusion across third-party ASICs/CPUs pulls Cadence interface-IP content (MS Scale-up primer, 2025-08-25).
- **Foundry node ramps** — design-tool pull-through from N2/A16 (TSMC), Intel 14A (CDNS already signed), and chiplet/3D-IC adoption (Core EDA + SD&A content per design). Sell-side channel-check frameworks flag EDA/IP go-to-market on N2/A16/3D-IC flows and chiplet-IP traction as a key verification item (DeepResearch TSM, supply-chain primer — CDNS referenced only as part of the EDA/IP channel, not a standalone call).
- **SNPS read-throughs** — Synopsys prints/guides are the cleanest duopoly tell for Cadence demand.

## Risks
- **China / export controls (10-K):** 13% of revenue; the May–Jul 2025 BIS EDA-software license episode "negatively impacted revenue in China during this period," and the US "may consider reimposing" restrictions; Entity-List 50%-ownership rule (effective 2025-09-29) widens the perimeter.
- **BIS/DOJ settlement (10-K):** 2025-07-27 settlement over ~$45.3M of pre-2021 sales/tech-transfer to a China customer without authorization — plea agreement plus ongoing audit/compliance obligations; residual reputational and operational overhang.
- **Domestic-substitution competition:** China's 2030 semiconductor self-sufficiency policy is funding local EDA entrants (Empyrean, Xpeedic, X-EPIC, Primarius, Univista, Giga DA) that could erode the long-term China opportunity.
- **Duopoly/structural competition:** Synopsys (enlarged by Ansys), Siemens EDA, Keysight, plus in-house EDA teams at major chip companies.
- **Revenue-timing lumpiness:** hardware (Palladium/Protium) and IP recognized up-front can swing a quarter's growth/margin even with stable underlying demand.
- **Cyclicality / customer R&D budgets:** ultimately tied to semiconductor and systems-company R&D spend; a broad design-start slowdown would pressure renewals and bookings.

## Intra-quarter — calls, comentários & relatórios (desde o último print)
_Q1 FY26 · May 1 → Jun 11, 2026 · sell-side / expert calls / relatórios entre os earnings. Timeline visual: [timeline.html](timeline.html)._

**Sinal vs gestão** — o posicionamento/guidance da empresa (Current state, sem tabela de evolution) × o que o fluxo intra-quarter está dizendo (✓ confirma · ⚠ nuança · ✗ contesta):

| Tema | Gestão / guidance | Fluxo intra-quarter | Sinal |
|---|---|---|---|
| **Custom-silicon / foundry** | Gestão (10-Q): wave de ASICs custom de hyperscalers é o tailwind mais limpo — mais tape-outs = mais demanda de seat/IP/emulação; "collateral regardless of which foundry wins" | firstadopter/Tae Kim: CDNS assinou IP no nó Intel 14A — citado pela BofA como sinal de credibilidade de foundry no double-upgrade da INTC | **✓ confirma** (ganha em qualquer foundry) |
| **Crescimento / print** | Q1 FY26 rev $1.474B, +18,7% y/y; backlog (RPO) $8,0B; China $189M (+36%) | (sem fluxo intra-quarter contestando) | **✓ confirma** (sem contraponto) |

**Log completo** (todo o fluxo intra-quarter, por data):

| Data | Fonte | Tema | Viés | O que disse |
|---|---|---|---|---|
| 06-11 | firstadopter / Tae Kim (briefing) | produto | bull | CDNS signed for IP on Intel's 14A node — cited by BofA as a foundry-credibility signal in the INTC double-upgrade, and a reminder that Cadence earns collateral regardless of which foundry/customer wins the node war. |

**Síntese do quarter:** fluxo intra-quarter raso — o único datapoint material (assinatura de IP no Intel 14A) confirma a tese de gestão de que a CDNS captura valor independentemente de qual foundry/cliente vença a guerra de nós; debate ainda gira em torno da normalização do mix recorrente e de um eventual guide-raise no Q2.

## Sources
- **Filings (16):** [CDNS_10-K_2023-02-13_0000813672-23-000011.html](../CDNS/CDNS_10-K_2023-02-13_0000813672-23-000011.html), [CDNS_10-K_2024-02-14_0000813672-24-000034.html](../CDNS/CDNS_10-K_2024-02-14_0000813672-24-000034.html), [CDNS_10-K_2025-02-21_0000813672-25-000024.html](../CDNS/CDNS_10-K_2025-02-21_0000813672-25-000024.html), [CDNS_10-K_2026-02-19_0000813672-26-000016.html](../CDNS/CDNS_10-K_2026-02-19_0000813672-26-000016.html), [CDNS_10-Q_2022-07-25_0000813672-22-000037.html](../CDNS/CDNS_10-Q_2022-07-25_0000813672-22-000037.html), [CDNS_10-Q_2022-10-24_0000813672-22-000054.html](../CDNS/CDNS_10-Q_2022-10-24_0000813672-22-000054.html)
- **Briefings:** [roll-up](../_briefings/by-ticker/CDNS.md)
- **Research reports (relatórios bons):**
  - [Barron's Tech Roundtable — 4 Experts on the Next Phase of AI and 22 Favorite Stocks](../relat%C3%B3rios%20bons/Barrons_Tech_Roundtable__Our_4_Experts_on_the_Next_Phase_of_AIand_22_Favorite_Stocks_-_Barrons.html)
  - [MS Scale-Up Network Primer](../relat%C3%B3rios%20bons/Scale_up_primer_MS.html)
  - [DeepResearch TSM](../relat%C3%B3rios%20bons/DeepResearch_TSM.html)
