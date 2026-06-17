# AI Apps Monitor — Sensor Tower

Dashboard de inteligência competitiva dos apps de IA de consumo (ChatGPT, Gemini,
DeepSeek, Grok, Copilot, Meta AI, Perplexity, Claude, Sora) a partir da base do
Sensor Tower.

## Como usar
1. Abra **index.html** no navegador (ou sirva a pasta: `py -m http.server 8769`).
2. Após atualizar a planilha de origem, dê duplo-clique em **refresh.bat** e recarregue a página.

## Fonte
A planilha de origem (`Sensor Tower base.xlsx`) **não** é versionada. O ETL resolve o
caminho nesta ordem: variável de ambiente `SENSOR_TOWER_XLSX` → arquivo local
`source_path.txt` (uma linha com o caminho) → `Sensor Tower base.xlsx` ao lado do script.

Dados:
- **Sensor Tower** (licenciado): downloads, MAU/DAU, time spent, Sora (launch/DAU/retenção)
- **Statcounter**: market share de chatbots (WW + US)
- Painel de visitas web por destino

> Os dados são propriedade de seus respectivos provedores e exibidos aqui apenas para fins de pesquisa.

## Abas
| Aba | Conteúdo |
|-----|----------|
| **Overview** | KPIs, leaderboard ordenável (MAU/DAU/stickiness/downloads, M/M e Y/Y) + sparklines, MAU histórico |
| **Engagement** | MAU, DAU, stickiness (DAU/MAU), tempo por MAU; Gemini MAU com marcos de releases |
| **Acquisition** | Downloads mensais, share de downloads, downloads diários (WW) |
| **Attention** | Time spent total, tempo por DAU, share do tempo |
| **Market Share** | Share de chatbot WW e US (Statcounter) |
| **Daily / Weekly** | DAU diário e WAU semanal absolutos (mostra sazonalidade) |
| **Sora** | Downloads/DAU diários, retenção 90d, Sora vs Threads (escala log) |
| **Web** | Visitas web mensais por destino |

Toggle **Global / U.S.** afeta Overview, Engagement, Acquisition e Attention.
Seletores de período (12M/24M/3Y/All; 90D/6M/1Y/All) em cada gráfico temporal.

## Arquitetura
- **build_data.py** — ETL: lê o .xlsx e gera `data.js` (`window.ST = {...}`). Trata
  os blocos mensais intercalados com "Y/Y growth", corta os blocos auxiliares "Sort",
  e detecta o fim da seção absoluta nas abas diárias/semanais (datas crescentes).
- **data.js** — dados gerados (não editar à mão).
- **chart.umd.min.js** — Chart.js 4.4.3 vendorizado (offline, sem CDN).
- **index.html** — app single-file (UI + lógica de gráficos).
