r"""
FEATURE 5 — Catalyst -> outcome feedback loop.

Parses every page's '## Catalysts / what to watch' section into one dated
calendar, then cross-checks past-due catalysts against a hand-kept outcomes
ledger (_meta/outcomes.md). Catalysts whose date has passed WITHOUT a logged
outcome are flagged for a post-mortem (did bull or bear win?) — turning the
wiki from a note-store into something that scores its own calls over time.

    py "E:/Wiki Felipe empresas/_wiki/_tools/build_catalysts.py"

Writes _meta/catalysts.md + _dashboards/catalysts.html, and scaffolds
_meta/outcomes.md if absent. Read-only on company pages.
"""
import sys, re, html, datetime as dt
sys.path.insert(0, str(__import__("pathlib").Path(__file__).parent))
from _wlib import META, DASH, company_pages, read, section, html_head, TODAY, DATE_RE
sys.stdout.reconfigure(encoding="utf-8")

PAST_WINDOW = 180   # only surface recently-passed catalysts for post-mortem (avoid ancient source-date noise)

OUTCOMES_SCAFFOLD = """# Catalyst outcomes ledger

One line per resolved catalyst. build_catalysts.py reads this to know which
past-due catalysts already have a post-mortem; the rest get flagged ⏰.

Format (ticker + the catalyst date, then the verdict):
    - TICKER YYYY-MM-DD — bull won | bear won | neutral — one-line note

Examples:
    - NVDA 2026-08-26 — bull won — Q2 beat + raise, GM held mid-70s
    - TSLA 2026-XX-XX — bear won — robotaxi ramp slipped, out-year EPS cut

Add lines here after each catalyst resolves. Newest first.
"""


def parse_outcomes():
    p = META / "outcomes.md"
    if not p.is_file():
        p.write_text(OUTCOMES_SCAFFOLD, encoding="utf-8")
        return {}
    done = {}
    for ln in read(p).split("\n"):
        m = re.match(r"^\s*[-*]\s+([A-Z]{1,10})\s+(20\d\d-\d\d-\d\d|20\d\d-XX-XX)\s*[—\-–]\s*(.*)$", ln)
        if m:
            done[(m.group(1), m.group(2))] = m.group(3).strip()
    return done


def catalyst_bullets(md):
    """Yield (watch_date|None, text) from the Catalysts section. watch_date = latest date in bullet."""
    body = section(md, r"Catalysts")
    # join wrapped lines into bullets
    bullets, cur = [], None
    for ln in body.split("\n"):
        if re.match(r"^\s*[-*]\s+", ln):
            if cur:
                bullets.append(cur)
            cur = ln.strip()[1:].strip()
        elif cur is not None and ln.strip():
            cur += " " + ln.strip()
    if cur:
        bullets.append(cur)
    for b in bullets:
        # event dates live in the main clause; source citations live in (parens) —
        # strip parentheticals so "(JPM, 2026-06-22)" doesn't masquerade as a catalyst date.
        clause = re.sub(r"\([^)]*\)", "", b)
        ds = DATE_RE.findall(clause)
        wd = max(ds) if ds else None
        yield wd, b


