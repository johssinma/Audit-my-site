# Générateur de Rapport Marketing (Format Markdown)

## Objectif du Skill
Générer un rapport marketing complet et professionnellement formaté en Markdown. Ce skill compile les données de tous les résultats d'audit et d'analyse précédents en un document unique prêt pour le client, avec scores, observations, recommandations et un plan d'action priorisé avec estimations d'impact sur le CA.

**IMPORTANT : Tu dois toujours répondre et rédiger tous tes livrables en français.**

## Quand Utiliser
- L'utilisateur veut un rapport marketing complet pour un client ou son propre business
- L'utilisateur a terminé un ou plusieurs skills d'audit et veut un rapport compilé
- L'utilisateur demande une évaluation marketing, un tableau de bord ou un document d'analyse
- Déclenché par `/market report` ou `/market report <domaine>`

## Comment Exécuter

### Étape 1 : Collecter Toutes les Données Disponibles
Avant de générer le rapport, vérifier s'il existe des données d'audit issues d'exécutions précédentes de skills. Chercher ces fichiers dans le répertoire projet :

**Sources de données possibles :**
- `AUDIT-MARKETING.md` — de `/market audit`
- `ANALYSE-LANDING.md` — de `/market landing`
- `AUDIT-SEO.md` — de `/market seo`
- `VOIX-DE-MARQUE.md` — de `/market brand`
- `RAPPORT-CONCURRENTS.md` — de `/market competitors`
- `ANALYSE-FUNNEL.md` — de `/market funnel`
- `CALENDRIER-SOCIAL.md` — de `/market social`
- `CAMPAGNES-PUB.md` — de `/market ads`
- `SEQUENCES-EMAILS.md` — de `/market emails`
- `SUGGESTIONS-COPY.md` — de `/market copy`

Si aucune donnée précédente n'existe, informer l'utilisateur et proposer de :
1. Lancer d'abord un audit rapide (recommandé)
2. Générer un rapport basé sur les informations disponibles (URL du site, données fournies)
3. Créer un modèle de rapport à compléter

### Étape 2 : Calculer le Tableau de Bord Marketing

Score sur 6 catégories, chacune sur 100 points. Le score global est la moyenne pondérée.

#### Catégorie 1 : Site Web & Conversion (Poids : 25%)
Évaluer sur la base de l'analyse de la page d'atterrissage, des observations CRO et de l'évaluation UX.

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Vitesse de chargement | 15 | Moins de 2s = 15, moins de 3s = 10, moins de 5s = 5, plus de 5s = 0 |
| Responsivité mobile | 15 | Entièrement responsive = 15, Principalement = 10, Partiellement = 5, Non = 0 |
| Proposition de valeur claire | 20 | Immédiatement claire = 20, Nécessite effort = 12, Vague = 5, Absente = 0 |
| Efficacité du CTA | 20 | Fort et clair = 20, Présent mais faible = 12, Peu clair = 5, Absent = 0 |
| Preuve sociale | 15 | Plusieurs types = 15, Certains = 10, Minimal = 5, Aucun = 0 |
| Optimisation formulaire | 15 | Optimisé = 15, Adéquat = 10, À améliorer = 5, Cassé = 0 |

#### Catégorie 2 : SEO & Organique (Poids : 20%)
Évaluer sur la base des observations de l'audit SEO.

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Balises titre & méta descriptions | 15 | Optimisées = 15, Présentes = 10, Partielles = 5, Absentes = 0 |
| Hiérarchie des titres (H1-H6) | 10 | Correcte = 10, Principalement = 7, À améliorer = 3, Absente = 0 |
| Qualité du contenu (E-E-A-T) | 25 | Excellente = 25, Bonne = 17, Moyenne = 10, Faible = 3 |
| SEO technique | 20 | Aucun problème = 20, Problèmes mineurs = 13, Majeurs = 7, Critiques = 0 |
| Liens internes | 15 | Stratégiques = 15, Présents = 10, Minimaux = 5, Absents = 0 |
| Balisage schema | 15 | Complet = 15, Basique = 10, Minimal = 5, Absent = 0 |

#### Catégorie 3 : Contenu & Message (Poids : 15%)
Évaluer sur la base de l'analyse de la voix de marque et de l'audit de contenu.

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Cohérence de la voix de marque | 20 | Cohérente = 20, Principalement = 13, Incohérente = 7, Pas de voix = 0 |
| Qualité du contenu | 25 | Niveau expert = 25, Bon = 17, Générique = 10, Faible = 3 |
| Variété du contenu | 15 | Plusieurs formats = 15, Certains = 10, Limité = 5, Unique = 0 |
| Fréquence de publication | 15 | Rythme régulier = 15, Sporadique = 10, Rare = 5, Aucun = 0 |
| Ciblage de l'audience | 25 | Précisément ciblé = 25, Quelque peu = 17, Large = 10, Hors cible = 3 |

