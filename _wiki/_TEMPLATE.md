<!-- TEMPLATE for per-company wiki pages. Each page synthesizes the co-located sources
     (filings + transcripts + decks + equity calls + briefing roll-up) with attribution.
     Keep it tight (~1.5-2 pages), buy-side voice, every datapoint sourced.
     The "Consensus estimates (BBG)" block is auto-injected by build_wiki_html.py from
     _data/estimates.json — do NOT hand-write it.
     THESIS-DRIFT RULE: never silently overwrite a number, rating, PT or thesis. When a new
     datapoint supersedes an old one, move the old value into the ## Changelog section with the
     date, then update the body. The drift over time is the alpha (this wiki is not git-tracked,
     so the Changelog IS the history). -->

# <TICKER> — <Company name>

_Wiki · generated <YYYY-MM-DD> · sources: `E:\Wiki Felipe\<TICKER>` (filings + transcripts + decks) · `_equity_calls` · `_briefings\by-ticker\<TICKER>.md`. Master index: [../INDEX.md](../INDEX.md)._

## Snapshot
What the company does, segment/revenue mix, and where it sits in the chain (AI / semis / power / internet). 3-5 lines.

## Current state (latest quarter)
Numbers and messaging from the **most recent transcript** (date) + guidance. Growth, margins, capex/demand. Attribute: "Q_ FY__ (date)".

## Debate / thesis
- **Bull:** key arguments (with source: broker/analyst/call + date).
- **Bear:** key risks to the thesis (same).
- **Where the sell-side/buy-side stands:** recent ratings/PTs from briefings and equity calls, attributed.

## Catalysts / what to watch
Upcoming prints, investor days, regulatory decisions, product ramps — with dates where available.

## Risks
Company-specific (from the 10-K/10-Q + the debate). Short bullets.

<!-- Consensus estimates (BBG) block auto-injected here by the HTML builder -->

## Sources
- **Filings:** the relevant 10-K/10-Q/20-F (relative link `../<TICKER>/<file>.html`).
- **Transcripts:** the ones used (`../<TICKER>/transcripts/<file>.md`).
- **Decks:** if cited.
- **Equity calls:** N attributed calls (see the <TICKER> section in [INDEX](../INDEX.md)).
- **Briefings:** [roll-up](../_briefings/by-ticker/<TICKER>.md) — if present.

## Changelog
<!-- One dated line per material change. Move superseded numbers/ratings/PTs/theses here
     (with the old value + date) instead of deleting them. Newest first. -->
- <YYYY-MM-DD> — page created.
