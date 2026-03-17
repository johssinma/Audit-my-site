#!/bin/bash
# claude-mark2 — Désinstallateur de la Suite Marketing en Français
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo ""
echo -e "${YELLOW}Désinstallation de claude-mark2 — Suite Marketing en Français...${NC}"
echo ""

SKILLS_DIR="$HOME/.claude/skills"
AGENTS_DIR="$HOME/.claude/agents"

# Supprimer les skills
SKILLS=("market" "market-audit" "market-copy" "market-emails" "market-social" "market-ads" "market-funnel" "market-competitors" "market-landing" "market-launch" "market-proposal" "market-report" "market-report-pdf" "market-seo" "market-brand")
for skill in "${SKILLS[@]}"; do
    if [ -d "$SKILLS_DIR/$skill" ]; then
        rm -rf "$SKILLS_DIR/$skill"
        echo -e "  ${GREEN}✓${NC} Skill supprimé : $skill"
    fi
done

# Supprimer les agents
AGENTS=("market-content" "market-conversion" "market-competitive" "market-technical" "market-strategy")
for agent in "${AGENTS[@]}"; do
    if [ -f "$AGENTS_DIR/$agent.md" ]; then
        rm "$AGENTS_DIR/$agent.md"
        echo -e "  ${GREEN}✓${NC} Agent supprimé : $agent"
    fi
done

echo ""
echo -e "${GREEN}claude-mark2 désinstallé avec succès.${NC}"
echo ""