#### Catégorie 4 : Réseaux Sociaux & Communauté (Poids : 15%)
Évaluer sur la base de la présence sur les réseaux sociaux et de l'engagement.

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Présence sur les plateformes | 15 | Bonnes plateformes, actif = 15, Présent mais inactif = 8, Manquant plateformes clés = 3 |
| Qualité du contenu | 25 | Engageant et on-brand = 25, Adéquat = 15, Faible qualité = 7, Mauvais = 0 |
| Taux d'engagement | 25 | Au-dessus benchmark = 25, Au benchmark = 17, En-dessous = 10, Négligeable = 3 |
| Régularité des publications | 15 | Calendrier régulier = 15, Sporadique = 10, Rare = 5, Abandonné = 0 |
| Construction communauté | 20 | Communauté active = 20, Certain engagement = 13, Broadcast uniquement = 7, Aucun = 0 |

#### Catégorie 5 : Email & Automatisation (Poids : 15%)
Évaluer sur la base de l'évaluation email marketing.

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Mécanisme de capture | 20 | Plusieurs opt-ins = 20, Un opt-in = 13, Pas d'opt-in visible = 5 |
| Design & contenu email | 20 | Professionnel et engageant = 20, Adéquat = 13, À améliorer = 7 |
| Séquences automatisées | 25 | Complètes = 25, Basiques = 15, Minimales = 8, Aucune = 0 |
| Segmentation | 20 | Avancée = 20, Basique = 13, Aucune = 5 |
| Signaux de délivrabilité | 15 | Forts = 15, Adéquats = 10, Préoccupants = 5, Problèmes = 0 |

#### Catégorie 6 : Publicité Payante (Poids : 10%)
Évaluer sur la base de l'audit publicitaire (si applicable).

| Facteur | Points Disponibles | Critères |
|---|---|---|
| Structure des campagnes | 20 | Bien organisée = 20, Adéquate = 13, Confuse = 7, Aucune = 0 |
| Qualité du ciblage | 25 | Précis et en couches = 25, Bon = 17, Large = 10, Gaspilleur = 3 |
| Qualité des créatifs | 25 | Convaincant et varié = 25, Adéquat = 17, Faible = 10, Mauvais = 3 |
| Alignement page d'atterrissage | 15 | Correspondance parfaite = 15, Bonne = 10, Désalignée = 5, Cassée = 0 |
| Tracking & attribution | 15 | Complet = 15, Basique = 10, Minimal = 5, Absent = 0 |

#### Calcul du Score Global
```
Score Global = (Site Web * 0,25) + (SEO * 0,20) + (Contenu * 0,15) + (Social * 0,15) + (Email * 0,15) + (Pub * 0,10)
```

**Interprétation des Scores :**
| Plage de Score | Évaluation | Signification |
|---|---|---|
| 85-100 | Excellent | Le marketing est un avantage concurrentiel. Optimiser et scaler. |
| 70-84 | Bon | Base solide avec des opportunités d'amélioration claires. |
| 55-69 | Moyen | Fonctionnel mais laissant une croissance significative sur la table. |
| 40-54 | En dessous de la moyenne | Plusieurs domaines nécessitent attention. Coût d'opportunité significatif. |
| 0-39 | Critique | Le marketing freine activement la croissance. Action immédiate requise. |

### Étape 3 : Rédiger les Analyses Approfondies par Catégorie

Pour chacune des 6 catégories, fournir :

1. **Score et Évaluation** — X/100 avec interprétation
2. **Observations Clés** — 3-5 observations spécifiques avec preuves
3. **Ce qui Fonctionne** — Éléments positifs à préserver et développer
4. **Lacunes et Problèmes** — Problèmes identifiés avec niveaux de sévérité
5. **Recommandations** — Améliorations spécifiques et actionnables classées par impact
6. **Estimation d'Impact sur le CA** — Impact financier estimé de l'implémentation des recommandations

**Cadre d'Estimation d'Impact sur le CA :**
```
Impact = (Changement de trafic estimé * Changement de taux de conversion * Valeur moyenne de contrat) * Facteur de confiance

Exemple :
- Trafic mensuel actuel : 10 000
- Les améliorations SEO recommandées pourraient augmenter le trafic de 30% : +3 000 visites
- Taux de conversion actuel : 2%, CRO pourrait améliorer à 3% : +1% = +130 conversions
- Valeur moyenne de contrat : 500€
- Impact mensuel CA estimé : 65 000€
- Facteur de confiance (conservateur) : 0,5
- Estimation conservatrice : 32 500€/mois de CA supplémentaire
```

