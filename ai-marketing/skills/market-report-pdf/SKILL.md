# Générateur de Rapport Marketing PDF

## Objectif du Skill
Générer un rapport marketing PDF professionnel et visuellement soigné à l'aide du script Python `scripts/generate_pdf_report.py`. Ce skill collecte toutes les données d'audit et d'analyse disponibles, les structure au format JSON attendu, invoque le script et produit un PDF de marque avec jauges de score, graphiques en barres, tableaux comparatifs, observations et plan d'action priorisé.

**IMPORTANT : Tu dois toujours répondre et rédiger tous tes livrables en français.**

## Quand Utiliser
- L'utilisateur veut un rapport PDF (pas seulement Markdown)
- L'utilisateur prépare un livrable pour une présentation client
- L'utilisateur demande un "rapport soigné", "rapport client" ou "rapport PDF"
- L'utilisateur veut un rapport visuel avec graphiques et scores
- Déclenché par `/market report-pdf` ou `/market report-pdf <domaine>`

## PDF vs Markdown

| Format | Idéal Pour | Avantages | Inconvénients |
|---|---|---|---|
| **PDF** | Présentations clients, pièces jointes email, supports commerciaux | Apparence professionnelle, mise en forme cohérente, graphiques visuels, imprimable | Plus difficile à modifier, nécessite le script Python |
| **Markdown** | Usage interne, référence rapide, édition itérative, gestion de version | Facile à modifier, lisible dans n'importe quel éditeur, compatible git | Moins soigné visuellement, pas de graphiques |

**Règle générale :** Si le rapport va à un client ou prospect, utiliser le PDF. Pour un usage interne ou une édition ultérieure, utiliser le Markdown.

## Comment Exécuter

### Étape 1 : Collecter Toutes les Données Disponibles
Rassembler les données de toutes les exécutions précédentes de skills. Chercher ces fichiers dans le répertoire projet :

**Sources de données principales :**
- `AUDIT-MARKETING.md` — Résultats globaux de l'audit
- `ANALYSE-LANDING.md` — Analyse de conversion de la page d'atterrissage
- `AUDIT-SEO.md` — Observations SEO
- `VOIX-DE-MARQUE.md` — Analyse de la voix de marque
- `RAPPORT-CONCURRENTS.md` — Données de comparaison concurrentielle
- `ANALYSE-FUNNEL.md` — Analyse du tunnel de vente
- `CALENDRIER-SOCIAL.md` — Audit des réseaux sociaux
- `SEQUENCES-EMAILS.md` — Audit email marketing
- `CAMPAGNES-PUB.md` — Audit publicitaire

**Si aucune donnée préalable n'existe :**
1. Recommander à l'utilisateur d'exécuter d'abord `/market audit <url>` pour de meilleurs résultats
2. Si l'utilisateur insiste pour générer un rapport sans audits préalables, analyser directement l'URL fournie et construire la structure de données de zéro
3. Utiliser le script analyze_page.py pour collecter des données automatisées : `python scripts/analyze_page.py <url>`

### Étape 2 : Construire la Structure de Données JSON
Le script `scripts/generate_pdf_report.py` attend un fichier JSON en entrée avec cette structure exacte :

```json
{
  "url": "https://exemple.fr",
  "date": "12 mars 2026",
  "brand_name": "Exemple SARL",
  "overall_score": 62,
  "executive_summary": "Un résumé en 2-4 phrases de la santé marketing globale, des principales opportunités et de l'impact CA estimé de la mise en œuvre des recommandations.",
  "categories": {
    "Contenu & Message": {
      "score": 68,
      "weight": "25%"
    },
    "Optimisation de Conversion": {
      "score": 52,
      "weight": "20%"
    },
    "SEO & Visibilité": {
      "score": 74,
      "weight": "20%"
    },
    "Positionnement Concurrentiel": {
      "score": 48,
      "weight": "15%"
    },
    "Marque & Confiance": {
      "score": 70,
      "weight": "10%"
    },
    "Croissance & Stratégie": {
      "score": 55,
      "weight": "10%"
    }
  },
  "findings": [
    {
      "severity": "Critique",
      "finding": "Description de l'observation la plus importante"
    },
    {
      "severity": "Haute",
      "finding": "Description d'une observation de haute priorité"
    },
    {
      "severity": "Moyenne",
      "finding": "Description d'une observation de priorité moyenne"
    },
    {
      "severity": "Basse",
      "finding": "Description d'une observation de moindre priorité"
    }
  ],
  "quick_wins": [
    "Premier élément d'action rapide",
    "Deuxième élément d'action rapide",
    "Troisième élément d'action rapide"
  ],
  "medium_term": [
    "Premier élément d'action moyen terme",
    "Deuxième élément d'action moyen terme",
    "Troisième élément d'action moyen terme"
  ],
  "strategic": [
    "Premier élément d'action stratégique",
    "Deuxième élément d'action stratégique",
    "Troisième élément d'action stratégique"
  ],
  "competitors": [
    {
      "name": "Concurrent A",
      "positioning": "Leur position sur le marché",
      "pricing": "Leur modèle de tarification",
      "social_proof": "Leurs signaux de confiance",
      "content": "Leur approche de contenu"
    },
    {
      "name": "Concurrent B",
      "positioning": "Leur position sur le marché",
      "pricing": "Leur modèle de tarification",
      "social_proof": "Leurs signaux de confiance",
      "content": "Leur approche de contenu"
    }
  ]
}
```

