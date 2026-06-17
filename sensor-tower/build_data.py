# -*- coding: utf-8 -*-
"""
ETL: Sensor Tower base.xlsx  ->  data.js  (window.ST = {...})
Parses every sheet into clean, charting-ready series.
Run via refresh.bat (or: python build_data.py)
"""
import openpyxl, io, json, os, datetime, unicodedata, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "data.js")

def resolve_src():
    """Source workbook path. Kept out of git so the internal share path is not
    published. Resolution order:
      1) env var SENSOR_TOWER_XLSX
      2) source_path.txt next to this script (one line with the full path)
      3) 'Sensor Tower base.xlsx' next to this script
    """
    p = os.environ.get("SENSOR_TOWER_XLSX")
    if p:
        return p
    cfg = os.path.join(HERE, "source_path.txt")
    if os.path.exists(cfg):
        with io.open(cfg, encoding="utf-8") as fh:
            line = fh.read().strip()
        if line:
            return line
    return os.path.join(HERE, "Sensor Tower base.xlsx")

SRC = resolve_src()
if not os.path.exists(SRC):
    sys.exit(f"Source workbook not found: {SRC}\n"
             f"Set env SENSOR_TOWER_XLSX or create source_path.txt with the path.")

# ---- canonical apps -------------------------------------------------------
APPS = ["ChatGPT", "Google Gemini", "DeepSeek", "Grok",
        "Microsoft Copilot", "Meta AI", "Perplexity", "Claude", "Sora"]

def norm(s):
    """normalise an app label: strip zero-width chars / spaces, map aliases"""
    if s is None:
        return ""
    s = "".join(ch for ch in str(s) if unicodedata.category(ch)[0] != "C")
    s = s.replace("​", "").strip()
    low = s.lower()
    alias = {
        "chatgpt": "ChatGPT",
        "google gemini": "Google Gemini", "gemini": "Google Gemini",
        "deepseek": "DeepSeek",
        "grok": "Grok",
        "microsoft copilot": "Microsoft Copilot", "copilot": "Microsoft Copilot",
        "meta ai": "Meta AI",
        "perplexity": "Perplexity",
        "claude": "Claude",
        "sora": "Sora",
    }
    return alias.get(low, s)

