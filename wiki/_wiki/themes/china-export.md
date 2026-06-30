# Theme — China AI Buildout & Export Controls

_Wiki · generated 2026-06-25 · cross-company theme · sources: equity calls, briefing roll-ups, earnings transcripts, research library, Twitter/X corpus (ported from research-wiki). Company pages: [../00_INDEX.md](../00_INDEX.md) · themes index: [00_THEMES.md](00_THEMES.md)._

## What it is / why it matters

The dual dynamic shaping semicap and foundry exposure to China: **export controls limiting what US/Dutch vendors can sell** while **China accelerates a domestic AI hardware stack** (Huawei Ascend + SMIC) that is structurally chip-count-inflationary, supporting domestic foundry/WFE demand even as US equipment names lose China revenue. China was 30–35% of WFE revenue for US semicap names (AMAT >30%, LRCX higher) pre-restrictions. Export controls cap that mix but simultaneously drive a China domestic buildout (Huawei Ascend roadmap, SMIC 7nm ramp, Hua Hong, NAURA/AMEC) that is **chip-count-inflationary** — Huawei's cluster architecture uses ~114× more chips vs Nvidia to achieve comparable aggregate compute. Net impact on global WFE and foundry capex is ambiguous; it depends on whether domestic China capex offsets the US-vendor revenue loss.

## State of play (latest)

- **Huawei advanced packaging (hybrid bonding):** Huawei **1.5µm hybrid bonding pitch** in 2026 Kirin smartphones — surpasses TSMC (just moved to 6µm SoIC; next step 4.5µm for **2030** products) and Intel (Foveros Direct at 9µm); roadmap to **1µm pitch by 2027**. "Necessity is the mother of innovation." Export controls blocked logic process scaling but did not block packaging innovation (SA @semianalysis_, May 2026; 75k views, 402 likes).
- **SMIC process technology (SA STEEL Lab, first public teardown):** **SMIC N+3 metal pitch 32.5nm** — ~10% tighter than Intel 18A (36nm) on Panther Lake. But "SMIC wins on metal pitch" is incomplete: N+3 reaches TSMC N6-class density **through aggressive DUV multi-patterning** (not EUV) — same density at higher process complexity, cost risk, and lower maturity. Kirin 9030 (N+3) performs similarly to **3-year-old Android flagships**; trails Apple/Qualcomm/MediaTek/Samsung current flagships. "Forced a different path, not stopped progress." Huawei τ-scaling and LogicFolding (active logic stacking + 3D packaging) show an alternative density path via STCO. CXMT + Samsung memory mix found in Huawei phones (@jukan05 analysis) (SA, SMIC N+3 Deep Dive + STEEL Lab launch, Jun 2026).
- **DeepSeek going heavy-asset:** posted job openings for IDC planning engineers scoped to "MW-to-GW scale infrastructure" (Jun 9); follows April hiring of O&M engineers in Ulanqab, Inner Mongolia. "First time DeepSeek has fully shown its hand on owning compute infrastructure" — no longer just an inference-efficiency player; now building sovereign compute capacity (SA @SemiAnalysis_, Jun 2026 / 2026-06-10; 104k views, 474 likes).
- **DeepSeekV4 / Huawei inference:** **Huawei 950DT Day-0 inference** benchmarked for the first time; DeepSeekV4 "co-designed in part for Huawei Ascend inference." "China currently dominates the open model landscape" — Kimi K2.6 beats NVIDIA's Nemotron 3 Ultra on coding. AMD ROCm also benchmarked: DeepSeekV4 performance improved **100× in 26 days** (AMD SGLang Day 0 → Day 26) (SA, DeepSeekV4 Day 0 to Day 43, Jun 2026).
- **Huawei / China domestic AI stack (Bernstein, Huawei Roadmap, 2025-09-22):** Ascend 950 single chip is ~**6%** the performance of Nvidia VR200, but UB networking deploys **114× more chips per SuperPoD** to achieve **6.8× higher total compute** vs NVL144 — WFE-inflationary by chip-count alone. Ascend roadmap: 950PR (1Q26) → 950DT (4Q26, **2 PFLOPS FP4**, 144GB HBM, 4 TB/s) → 960 (4Q27) → 970 (4Q28, **8 PFLOPS FP4**, 288GB, 14.4 TB/s). Atlas SuperPoD: Atlas 950 (4Q26) = **8,192 NPUs**, 8/16 EFLOPS FP8/FP4, 16.3 PB/s interconnect; Atlas 960 (4Q27) = **15,488 NPUs**, 30/60 EFLOPS FP8/FP4, 34 PB/s. Atlas 960 SuperCluster: **>1 million chips** to deliver 4 ZFLOPS FP4; FT reports local AI production capacity set to **triple in 2026**. Cluster comparison vs Nvidia: Atlas 950 vs NVL144 = **113.8× NPU count, 6.8× cluster FP8, 63.0× interconnect bandwidth, 15.4× memory capacity** (0.06× per-chip perf); Atlas 960 vs NVL576 = 107.6× NPUs, 6.5× cluster FP8, 22.7× interconnect, 12.2× memory (Bernstein, Huawei Roadmap, 2025-09-22).
- **China foundry & domestic semicap (Bernstein, Huawei Roadmap, 2025-09-22):** SMIC **7nm capacity expansion** directly supports Huawei accelerator production; SMIC H-share **Outperform HKD 30** (A-share CNY 110, 1.5× NTM P/B); Hua Hong H HKD 60 / A CNY 85 (2.0× P/B H, 55% A/H premium, Outperform). China semicap PTs (all **Outperform**): NAURA **CNY 450**, AMEC **CNY 300**, Piotech **CNY 300**. AI fabless: Hygon **CNY 220** (Outperform — leading domestic x86 server CPU on AMD license); Cambricon CNY 1,100 (Market-Perform — best Huawei alternative but overvalued).
- **Tariffs & export-control macro (Bernstein Deck Maio25, 2025-05-05):** tariffs "the dominant swing factor" for Asian semis; **long delivery times protect TSMC/HBM CY25 earnings** but delay tariff damage to late CY25/CY26. Mature-node foundry under ongoing China competition pressure. UMC **Underperform TWD 32.0** (vs cons 45.8, −29%). Memory names (Outperform): Samsung **KRW 82,000** (vs cons 70,893); SK Hynix **KRW 240,000**; Micron **USD 120** (vs cons 127) — mainstream memory pricing inflecting up but sustainability subject to tariff path.

