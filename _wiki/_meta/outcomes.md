# Catalyst outcomes ledger

One line per resolved catalyst. build_catalysts.py reads this to know which
past-due catalysts already have a post-mortem; the rest get flagged ⏰.

Format (ticker + the catalyst date, then the verdict):
    - TICKER YYYY-MM-DD — bull won | bear won | neutral — one-line note

Examples:
    - NVDA 2026-08-26 — bull won — Q2 beat + raise, GM held mid-70s
    - TSLA 2026-XX-XX — bear won — robotaxi ramp slipped, out-year EPS cut

Add lines here after each catalyst resolves. Newest first.