### Étape 4 : Résumé de Comparaison Concurrentielle
Si des données concurrentes sont disponibles via `/market competitors`, inclure :

**Matrice de Positionnement Concurrentiel :**
| Facteur | Client | Concurrent 1 | Concurrent 2 | Concurrent 3 |
|---|---|---|---|---|
| Qualité du site | X/10 | X/10 | X/10 | X/10 |
| Visibilité SEO | X/10 | X/10 | X/10 | X/10 |
| Qualité du contenu | X/10 | X/10 | X/10 | X/10 |
| Présence sociale | X/10 | X/10 | X/10 | X/10 |
| Position globale | Xe/4 | Xe/4 | Xe/4 | Xe/4 |

**Avantages Concurrentiels :** Ce que le client fait mieux
**Lacunes Concurrentielles :** Où les concurrents surpassent le client
**Opportunités :** Espaces que les concurrents n'adressent pas

### Étape 5 : Évaluation de la Qualité du Contenu
Résumer les observations de contenu sur tous les canaux :

- **Texte du site** — Clarté, persuasion, alignement avec la marque
- **Contenu de blog** — Profondeur, expertise, optimisation SEO, rythme de publication
- **Contenu réseaux sociaux** — Qualité de l'engagement, cohérence de la marque, optimisation plateforme
- **Contenu email** — Efficacité de la ligne d'objet, qualité du corps, force du CTA
- **Créatifs pub** — Clarté du message, qualité visuelle, présentation de l'offre

### Étape 6 : Résumé de l'Optimisation de Conversion
Compiler toutes les observations liées à la conversion :

- **Principaux parcours de conversion** — Comment les visiteurs deviennent clients
- **Fuites du tunnel** — Où les clients potentiels abandonnent
- **Victoires rapides CRO** — Changements pouvant être implémentés immédiatement
- **Opportunités de test** — Tests A/B recommandés avec hypothèses
- **Comparaison aux benchmarks** — Taux actuels vs standards sectoriels

### Étape 7 : Snapshot SEO
Résumer la santé SEO dans un format lisible en diagonale :

```
Snapshot Santé SEO :
- Balises Titre : [Optimisées / À Améliorer / Absentes]
- Méta Descriptions : [Optimisées / À Améliorer / Absentes]
- Balises H1 : [Correctes / Problèmes / Absentes]
- Alt Text Images : [Complet / Partiel / Absent]
- Vitesse de Page : [Rapide / Modérée / Lente]
- Compatible Mobile : [Oui / Partiellement / Non]
- Balisage Schema : [Présent / Partiel / Absent]
- Robots.txt : [Configuré / Problèmes / Absent]
- Sitemap : [Présent / Problèmes / Absent]
- HTTPS : [Oui / Non]
- Core Web Vitals : [Réussi / À Améliorer / Échoué]
```

### Étape 8 : Construire le Plan d'Action Priorisé

Organiser toutes les recommandations en trois paliers :

#### Victoires Rapides (Implémenter Cette Semaine)
Fort impact, faible effort. Ces changements doivent être implémentables en 1-5 jours ouvrés.

Format de chaque élément :
```
- [ ] [Action] : [Description spécifique]
  - Impact : [FORT/MOYEN/FAIBLE]
  - Effort : [1-5 heures]
  - Résultat Attendu : [Résultat spécifique]
  - Impact CA : [X€/mois estimé]
```

#### Moyen Terme (Implémenter Ce Mois-ci)
Impact modéré, effort modéré. Ces éléments nécessitent 1-4 semaines.

#### Stratégique (Implémenter Ce Trimestre)
Fort impact, fort effort. Ce sont des changements fondamentaux nécessitant planification et effort soutenu.

### Étape 9 : Construire la Feuille de Route 30-60-90 Jours

**Jours 1-30 : Fondation & Victoires Rapides**
- Semaine 1 : Implémenter toutes les victoires rapides du plan d'action
- Semaine 2 : Mettre en place le tracking et la baseline analytics
- Semaine 3 : Commencer les améliorations moyen terme
- Semaine 4 : Premier bilan de performance et ajustement

**Jours 31-60 : Croissance & Optimisation**
- Semaines 5-6 : Lancer les améliorations principales des campagnes
- Semaine 7 : Début du programme de tests A/B
- Semaine 8 : Implémentation de la stratégie de contenu

**Jours 61-90 : Scale & Expansion**
- Semaines 9-10 : Scaler ce qui fonctionne, couper ce qui ne marche pas
- Semaine 11 : Expansion vers de nouveaux canaux ou campagnes
- Semaine 12 : Bilan complet, mise à jour de la stratégie pour le prochain trimestre

