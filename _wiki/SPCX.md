<!-- Per-company wiki page. Synthesizes the IPO prospectus (424B4 / S-1) + FinTwit. Every datapoint sourced.
     THESIS-DRIFT RULE: move superseded numbers/views into ## Changelog with a date — don't overwrite. -->

# SPCX — Space Exploration Technologies Corp.

_Wiki · generated 2026-06-29 · sources: IPO prospectus (424B4 2026-06-12 / S-1 2026-05-20, archived in `../SPCX/`) + FinTwit. **Newly public — IPO'd June 2026 (Nasdaq: SPCX).** Master index: [../INDEX.md](../INDEX.md). Themes: [ai-datacenter-power](themes/ai-datacenter-power.md) · [custom-asic-tpu](themes/custom-asic-tpu.md)._

> ⚠️ **Page corrected 2026-06-29:** SpaceX is **not private** — it completed the largest IPO on record (~$75B raised) and absorbed **xAI** (Grok, X, AI compute) in Feb 2026. The earlier "private, single-tweet" version of this page was wrong; superseded facts are in the [Changelog](#changelog).

## Snapshot
Space Exploration Technologies Corp. (SpaceX, **Nasdaq: SPCX**, Texas-incorporated) is Elon Musk's vertically-integrated space-and-AI conglomerate. Post the **February 2026 acquisition of xAI**, it reports in **three segments** (424B4 2026-06-12):
- **Connectivity** — Starlink LEO broadband + direct-to-cell: **~10.3M Starlink subscribers** across 164 countries; **~7.4M monthly unique devices** for direct-to-cell/messaging across ~30 countries.
- **Launch** — Falcon 9 / Falcon Heavy / Dragon (operational, reusable) + **Starship** (Super Heavy + upper stage, in development); the launch backbone that uniquely enables the orbital-compute ambition.
- **AI** (ex-xAI) — **Grok** frontier models, **X** (social/advertising), and **AI compute** — the COLOSSUS / COLOSSUS II training clusters.

**FY2025 total revenue $17.2bn** (FY24 $12.5bn, FY23 $9.3bn); pro-forma (incl. xAI) **net loss attributable to common shareholders ~$(4.9)bn** in FY2025, driven by AI-segment compute scaling (424B4). It sits at the intersection of three of this wiki's biggest themes — AI compute/datacenter power, satellite connectivity, and reusable launch.

## The IPO (424B4, 2026-06-12 · Reg. No. 333-296070)
- **555,555,555 Class A shares at $135.00** → **~$75.0bn gross** (the largest IPO on record); underwriting discount $0.90/sh (~$500M); net proceeds ~$74.5bn before expenses. Over-allotment: up to 83,333,333 additional shares.
- **Listing:** Nasdaq + **Nasdaq Texas** under **SPCX**.
- **Dual-class control:** Class A = 1 vote, Class B = 10 votes. **Musk holds ~82.4% of voting power** post-IPO → SPCX is a **"controlled company"** (relies on Nasdaq governance exemptions). Musk's Class B vests against extreme milestones — market-cap tranches **plus a permanent Mars colony (≥1M people)** and **non-Earth-based datacenters delivering 100 Tbps** (424B4).
- **Shares outstanding post-IPO:** ~7.38bn Class A + ~5.70bn Class B ≈ **~13.1bn total** → implied equity value very roughly **~$1.7–1.8tn** at the $135 IPO price (computed; SPCX did not print an explicit market cap — treat as ESTIMATE).
- **Use of proceeds:** fund growth — **expansion of AI compute infrastructure**, launch infrastructure/vehicles, and scale/capacity (424B4).

## AI compute — the neocloud / datacenter story (the reason this name is here)
- **COLOSSUS (Memphis, TN) + COLOSSUS II (Memphis + Southaven, MS)** — described as the **largest AI training data center clusters on Earth**; collectively **~1.0 GW of compute power** today (424B4). SpaceX claims it was **first to deploy a coherent gigawatt-scale AI training cluster (2026)**; built COLOSSUS's first cluster in **122 days**, COLOSSUS II's in **91 days**, at per-MW construction cost "considerably below industry benchmarks."
- **~325,000 NVIDIA GPUs** across COLOSSUS / COLOSSUS II (disclosed via the Cursor compute agreement), backed by hyperscale CPUs, exabyte storage and high-speed interconnect.
- **GPU sourcing:** all GPUs procured **purchase-order basis, no long-term supplier contracts** — flagged as a supply-concentration risk (depends on a concentrated set of advanced fabs).
- **Terafab** — chip-manufacturing initiative **with Tesla and Intel** (framework announced Mar 2026); long-term goal **~1 terawatt of compute hardware per year** → vertical integration into chip design/manufacturing.
- **Cursor (Anysphere) — Apr 2026 compute + option agreement:** SPCX provides Cursor GPU-cluster capacity and gets a **right (not obligation) to acquire Cursor** at a predetermined price; tied to an implied Cursor equity value of ~$60bn (424B4, "Recent Developments"). Drives inference demand + developer-interaction data.
- **Orbital compute ambition:** stated goal to **launch ~100 GW of compute to space per year** via satellites carrying >100 kW compute/metric ton — "AI compute satellites" / "non-Earth-based datacenters." This is the moonshot the launch business is meant to enable (and is explicitly flagged as unproven/uncertain timeline).

## Reconciling the Jeff Pu datapoint with the filing
- **Jeff Pu (@sssjeffpu, 2026-06-29):** SpaceX neocloud **1 GW (2026) → 4.5 GW (2027) → 9.5 GW (2028)**; **~2.2M / 2.5M Blackwell-equivalent GPUs in 2027 / 2028**; **new Buy on [CRDO](CRDO.md)** off the connectivity read-through.
- **Maps onto disclosure:** Pu's **1 GW 2026 = the company's ~1.0 GW COLOSSUS+II today** (HARD anchor). The **4.5→9.5 GW** ramp and the **2.2M/2.5M GPU** figures are **Pu's estimates**, not company guidance — but they're directionally consistent with SPCX's stated aggressive scaling and the IPO's "expand AI compute" use-of-proceeds. The ~325k GPUs disclosed today → ~2.2M by 2027 implies a ~7x ramp (Pu's model).
- **Read-throughs if the ramp is real:** [NVDA](NVDA.md) (Blackwell/Rubin units), [CRDO](CRDO.md)/[ALAB](ALAB.md)/[MRVL](MRVL.md) (AEC/optical/retimer content per GPU), [ai-datacenter-power](themes/ai-datacenter-power.md) (1→9.5 GW firm-power step-change). Pu's CRDO Buy is the explicit connectivity play on this.

## Debate / thesis
- **Bull:** Unique vertical integration — the only entity pairing frontier AI (Grok/xAI), gigawatt-scale terrestrial compute (COLOSSUS), a dominant satellite-connectivity franchise (Starlink ~10.3M subs), reusable launch (Falcon/Starship) and a chip ambition (Terafab). Fast, low-cost datacenter construction (91–122 days/cluster, below-benchmark per-MW cost). Starlink is the cash-generative anchor; the orbital-compute angle is asymmetric optionality. New incremental AI-compute demand node for the supply chain (Jeff Pu CRDO Buy, 2026-06-29).
- **Bear:** **Deep losses** — pro-forma net loss ~$(4.9)bn FY2025, AI-segment Adj. EBITDA **$(1,237)M in 2025** (from +$347M in 2024) and **$(609)M in Q1-26** as it scales compute. **Extreme key-man / governance risk** — Musk ~82.4% voting, controlled-company exemptions, Class B vesting tied to a literal Mars colony. **GPU supply on purchase-orders only** (no long-term contracts). The 100 GW-to-orbit goal is explicitly unproven. Valuation (~$1.7tn+ implied) prices in enormous execution.
- **Where the sell-side stands:** brand-new issue (priced 2026-06-12) — formal coverage is just initiating. Jeff Pu's connectivity read-through (CRDO new Buy) is the first in-corpus datapoint; no SPCX consensus/PT set yet.

## Catalysts / what to watch
- **First post-IPO earnings** (Q2 2026) — first public read on segment revenue (Connectivity vs Launch vs AI), AI-segment cash burn, and the compute capex run-rate.
- **Compute ramp** — COLOSSUS II scale-up; whether installed GPUs trend toward Pu's ~2.2M (2027) / ~2.5M (2028); the next GW milestones (4.5 GW Pu '27 est).
- **Terafab** — any concrete Tesla/Intel chip-manufacturing progress (the 1 TW/yr hardware goal).
- **Cursor option** — exercise/acquire decision and its implied valuation.
- **Starship cadence** — gating for both Starlink V3 deployment and the orbital-compute ambition.
- **Lock-up expiry** — all pre-IPO shares subject to restriction; eventual unlock is a supply overhang.

## Risks
- **Profitability / cash burn** — multi-billion net losses; AI segment deeply EBITDA-negative while scaling.
- **Key-man & governance** — Musk control (~82.4% vote), controlled-company exemptions, Mars/Tbps milestone vesting; concentrated decision-making.
- **GPU / supply concentration** — purchase-order-only GPU procurement; dependence on a concentrated set of advanced fabs and on power availability.
- **Execution / unproven moonshots** — 100 GW orbital compute, Terafab (1 TW/yr), Starship — all explicitly uncertain in the prospectus.
- **Valuation** — ~$1.7tn+ implied equity value on a still loss-making, capex-heavy combination.
- **Regulatory** — spectrum, launch licensing, AI/chatbot safety (Grok), cross-border satellite operations.

<!-- Consensus estimates (BBG) block auto-injected here by the HTML builder once estimates exist -->

## Sources
- **Prospectus (definitive):** [424B4 — final IPO prospectus (2026-06-12)](../SPCX/SPCX_424B4_2026-06-12.html) · [SEC](https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm) — Reg. No. 333-296070; $135.00/sh; 555,555,555 shares; SPCX on Nasdaq/Nasdaq Texas.
- **Registration:** [S-1 (2026-05-20)](../SPCX/SPCX_S-1_2026-05-20.html) · [SEC](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm). IPO trail: DRS 2026-03-30 → S-1 2026-05-20 → S-1/A 06-01 & 06-03 → EFFECT 06-11 → 424B4 06-12 (CIK 0001181412).
- **Archive copy:** `E:\sec-filings\SPCX\` (424B4 + S-1).
- **FinTwit:** Jeff Pu / @sssjeffpu (2026-06-29) — neocloud buildout 1→4.5→9.5 GW (2026-28), ~2.2M/2.5M Blackwell-equiv GPUs (2027/28), CRDO new Buy.

## Changelog
- **2026-06-29 — major correction + S-1/424B4 ingest.** Page had been created earlier the same day as a "**private company — no public financials, single-source tweet**" reference page. That was **wrong**: SpaceX completed its IPO (Nasdaq: SPCX, priced $135.00, ~$75bn raised, 424B4 2026-06-12), and had **acquired xAI in Feb 2026** (Grok/X/AI compute). Rewrote the page off the prospectus: added IPO terms, 3-segment structure, FY2023–25 financials ($9.3 → $12.5 → $17.2bn revenue; ~$(4.9)bn FY25 net loss), COLOSSUS/COLOSSUS II (~1.0 GW, ~325k NVIDIA GPUs), Terafab (Tesla/Intel), Cursor option, and the 100 GW orbital-compute ambition. Jeff Pu's 1 GW-2026 figure now anchored to the company's disclosed ~1.0 GW; his 4.5/9.5 GW and 2.2M/2.5M-GPU figures retained as his estimates.
- 2026-06-29 — page created (original, since superseded). Seeded from the Jeff Pu tweet only.
