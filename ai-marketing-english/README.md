
# 🔍 Audit My Site — Complete AI Marketing Suite for Claude Code

<div align="right">

🌐 **Langue / Language** &nbsp;|&nbsp; [🇫🇷 Français](README.md) &nbsp;|&nbsp; 🇬🇧 English

</div>

> **15 slash commands · 5 parallel agents · 4 Python scripts · Bilingual FR/EN**
> The most complete AI-powered marketing audit toolkit built for Claude Code.

---

## ⚡ Quick Install

**Option 1 — Clone & install locally:**

```bash
git clone https://github.com/johssinma/test_marketing.git
cd test_marketing
bash install.sh
```

**Option 2 — One-line install from anywhere:**

```bash
curl -fsSL https://raw.githubusercontent.com/johssinma/test_marketing/main/install.sh | bash
```

---

## 📦 What Gets Installed

| Component    | Count | Description                             |
| ------------ | ----- | --------------------------------------- |
| 🧠 Skills    | 15    | Slash commands for every marketing task |
| 🤖 Agents    | 5     | Specialized sub-agents for full audits  |
| 🐍 Scripts   | 4     | Python analysis & generation scripts    |
| 📄 Templates | 4     | Ready-to-use client-facing templates    |

---

## 🚀 Available Commands

```
/market audit <url>        → Full marketing audit (5 parallel agents)
/market quick <url>        → 60-second marketing overview
/market copy <url>         → Generate optimised copywriting
/market emails <topic>     → Generate email sequences
/market social <topic>     → Social media content calendar
/market ads <url>          → Ad creatives & copy
/market funnel <url>       → Sales funnel analysis
/market competitors <url>  → Competitive intelligence
/market landing <url>      → Landing page CRO analysis
/market launch <product>   → Product launch plan
/market proposal <client>  → Client proposal generator
/market report <url>       → Full marketing report (Markdown)
/market report-pdf <url>   → Full marketing report (PDF)
/market seo <url>          → Content SEO audit
/market brand <url>        → Brand voice analysis
```

---

## 📖 Command Details

### 🏆 1. The Master Commands (Global Audit)

#### `/market audit <url>`

**What it does:** A complete scanner of any website. Analyses everything — the purchase journey, SEO, design, trust signals, conversion rate and competitive positioning — using 5 AI agents running in parallel.

> **💡 E-commerce example:** Before spending thousands on Black Friday Facebook ads, run this on your store. It will tell you: *"Warning — customer reviews are missing from product pages"* or *"The 'Add to Cart' button is not visible on mobile without scrolling."*

---

#### `/market quick <url>`

**What it does:** The flash version of the audit. Scans your homepage in under 60 seconds and gives you the top 2 strengths and top 3 urgent fixes.

> **💡 E-commerce example:** You just updated your homepage banner. Run this to verify whether the offer *("-20% on the summer collection")* is clear to a visitor within 3 seconds.

---

### 💰 2. Sales Funnel & Conversion

#### `/market funnel <url>`

**What it does:** Maps the full customer journey from first click to payment page. Identifies exactly where visitors drop off and estimates the revenue impact of each bottleneck.

> **💡 E-commerce example:** You have 10,000 visitors/month but only 50 sales. Run this to find the problem. It might reveal: *"The bottleneck is at the shipping cost step — customers abandon because fees appear too late."*

---

#### `/market landing <url>`

**What it does:** Deep CRO analysis of a specific page. Tells you exactly what to add, move or rewrite to improve conversions.

> **💡 E-commerce example:** You built a dedicated sales page for your best-selling serum. This command will tell you to add Before/After photos, move benefits above the price and add urgency elements.

---

### ✍️ 3. Product Pages & Copywriting

#### `/market copy <url>`

**What it does:** Rewrites boring feature-focused text into benefit-driven copy that sells. Gives you before/after examples for every section.

> **💡 E-commerce example:** Instead of *"100% cotton T-shirt, round neck, black"* — the command rewrites: *"The perfect black T-shirt that won't shrink in the wash and flatters your shoulders."*

---

#### `/market brand <url>`

**What it does:** Analyses your brand voice across all visible channels and creates a complete brand style guide your whole team can follow.

> **💡 E-commerce example:** If you sell luxury watches, you don't speak to customers the same way as an eco-friendly Gen Z beauty brand. This command creates your *"brand bible"* — the exact vocabulary to use on your site and socials.

---

#### `/market seo <url>`

**What it does:** Full on-page SEO audit. Checks titles, meta descriptions, heading structure, image alt text, internal links, schema markup and content gaps.

> **💡 E-commerce example:** Launching a new range of waterproof backpacks? This command checks whether you're targeting the right keywords in H1/H2 tags, image alt attributes and descriptions.

---

### 📣 4. Acquisition (Ads & Social)

#### `/market ads <url>`

**What it does:** Generates complete ad creative briefs — hooks, scripts, copy and visual direction — for paid social channels.

> **💡 E-commerce example:** You have a budget for TikTok or Instagram ads. Provide your hero product URL and get 3 short video scripts: *Unboxing*, *Problem/Solution*, and *UGC Testimonial* — ready to film.

---

#### `/market social <topic/url>`