### Étape 3 : Guide d'Assemblage des Données Champ par Champ

#### `url` (chaîne, requis)
L'URL du site cible. Utiliser l'URL complète avec le protocole.

#### `date` (chaîne, requis)
La date de génération du rapport. Format : "JJ mois AAAA" (ex. "12 mars 2026").

#### `brand_name` (chaîne, requis)
Le nom de l'entreprise ou de la marque. Utilisé dans les en-têtes du tableau de comparaison avec les concurrents.

#### `overall_score` (entier, 0-100, requis)
La moyenne pondérée de tous les scores de catégorie. Calculer comme :
```
score_global = (contenu * 0,25) + (conversion * 0,20) + (seo * 0,20) + (concurrentiel * 0,15) + (marque * 0,10) + (croissance * 0,10)
```

#### `executive_summary` (chaîne, requis)
Un résumé en 2-4 phrases couvrant :
- Évaluation actuelle de la santé marketing
- 1-2 observations les plus impactantes
- Impact CA estimé de la mise en œuvre des recommandations
- Première étape recommandée

Rester concis et percutant. Apparaît sur la page de couverture juste en dessous de la jauge de score.

#### `categories` (objet, requis)
Exactement 6 catégories avec leurs scores. Les catégories correspondent à ces domaines d'évaluation :

| Catégorie | Ce qu'elle Mesure | Guide de Score |
|---|---|---|
| Contenu & Message | Qualité du texte, proposition de valeur, clarté des titres, texte CTA, cohérence de la voix de marque | 80+ : Clair, axé bénéfices, spécifique. 60-79 : Adéquat mais générique. <60 : Vague, axé fonctionnalités, peu clair |
| Optimisation de Conversion | Preuve sociale, design des formulaires, placement CTA, gestion des objections, urgence | 80+ : Plusieurs types de preuves, formulaires optimisés, CTAs clairs. 60-79 : Certains éléments présents. <60 : Éléments critiques manquants |
| SEO & Visibilité | Balises titre, méta descriptions, titres, schema, liens internes, vitesse de page | 80+ : Entièrement optimisé. 60-79 : Principalement présent avec des lacunes. <60 : Problèmes majeurs |
| Positionnement Concurrentiel | Différenciation, clarté tarifaire, contenu comparatif, conscience du marché | 80+ : Positionnement clair, pages comparatives. 60-79 : Quelque différenciation. <60 : Pas de positionnement clair |
| Marque & Confiance | Qualité du design, badges de confiance, indicateurs de sécurité, apparence professionnelle | 80+ : Design moderne, signaux de confiance partout. 60-79 : Design adéquat. <60 : Désuet ou non professionnel |
| Croissance & Stratégie | Capture de leads, email marketing, stratégie de contenu, canaux d'acquisition | 80+ : Stratégie multi-canal en place. 60-79 : Certains canaux actifs. <60 : Pas de stratégie de croissance claire |

#### `findings` (tableau, requis)
Un tableau d'objets observation, chacun avec les champs `severity` et `finding`.

**Niveaux de sévérité :**
- `Critique` — Perd directement du CA ou des clients. Corriger immédiatement.
- `Haute` — Impact significatif sur la croissance. Corriger dans 1-2 semaines.
- `Moyenne` — Opportunité d'amélioration significative. Corriger dans 1 mois.
- `Basse` — Amélioration souhaitable. Corriger quand le temps le permet.

