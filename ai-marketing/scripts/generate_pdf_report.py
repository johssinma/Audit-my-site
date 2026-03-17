#!/usr/bin/env python3
"""
Générateur de Rapport Marketing PDF — claude-mark2
Génère des rapports marketing PDF professionnels et prêts pour les clients, avec graphiques,
visualisations de scores et plans d'action priorisés.

Prérequis : reportlab (pip install reportlab)
"""

import sys
import json
import os
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib.colors import HexColor, white, black
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                     TableStyle, PageBreak, Image)
    from reportlab.graphics.shapes import Drawing, Rect, Circle, String, Line, Wedge
    from reportlab.graphics.charts.barcharts import VerticalBarChart
    from reportlab.graphics import renderPDF
except ImportError:
    print("Erreur : reportlab est requis. Installez avec : pip install reportlab")
    sys.exit(1)


# Palette de couleurs
COLORS = {
    "primary": HexColor("#1B2A4A"),
    "accent": HexColor("#2D5BFF"),
    "highlight": HexColor("#FF6B35"),
    "success": HexColor("#00C853"),
    "warning": HexColor("#FFB300"),
    "danger": HexColor("#FF1744"),
    "light_bg": HexColor("#F5F7FA"),
    "text": HexColor("#2C3E50"),
    "text_light": HexColor("#7F8C9B"),
    "border": HexColor("#E0E6ED"),
    "white": white,
    "black": black,
}


def score_color(score):
    """Retourner la couleur selon la valeur du score."""
    if score >= 80:
        return COLORS["success"]
    elif score >= 60:
        return COLORS["accent"]
    elif score >= 40:
        return COLORS["warning"]
    else:
        return COLORS["danger"]


def draw_score_gauge(score, x, y, size=80):
    """Créer un dessin de jauge de score circulaire."""
    d = Drawing(size + 20, size + 30)

    # Cercle de fond
    d.add(Circle(size / 2 + 10, size / 2 + 15, size / 2,
                 fillColor=COLORS["light_bg"], strokeColor=COLORS["border"], strokeWidth=2))

    # Arc de score (simplifié comme cercle intérieur coloré)
    color = score_color(score)
    inner_r = size / 2 - 8
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r,
                 fillColor=color, strokeColor=None))

    # Centre blanc
    d.add(Circle(size / 2 + 10, size / 2 + 15, inner_r - 10,
                 fillColor=COLORS["white"], strokeColor=None))

    # Texte du score
    d.add(String(size / 2 + 10, size / 2 + 10, str(int(score)),
                 fontSize=20, fillColor=COLORS["primary"],
                 textAnchor="middle", fontName="Helvetica-Bold"))

    return d