**What it does:** Generates a full 30-day social content calendar with platform-specific posts, hook formulas, hashtag strategy and a content repurposing workflow.

> **💡 E-commerce example:** No content ideas for December? Get a full month planned: *"Monday: product use in winter · Wednesday: customer review · Friday: eco-friendly packaging — perfect as a gift."*

---

#### `/market competitors <url>`

**What it does:** Identifies 3–10 competitors, analyses their positioning, pricing, features and content strategy, then recommends differentiation moves.

> **💡 E-commerce example:** You sell insulated water bottles. Run this on the market leader — see their best offers and get specific ways to differentiate your brand.

---

### 📧 5. Retention & Email Sequences

#### `/market emails <topic/url>`

**What it does:** Writes complete email sequences — welcome, nurture, abandoned cart, re-engagement — ready to paste into your ESP.

> **💡 E-commerce example:** Abandoned cart sequence for a jewellery brand:
>
> - ✉️ Email 1 (4h after): *"Oops, you left something behind..."*
> - ✉️ Email 2 (next day): Social proof + guarantee
> - ✉️ Email 3 (48h later): *"-10% discount code — last chance"*

---

#### `/market launch <product>`

**What it does:** Creates a full product launch plan with an 8-week timeline, teaser strategy, launch day checklist and post-launch follow-up.

---

### 📊 6. Agency & B2B

#### `/market proposal <client>`

**What it does:** Generates a complete client proposal with situation analysis, phased strategy, scope of work, 3-tier pricing options and ROI projections.

---

#### `/market report <url>` & `/market report-pdf <url>`

**What it does:** Compiles all available analysis data into a presentation-ready report. The PDF version uses professional formatting suitable for client delivery.

---

## 🛠️ Prerequisites

- **Claude Code** — installed and configured
- **Python 3.8+** — for the analysis scripts
- **reportlab** *(optional, for PDF reports)*:

```bash
pip install reportlab
```

---

## 🗂️ Project Structure

```
audit-my-site/
├── 🤖 agents/
│   ├── market-content.md       # Content & messaging agent
│   ├── market-conversion.md    # CRO & funnel agent
│   ├── market-competitive.md   # Competitive intelligence agent
│   ├── market-technical.md     # SEO & technical agent
│   └── market-strategy.md      # Brand & growth strategy agent
├── 🧠 market/
│   └── SKILL.md                # Main orchestrator
├── ⚡ skills/
│   ├── market-audit/           # Full marketing audit
│   ├── market-brand/           # Brand voice analysis
│   ├── market-copy/            # Copywriting optimisation
│   ├── market-emails/          # Email sequences
│   ├── market-competitors/     # Competitive analysis
│   ├── market-social/          # Social media calendar
│   ├── market-funnel/          # Funnel analysis
│   ├── market-ads/             # Ad campaigns
│   ├── market-proposal/        # Client proposals
│   ├── market-landing/         # Landing page CRO
│   ├── market-launch/          # Product launch plan
│   ├── market-report/          # Marketing report (MD)
│   ├── market-report-pdf/      # Marketing report (PDF)
│   └── market-seo/             # SEO audit
├── 🐍 scripts/
│   ├── analyze_page.py         # Web page analyser
│   ├── competitor_scanner.py   # Competitor scanner
│   ├── social_calendar.py      # Social calendar generator
│   └── generate_pdf_report.py  # PDF report generator
├── 📄 templates/
│   ├── email-welcome.md        # Welcome email sequence
│   ├── proposal-template.md    # Client proposal template
│   ├── content-calendar.md     # 30-day content calendar
│   └── launch-checklist.md     # Product launch checklist
├── install.sh                  # Installer
├── uninstall.sh                # Uninstaller
└── requirements.txt            # Python dependencies
```

---

## 📁 Generated Output Files

| Command                 | Output File                       |
| ----------------------- | --------------------------------- |
| `/market audit`       | `MARKETING-AUDIT.md`            |
| `/market brand`       | `BRAND-VOICE.md`                |
| `/market copy`        | `COPY-SUGGESTIONS.md`           |
| `/market emails`      | `EMAIL-SEQUENCES.md`            |
| `/market competitors` | `COMPETITORS-REPORT.md`         |
| `/market social`      | `SOCIAL-CALENDAR.md`            |
| `/market funnel`      | `FUNNEL-ANALYSIS.md`            |
| `/market ads`         | `AD-CAMPAIGNS.md`               |
| `/market proposal`    | `CLIENT-PROPOSAL.md`            |
| `/market landing`     | `LANDING-ANALYSIS.md`           |
| `/market launch`      | `LAUNCH-PLAN.md`                |
| `/market report`      | `MARKETING-REPORT.md`           |
| `/market report-pdf`  | `MARKETING-REPORT-<domain>.pdf` |
| `/market seo`         | `SEO-AUDIT.md`                  |

---

## 🗑️ Uninstall

```bash
bash uninstall.sh
```

---

## 📜 Licence

MIT License — see [LICENSE](LICENSE)

---

<div align="center">

**Built for Claude Code · Bilingual FR/EN · MIT Licensed**

*Turn any website into a revenue opportunity — in minutes.*

</div>
