# -*- coding: utf-8 -*-
"""Mantem o pe_history_data.js da aba Historical P/E do semicap dashboard.

Uso:
    py build_pe_history.py --add "MU US"     # adiciona empresa (busca BBG 2000-hoje)
    py build_pe_history.py --remove MU       # remove empresa adicionada (as 7 base nao)

Series por ticker (semanais, grade W-FRI desde 2000, casadas por semana ISO):
    fwd = BEST_PE_RATIO 1BF · fwd2 = BEST_PE_RATIO 2BF · ltm = PE_RATIO
Requer terminal Bloomberg aberto (bbg_wrapper local).
"""
import sys, os, json, datetime
sys.path.insert(0, r"P:\Felipe Monteiro\US Equities")

DIR = os.path.dirname(os.path.abspath(__file__))
JS = os.path.join(DIR, "pe_history_data.js")
BASE = ["ASML", "AMAT", "KLAC", "LRCX", "TER", "AEIS", "TEL"]
SPECS = [("fwd", "BEST_PE_RATIO", "1BF"), ("fwd2", "BEST_PE_RATIO", "2BF"),
         ("ltm", "PE_RATIO", None)]


def load():
    txt = open(JS, encoding="utf-8").read()
    txt = txt[txt.index("{"):].rstrip().rstrip(";")
    return json.loads(txt)


def save(peh):
    peh["buildStamp"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(JS, "w", encoding="utf-8") as fh:
        fh.write("window.PEH = " + json.dumps(peh, separators=(",", ":")) + ";")


def normalize(q):
    parts = q.strip().upper().split()
    if not parts:
        raise SystemExit("ticker vazio")
    if parts[-1] == "EQUITY":
        parts = parts[:-1]
    if len(parts) == 1:
        parts.append("US")
    return " ".join(parts) + " Equity"


def display_key(tk):
    parts = tk.split()
    return parts[0] if parts[1] == "US" else f"{parts[0]} {parts[1]}"


def week_key(iso_date):
    y, m, d = map(int, iso_date.split("-"))
    c = datetime.date(y, m, d).isocalendar()
    return (c[0], c[1])


def fetch_ticker(bbg, tk, peh):
    """Busca as 3 series semanais; alinha cada uma na grade de datas do seu bloco (semana ISO)."""
    end = datetime.date.today().strftime("%Y%m%d")
    out = {}
    for key, fld, ovrd in SPECS:
        dates = peh[key]["dates"]
        grid = {week_key(d): i for i, d in enumerate(dates)}
        o = {"BEST_FPERIOD_OVERRIDE": ovrd} if ovrd else None
        data, errs = bbg.bdh([tk], [fld], dates[0].replace("-", ""), end, o, "WEEKLY")
        vals = [None] * len(dates)
        n = 0
        for row in data.get(tk, []):
            v = row.get(fld)
            if v is None:
                continue
            i = grid.get(week_key(row["date"]))
            if i is not None:
                vals[i] = round(v, 3)
                n += 1
        print(f"  {key}: {n} pontos")
        out[key] = vals
    return out


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("--add", "--remove"):
        raise SystemExit(__doc__)
    mode, arg = sys.argv[1], sys.argv[2]
    peh = load()
    peh.setdefault("extras", [])

    if mode == "--remove":
        key = arg.strip().upper()
        if key not in peh["extras"]:
            raise SystemExit(f"{key} nao e um ticker adicionado (base fixa: {', '.join(BASE)})")
        peh["extras"].remove(key)
        peh["order"].remove(key)
        peh["tickers"].pop(key, None)
        for m, _f, _o in SPECS:
            peh[m]["series"].pop(key, None)
        save(peh)
        print(f"OK — {key} removido ({len(peh['order'])} tickers)")
        return

    tk = normalize(arg)
    key = display_key(tk)
    if key in peh["order"]:
        raise SystemExit(f"{key} ja esta no Historical P/E")
    from bbg_wrapper import BBG
    bbg = BBG()
    meta, _ = bbg.bdp([tk], ["NAME"])
    name = (meta.get(tk) or {}).get("NAME")
    if not name:
        bbg.close()
        raise SystemExit(f"nao encontrado no Bloomberg: {tk}")
    print(f"Buscando {key} ({name}) — 3 series semanais desde {peh['start']}...")
    series = fetch_ticker(bbg, tk, peh)
    bbg.close()
    if not any(v is not None for v in series["fwd"]) and not any(v is not None for v in series["ltm"]):
        raise SystemExit(f"{key}: sem dados de P/E no BBG — nao adicionado")
    for m, _f, _o in SPECS:
        peh[m]["series"][key] = series[m]
    peh["order"].append(key)
    peh["tickers"][key] = tk
    peh["extras"].append(key)
    save(peh)
    print(f"OK — {key} adicionado ({len(peh['order'])} tickers)")


if __name__ == "__main__":
    main()