def create_bar_chart(categories, scores, width=450, height=180):
    """Créer un graphique en barres horizontales pour les scores de catégorie."""
    d = Drawing(width, height)

    bar_height = 20
    gap = 8
    max_bar_width = width - 180
    start_y = height - 30
    label_x = 5
    bar_x = 160

    for i, (cat, score) in enumerate(zip(categories, scores)):
        y = start_y - i * (bar_height + gap)

        # Label de catégorie
        d.add(String(label_x, y + 5, cat[:22],
                     fontSize=9, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica"))

        # Barre de fond
        d.add(Rect(bar_x, y, max_bar_width, bar_height,
                   fillColor=COLORS["light_bg"], strokeColor=None))

        # Barre de score
        bar_width = (score / 100) * max_bar_width
        color = score_color(score)
        d.add(Rect(bar_x, y, bar_width, bar_height,
                   fillColor=color, strokeColor=None))

        # Label du score
        d.add(String(bar_x + max_bar_width + 10, y + 5, f"{int(score)}",
                     fontSize=10, fillColor=COLORS["text"],
                     textAnchor="start", fontName="Helvetica-Bold"))

    return d


def generate_report(data, output_path):
    """Générer un rapport marketing PDF professionnel."""
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    # Styles personnalisés
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=28,
        textColor=COLORS["primary"],
        spaceAfter=6,
        fontName="Helvetica-Bold"
    )

    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=styles["Normal"],
        fontSize=14,
        textColor=COLORS["text_light"],
        spaceAfter=20,
        fontName="Helvetica"
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading1"],
        fontSize=18,
        textColor=COLORS["primary"],
        spaceBefore=20,
        spaceAfter=10,
        fontName="Helvetica-Bold"
    )

    subheading_style = ParagraphStyle(
        "CustomSubheading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=COLORS["accent"],
        spaceBefore=14,
        spaceAfter=8,
        fontName="Helvetica-Bold"
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["Normal"],
        fontSize=10,
        textColor=COLORS["text"],
        spaceAfter=6,
        fontName="Helvetica",
        leading=14
    )

    # Construire les éléments du document
    elements = []

    # === PAGE DE COUVERTURE ===
    elements.append(Spacer(1, 1.5 * inch))
    elements.append(Paragraph("Rapport d'Audit Marketing", title_style))

    url = data.get("url", "exemple.fr")
    date_str = data.get("date", datetime.now().strftime("%d %B %Y"))
    elements.append(Paragraph(f"{url}", subtitle_style))
    elements.append(Paragraph(f"Généré le : {date_str}", subtitle_style))
    elements.append(Spacer(1, 0.5 * inch))

    # Jauge de score global
    overall_score = data.get("overall_score", 0)
    gauge = draw_score_gauge(overall_score, 0, 0, size=100)
    elements.append(gauge)
    elements.append(Spacer(1, 0.3 * inch))

    grade = "A+" if overall_score >= 90 else "A" if overall_score >= 80 else "B" if overall_score >= 70 else "C" if overall_score >= 60 else "D" if overall_score >= 50 else "F"
    elements.append(Paragraph(f"Score Marketing Global : {int(overall_score)}/100 (Note : {grade})", heading_style))

    exec_summary = data.get("executive_summary", "Ce rapport fournit une analyse complète de l'efficacité marketing du site web à travers le contenu, la conversion, le SEO, le positionnement concurrentiel, la confiance de marque et la stratégie de croissance.")
    elements.append(Paragraph(exec_summary, body_style))

    elements.append(PageBreak())

    # === TABLEAU DE BORD DES SCORES ===
    elements.append(Paragraph("Tableau de Bord des Scores", heading_style))

    categories = data.get("categories", {})
    cat_names = list(categories.keys()) if categories else [
        "Contenu & Message", "Optimisation de Conversion", "SEO & Visibilité",
        "Positionnement Concurrentiel", "Marque & Confiance", "Croissance & Stratégie"
    ]
    cat_scores = [categories.get(c, {}).get("score", 50) for c in cat_names] if categories else [65, 58, 72, 55, 68, 60]

    # Graphique en barres
    chart = create_bar_chart(cat_names, cat_scores)
    elements.append(chart)
    elements.append(Spacer(1, 0.3 * inch))

    # Tableau des scores
    score_data = [["Catégorie", "Score", "Poids", "Statut"]]
    weights = ["25%", "20%", "20%", "15%", "10%", "10%"]
    for i, (name, score) in enumerate(zip(cat_names, cat_scores)):
        status = "Fort" if score >= 75 else "À Améliorer" if score >= 50 else "Critique"
        weight = weights[i] if i < len(weights) else "—"
        score_data.append([name, f"{int(score)}/100", weight, status])

    score_table = Table(score_data, colWidths=[180, 70, 60, 90])
    score_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    elements.append(score_table)

    elements.append(PageBreak())

    # === OBSERVATIONS CLÉS ===
    elements.append(Paragraph("Observations Clés", heading_style))

    findings = data.get("findings", [])
    if not findings:
        findings = [
            {"severity": "Critique", "finding": "Le titre de la page d'accueil manque de clarté — les visiteurs ne comprennent pas la proposition de valeur en moins de 5 secondes"},
            {"severity": "Haute", "finding": "Pas de preuve sociale sur la page d'accueil — témoignages, logos clients et badges de confiance manquants"},
            {"severity": "Haute", "finding": "Le CTA principal utilise un texte générique ('Commencer') au lieu d'un texte axé sur la valeur"},
            {"severity": "Moyenne", "finding": "Méta descriptions manquantes sur les pages d'atterrissage principales"},
            {"severity": "Moyenne", "finding": "Aucun mécanisme de capture email ou lead magnet visible"},
            {"severity": "Basse", "finding": "Le contenu du blog ne comporte pas de liens internes vers les pages produit"},
        ]

    findings_data = [["Sévérité", "Observation"]]
    for f in findings:
        severity = f.get("severity", "Moyenne")
        finding = f.get("finding", "")
        findings_data.append([severity, Paragraph(finding, body_style)])

    findings_table = Table(findings_data, colWidths=[70, 400])
    severity_colors = {
        "Critique": COLORS["danger"],
        "Critical": COLORS["danger"],
        "Haute": COLORS["highlight"],
        "High": COLORS["highlight"],
        "Moyenne": COLORS["warning"],
        "Medium": COLORS["warning"],
        "Basse": COLORS["accent"],
        "Low": COLORS["accent"]
    }
    table_style_cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
    ]
    for i, f in enumerate(findings, 1):
        color = severity_colors.get(f.get("severity", "Moyenne"), COLORS["warning"])
        table_style_cmds.append(("TEXTCOLOR", (0, i), (0, i), color))
        table_style_cmds.append(("FONTNAME", (0, i), (0, i), "Helvetica-Bold"))

    findings_table.setStyle(TableStyle(table_style_cmds))
    elements.append(findings_table)

    elements.append(PageBreak())

    # === PLAN D'ACTION ===
    elements.append(Paragraph("Plan d'Action Priorisé", heading_style))

    # Victoires Rapides
    elements.append(Paragraph("Victoires Rapides (Cette Semaine)", subheading_style))
    quick_wins = data.get("quick_wins", [
        "Réécrire le titre de la page d'accueil pour qu'il soit spécifique et axé bénéfice",
        "Ajouter 3-5 logos clients ou badges de confiance au-dessus de la ligne de flottaison",
        "Changer le CTA principal pour un texte axé sur la valeur (ex. 'Démarrer l'Essai Gratuit — Sans CB')",
        "Ajouter des méta descriptions aux 5 pages d'atterrissage principales",
    ])
    for i, win in enumerate(quick_wins, 1):
        elements.append(Paragraph(f"{i}. {win}", body_style))

    elements.append(Spacer(1, 0.2 * inch))

    # Moyen Terme
    elements.append(Paragraph("Moyen Terme (1-3 Mois)", subheading_style))
    medium_term = data.get("medium_term", [
        "Construire un tunnel de capture email avec lead magnet",
        "Créer des pages de comparaison pour les 3 principaux concurrents",
        "Développer 3 études de cas avec résultats mesurables",
        "Mettre en place une stratégie de contenu de blog ciblant des mots-clés à forte intention",
    ])
    for i, action in enumerate(medium_term, 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(Spacer(1, 0.2 * inch))

    # Stratégique
    elements.append(Paragraph("Stratégique (3-6 Mois)", subheading_style))
    strategic = data.get("strategic", [
        "Lancer un programme de parrainage avec une structure d'incitation",
        "Construire un hub d'autorité de contenu avec du contenu pilier",
        "Mettre en place une campagne de remarketing full-funnel",
        "Développer une optimisation de la tarification basée sur les métriques de valeur",
    ])
    for i, action in enumerate(strategic, 1):
        elements.append(Paragraph(f"{i}. {action}", body_style))

    elements.append(PageBreak())

    # === PAYSAGE CONCURRENTIEL ===
    if data.get("competitors"):
        elements.append(Paragraph("Paysage Concurrentiel", heading_style))

        comp_data = [["", data.get("brand_name", "Cible")] + [c.get("name", f"Concurrent {i+1}") for i, c in enumerate(data["competitors"][:3])]]
        comp_rows_fr = ["Positionnement", "Tarification", "Preuve Sociale", "Contenu"]
        comp_rows_keys = ["positioning", "pricing", "social_proof", "content"]

        for row_name, row_key in zip(comp_rows_fr, comp_rows_keys):
            row = [row_name, data.get("brand_name", "Cible")]
            for comp in data["competitors"][:3]:
                row.append(comp.get(row_key, "—"))
            while len(row) < len(comp_data[0]):
                row.append("—")
            comp_data.append(row)

        col_count = len(comp_data[0])
        col_width = 470 / col_count
        comp_table = Table(comp_data, colWidths=[col_width] * col_count)
        comp_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
            ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ]))
        elements.append(comp_table)
        elements.append(PageBreak())

    # === MÉTHODOLOGIE ===
    elements.append(Paragraph("Méthodologie", heading_style))
    elements.append(Paragraph(
        "Cet audit évalue six dimensions clés de l'efficacité marketing. "
        "Chaque catégorie est notée de 0 à 100 sur la base des meilleures pratiques sectorielles et des benchmarks concurrentiels.",
        body_style
    ))

    method_data = [
        ["Catégorie", "Poids", "Ce que Nous Mesurons"],
        ["Contenu & Message", "25%", "Qualité du texte, clarté de la proposition de valeur, efficacité des CTAs"],
        ["Optimisation de Conversion", "20%", "Design du tunnel, formulaires, preuve sociale, réduction de la friction"],
        ["SEO & Visibilité", "20%", "SEO on-page, SEO technique, structure du contenu"],
        ["Positionnement Concurrentiel", "15%", "Différenciation marché, tarification, stratégie alternatives"],
        ["Marque & Confiance", "10%", "Qualité du design, signaux de confiance, indicateurs d'autorité"],
        ["Croissance & Stratégie", "10%", "Stratégie tarifaire, canaux d'acquisition, rétention"],
    ]

    method_table = Table(method_data, colWidths=[140, 50, 280])
    method_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COLORS["primary"]),
        ("TEXTCOLOR", (0, 0), (-1, 0), COLORS["white"]),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, COLORS["border"]),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [COLORS["white"], COLORS["light_bg"]]),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    elements.append(method_table)

    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(
        "Généré par claude-mark2 — Suite Marketing IA pour Claude Code",
        ParagraphStyle("Footer", parent=body_style, fontSize=8, textColor=COLORS["text_light"])
    ))

    # Construire le PDF
    doc.build(elements)
    return output_path