**Rédiger des observations efficaces :**
- Être spécifique : "Le titre de la page d'accueil dit 'Bienvenue sur Notre Plateforme'" pas "Le titre doit être amélioré"
- Quantifier l'impact : "Méta descriptions manquantes sur 8 des 12 pages d'atterrissage"
- Référencer les benchmarks : "Le temps de chargement est de 4,2s (benchmark : moins de 2s)"
- Inclure des preuves : "Aucun témoignage trouvé sur la page d'accueil, la page de tarification ou la page d'inscription"

Viser 5-10 observations. Ordonner de la plus à la moins sévère.

#### `quick_wins` (tableau, requis)
3-5 actions pouvant être implémentées en une semaine avec un effort minimal. Chacune doit être une instruction spécifique et actionnable.

**Bon exemple :** "Réécrire le titre de la page d'accueil de 'Bienvenue sur Notre Plateforme' à 'Réduisez Votre Temps de Reporting de 75% — Analytics Automatisés pour les Équipes de Croissance'"

**Mauvais exemple :** "Améliorer le titre" (trop vague)

#### `medium_term` (tableau, requis)
3-5 actions nécessitant 1-3 mois pour être implémentées. Plus engagées mais à fort impact.

#### `strategic` (tableau, requis)
3-5 actions nécessitant 3-6 mois. Ce sont des changements fondamentaux nécessitant planification et effort soutenu.

#### `competitors` (tableau, optionnel)
Jusqu'à 3 objets concurrent pour le tableau comparatif. Si aucune donnée concurrentielle n'est disponible, omettre ce champ — le script ignorera la section concurrents.

### Étape 4 : Écrire le Fichier JSON
Sauvegarder les données assemblées dans un fichier JSON temporaire :

```bash
cat > /tmp/report_data.json << 'JSONEOF'
{
  ... données JSON assemblées ...
}
JSONEOF
```

### Étape 5 : Invoquer le Script Générateur de PDF

**Vérification des prérequis :**
D'abord, vérifier que `reportlab` est installé :
```bash
python3 -c "import reportlab" 2>/dev/null || pip3 install reportlab
```

**Générer le rapport :**
```bash
python3 scripts/generate_pdf_report.py /tmp/report_data.json "RAPPORT-MARKETING-<domaine>.pdf"
```

Remplacer `<domaine>` par le nom de domaine du site cible (sans protocole ni www), en utilisant des tirets à la place des points. Par exemple :
- `exemple.fr` devient `RAPPORT-MARKETING-exemple-fr.pdf`
- `monapp.io` devient `RAPPORT-MARKETING-monapp-io.pdf`

**Mode démo (sans arguments) :**
Exécuter le script sans arguments génère un rapport exemple avec des données de démonstration :
```bash
python3 scripts/generate_pdf_report.py
# Crée : MARKETING-REPORT-sample.pdf
```

### Étape 6 : Vérifier la Sortie
Après génération, vérifier que le PDF a bien été créé :
```bash
ls -la "RAPPORT-MARKETING-<domaine>.pdf"
```

Indiquer le chemin du fichier et sa taille à l'utilisateur.

### Étape 7 : Nettoyage
Supprimer le fichier JSON temporaire :
```bash
rm /tmp/report_data.json
```

## Contenu du Rapport PDF

Le PDF généré comprend les pages suivantes :

### Page 1 : Page de Couverture
- Titre du rapport : "Rapport d'Audit Marketing"
- URL cible
- Date de génération
- Jauge de score global (visualisation circulaire avec code couleur)
- Lettre de note (A+ à F)
- Paragraphe de résumé exécutif

### Page 2 : Tableau de Bord des Scores
- Graphique en barres horizontales montrant les 6 scores de catégorie avec code couleur
- Tableau des scores avec noms de catégorie, scores, poids et labels de statut
- Code couleur : Vert (80+), Bleu (60-79), Jaune (40-59), Rouge (<40)

### Page 3 : Observations Clés
- Tableau des observations avec labels de sévérité et descriptions
- Indicateurs de sévérité avec code couleur (Critique = rouge, Haute = orange, Moyenne = jaune, Basse = bleu)
- Observations ordonnées de la plus à la moins sévère

