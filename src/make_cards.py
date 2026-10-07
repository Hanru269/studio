"""Builds portfolio images 5-8 (1600x1200) as HTML, screenshots them with headless Chromium."""
import subprocess, pathlib, html
OUT = pathlib.Path("/root/portfolio-site/img"); SRC = pathlib.Path(__file__).parent
SH = "/root/.cache/ms-playwright/chromium_headless_shell-1243/chrome-headless-shell-linux64/chrome-headless-shell"
C = dict(o="#f5a623", t="#5cc6b4", p="#9b8cff", r="#f07a7a", b="#5aa9f0")

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
*{margin:0;box-sizing:border-box}body{width:1600px;height:1200px;background:#121a22;color:#eef2f6;font-family:Poppins,sans-serif;position:relative;overflow:hidden}
h1{position:absolute;left:80px;top:62px;font-size:52px;font-weight:700;letter-spacing:-.5px}
.sub{position:absolute;left:80px;top:134px;font-size:25px;color:#93a1b0}
.box{position:absolute;background:#1c2631;border:3px solid;border-radius:18px;padding:22px 24px}
.box b{display:block;font-size:26px;font-weight:600;margin-bottom:10px}
.box div{font-size:19px;color:#a9b5c2;line-height:1.5}
.foot{position:absolute;left:80px;bottom:62px;font-size:22px;color:#93a1b0}
.chip{display:inline-block;background:#26323f;border-radius:99px;padding:4px 14px;margin:6px 6px 0 0;font-size:16px;color:#cfd8e1}
.phone{position:absolute;background:#0b1117;border:10px solid #2a3542;border-radius:40px;padding:26px 18px}
.msg{background:#1f2b38;border-radius:14px;padding:12px 14px;font-size:16px;color:#dfe6ee;margin-bottom:12px;line-height:1.45}
.msg small{display:block;color:#7f8d9b;font-size:13px;margin-top:4px}
svg{position:absolute;left:0;top:0}
"""

def box(x, y, w, h, col, title, lines):
    body = "<br>".join(html.escape(l) for l in lines)
    return f'<section class="box" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-color:{C[col]}"><b>{html.escape(title)}</b><div>{body}</div></section>'

def arrows(pairs):
    s = '<svg width="1600" height="1200"><defs><marker id="a" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0,0 L12,6 L0,12 z" fill="#93a1b0"/></marker></defs>'
    for x1, y1, x2, y2 in pairs:
        s += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#93a1b0" stroke-width="3" marker-end="url(#a)"/>'
    return s + "</svg>"

def page(title, sub, body, foot):
    return f"<!doctype html><meta charset=utf-8><style>{CSS}</style><body><h1>{html.escape(title)}</h1><p class=sub>{html.escape(sub)}</p>{body}<p class=foot>{html.escape(foot)}</p>"

cards = {}

cards["portfolio-5-trading-bot"] = page(
    "Prediction-market trading bot + Telegram alerts",
    "Research-driven Python bot for short-window crypto markets, with risk limits and live alerts",
    arrows([(470,330,600,300),(470,520,600,560),(1000,300,1100,300),(1000,560,1100,560),(1300,400,1300,450),(800,660,800,760)]) +
    box(80,220,390,200,"o","Market data",["Live exchange price feed","Order book WebSocket","Market discovery per window"]) +
    box(80,450,390,200,"b","Research",["Study of 1,853 resolved markets","and 3.5M trades shaped","every strategy parameter"]) +
    box(600,210,400,230,"t","Fair-value model",["Real-time probability per market","Fat-tail volatility model","Edge must hold in two regimes"]) +
    box(600,470,400,190,"p","Strategy legs",["Stale-quote sniping","End-of-window scalping","Market making (kept off by data)"]) +
    box(1100,210,420,190,"r","Risk engine",["Per-trade and daily limits","Session kill switch","Fill guards, duplicate-exit lock"]) +
    box(1100,450,420,210,"o","Execution + storage",["Limit and fill-or-kill orders","SQLite trade log","Paper mode before live"]) +
    box(80,760,1440,170,"t","Monitoring",["Telegram alerts on fills, exits and kill-switch trips, plus a 30-minute P&L report","Systemd service with a lock file, so only one copy can trade at a time"]),
    "Python · asyncio · WebSockets · SQLite · Telegram Bot API · pytest. Strategy details and results kept private.")

cards["portfolio-6-paid-api"] = page(
    "Pay-per-call API that AI agents can find and pay",
    "34 tested endpoints, paid per request in USDC, with an MCP server and marketplace listings",
    arrows([(470,330,600,330),(1000,330,1100,300),(1000,330,1100,560),(800,450,800,560),(470,640,600,640)]) +
    box(80,220,390,230,"o","34 curated endpoints",["Web to markdown, crawling","PDF tables, DNS, SSL, CVEs","Each tested before listing"]) +
    box(600,220,400,230,"t","Payment layer",["HTTP 402 pay-per-request","USDC micropayments","No accounts or API keys"]) +
    box(1100,200,420,200,"p","MCP server for agents",["Every endpoint as a paid tool","Free tool listing","Published to an MCP registry"]) +
    box(1100,450,420,200,"b","Discovery listings",["Auto-built spec from real outputs","Indexed in an agent marketplace","Descriptions match real fields"]) +
    box(80,530,390,220,"r","Hardening",["SSRF-safe fetching","Redirect checks","IPv4 fallback, rate limits"]) +
    box(600,560,400,190,"o","19 Apify Actors",["Bulk versions of the endpoints","Pay-per-result pricing","Output schemas for the Store"]) +
    box(80,800,1440,130,"t","Operations",["Node.js + TypeScript service under systemd behind a reverse proxy. Payment-free test harness checks every endpoint before release."]),
    "TypeScript · Node.js · x402 · MCP · Apify SDK · Caddy · systemd")

cards["portfolio-7-ops-server"] = page(
    "Remote AI operations server",
    "Claude Code on a Linux server, run from a phone or laptop over SSH (Termius)",
    arrows([(470,380,600,380),(1000,320,1100,290),(1000,380,1100,520),(1000,440,1100,760),(800,520,800,640)]) +
    box(80,240,390,270,"o","Phone + laptop",["Termius SSH app","Same session on any device","Work from anywhere"]) +
    box(600,240,400,280,"t","Claude Code on a VPS",["AI agent with shell access","Builds, deploys and monitors","Persistent memory notes","between sessions"]) +
    box(1100,200,420,180,"p","Always-on services",["APIs and bots under systemd","Auto-restart on failure"]) +
    box(1100,430,420,190,"b","Scheduled jobs",["Dashboard refresh every 3h","Hourly ad-budget guard","Daily catalogue sync"]) +
    box(1100,670,420,180,"r","Desktop apps headless",["Virtual display + VNC","Operated by screenshots"]) +
    box(600,640,400,210,"o","Secrets + safety",["Tokens in a locked folder","Spending caps and stop rules","Owner approves money moves"]) +
    box(80,580,390,270,"t","What it runs",["Online store + feeds","Ads and social posting","Paid API + 19 Actors","Sales dashboard"]),
    "Ubuntu · Claude Code · Termius · systemd · cron · Xvfb/VNC · GitHub Pages")

cards["portfolio-8-image-pipeline"] = page(
    "Product image & brand pipeline",
    "Designs, mockups, listing images, pins and social graphics generated from one product catalogue",
    arrows([(470,330,600,330),(1000,330,1100,330),(800,450,800,540),(1300,450,1300,540),(1000,640,1100,640)]) +
    box(80,220,390,230,"o","Product catalogue",["One record per product","Text, palette, language","Price floors per type"]) +
    box(600,220,400,230,"t","Design renderer",["Artwork sized to each","product's exact print area","Light and dark variants"]) +
    box(1100,220,420,230,"p","Mockups + listings",["Print-on-demand mockups","Listing image sets","Published by API"]) +
    box(600,540,400,210,"b","Brand kit",["Profile, cover, banners","Shop icon and receipts","Consistent type + colour"]) +
    box(1100,540,420,210,"r","Marketing images",["1000x1500 Pinterest pins","Social promo collages","Bulk-upload CSV files"]) +
    box(80,540,390,210,"o","Output so far",["107 print-on-demand products","170 marketplace listings","120+ scheduled pins"]) +
    box(80,800,1440,130,"t","Why it matters",["A new product goes from idea to live listing, pins and social posts in minutes, with every image on-brand."]),
    "Python · Pillow · ReportLab · Printify API · Etsy API · headless Chromium")

cards["portfolio-9-blender-addons"] = page(
    "Blender add-ons for 3D printing, sold on Gumroad",
    "Three tested add-ons: split big models to fit the bed, repair broken meshes, preflight game assets",
    arrows([(470,330,600,330),(1000,330,1100,330),(800,450,800,540),(1000,640,1100,640)]) +
    box(80,220,390,230,"o","Bed Fit Splitter ($19)",["Enter your printer bed size","Plans cuts + alignment dowels","Exports oriented STLs + plan"]) +
    box(600,220,400,230,"t","Print Fix ($15)",["Finds print-blocking problems","Repairs a copy in stages","Re-verifies, original untouched"]) +
    box(1100,220,420,230,"p","Asset Preflight ($19)",["Transforms, UVs, texel density","Verified one-click fixes","Rolls back if shape changes"]) +
    box(600,540,400,210,"b","Testing",["97 automated tests","Blender 4.2 LTS and 5.1","Buyer-path test on the download"]) +
    box(1100,540,420,210,"r","Launch",["Gumroad listings + covers","GitHub pages","BlenderNation article"]) +
    box(80,540,390,210,"o","Result so far",["First paid sale ($19) from","the BlenderNation article","82 referred views"]) +
    box(80,800,1440,130,"t","Speed",["1.3M triangles split into 8 printable parts with dowels in about 15 seconds; a 600k-face model repaired in about 20 seconds."]),
    "Python · Blender API (bmesh, booleans, voxel remesh) · pytest-style suites · Gumroad")

cards["portfolio-10-kdp-books"] = page(
    "Print-ready paperback pipeline (Amazon KDP)",
    "25 books generated from code: interiors, full-wrap covers and listings, ready to upload",
    arrows([(470,330,600,330),(1000,330,1100,330),(800,450,800,540),(1300,450,1300,540)]) +
    box(80,220,390,230,"o","Niche research",["Search and bestseller checks","Low-competition puzzle,","journal and story books"]) +
    box(600,220,400,230,"t","Interior generator",["Large-print puzzles with","verified unique answers","Journals, planners, stories"]) +
    box(1100,220,420,230,"p","Cover builder",["Full wrap: back, spine, front","Spine width from page count","Vector art, print-safe"]) +
    box(600,540,400,210,"b","Print checks",["All fonts embedded (pdffonts)","Trim, margins, spine clearance","Preview pages per book"]) +
    box(1100,540,420,210,"r","Listing kit",["Title, subtitle, description","7 keywords, categories","Royalty-aware pricing"]) +
    box(80,540,390,210,"o","Output",["25 print-ready paperbacks","6x9 and 8.5x11 trims","5 imprints"]) +
    box(80,800,1440,130,"t","Why it matters",["A new book in a proven format takes minutes to build, and every file is checked against the printer's technical rules before upload."]),
    "Python · ReportLab · Node.js + jsPDF · pdffonts · Amazon KDP")

cards["portfolio-11-printables"] = page(
    "Printable product generators (Etsy digital downloads)",
    "Code that builds puzzle, game and planner products, and proves every answer is right",
    arrows([(470,330,600,330),(1000,330,1100,330),(800,450,800,540),(1300,450,1300,540)]) +
    box(80,220,390,230,"o","Product ideas",["Scraped marketplace data","Scored niches by demand","and competition"]) +
    box(600,220,400,230,"t","Generators",["Sudoku with unique solutions","Line-solvable nonograms","Escape room + mystery cases"]) +
    box(1100,220,420,230,"p","Self-checks",["Every puzzle solved by code","Escape room codes asserted","Math pictures auto-checked"]) +
    box(600,540,400,210,"b","Listing images",["Hero mockups + previews","'What is included' panels","Bundle collages"]) +
    box(1100,540,420,210,"r","Publishing",["Created, uploaded and","activated by Etsy API","Sections + bundles"]) +
    box(80,540,390,210,"o","Output",["60+ digital products","Party games, kids learning,","puzzles, planners"]) +
    box(80,800,1440,130,"t","Why it matters",["Buyers never get a puzzle with two answers or a wrong code: the build fails before a broken product can ship."]),
    "Python · ReportLab · Pillow · Etsy API · search + scoring scripts")

cards["portfolio-13-accessibility-pipeline"] = page(
    "Accessibility scanner + outreach pipeline",
    "Finds EU shops with WCAG problems, writes a personal report, emails it and tracks every reply",
    arrows([(470,330,600,330),(1000,330,1100,330),(1300,430,1300,540),(1100,640,1000,640),(600,640,470,640)]) +
    box(80,220,390,210,"o","Lead finder",["Public company data","Size + country rules","One contact per company"]) +
    box(600,220,400,210,"t","WCAG 2.1 scanner",["Alt text, labels, link names","Zoom blocking, headings, lang","Accessibility statement check"]) +
    box(1100,220,420,210,"p","Personal email",["Real issues from the scan","Opt-out line in every mail","Daily cap + warm-up"]) +
    box(1100,540,420,210,"b","Inbox robot",["IMAP every 20 min","Auto-replies + bounces sorted","Opt-outs suppressed for good"]) +
    box(600,540,400,210,"r","Report on request",["PDF sneak-peek report","Detailed fix list + quote","Excel funnel tracker"]) +
    box(80,540,390,210,"o","Alerts",["Telegram ping only when a","real person replies","Live counts on a dashboard"]) +
    box(80,800,1440,130,"t","Why it matters",["Hours of manual auditing become a 60-second scan, and nobody is emailed twice or after they opt out."]),
    "Python · requests + HTML parsing · SMTP/IMAP · openpyxl · ReportLab · cron")

for name, doc in cards.items():
    if not name.startswith(("portfolio-13",)): continue
    p = SRC / f"{name}.html"; p.write_text(doc)
    png = OUT / f"{name}.png"
    subprocess.run([SH, "--no-sandbox", "--hide-scrollbars", "--virtual-time-budget=4000", "--window-size=1600,1200",
                    f"--screenshot={png}", p.as_uri()], capture_output=True)
    from PIL import Image
    Image.open(png).convert("RGB").save(OUT / f"{name}.jpg", quality=86); png.unlink()
    print(name, "ok")
