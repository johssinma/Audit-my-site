# 🔍 Audit My Site — Suite Marketing IA pour Claude Code

> **15 commandes slash · 5 agents IA parallèles · 4 scripts Python · Bilingue FR/EN**

[![Licence](https://img.shields.io/badge/licence-MIT-22d38a.svg)](ai-marketing/LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-2d8bff.svg)](#)
[![Bilingue](https://img.shields.io/badge/bilingue-FR%20%2F%20EN-f0b429.svg)](#)
[![Conçu pour](https://img.shields.io/badge/conçu%20pour-Claude%20Code-7a8499.svg)](#)

🇫🇷 **Français**  |  **[🇬🇧 English version](README.en.md)**

---

## 🛒 Obtenir le Bundle Premium

**[Acheter sur Gumroad — €29 paiement unique](https://auditmysiteai.gumroad.com/l/audit-my-site)**

> Inclus : template de rapport HTML premium · template de proposition client · ZIP pré-organisé · support personnel 30 jours

---

## ✨ C'est quoi ?

**Audit My Site** est une suite complète d'outils marketing IA qui s'intègre à Claude Code. Collez une URL, lancez une commande — obtenez un audit marketing professionnel et scoré en quelques minutes.

Pas d'abonnement SaaS. Pas de frais mensuels. Fonctionne en local depuis votre terminal.

---

## 🏆 Exemple de Résultat Réel

Lancez `/market quick https://nike.com` → obtenez ceci en 60 secondes :

```
⚡ APERÇU RAPIDE : Nike.com
Score : 85/100

✅ TOP 2 POINTS FORTS
1. Clarté de marque iconique — aucune ambiguïté sur la valeur
2. L'écosystème membership crée de fortes boucles de rétention

⚠️ TOP 3 URGENCES À CORRIGER
1. Aucun titre orienté bénéfices au-dessus de la ligne de flottaison
   → Ajouter "Conçu pour les athlètes qui refusent d'arrêter" en H1

2. Preuve sociale trop enfouie dans le tunnel
   → Remonter "4,8★ sur 12K avis" près du CTA principal

3. Méga-menu avec 20+ liens crée une paralysie décisionnelle
   → Réduire à 6 catégories principales avec navigation progressive

💡 RECOMMANDATION EN UNE PHRASE :
Arrêtez de montrer vos produits. Montrez la transformation.
```

---

## 📦 Ce qui est Installé

|    | Composant          | Quantité | Description                                  |
| -- | ------------------ | --------- | -------------------------------------------- |
| 🧠 | **Skills**   | 15        | Commandes slash pour chaque tâche marketing |
| 🤖 | **Agents**   | 5         | Sous-agents spécialisés en parallèle      |
| 🐍 | **Scripts**  | 4         | Outils Python d'analyse et génération PDF  |
| 📄 | **Modèles** | 4         | Templates prêts à l'emploi                 |

---

## ⚡ Installation Rapide

**Option 1 — Une commande depuis n'importe où :**

```bash
curl -fsSL https://raw.githubusercontent.com/johssinma/audit-my-site/main/ai-marketing/install.sh | bash
```

**Option 2 — Cloner en local :**

```bash
git clone https://github.com/johssinma/audit-my-site.git
cd audit-my-site/ai-marketing
bash install.sh
```

> **Requis :** Claude Code (Pro ou clé API) · Python 3.8+

---

## 🚀 Les 15 Commandes

| Commande                      | Ce qu'elle fait                               | Fichier généré          |
| ----------------------------- | --------------------------------------------- | -------------------------- |
| `/market audit <url>`       | 🔥 Audit complet — 5 agents IA en parallèle | `AUDIT-MARKETING.md`     |
| `/market quick <url>`       | ⚡ Scan de page d'accueil en 60 secondes      | Terminal                   |
| `/market copy <url>`        | ✍️ Analyse copywriting + réécritures      | `SUGGESTIONS-COPY.md`    |
| `/market emails <sujet>`    | 📧 Séquences d'emails complètes             | `SEQUENCES-EMAILS.md`    |
| `/market social <sujet>`    | 📱 Calendrier réseaux sociaux 30 jours       | `CALENDRIER-SOCIAL.md`   |
| `/market ads <url>`         | 📣 Scripts pub + briefs créatifs             | `CAMPAGNES-PUB.md`       |
| `/market funnel <url>`      | 💰 Analyse du tunnel de vente                 | `ANALYSE-FUNNEL.md`      |
| `/market competitors <url>` | 🔍 Intelligence concurrentielle               | `RAPPORT-CONCURRENTS.md` |
| `/market landing <url>`     | 🎯 CRO de page d'atterrissage                 | `ANALYSE-LANDING.md`     |
| `/market launch <produit>`  | 🚀 Plan de lancement produit 8 semaines       | `PLAN-LANCEMENT.md`      |
| `/market proposal <client>` | 📋 Proposition commerciale avec ROI           | `PROPOSITION-CLIENT.md`  |
| `/market report <url>`      | 📊 Rapport marketing complet (MD)             | `RAPPORT-MARKETING.md`   |
| `/market report-pdf <url>`  | 📄 Rapport marketing professionnel (PDF)      | `RAPPORT-MARKETING.pdf`  |
| `/market seo <url>`         | 🔎 Audit SEO de contenu                       | `AUDIT-SEO.md`           |
| `/market brand <url>`       | 🎨 Guide de voix de marque                    | `VOIX-DE-MARQUE.md`      |

---

## 🏗️ Comment Fonctionne l'Audit Complet

```
/market audit <url>
       │
       ▼
  Orchestrateur — récupère la page d'accueil + 5 pages clés
       │
       ├─────────────────│────────────────│───────────────────│────────────────┐
       ▼                 ▼                ▼                   ▼                ▼
  market-content  market-conversion  market-technical  market-competitive  market-strategy
  Contenu & Copy   CRO & Tunnels    SEO & Tracking   Intelligence conc.  Marque & Croissance
     25% poids       20% poids       20% poids          15% poids         10% + 10%
       │
       ▼
  Score composite pondéré → AUDIT-MARKETING.md (scoré, PDF prêt client)
```

---

## 🎯 Pour Qui ?

| Profil                           | Comment l'utiliser                                                 |
| -------------------------------- | ------------------------------------------------------------------ |
| 🏢**Agences marketing**    | Livrer des audits IA à vos clients en quelques minutes            |
| 👤**Freelances marketing** | Vous démarquer avec des rapports scorés et professionnels        |
| 🛒**E-commerces**          | Trouver exactement ce qui tue vos conversions                      |
| 💻**Fondateurs SaaS**      | Avoir un regard extérieur sur votre tunnel et vos messages        |
| 🎓**Consultants**          | Générer des propositions clients appuyées par une vraie analyse |
| 🔧**Développeurs**        | Construire des outils marketing sur une base solide                |

---

## 🆓 Gratuit vs ⭐ Premium

| Fonctionnalité               | GitHub (Gratuit) | Bundle Gumroad (€29) |
| ----------------------------- | :--------------: | :-------------------: |
| 15 commandes slash            |        ✅        |          ✅          |
| 5 agents IA                   |        ✅        |          ✅          |
| Versions FR + EN              |        ✅        |          ✅          |
| Scripts Python                |        ✅        |          ✅          |
| Template rapport HTML premium |        ❌        |          ✅          |
| Template proposition client   |        ❌        |          ✅          |
| ZIP pré-organisé            |        ❌        |          ✅          |
| Mises à jour par email       |        ❌        |          ✅          |
| Support personnel 30 jours    |        ❌        |          ✅          |

**[Obtenir le Bundle Premium sur Gumroad — €29](https://auditmysiteai.gumroad.com/l/audit-my-site)**

---

## 🗂️ Structure du Projet

```
audit-my-site/
├── ai-marketing/               🇫🇷 Version française
│   ├── agents/                 5 sous-agents IA spécialisés
│   ├── market/                 Skill orchestrateur principal
│   ├── skills/                 15 skills slash command
│   ├── scripts/                Scripts Python d'analyse
│   ├── templates/              Templates clients
│   └── install.sh
│
├── ai-marketing-english/       🇬🇧 Version anglaise
│   ├── agents/
│   ├── market/
│   ├── skills/
│   ├── scripts/
│   ├── templates/
│   └── install.sh
│
├── README.md                   🇫🇷 Documentation française
└── README.en.md                🇬🇧 Documentation anglaise
```

---

## 🛠️ Prérequis

```bash
# Requis
npm install -g @anthropic-ai/claude-code   # Claude Code CLI

# Optionnel — pour les rapports PDF
pip install reportlab==4.0.4
```

> Nécessite un abonnement **Claude Pro** ($20/mois) ou une **clé API Anthropic**

---

## 🗑️ Désinstallation

```bash
bash uninstall.sh
```

---

## 📜 Licence

**MIT** — utilisation commerciale autorisée, modification libre, livraison aux clients sous votre propre marque.

Voir [LICENSE](ai-marketing/LICENSE)

---

Créé par [Mohssine Mazouz](https://github.com/johssinma) · Bilingue FR/EN · Licence MIT

**[⭐ Star ce repo](https://github.com/johssinma/audit-my-site)**  ·  **[🛒 Bundle Premium — €29](https://auditmysiteai.gumroad.com/l/audit-my-site)**

*Transformez n'importe quel site en opportunité de revenus — en quelques minutes.*`<div align="center">`
`<img src="https://img.shields.io/badge/Audit_My_Site-Suite_Marketing_IA-0f1117?style=for-the-badge&labelColor=0f1117&color=2d8bff" alt="Audit My Site"/>`

# 🔍 Audit My Site
