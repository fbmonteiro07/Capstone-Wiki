#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily price updater for the SemiCap dashboard.

Fetches Yahoo Finance daily-close prices for the peer set and writes
semicap/live_prices.js:  window.SEMICAP_LIVE_PX = {"ASML":..., "_asof":"YYYY-MM-DD"};

Zero external dependencies (urllib, stdlib) so it runs on a bare GitHub Actions
runner with no `pip install`. Tickers that fail to fetch keep their prior value
(the file is never wiped); if nothing at all is fetched, the file is left
unchanged and the job exits non-zero.

Run locally:  python update_prices.py
Run in CI:    .github/workflows/update-prices.yml (daily cron)
"""
import json
import os
import sys
import datetime
import urllib.request

TICKERS = {  # dashboard ticker -> Yahoo symbol
    "ASML": "ASML", "AMAT": "AMAT", "KLAC": "KLAC",
    "LRCX": "LRCX", "TER": "TER", "AEIS": "AEIS",
}
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; SemiCapBot/1.0)"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "semicap", "live_prices.js")


def yahoo_price(symbol: str) -> float:
    url = ("https://query1.finance.yahoo.com/v8/finance/chart/"
           f"{symbol}?interval=1d&range=1d")
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=25) as resp:
        data = json.load(resp)
    meta = data["chart"]["result"][0]["meta"]
    return round(float(meta["regularMarketPrice"]), 2)


def load_prior() -> dict:
    if not os.path.exists(OUT):
        return {}
    try:
        txt = open(OUT, encoding="utf-8").read()
        return json.loads(txt[txt.index("{"): txt.rindex("}") + 1])
    except Exception:
        return {}


def main() -> int:
    px = {}
    for tk, sym in TICKERS.items():
        try:
            px[tk] = yahoo_price(sym)
            print(f"[ok]   {tk:5} {px[tk]}")
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] {tk:5} fetch failed: {exc}", file=sys.stderr)

    prior = load_prior()
    for tk in TICKERS:                 # carry prior price for any ticker that failed
        if tk not in px and tk in prior and isinstance(prior[tk], (int, float)):
            px[tk] = prior[tk]
            print(f"[keep] {tk:5} {px[tk]} (prior)")

    if not any(tk in px for tk in TICKERS):
        print("[error] no prices fetched and no prior file - leaving unchanged", file=sys.stderr)
        return 1

    px["_asof"] = datetime.date.today().isoformat()
    px["_src"] = "Yahoo Finance daily close"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("window.SEMICAP_LIVE_PX = " + json.dumps(px) + ";\n")
    print(f"[done] wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
