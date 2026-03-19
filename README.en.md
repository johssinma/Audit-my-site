# 🔍 Audit My Site — AI Marketing Suite for Claude Code

> **15 slash commands · 5 parallel AI agents · 4 Python scripts · Bilingual FR/EN**

[![License](https://img.shields.io/badge/license-MIT-22d38a.svg)](ai-marketing/LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-2d8bff.svg)](#)
[![Bilingual](https://img.shields.io/badge/bilingual-FR%20%2F%20EN-f0b429.svg)](#)
[![Built for](https://img.shields.io/badge/built%20for-Claude%20Code-7a8499.svg)](#)

**[🇫🇷 Version Française](README.md)**  |  🇬🇧 English

---

## 🛒 Get the Premium Bundle

**[Buy on Gumroad — €29 one-time](https://auditmysiteai.gumroad.com/l/audit-my-site)**

> Includes: premium bilingual report template · client proposal template · pre-organised ZIP · 30-day personal support

---

## ✨ What Is This?

**Audit My Site** is a complete AI-powered marketing toolkit that runs inside Claude Code. Paste a URL, run a command — get a professional, scored marketing audit in minutes.

No SaaS subscription. No monthly fees. Runs locally from your terminal.

---

## 🏆 Real Output Example

Run `/market quick https://nike.com` → get this in 60 seconds:

```
⚡ QUICK OVERVIEW: Nike.com
Score: 85/100

✅ TOP 2 STRENGTHS
1. Iconic brand clarity — zero ambiguity on value prop
2. Membership ecosystem creates strong retention loops

⚠️ TOP 3 URGENT FIXES
1. No benefit-driven headline above the fold
   → Add "Built for athletes who refuse to stop" as H1

2. Social proof buried too deep in funnel
   → Surface "4.8★ from 12K reviews" badge near CTA

3. Mega-menu with 20+ links creates decision fatigue
   → Reduce to 6 top-level categories with drill-down

💡 ONE-LINE RECOMMENDATION:
Stop showing products. Start showing transformation.
```

---

## 📦 What Gets Installed

|    | Component           | Count | Description                                |
| -- | ------------------- | ----- | ------------------------------------------ |
| 🧠 | **Skills**    | 15    | Slash commands for every marketing task    |
| 🤖 | **Agents**    | 5     | Specialized sub-agents running in parallel |
| 🐍 | **Scripts**   | 4     | Python analysis & PDF generation tools     |
| 📄 | **Templates** | 4     | Ready-to-use client-facing documents       |

---

## ⚡ Quick Install

**Option 1 — One command from anywhere:**

```bash
curl -fsSL https://raw.githubusercontent.com/johssinma/audit-my-site/main/ai-marketing-english/install.sh | bash
```

**Option 2 — Clone locally:**

```bash
git clone https://github.com/johssinma/audit-my-site.git
cd audit-my-site/ai-marketing-english
bash install.sh
```

> **Requires:** Claude Code (Pro or API key) · Python 3.8+

---

## 🚀 The 15 Commands

| Command                       | What it does                          | Output file               |
| ----------------------------- | ------------------------------------- | ------------------------- |
| `/market audit <url>`       | 🔥 Full audit — 5 parallel AI agents | `MARKETING-AUDIT.md`    |
| `/market quick <url>`       | ⚡ 60-second homepage scan            | Terminal                  |
| `/market copy <url>`        | ✍️ Copywriting analysis + rewrites  | `COPY-SUGGESTIONS.md`   |
| `/market emails <topic>`    | 📧 Complete email sequences           | `EMAIL-SEQUENCES.md`    |
| `/market social <topic>`    | 📱 30-day social media calendar       | `SOCIAL-CALENDAR.md`    |
| `/market ads <url>`         | 📣 Ad scripts + creative briefs       | `AD-CAMPAIGNS.md`       |
| `/market funnel <url>`      | 💰 Sales funnel analysis              | `FUNNEL-ANALYSIS.md`    |
| `/market competitors <url>` | 🔍 Competitive intelligence           | `COMPETITORS-REPORT.md` |
| `/market landing <url>`     | 🎯 Landing page CRO analysis          | `LANDING-ANALYSIS.md`   |
| `/market launch <product>`  | 🚀 8-week product launch plan         | `LAUNCH-PLAN.md`        |
| `/market proposal <client>` | 📋 Client proposal with ROI           | `CLIENT-PROPOSAL.md`    |
| `/market report <url>`      | 📊 Full marketing report (MD)         | `MARKETING-REPORT.md`   |
| `/market report-pdf <url>`  | 📄 Professional PDF report            | `MARKETING-REPORT.pdf`  |
| `/market seo <url>`         | 🔎 Content SEO audit                  | `SEO-AUDIT.md`          |
| `/market brand <url>`       | 🎨 Brand voice style guide            | `BRAND-VOICE.md`        |

---

## 🏗️ How the Full Audit Works

```
/market audit <url>
       │
       ▼
  Orchestrator — fetches homepage + 5 key pages
       │
       ├──────────────────────────────────────────┐
       ▼              ▼              ▼             ▼             ▼
  market-content  market-conversion  market-technical  market-competitive  market-strategy
  Copy & Messaging  CRO & Funnels   SEO & Tracking   Competitor Intel    Brand & Growth
     25% weight      20% weight      20% weight        15% weight        10% + 10%
       │
       ▼
  Weighted composite score → MARKETING-AUDIT.md (scored, client-ready PDF)
```

---

## 🎯 Who Is This For?

| Profile                         | How they use it                                    |
| ------------------------------- | -------------------------------------------------- |
| 🏢**Marketing agencies**  | Deliver AI-powered audits to clients in minutes    |
| 👤**Freelance marketers** | Stand out with data-driven, scored reports         |
| 🛒**E-commerce owners**   | Find exactly what's killing your conversions       |
| 💻**SaaS founders**       | Get an outside view of your funnel and messaging   |
| 🎓**Consultants**         | Generate client proposals backed by real analysis  |
| 🔧**Developers**          | Build marketing tools on top of a solid foundation |

---

## 🆓 Free vs ⭐ Premium

| Feature                      | GitHub (Free) | Gumroad Bundle (€29) |
| ---------------------------- | :-----------: | :-------------------: |
| All 15 slash commands        |      ✅      |          ✅          |
| All 5 AI agents              |      ✅      |          ✅          |
| FR + EN versions             |      ✅      |          ✅          |
| Python scripts               |      ✅      |          ✅          |
| Premium HTML report template |      ❌      |          ✅          |
| Client proposal template     |      ❌      |          ✅          |
| Pre-organised ZIP            |      ❌      |          ✅          |
| Email updates                |      ❌      |          ✅          |
| 30-day personal support      |      ❌      |          ✅          |

**[Get the Premium Bundle on Gumroad — €29](https://auditmysiteai.gumroad.com/l/audit-my-site)**

---

## 🗂️ Project Structure

```
audit-my-site/
├── ai-marketing/               🇫🇷 French version
│   ├── agents/                 5 specialized AI sub-agents
│   ├── market/                 Main orchestrator skill
│   ├── skills/                 15 slash command skills
│   ├── scripts/                Python analysis scripts
│   ├── templates/              Client-facing templates
│   └── install.sh
│
├── ai-marketing-english/       🇬🇧 English version
│   ├── agents/
│   ├── market/
│   ├── skills/
│   ├── scripts/
│   ├── templates/
│   └── install.sh
│
├── README.md                   🇫🇷 French documentation
└── README.en.md                🇬🇧 English documentation
```

---

## 🛠️ Prerequisites

```bash
# Required
npm install -g @anthropic-ai/claude-code   # Claude Code CLI

# Optional — for PDF reports
pip install reportlab==4.0.4
```

> You need either a **Claude Pro** subscription ($20/mo) or an **Anthropic API key**

---

## 🗑️ Uninstall

```bash
bash uninstall.sh
```

---

## 📜 Licence

**MIT** — use commercially, modify freely, deliver to clients under your own brand.

See [LICENSE](ai-marketing/LICENSE)

---

Built by [Mohssine Mazouz](https://github.com/johssinma) · Bilingual FR/EN · MIT Licensed

**[⭐ Star this repo](https://github.com/johssinma/audit-my-site)**  ·  **[🛒 Get Premium Bundle — €29](https://auditmysiteai.gumroad.com/l/audit-my-site)**

*Turn any website into a revenue opportunity — in minutes.*`<div align="center">`
`<img src="https://img.shields.io/badge/Audit_My_Site-AI_Marketing_Suite-0f1117?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNSIgZmlsbD0iIzJkOGJmZiIvPjwvc3ZnPg==&labelColor=0f1117&color=2d8bff" alt="Audit My Site"/>`

# 🔍 Audit My Site