### Page 4 : Plan d'Action Priorisé
- Section Victoires Rapides (Cette Semaine)
- Section Moyen Terme (1-3 Mois)
- Section Stratégique (3-6 Mois)
- Actions numérotées dans chaque niveau

### Page 5 : Paysage Concurrentiel (si données fournies)
- Tableau comparatif client vs jusqu'à 3 concurrents
- Lignes : Positionnement, Tarification, Preuve Sociale, Contenu

### Dernière Page : Méthodologie
- Explication de la méthodologie de scoring
- Poids des catégories et critères de mesure
- Pied de page : "Généré par AI Marketing Suite pour Claude Code"

## Palette de Couleurs

Le PDF utilise une palette professionnelle :

| Élément | Couleur | Code Hex |
|---|---|---|
| Principal (en-têtes, titres) | Bleu Marine Foncé | #1B2A4A |
| Accent (liens, surlignages) | Bleu | #2D5BFF |
| Mise en Valeur (attention) | Orange | #FF6B35 |
| Succès (scores élevés) | Vert | #00C853 |
| Avertissement (scores moyens) | Ambre | #FFB300 |
| Danger (scores faibles, critique) | Rouge | #FF1744 |
| Fond clair | Gris Clair | #F5F7FA |
| Texte principal | Gris Foncé | #2C3E50 |
| Texte secondaire | Gris Moyen | #7F8C9B |
| Bordures | Bordure Claire | #E0E6ED |

## Correspondance Score-Couleur
- 80-100 : Vert (#00C853) — Performance solide
- 60-79 : Bleu (#2D5BFF) — Bon avec de la marge d'amélioration
- 40-59 : Ambre (#FFB300) — Nécessite attention
- 0-39 : Rouge (#FF1744) — Problèmes critiques

## Résolution des Problèmes

| Problème | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'reportlab'` | Exécuter `pip3 install reportlab` |
| Le script produit un PDF vide | Vérifier que les données JSON ont tous les champs requis |
| La jauge de score ne s'affiche pas | S'assurer que `overall_score` est un nombre entre 0 et 100 |
| Tableau des concurrents manquant | S'assurer que le tableau `competitors` a des objets avec les champs `name`, `positioning`, `pricing`, `social_proof`, `content` |
| Le PDF n'a qu'une page | Vérifier les erreurs de parsing JSON — exécuter `python3 -c "import json; json.load(open('/tmp/report_data.json'))"` |
| Les polices ont l'air étranges | Le script utilise Helvetica (intégré à reportlab). Aucune police personnalisée nécessaire. |

## Intégration avec les Autres Skills

Ce skill fonctionne mieux en combinaison avec d'autres skills d'audit. Le flux de travail recommandé :

1. Exécuter `/market audit <url>` — Génère des données d'audit complètes
2. Exécuter `/market competitors <url>` — Ajoute des données de comparaison concurrentielle
3. Exécuter `/market seo <url>` — Ajoute des observations SEO détaillées
4. Exécuter `/market landing <url>` — Ajoute l'analyse CRO
5. Exécuter `/market report-pdf <url>` — Compile tout dans un PDF

Le skill de rapport PDF cherchera automatiquement les fichiers de sortie de ces skills et intégrera leurs données dans le JSON du rapport.

## Sortie
- **Fichier :** `RAPPORT-MARKETING-<domaine>.pdf`
- **Emplacement :** Répertoire racine du projet
- **Taille :** Typiquement 200Ko-500Ko selon le volume de contenu
- **Pages :** 5-7 pages selon si des données concurrentielles et des sections supplémentaires sont incluses

## Principes Clés
- Le rapport PDF est le livrable le plus orienté client de la boîte à outils. La qualité compte.
- Toujours vérifier que les données JSON sont complètes et précises avant de générer. Mauvaises données = mauvais rapport.
- Utiliser le PDF pour les premières impressions clients et les conversations commerciales. Faire un suivi avec le rapport Markdown plus détaillé si le client s'engage.
- Chaque score doit être justifiable. Si un client demande "pourquoi j'ai eu 52 en Optimisation de Conversion ?", les observations doivent fournir des preuves claires.
- Arrondir les scores à des nombres entiers. Les décimales suggèrent une fausse précision.
- Garder le résumé exécutif concis — 2-4 phrases maximum. Les clients survolent les pages de couverture.
- Si le rapport est généré pour un prospect (pas encore client), le rapport sert d'outil commercial. Rendre les opportunités convaincantes et le plan d'action réalisable.