def num(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        f = float(v)
        if f != f:           # NaN
            return None
        return f
    s = str(v).strip()
    if s in ("", "#DIV/0!", "#N/A", "#VALUE!", "#REF!", "-"):
        return None
    try:
        return float(s.replace(",", ""))
    except ValueError:
        return None

def iso(d):
    return d.strftime("%Y-%m-%d") if hasattr(d, "strftime") else None
def isomonth(d):
    return d.strftime("%Y-%m") if hasattr(d, "strftime") else None

wb = openpyxl.load_workbook(SRC, read_only=True, data_only=True)
def grid(name):
    return [list(r) for r in wb[name].iter_rows(values_only=True)]

# ===========================================================================
# 1) MONTHLY METRICS  (AI Apps Global / US)
# ===========================================================================
# metric title keyword -> key   (most specific first!)
METRIC_RULES = [
    ("time spent per mau", "timePerMau"),
    ("time spent per dau", "timePerDau"),
    ("downloads",          "downloads"),
    ("maus",               "mau"),
    ("daus",               "dau"),
    ("time spent",         "timeSpent"),
]
def metric_key(title):
    t = title.lower()
    for kw, key in METRIC_RULES:
        if kw in t:
            return key
    return None

def month_axis(rows):
    """canonical monthly columns = first contiguous run of month-end dates."""
    best = None
    for r in rows:
        cols = [(i, c) for i, c in enumerate(r) if hasattr(c, "strftime")]
        if len(cols) >= 12:
            best = cols
            break
    # keep the first contiguous monthly run (drops the 'Sort' helper block)
    keep = []
    prev = None
    for i, d in best:
        if prev is None or (0 < (d.year*12+d.month) - (prev.year*12+prev.month) <= 1):
            keep.append((i, d)); prev = d
        else:
            break
    idxs = [i for i, _ in keep]
    months = [isomonth(d) for _, d in keep]
    return idxs, months

def parse_monthly(sheet):
    rows = grid(sheet)
    col_idx, months = month_axis(rows)
    first_data_col = col_idx[0]
    out = {}                      # key -> {app -> [vals]}
    cur = None
    for r in rows:
        # detect a metric title: a text cell (before the data cols) holding a keyword
        title_cell = None
        for c in r[:first_data_col]:
            if isinstance(c, str) and metric_key(c):
                title_cell = c; break
        if title_cell:
            k = metric_key(title_cell)
            cur = k
            out.setdefault(k, {})
            continue
        if cur is None:
            continue
        # app row? find an app name in the label columns
        app = None
        for c in r[:first_data_col]:
            n = norm(c)
            if n in APPS:
                app = n; break
        if app is None:
            continue
        if app in out[cur]:        # keep first occurrence only
            continue
        out[cur][app] = [num(r[i]) if i < len(r) else None for i in col_idx]
    # derived: dau/mau stickiness
    out["dauMau"] = {}
    for app in APPS:
        dau = out.get("dau", {}).get(app)
        mau = out.get("mau", {}).get(app)
        if dau and mau:
            out["dauMau"][app] = [
                (d/m if (d is not None and m not in (None, 0)) else None)
                for d, m in zip(dau, mau)
            ]
    return months, out

g_months, g_metrics = parse_monthly("AI Apps (Global)")
u_months, u_metrics = parse_monthly("AI Apps (US)")
assert g_months == u_months, "month axes differ"
MONTHS = g_months

# ===========================================================================
# 2) DAILY / WEEKLY ABSOLUTE TRENDS
# ===========================================================================
def parse_trends(sheet):
    rows = grid(sheet)
    hdr = rows[0]
    # locate the two blocks via their header labels
    def block_cols(start):
        m = {}
        for i in range(start, len(hdr)):
            n = norm(hdr[i])
            if n in APPS:
                m[i] = n
            elif hdr[i] not in (None, "") and m:
                break
        return m
    # left block right after col0; right block after first blank gap
    left = block_cols(1)
    gap = max(left) + 1 if left else 1
    while gap < len(hdr) and norm(hdr[gap]) not in APPS:
        gap += 1
    right = block_cols(gap)
    def harvest(date_col, colmap):
        dates, series = [], {a: [] for a in colmap.values()}
        prev = None
        for r in rows[1:]:
            d = r[date_col] if date_col < len(r) else None
            if not hasattr(d, "strftime"):
                continue
            if prev is not None and d <= prev:   # growth block restarts -> stop
                break
            prev = d
            dates.append(iso(d))
            for ci, app in colmap.items():
                series[app].append(num(r[ci]) if ci < len(r) else None)
        return dates, series
    ldates, lseries = harvest(0, left)
    # right block date col = the column just left of its first app col
    rdate = min(right) - 1
    rdates, rseries = harvest(rdate, right)
    return (ldates, lseries), (rdates, rseries)

(d_dates, d_dau), (dd_dates, d_dl) = parse_trends("Daily Trends")
(w_dates, w_wau), (wd_dates, w_dl) = parse_trends("Weekly Trends")

# ===========================================================================
# 3) AI CHATBOT MARKET SHARE  (Statcounter, WW + US)
# ===========================================================================
def parse_share():
    rows = grid("AI Chatbot Market Share")
    hdr = rows[0]
    # find the two region blocks (each: date header then vendor headers)
    def region(date_col):
        vendors = {}
        for i in range(date_col+1, len(hdr)):
            h = hdr[i]
            if h in (None, ""):
                break
            vendors[i] = str(h).strip()
        dates, series = [], {v: [] for v in vendors.values()}
        for r in rows[1:]:
            d = r[date_col] if date_col < len(r) else None
            if not hasattr(d, "strftime"):
                continue
            dates.append(iso(d))
            for ci, v in vendors.items():
                series[v].append(num(r[ci]))
        return dates, series
    # WW block starts col0; US block: find 2nd date header column
    us_col = None
    for i in range(1, len(hdr)):
        if isinstance(hdr[i], str) and hdr[i].strip().lower() in ("u.s.", "us", "united states"):
            us_col = i; break
    ww_dates, ww = region(0)
    us_dates, us = region(us_col)
    return {"dates": ww_dates, "WW": ww, "US": us}

share = parse_share()

# ===========================================================================
# 4) GEMINI RELEASES (timeline)
# ===========================================================================
def parse_gemini():
    rows = grid("Gemini Releases")
    out = []
    mon = {"jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,"jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12}
    for r in rows:
        cells = [c for c in r if c not in (None, "")]
        if len(cells) >= 2 and isinstance(cells[0], str) and "'" in cells[0]:
            lab = cells[0].strip().lower().replace("’", "'")
            try:
                mm, yy = lab.split("'")
                m = mon[mm.strip()[:3]]; y = 2000 + int(yy.strip())
                out.append({"month": f"{y:04d}-{m:02d}", "label": str(cells[1]).strip()})
            except Exception:
                pass
    return out

gemini = parse_gemini()

# ===========================================================================
# 5) AI WEB VISITS (web traffic by company, millions)
# ===========================================================================
def parse_web():
    rows = grid("AI Web")
    out = []
    for r in rows:
        if len(r) >= 4 and isinstance(r[2], str) and num(r[3]) is not None:
            out.append({"company": r[2].strip(), "visitsM": num(r[3])})
    out.sort(key=lambda x: -x["visitsM"])
    return out

web = parse_web()

# ===========================================================================
# 6) SORA  (launch downloads, DAUs, retention, vs Threads)
# ===========================================================================
def col_series(rows, date_col, val_cols, stop_words=("total", "avg.", "avg", "source:")):
    dates = []; series = {k: [] for k in val_cols}
    for r in rows:
        d = r[date_col] if date_col < len(r) else None
        if isinstance(d, str) and d.strip().lower() in stop_words:
            break
        if not hasattr(d, "strftime"):
            continue
        dates.append(iso(d))
        for k, ci in val_cols.items():
            series[k].append(num(r[ci]) if ci < len(r) else None)
    return dates, series

def parse_sora():
    s = grid("Sora")
    a = grid("Sora App Data")
    # Sora sheet: left = Sora dl (0:date,1:US,2:Intl,3:WW); right = Threads (5:date,6:US,7:Intl,8:WW)
    sora_dates, sora_dl = col_series(s[2:], 0, {"us":1,"intl":2,"ww":3})
    thr_dates,  thr_dl  = col_series(s[2:], 5, {"us":6,"intl":7,"ww":8})
    # Sora App Data: DAUs block (9:date,10:US,11:WW); retention (13:Day,14:US,15:WW); summary col1/col2
    dau_dates, dau = col_series(a[2:], 9, {"us":10,"ww":11})
    ret = {"day": [], "us": [], "ww": []}
    for r in a[2:]:
        lab = r[13] if len(r) > 13 else None
        if isinstance(lab, str) and lab.strip().lower().startswith("day"):
            ret["day"].append(lab.strip())
            ret["us"].append(num(r[14]) if len(r) > 14 else None)
            ret["ww"].append(num(r[15]) if len(r) > 15 else None)
    summary = {}
    for r in a:
        if len(r) > 2 and isinstance(r[1], str) and r[1].strip():
            key = r[1].strip()
            if key.lower() in ("time spent","session count","downloads (m)","daus (k)","7-day retention"):
                summary[key] = (str(r[2]).strip() if isinstance(r[2], str) else num(r[2]))
    return {
        "downloads": {"dates": sora_dates, **sora_dl},
        "threads":   {"dates": thr_dates,  **thr_dl},
        "dau":       {"dates": dau_dates,  **dau},
        "retention": ret,
        "summary":   summary,
    }

sora = parse_sora()

# ===========================================================================
# ASSEMBLE + WRITE
# ===========================================================================
PALETTE = {
    "ChatGPT": "#10a37f", "Google Gemini": "#4285f4", "DeepSeek": "#4d6bfe",
    "Grok": "#111827", "Microsoft Copilot": "#0ea5e9", "Meta AI": "#a855f7",
    "Perplexity": "#20b8cd", "Claude": "#d97757", "Sora": "#ec4899",
}

src_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(SRC)).strftime("%Y-%m-%d %H:%M")

