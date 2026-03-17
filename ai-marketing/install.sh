#!/bin/bash
# claude-mark2 — Installateur de Skills Claude Code en Français
# Installe les skills marketing, agents et scripts dans Claude Code

set -e

# Couleurs
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo -e "${CYAN}╔══════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║   claude-mark2 — Suite Marketing en Français ║${NC}"
echo -e "${CYAN}║   15 Skills · 5 Agents · 4 Scripts · PDF     ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════╝${NC}"
echo ""

# Détecter le répertoire du script
if [ -n "$BASH_SOURCE" ] && [ "$BASH_SOURCE" != "bash" ] && [ -f "$BASH_SOURCE" ]; then
    SCRIPT_DIR="$(cd "$(dirname "$BASH_SOURCE")" && pwd)"
else
    # Exécution via curl | bash — besoin de cloner
    echo -e "${YELLOW}Installation distante — clonage du dépôt...${NC}"
    TEMP_DIR=$(mktemp -d)
    git clone --depth 1 https://github.com/johssinma/test_marketing.git "$TEMP_DIR/claude-mark2" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo -e "${RED}Échec du clonage du dépôt.${NC}"
        exit 1
    fi
    SCRIPT_DIR="$TEMP_DIR/claude-mark2"
fi

# Répertoires cibles
SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

echo -e "${BLUE}Source :${NC} $SCRIPT_DIR"
echo -e "${BLUE}Cible :${NC}  $SKILLS_DIR"
echo ""

# Vérifier si Claude Code est disponible
if command -v claude &>/dev/null; then
    echo -e "${GREEN}✓ Claude Code détecté${NC}"
else
    echo -e "${YELLOW}⚠ Claude Code non trouvé dans PATH${NC}"
    if [ -t 0 ]; then
        read -p "  Continuer quand même ? (o/n) : " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[OoYy]$ ]]; then
            echo "Installation annulée."
            exit 0
        fi
    else
        echo "  Continuation (mode non-interactif)..."
    fi
fi

# Créer les répertoires
echo -e "\n${BLUE}Création des répertoires...${NC}"
mkdir -p "$SKILLS_DIR"
mkdir -p "$AGENTS_DIR"

# Installer le skill orchestrateur principal
echo -e "${BLUE}Installation du skill principal...${NC}"
mkdir -p "$SKILLS_DIR/market"
cp "$SCRIPT_DIR/market/SKILL.md" "$SKILLS_DIR/market/SKILL.md"
echo -e "  ${GREEN}✓${NC} market/SKILL.md (orchestrateur)"

# Installer les sous-skills
echo -e "\n${BLUE}Installation des sous-skills...${NC}"
SKILLS=(
    "market-audit"
    "market-quick"
    "market-copy"
    "market-emails"
    "market-social"
    "market-ads"
    "market-funnel"
    "market-competitors"
    "market-landing"
    "market-launch"
    "market-proposal"
    "market-report"
    "market-report-pdf"
    "market-seo"
    "market-brand"
)

SKILL_COUNT=0
for skill in "${SKILLS[@]}"; do
    if [ -f "$SCRIPT_DIR/skills/$skill/SKILL.md" ]; then
        mkdir -p "$SKILLS_DIR/$skill"
        cp "$SCRIPT_DIR/skills/$skill/SKILL.md" "$SKILLS_DIR/$skill/SKILL.md"
        echo -e "  ${GREEN}✓${NC} $skill"
        SKILL_COUNT=$((SKILL_COUNT + 1))
    else
        echo -e "  ${YELLOW}⚠${NC} $skill (non trouvé, ignoré)"
    fi
done

# Installer les agents
echo -e "\n${BLUE}Installation des agents...${NC}"
AGENTS=(
    "market-content"
    "market-conversion"
    "market-competitive"
    "market-technical"
    "market-strategy"
)

AGENT_COUNT=0
for agent in "${AGENTS[@]}"; do
    if [ -f "$SCRIPT_DIR/agents/$agent.md" ]; then
        cp "$SCRIPT_DIR/agents/$agent.md" "$AGENTS_DIR/$agent.md"
        echo -e "  ${GREEN}✓${NC} $agent"
        AGENT_COUNT=$((AGENT_COUNT + 1))
    else
        echo -e "  ${YELLOW}⚠${NC} $agent (non trouvé, ignoré)"
    fi
done

# Installer les scripts
echo -e "\n${BLUE}Installation des scripts...${NC}"
SCRIPTS_TARGET="$SKILLS_DIR/market/scripts"
mkdir -p "$SCRIPTS_TARGET"