def main():
    done = parse_outcomes()
    upcoming, passed = [], []
    for tk, pf in company_pages():
        for wd, txt in catalyst_bullets(read(pf)):
            if not wd:
                continue
            try:
                d = dt.date.fromisoformat(wd)
            except ValueError:
                continue
            short = re.sub(r"\s+", " ", txt)[:200]
            if d >= TODAY:
                upcoming.append((wd, tk, short))
            elif (TODAY - d).days <= PAST_WINDOW:
                has_outcome = (tk, wd) in done
                passed.append((wd, tk, short, has_outcome, done.get((tk, wd), "")))
    upcoming.sort()
    passed.sort(reverse=True)
    need_pm = [p for p in passed if not p[3]]

    # ---------- markdown ----------
    md = [f"# Catalyst calendar & outcome loop\n",
          f"_Generated {TODAY.isoformat()} · parsed from every page's 'Catalysts / what to watch'. "
          f"Dates are heuristic (latest date in the bullet). Log results in "
          f"`_meta/outcomes.md`. Rebuild: `py _wiki/_tools/build_catalysts.py`._\n",
          f"## 📅 Upcoming ({len(upcoming)})\n",
          "| Date | Ticker | Catalyst |", "|---|---|---|"]
    for wd, tk, txt in upcoming:
        md.append(f"| {wd} | {tk} | {txt} |")
    if not upcoming:
        md.append("| _none parsed_ | | |")
    md.append(f"\n## ⏰ Passed — need a post-mortem ({len(need_pm)})\n")
    md.append("_Date passed, no outcome logged. Decide bull/bear/neutral and add a line to "
              "`_meta/outcomes.md`._\n")
    md.append("| Date | Ticker | Catalyst |")
    md.append("|---|---|---|")
    for wd, tk, txt, _, _ in need_pm:
        md.append(f"| {wd} | {tk} | {txt} |")
    if not need_pm:
        md.append("| _none_ | | |")
    resolved = [p for p in passed if p[3]]
    md.append(f"\n## ✅ Resolved ({len(resolved)})\n")
    md.append("| Date | Ticker | Verdict |")
    md.append("|---|---|---|")
    for wd, tk, txt, _, verdict in resolved:
        md.append(f"| {wd} | {tk} | {verdict} |")
    if not resolved:
        md.append("| _none yet — log them in outcomes.md_ | | |")
    META.mkdir(parents=True, exist_ok=True)
    (META / "catalysts.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # ---------- html ----------
    head, foot = html_head("Catalyst calendar & outcome loop",
                           f"{TODAY.isoformat()} · {len(upcoming)} upcoming · {len(need_pm)} awaiting post-mortem")
    h = [head, "<p class='byline'>Dates heuristic (latest date in each catalyst bullet). "
               "Log results in <code>_meta/outcomes.md</code> to clear the ⏰ flags and build a hit-rate.</p>"]
    h.append(f"<h2>📅 Upcoming ({len(upcoming)})</h2>")
    h.append("<table class='sortable'><thead><tr><th>Date</th><th>Ticker</th><th>Catalyst</th></tr></thead><tbody>")
    for wd, tk, txt in upcoming:
        h.append(f"<tr><td>{wd}</td><td class='tk'>{tk}</td><td>{html.escape(txt)}</td></tr>")
    h.append("</tbody></table>")
    h.append(f"<h2>⏰ Passed — need a post-mortem ({len(need_pm)})</h2>")
    h.append("<table class='sortable'><thead><tr><th>Date</th><th>Ticker</th><th>Catalyst</th></tr></thead><tbody>")
    for wd, tk, txt, _, _ in need_pm:
        h.append(f"<tr><td>{wd}</td><td class='tk'><span class='pill due'>⏰</span> {tk}</td>"
                 f"<td>{html.escape(txt)}</td></tr>")
    h.append("</tbody></table>")
    if resolved:
        h.append(f"<h2>✅ Resolved ({len(resolved)})</h2>")
        h.append("<table><thead><tr><th>Date</th><th>Ticker</th><th>Verdict</th></tr></thead><tbody>")
        for wd, tk, txt, _, verdict in resolved:
            h.append(f"<tr><td>{wd}</td><td class='tk'>{tk}</td><td>{html.escape(verdict)}</td></tr>")
        h.append("</tbody></table>")
    h.append(foot)
    DASH.mkdir(parents=True, exist_ok=True)
    (DASH / "catalysts.html").write_text("\n".join(h), encoding="utf-8")

    print(f"catalysts: {len(upcoming)} upcoming, {len(need_pm)} need post-mortem, "
          f"{len(resolved)} resolved")
    print(f"  -> {META/'catalysts.md'}\n  -> {DASH/'catalysts.html'}\n  -> {META/'outcomes.md'} (ledger)")


if __name__ == "__main__":
    main()
