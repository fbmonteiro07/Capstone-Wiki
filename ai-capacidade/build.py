"""
build.py  —  monta o dashboard combinado "AI: Capacidade & Economics por GW".

Junta as duas réplicas (economics_1gw + como_flui_capacidade), geradas a partir do
"AI Model (comentado)" por E:\\Wiki Felipe empresas\\_wiki\\_tools\\build_ai_dashboards.py,
num único dashboard com abas para publicar no Capstone-Wiki (GitHub Pages).

Estratégia (à prova de colisão): cada réplica vira uma página "embed" (header/nav ocultos,
+ beacon de altura) carregada num <iframe> do shell index.html. Documentos separados =
sem colisão de const/id globais; os gráficos renderizam em viewport real (sem canvas 0px).

Fontes (as réplicas já verificadas):
  E:\\Wiki Felipe empresas\\_wiki\\_dashboards\\economics_1gw.html         -> economics.html
  E:\\Wiki Felipe empresas\\_wiki\\_dashboards\\como_flui_capacidade.html  -> fluxo.html
Saída: esta pasta (index.html + economics.html + fluxo.html).

Uso:  py build.py
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = r"E:\Wiki Felipe empresas\_wiki\_dashboards"
CHILDREN = {                       # arquivo destino -> arquivo fonte
    "economics.html": "economics_1gw.html",
    "fluxo.html":     "como_flui_capacidade.html",
}

# beacon: reporta a altura do conteúdo ao shell (auto-resize do iframe, sem scroll aninhado)
BEACON = """
<script>
(function(){
  var last=0;
  function H(){return Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);}
  function ping(){var v=H(); if(Math.abs(v-last)>2){last=v; try{parent.postMessage({__aidash:1,h:v},'*');}catch(e){}}}
  addEventListener('load',ping); addEventListener('resize',ping);
  if(window.ResizeObserver){try{new ResizeObserver(ping).observe(document.body);}catch(e){}}
  [150,500,1200,2500,4000].forEach(function(t){setTimeout(ping,t);});
})();
</script>
"""

# oculta o header/nav próprios da réplica (o shell fornece título + abas). NÃO remove os
# elementos — os scripts das réplicas referenciam #asof etc., que precisam existir no DOM.
HIDE = '<style id="embed-hide">header,nav.tabs{display:none!important}</style>\n</head>'


def make_embed(name_src):
    with open(os.path.join(SRC, name_src), "r", encoding="utf-8") as f:
        html = f.read()
    if 'id="embed-hide"' not in html:
        html = html.replace("</head>", HIDE, 1)
    if "__aidash" not in html:
        html = html.replace("</body>", BEACON + "</body>", 1)
    return html


for dst, src in CHILDREN.items():
    with open(os.path.join(HERE, dst), "w", encoding="utf-8") as f:
        f.write(make_embed(src))
    print(f"  {dst} <- {src}")

SHELL = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI: Capacidade & Economics por GW</title>
<style>
:root{--bg:#0b1018;--panel:#121a27;--panel2:#0f1622;--line:#1f2b3e;--txt:#e8edf5;--mut:#8696ad;--acc:#5aa2ff;--gold:#e8b54d}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--txt);font-family:"Segoe UI",system-ui,sans-serif;font-size:13px;padding:0 0 40px}
.backpill{display:inline-flex;align-items:center;gap:6px;margin:10px 0 4px 14px;padding:6px 12px;font:600 12px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color:#8b949e;background:#161b22;border:1px solid #30363d;border-radius:8px;text-decoration:none;transition:color .15s,border-color .15s}
.backpill:hover{color:#58a6ff;border-color:#58a6ff}
header.top{padding:8px 22px 2px}
header.top h1{font-size:20px;font-weight:600;letter-spacing:.3px}
header.top .src{color:var(--mut);font-size:11px;margin-top:3px}
nav.tabs{display:flex;gap:8px;padding:12px 22px 10px;flex-wrap:wrap}
nav.tabs button{color:var(--mut);background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:7px 16px;font-size:13px;cursor:pointer;transition:.15s}
nav.tabs button:hover{color:var(--txt);border-color:var(--acc)}
nav.tabs button.on{background:var(--gold);border-color:var(--gold);color:#06101f;font-weight:600}
.frames{position:relative;width:100%}
.frames iframe{width:100%;border:0;display:block;background:var(--bg);min-height:78vh}
</style>
</head>
<body>
<a class="backpill" href="../"><span style="font-size:15px;line-height:1">&larr;</span> Capstone Wiki</a>
<header class="top">
  <h1>AI: Capacidade &amp; Economics <span style="color:var(--mut);font-weight:400">| por GW</span></h1>
  <div class="src">dados: <b>AI Model (comentado 2026-07-06).xlsx</b> &middot; r&eacute;plica &middot; CY24&ndash;CY28E &middot; <span id="asof"></span></div>
</header>
<nav class="tabs">
  <button data-k="econ" class="on">Qual o economics de 1&nbsp;GW?</button>
  <button data-k="flux">Como flui a capacidade?</button>
</nav>
<div class="frames">
  <iframe id="frame" src="economics.html" title="dashboard"></iframe>
</div>
<script>
// Um único iframe sempre visível; trocar de aba recarrega o filho em viewport real
// (evita canvas 0px de iframe fora de tela). O reload é instantâneo (arquivo local).
const SRC={econ:'economics.html',flux:'fluxo.html'};
const frame=document.getElementById('frame');
const btns=[...document.querySelectorAll('nav.tabs button')];
let cur='econ';
function show(k){
  if(k!==cur){ cur=k; frame.src=SRC[k]; }
  btns.forEach(b=>b.classList.toggle('on',b.dataset.k===k));
  window.scrollTo(0,0);
}
btns.forEach(b=>b.onclick=()=>show(b.dataset.k));
addEventListener('message',e=>{ if(e.data&&e.data.__aidash){ frame.style.height=(e.data.h+24)+'px'; } });
document.getElementById('asof').textContent='as of '+new Date().toISOString().slice(0,10);
</script>
</body>
</html>
"""

with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
    f.write(SHELL)
print("  index.html (shell)")
print("Concluído em:", HERE)