SCRIPT_FILES=(
    "analyze_page.py"
    "competitor_scanner.py"
    "social_calendar.py"
    "generate_pdf_report.py"
)

SCRIPT_COUNT=0
for script in "${SCRIPT_FILES[@]}"; do
    if [ -f "$SCRIPT_DIR/scripts/$script" ]; then
        cp "$SCRIPT_DIR/scripts/$script" "$SCRIPTS_TARGET/$script"
        chmod +x "$SCRIPTS_TARGET/$script"
        echo -e "  ${GREEN}✓${NC} $script"
        SCRIPT_COUNT=$((SCRIPT_COUNT + 1))
    else
        echo -e "  ${YELLOW}⚠${NC} $script (non trouvé, ignoré)"
    fi
done

# Installer les modèles
echo -e "\n${BLUE}Installation des modèles...${NC}"
TEMPLATES_TARGET="$SKILLS_DIR/market/templates"
mkdir -p "$TEMPLATES_TARGET"

TEMPLATE_COUNT=0
if [ -d "$SCRIPT_DIR/templates" ]; then
    for template in "$SCRIPT_DIR/templates"/*.md; do
        if [ -f "$template" ]; then
            cp "$template" "$TEMPLATES_TARGET/$(basename "$template")"
            echo -e "  ${GREEN}✓${NC} $(basename "$template")"
            TEMPLATE_COUNT=$((TEMPLATE_COUNT + 1))
        fi
    done
fi

# Vérifier les dépendances Python
echo -e "\n${BLUE}Vérification des dépendances Python...${NC}"
if command -v python3 &>/dev/null; then
    PYTHON_VERSION=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null)
    echo -e "  ${GREEN}✓${NC} Python $PYTHON_VERSION détecté"

    # Vérifier reportlab (nécessaire pour les rapports PDF)
    if python3 -c "import reportlab" 2>/dev/null; then
        echo -e "  ${GREEN}✓${NC} reportlab installé (rapports PDF prêts)"
    else
        echo -e "  ${YELLOW}⚠${NC} reportlab non installé (nécessaire pour les rapports PDF)"
        echo -e "    Installer avec : ${CYAN}pip install reportlab${NC}"
    fi

    # Vérifier requests (optionnel, les scripts utilisent urllib comme fallback)
    if python3 -c "import requests" 2>/dev/null; then
        echo -e "  ${GREEN}✓${NC} requests installé"
    fi
else
    echo -e "  ${YELLOW}⚠${NC} Python 3 non trouvé — les scripts ne fonctionneront pas"
    echo -e "    Installer Python : ${CYAN}https://python.org${NC}"
fi

# Nettoyer le répertoire temporaire si utilisé
if [ -n "$TEMP_DIR" ] && [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi

# Résumé
echo ""
echo -e "${GREEN}╔══════════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║         Installation Terminée !               ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  Skills installés :    ${GREEN}$SKILL_COUNT${NC}"
echo -e "  Agents installés :    ${GREEN}$AGENT_COUNT${NC}"
echo -e "  Scripts installés :   ${GREEN}$SCRIPT_COUNT${NC}"
echo -e "  Modèles installés :   ${GREEN}$TEMPLATE_COUNT${NC}"
echo ""
echo -e "${CYAN}Commandes Disponibles :${NC}"
echo "  /market audit <url>        Audit marketing complet (5 agents parallèles)"
echo "  /market quick <url>        Aperçu marketing en 60 secondes"
echo "  /market copy <url>         Générer du texte optimisé"
echo "  /market emails <sujet>     Générer des séquences d'emails"
echo "  /market social <sujet>     Calendrier de contenu réseaux sociaux"
echo "  /market ads <url>          Créatifs et textes publicitaires"
echo "  /market funnel <url>       Analyse du tunnel de vente"
echo "  /market competitors <url>  Intelligence concurrentielle"
echo "  /market landing <url>      CRO de page d'atterrissage"
echo "  /market launch <produit>   Plan de lancement"
echo "  /market proposal <client>  Générateur de proposition commerciale"
echo "  /market report <url>       Rapport marketing (Markdown)"
echo "  /market report-pdf <url>   Rapport marketing (PDF)"
echo "  /market seo <url>          Audit SEO de contenu"
echo "  /market brand <url>        Analyse de la voix de marque"
echo ""
echo -e "  ${YELLOW}Démarrez une nouvelle session Claude Code pour utiliser les skills.${NC}"
echo ""