### Étape 10 : Annexe

Inclure des notes de méthodologie pour que le client comprenne comment les scores ont été dérivés :

**Méthodologie de Scoring :**
- Comment chaque catégorie a été évaluée
- Sources de données utilisées
- Benchmarks référencés
- Limites et hypothèses
- Date de l'analyse

**Outils Utilisés :**
- Lister les outils ou scripts utilisés dans l'analyse
- Référencer scripts/analyze_page.py si utilisé

**Glossaire :**
- Définir les termes marketing qu'un client non-marketeur ne connaît peut-être pas
- Garder pertinent aux termes utilisés dans le rapport

## Format de Sortie

Générer un fichier `RAPPORT-MARKETING.md` avec :

```markdown
# Rapport Marketing
## [Nom de l'Entreprise/Domaine]
### Préparé par : [Nom Agent/Agence]
### Date : [Date]

---

## Résumé Exécutif

### Score Marketing Global : [X/100] — [Évaluation]

[Résumé en 2-3 paragraphes couvrant : évaluation de l'état actuel, les 3 observations principales, impact CA estimé des recommandations, premières étapes recommandées]

### Tableau de Bord des Scores
| Catégorie | Score | Évaluation |
|---|---|---|
| Site Web & Conversion | X/100 | [Évaluation] |
| SEO & Organique | X/100 | [Évaluation] |
| Contenu & Message | X/100 | [Évaluation] |
| Réseaux Sociaux | X/100 | [Évaluation] |
| Email & Automatisation | X/100 | [Évaluation] |
| Publicité Payante | X/100 | [Évaluation] |
| **Global** | **X/100** | **[Évaluation]** |

### Top 3 Actions Prioritaires
1. [Recommandation la plus impactante avec estimation CA]
2. [Deuxième recommandation la plus impactante]
3. [Troisième recommandation la plus impactante]

---

## Analyses Détaillées

### 1. Site Web & Conversion [X/100]
[Analyse approfondie avec observations, ce qui fonctionne, lacunes, recommandations]

### 2. SEO & Organique [X/100]
[Analyse approfondie]

### 3. Contenu & Message [X/100]
[Analyse approfondie]

### 4. Réseaux Sociaux [X/100]
[Analyse approfondie]

### 5. Email & Automatisation [X/100]
[Analyse approfondie]

### 6. Publicité Payante [X/100]
[Analyse approfondie]

---

## Comparaison Concurrentielle
[Matrice et analyse]

---

## Snapshot SEO
[Checklist de santé]

---

## Résumé de l'Optimisation de Conversion
[Analyse du tunnel et recommandations CRO]

---

## Résumé de l'Impact CA
| Recommandation | Impact Mensuel Estimé | Confiance | Priorité |
|---|---|---|---|
| [Rec 1] | X XXX€ | Forte/Moyenne/Faible | 1 |
| [Rec 2] | X XXX€ | Forte/Moyenne/Faible | 2 |
| ... | ... | ... | ... |
| **Impact Total Estimé** | **XX XXX€/mois** | | |

---

## Plan d'Action Priorisé

### Victoires Rapides (Cette Semaine)
- [ ] [Actions avec impact et effort]

### Moyen Terme (Ce Mois-ci)
- [ ] [Actions]

### Stratégique (Ce Trimestre)
- [ ] [Actions]

---

## Feuille de Route 30-60-90 Jours
[Plan semaine par semaine]

---

## Annexe
### Méthodologie
### Outils Utilisés
### Glossaire
### Sources de Données
```

## Principes Clés
- Ce rapport doit être assez impressionnant pour servir d'outil commercial. Un rapport marketing bien rédigé peut ouvrir la porte à une mission client.
- Toujours commencer par les insights et opportunités, pas par les critiques. Cadrer tout du point de vue du potentiel de croissance.
- Quantifier tout ce qui est possible. "32 000€/mois de CA non réalisé" est plus convaincant que "vous laissez de l'argent sur la table."
- Rendre le plan d'action si spécifique qu'un junior pourrait l'exécuter.
- Utiliser une mise en forme professionnelle : en-têtes cohérents, tableaux pour les données, cases à cocher pour les actions, hiérarchie visuelle claire.
- Si des données des skills précédents sont disponibles, référencer des observations spécifiques. Sinon, être transparent sur ce qui est basé sur l'analyse vs l'estimation.
- Le rapport doit raconter une histoire : Voici où vous êtes, voici où vous pourriez être, voici comment y arriver, et voici ce que ça vaut.