def main():
    if len(sys.argv) < 2:
        # Mode démo — générer un rapport exemple
        sample_data = {
            "url": "https://exemple.fr",
            "date": datetime.now().strftime("%d %B %Y"),
            "overall_score": 62,
            "executive_summary": "Cet audit marketing révèle plusieurs opportunités à fort impact pour améliorer les taux de conversion et renforcer le positionnement concurrentiel. Le site web dispose de bases de contenu solides mais sous-performe en optimisation de conversion et en veille concurrentielle.",
            "categories": {
                "Contenu & Message": {"score": 68, "weight": "25%"},
                "Optimisation de Conversion": {"score": 52, "weight": "20%"},
                "SEO & Visibilité": {"score": 74, "weight": "20%"},
                "Positionnement Concurrentiel": {"score": 48, "weight": "15%"},
                "Marque & Confiance": {"score": 70, "weight": "10%"},
                "Croissance & Stratégie": {"score": 55, "weight": "10%"},
            },
            "findings": [
                {"severity": "Critique", "finding": "Le titre de la page d'accueil est générique — ne communique pas une valeur spécifique à la cible"},
                {"severity": "Critique", "finding": "Aucune preuve sociale visible au-dessus de la ligne de flottaison sur la page d'accueil"},
                {"severity": "Haute", "finding": "Le bouton CTA principal dit 'Envoyer' — devrait utiliser un texte axé sur la valeur"},
                {"severity": "Haute", "finding": "La page de tarification manque de fonctionnalités comparatives et ne gère pas les objections"},
                {"severity": "Moyenne", "finding": "Pages de comparaison concurrentes manquantes — perte de trafic à forte intention"},
                {"severity": "Moyenne", "finding": "Les articles de blog ne comportent pas de liens internes vers les pages produit"},
                {"severity": "Basse", "finding": "Liens réseaux sociaux dans le pied de page mais pas d'intégration de preuve sociale"},
            ],
            "quick_wins": [
                "Réécrire le titre de la page d'accueil : 'Nous aidons les entreprises à croître' → 'Obtenez 3x plus de leads qualifiés en 30 jours — sans démarchage à froid'",
                "Ajouter 5 logos clients au-dessus de la ligne de flottaison avec 'Fait confiance par 500+ entreprises'",
                "Changer le bouton de formulaire de 'Envoyer' à 'Obtenir Mon Audit Marketing Gratuit'",
                "Ajouter une section témoignages avec nom, photo, entreprise et résultats spécifiques",
            ],
            "medium_term": [
                "Créer des pages '[Concurrent] Alternative' pour les 3 principaux concurrents",
                "Créer 3 études de cas vidéo montrant les résultats clients mesurables",
                "Mettre en place un pop-up d'intention de sortie avec une offre de lead magnet",
                "Lancer une séquence email de nurturing pour les leads qui ne convertissent pas immédiatement",
            ],
            "strategic": [
                "Développer un hub d'autorité de contenu avec 10 pages pilier ciblant des mots-clés à fort volume",
                "Construire un programme de parrainage avec incitations mutuelles",
                "Lancer des campagnes de remarketing sur Meta et Google avec des messages basés sur le tunnel",
                "Créer un outil ou évaluation gratuite pour capturer des leads en haut du tunnel",
            ],
            "competitors": [
                {"name": "Concurrent A", "positioning": "Plateforme tout-en-un", "pricing": "49-199€/mois", "social_proof": "10K+ utilisateurs", "content": "Blog actif"},
                {"name": "Concurrent B", "positioning": "Focus entreprise", "pricing": "Sur devis", "social_proof": "Logos CAC 40", "content": "Livres blancs"},
                {"name": "Concurrent C", "positioning": "Économique", "pricing": "Gratuit-29€/mois", "social_proof": "4.8★ G2", "content": "Chaîne YouTube"},
            ],
            "brand_name": "Exemple SARL"
        }

        output = "MARKETING-REPORT-sample.pdf"
        generate_report(sample_data, output)
        print(f"Rapport exemple généré : {output}")
        return

    # Mode entrée JSON
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "RAPPORT-MARKETING.pdf"

    with open(input_file, "r") as f:
        data = json.load(f)

    generate_report(data, output_file)
    print(f"Rapport généré : {output_file}")


if __name__ == "__main__":
    main()