DATA = {
    "generated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    "sourceFile": os.path.basename(SRC),
    "sourceMtime": src_mtime,
    "apps": APPS,
    "colors": PALETTE,
    "months": MONTHS,
    "metricLabels": {
        "downloads": "Downloads (M)", "mau": "MAU (M)", "dau": "DAU (M)",
        "timeSpent": "Time Spent (M hrs)", "timePerMau": "Time / MAU (hrs)",
        "timePerDau": "Time / DAU (min)", "dauMau": "DAU/MAU (stickiness)",
    },
    "regions": {"Global": g_metrics, "US": u_metrics},
    "daily":  {"dates": d_dates, "dau": d_dau, "downloads": d_dl},
    "weekly": {"dates": w_dates, "wau": w_wau, "downloads": w_dl},
    "share": share,
    "gemini": gemini,
    "web": web,
    "sora": sora,
}

with io.open(OUT, "w", encoding="utf-8") as f:
    f.write("// auto-generated by build_data.py — do not edit\n")
    f.write("window.ST = ")
    json.dump(DATA, f, ensure_ascii=False, allow_nan=False)
    f.write(";\n")

# ---- diagnostics ----------------------------------------------------------
def last(series):
    for v in reversed(series or []):
        if v is not None:
            return v
    return None
print("WROTE", OUT, f"({os.path.getsize(OUT)//1024} KB)")
print("months:", MONTHS[0], "->", MONTHS[-1], f"({len(MONTHS)})")
print("source last modified:", src_mtime)
print("\n[Global MAU, latest non-null]")
for a in APPS:
    print(f"  {a:18s} mau={last(g_metrics['mau'].get(a)):>10.2f}  dau={str(round(last(g_metrics['dau'].get(a) or [None]) or 0,2)):>8}  dl={str(round(last(g_metrics['downloads'].get(a) or [None]) or 0,2)):>7}")
print("\ndaily DAU rows:", len(d_dates), d_dates[0], "->", d_dates[-1])
print("weekly WAU rows:", len(w_dates), w_dates[0], "->", w_dates[-1])
print("share dates:", share["dates"][0], "->", share["dates"][-1], "| WW vendors:", list(share["WW"].keys()))
print("gemini releases:", len(gemini), gemini[-1] if gemini else None)
print("web:", [ (w["company"], round(w["visitsM"])) for w in web[:4] ])
print("sora dl days:", len(sora["downloads"]["dates"]), "| sora dau days:", len(sora["dau"]["dates"]),
      "| retention pts:", len(sora["retention"]["day"]), "| summary:", sora["summary"])