## Key debates

- **Bull / China-neutral / offset:** domestic AI buildout (Huawei Ascend + SMIC ramp) inflates WFE demand globally; local semicap vendors (NAURA, AMEC, Piotech) gain share; foundry (SMIC, Hua Hong) expand. Net WFE not much lower; US names shift product mix to leading-edge (research-wiki synthesis).
- **Bear / export-control:** US vendors permanently lose the 25–35% revenue bucket; China domestic tools are 1–2 generations behind; SMIC/Hua Hong can't produce HBM or leading-edge logic below 7nm at scale; the domestic-substitute timeline is long (research-wiki synthesis).
- **Timeline / inflection points:** Huawei packaging roadmap to 1µm pitch by 2027 (SA, May 2026); local AI production capacity tripling in 2026 (Bernstein, 2025-09-22); tariff damage delayed to late CY25/CY26 by long delivery times (Bernstein, 2025-05-05); DeepSeek sovereign-compute buildout now underway (SA, 2026-06-10).

## Who's exposed (companies)

| Ticker | Angle | Read |
|---|---|---|
| [ASML](../ASML.md) | DUV sales to China restricted; SMIC DUV-multi-patterning watch | Net export-control headwind; SMIC reaching N6-class density via DUV multi-patterning, no EUV access (SA STEEL Lab, Jun 2026) |
| [AMAT](../AMAT.md) | Largest China revenue exposure among US semicap names (>30% pre-restrictions) | Most exposed to the China-mix ceiling; offset hinges on domestic capex (Bernstein, 2025-05-05) |
| [LRCX](../LRCX.md) | Elevated China NAND/DRAM exposure pre-restrictions; mix-shift watch | Watch ongoing China mix shift (Bernstein, 2025-05-05) |
| [KLAC](../KLAC.md) | Inspection tools; China local alternatives lagging on process-control intensity | Relatively defended — local alternatives lag on PC intensity (research-wiki) |
| [INTC](../INTC.md) | 18A process compared directly vs SMIC N+3 in SA STEEL Lab teardown | 18A 36nm metal pitch vs SMIC N+3 32.5nm; Foveros Direct 9µm vs Huawei 1.5µm hybrid bonding (SA, Jun 2026 / May 2026) |
| [SMIC](../SMIC.md) | Domestic foundry; 7nm/N+3 ramp supporting Huawei accelerators | Capacity expansion supports Huawei; density via DUV multi-patterning (Bernstein, 2025-09-22; SA STEEL Lab, Jun 2026) |
| [TSM](../TSM.md) | Leading-edge foundry; SoIC packaging benchmark vs Huawei | 6µm SoIC now, 4.5µm for 2030 — Huawei ahead on hybrid-bonding pitch (SA, May 2026); long delivery times protect CY25 earnings (Bernstein, 2025-05-05) |
| [SAMSUNG](../SAMSUNG.md) | Memory vendor; mix found in Huawei phones | Bernstein Outperform KRW 82,000 (vs cons 70,893) (Bernstein, 2025-05-05) |
| [SKHYNIX](../SKHYNIX.md) | Memory vendor | Bernstein Outperform KRW 240,000 (Bernstein, 2025-05-05) |
| [MU](../MU.md) | Memory vendor | Bernstein Outperform USD 120 (vs cons 127) (Bernstein, 2025-05-05) |
| [AMD](../AMD.md) | ROCm benchmarked on DeepSeekV4; x86 server CPU licensed to Hygon | DeepSeekV4 perf +100× in 26 days on AMD SGLang (SA, Jun 2026); Hygon on AMD license (Bernstein, 2025-09-22) |
| NAURA / AMEC / Piotech | Domestic China semicap — share gainers | Bernstein Outperform CNY 450 / 300 / 300 (2025-09-22). No destination pages |
| Hua Hong / Hygon / Cambricon / Huawei-HiSilicon | Domestic foundry / fabless / accelerator | Hua Hong/Hygon Outperform; Cambricon Market-Perform (Bernstein, 2025-09-22). No destination pages |
| UMC | Mature-node foundry under China competition | Bernstein Underperform TWD 32.0 (vs cons 45.8, −29%) (2025-05-05). No destination page |

## Sources

- **Sell-side / research library:** Bernstein (Huawei Roadmap, 2025-09-22 — Ascend/Atlas roadmap, chip-count inflation, China semicap PTs); Bernstein (Deck Maio25, 2025-05-05 — tariffs, UMC, memory PTs).
- **Twitter/X corpus / SA:** Huawei hybrid bonding 1.5µm (May 2026); SMIC N+3 STEEL Lab teardown (Jun 2026); DeepSeek heavy-asset / IDC buildout (2026-06-10); DeepSeekV4 Huawei 950DT inference (Jun 2026); @jukan05 (CXMT + Samsung memory mix).
- **Company pages:** [ASML](../ASML.md) · [AMAT](../AMAT.md) · [LRCX](../LRCX.md) · [KLAC](../KLAC.md) · [INTC](../INTC.md) · [SMIC](../SMIC.md) · [TSM](../TSM.md) · [SAMSUNG](../SAMSUNG.md) · [SKHYNIX](../SKHYNIX.md) · [MU](../MU.md) · [AMD](../AMD.md).
- **Related themes:** [HBM / memory super-cycle](hbm-memory.md) · [Semicap / WFE](semicap-wfe.md).

## Changelog
- 2026-06-25 — page created; ported from research-wiki corpus.
