# Analyse CRO de Page d'Atterrissage

## Objectif du Skill
Effectuer une analyse complète d'Optimisation du Taux de Conversion (CRO) sur toute page d'atterrissage. Ce skill produit un démontage section par section avec des corrections prioritaires et actionnables ayant un impact direct sur les taux de conversion.

**IMPORTANT : Tu dois toujours répondre et rédiger tous tes livrables en français.**

## Quand Utiliser
- L'utilisateur fournit une URL de page d'atterrissage et demande une optimisation de conversion
- L'utilisateur demande un retour, une revue ou un audit de page d'atterrissage
- L'utilisateur veut améliorer les taux d'inscription, de capture de leads ou d'achat
- Déclenché par `/market landing <url>` ou `/market cro <url>`

## Comment Exécuter

### Étape 1 : Identifier le Type de Page
Déterminer quel type de page d'atterrissage est analysé. Cela impacte les benchmarks et les pondérations de score.

| Type de Page | Objectif Principal | Bon TR | Excellent TR |
|---|---|---|---|
| Capture de leads | Soumission email/formulaire | 5-10% | 15%+ |
| Inscription SaaS | Essai gratuit ou freemium | 3-7% | 10%+ |
| Produit e-commerce | Ajout au panier / Achat | 2-4% | 5%+ |
| Inscription webinaire | S'inscrire à un événement | 20-30% | 40%+ |
| Téléchargement app | Installer l'app | 10-15% | 20%+ |
| Liste d'attente | Rejoindre la waitlist | 15-25% | 35%+ |
| Prise de RDV | Planifier un appel | 5-10% | 15%+ |
| Don associatif | Faire un don | 2-5% | 8%+ |

### Étape 2 : Appliquer le Cadre CRO en 7 Points
Analyser chaque section dans l'ordre. Attribuer un score de 1-10 et fournir des observations spécifiques.

#### Section 1 : Zone Héros (Poids : 25%)
Le premier écran vu par le visiteur. C'est là que 80% des décisions de conversion commencent.

**Checklist :**
- [ ] Le titre est visible dans les 2 secondes après le chargement de la page
- [ ] Le titre communique le bénéfice principal (pas une fonctionnalité)
- [ ] Le titre fait moins de 10 mots
- [ ] Le sous-titre développe le titre avec de la spécificité
- [ ] Le CTA principal est au-dessus de la ligne de flottaison
- [ ] La couleur du bouton CTA contraste avec le fond
- [ ] Le texte du CTA est orienté action (pas "Envoyer" ou "Cliquer ici")
- [ ] L'image ou vidéo héros soutient le message (pas une photo stock générique)
- [ ] Badges de confiance ou preuve sociale visibles au-dessus de la ligne de flottaison
- [ ] La page se charge en moins de 3 secondes
- [ ] Pas de menu de navigation concurrençant le CTA (pour les pages d'atterrissage dédiées)

**Critères de Score :**
- 9-10 : Titre axé bénéfice, spécifique et convaincant. CTA clair et contrasté. Visuel soutient le message. Indicateurs de confiance présents.
- 7-8 : Titre et CTA solides mais manquant un élément (badges de confiance, visuel de support ou spécificité).
- 5-6 : Titre générique ou CTA faible. Plusieurs éléments au-dessus de la ligne de flottaison manquants.
- 3-4 : Titre axé fonctionnalité ou vague. CTA sous la ligne de flottaison ou peu clair.
- 1-2 : Pas de titre ou CTA clair. Le visiteur ne peut pas comprendre l'offre en 5 secondes.

#### Section 2 : Proposition de Valeur (Poids : 20%)
À quel point la page communique POURQUOI quelqu'un devrait convertir.

**Checklist :**
- [ ] Énoncé clair de ce que fait le produit/service
- [ ] Résultats ou bénéfices spécifiques promis
- [ ] Différenciation par rapport aux alternatives (pourquoi CETTE solution)
- [ ] La cible est claire (le visiteur sait si c'est fait pour lui)
- [ ] Les bénéfices sont quantifiés quand possible (économiser X heures, augmenter Y%)
- [ ] La proposition de valeur est lisible en diagonale (pas noyée dans des paragraphes)

**Évaluation avec le Cadre 4U :**
1. **Utile** — Résout-elle un vrai problème du visiteur ?
2. **Urgent** — Y a-t-il une raison d'agir maintenant ?
3. **Unique** — Est-elle différente des concurrents ?
4. **Ultra-spécifique** — Les affirmations sont-elles concrètes, pas vagues ?

#### Section 3 : Preuve Sociale (Poids : 15%)
Preuves que d'autres font confiance et bénéficient de ce produit/service.

**Types de Preuve Sociale (classés par pouvoir de persuasion) :**
1. Métriques de résultats/CA ("2,4 Mds€ traités", "500K utilisateurs")
2. Témoignages clients nommés avec photos, titres et entreprises
3. Logos de clients reconnaissables
4. Études de cas avec résultats spécifiques
5. Scores et nombre d'avis
6. Mentions médias ("Comme vu dans...")
7. Certifications et récompenses
8. Contenu généré par les utilisateurs
9. Nombre d'abonnés sur les réseaux sociaux

**Checklist :**
- [ ] Au moins 2 types de preuve sociale présents
- [ ] Les témoignages incluent de vrais noms et photos
- [ ] Les témoignages mentionnent des résultats ou bénéfices spécifiques
- [ ] La preuve sociale est placée près des points de décision (proche des CTAs)
- [ ] Les chiffres sont spécifiques (pas arrondis — "11 847" bat "10 000+")
- [ ] Les logos sont reconnaissables pour la cible
- [ ] La preuve sociale est récente et pertinente

#### Section 4 : Fonctionnalités et Bénéfices (Poids : 15%)
Comment la page présente ce que contient le produit/service.

**Checklist :**
- [ ] Les fonctionnalités sont traduites en bénéfices (ce que la fonctionnalité FAIT pour l'utilisateur)
- [ ] Le contenu est lisible en diagonale (icônes, puces, paragraphes courts)
- [ ] La hiérarchie visuelle guide l'œil à travers les fonctionnalités
- [ ] Les fonctionnalités/bénéfices les plus importants sont listés en premier
- [ ] Chaque section de fonctionnalité a un mini-titre clair
- [ ] Des captures d'écran, démos ou visuels accompagnent les descriptions
- [ ] La liste de fonctionnalités est complète mais pas accablante (3-7 fonctionnalités clés)

**Vérification Fonctionnalité-vers-Bénéfice :**
Mal : "Tableau de bord analytique propulsé par IA"
Bien : "Voyez exactement quelles campagnes génèrent du CA — l'IA analyse vos données à votre place"

#### Section 5 : Gestion des Objections (Poids : 10%)
Comment la page adresse les raisons pour lesquelles un visiteur pourrait NE PAS convertir.

**Objections Courantes par Type de Page :**

| Objection | Comment l'Adresser |
|---|---|
| "Trop cher" | Calculateur ROI, comparaison prix, garantie remboursement |
| "Pas sûr que ça marche" | Études de cas, essai gratuit, vidéo démo |
| "Trop compliqué" | Assistant de configuration, support onboarding, "démarrez en 5 minutes" |
| "Pas sûr d'en avoir besoin" | Agitation du problème, coût de l'inaction |
| "Et si ça ne me convient pas ?" | Essai gratuit, garantie remboursement, annulation à tout moment |
| "Mes données sont-elles en sécurité ?" | Badges de sécurité, logos de conformité, lien politique de confidentialité |
| "J'ai besoin d'en parler à mon équipe" | Page de comparaison partageable, essai équipe, résumé ROI |

**Checklist :**
- [ ] Section FAQ répondant aux 3-5 principales objections
- [ ] Éléments de réduction du risque présents (garantie, essai gratuit, annulation à tout moment)
- [ ] Transparence tarifaire (pas de frais cachés ou surprises)
- [ ] Indicateurs de sécurité et confidentialité si pertinents
- [ ] Comparaison avec les alternatives (si applicable)

#### Section 6 : Appel à l'Action (Poids : 10%)
Le mécanisme de conversion lui-même.

**Checklist du Bouton CTA :**
- [ ] Le texte du CTA décrit la VALEUR, pas l'action ("Obtenir Mon Rapport Gratuit" vs "Envoyer")
- [ ] Le bouton CTA est visuellement dominant (taille, couleur, espace blanc)
- [ ] Le CTA apparaît plusieurs fois sur les pages longues
- [ ] Un CTA secondaire existe pour les visiteurs pas encore prêts
- [ ] Le CTA a un micro-texte de support (ex. "Sans carte bancaire requise")
- [ ] Le texte du bouton utilise la première personne ("Commencer MON essai" vs "Commencer VOTRE essai")
- [ ] Le CTA est spécifique à l'offre (pas générique)

**Score du Texte CTA :**
- Faible : "Envoyer", "Cliquez ici", "En savoir plus"
- Moyen : "S'inscrire", "Commencer", "Télécharger"
- Fort : "Démarrer Mon Essai Gratuit", "Obtenir Mon Rapport Personnalisé", "Profiter de la Remise"

#### Section 7 : Pied de Page et Éléments Secondaires (Poids : 5%)
Le bas de la page et les éléments de support.

**Checklist :**
- [ ] CTA final présent en bas de la page
- [ ] Coordonnées ou options de support visibles
- [ ] Politique de confidentialité et CGU liées
- [ ] Badges de confiance répétés près du CTA final
- [ ] Pas de liens concurrents menant à l'extérieur de la conversion
- [ ] Mentions légales et copyright présents
- [ ] Liens réseaux sociaux (seulement s'ils soutiennent la conversion, pas distraient)

### Étape 3 : Score du Texte
Évaluer le texte global de la page sur 5 dimensions (1-10 chacune) :

1. **Clarté** — Un visiteur peut-il comprendre l'offre en 5 secondes ?
2. **Urgence** — Y a-t-il une raison d'agir MAINTENANT plutôt que plus tard ?
3. **Spécificité** — Les affirmations sont-elles concrètes avec des chiffres, délais, résultats ?
4. **Preuve** — Les affirmations sont-elles soutenues par des preuves, données ou témoignages ?
5. **Orientation Action** — Le texte pousse-t-il vers une prochaine étape spécifique ?

Calculer le Score Texte : moyenne des 5 dimensions, multipliée par 10 pour un score sur 100.

### Étape 4 : Audit d'Optimisation du Formulaire
Si la page a un formulaire, évaluer :

| Élément | Bonne Pratique |
|---|---|
| Nombre de champs | Chaque champ supplémentaire réduit la conversion d'environ 7%. Capture lead : 3-5 champs max. |
| Labels | Utiliser des labels intégrés ou flottants. Éviter les labels uniquement en placeholder. |
| Texte du bouton | Correspondre à la proposition de valeur. "Obtenir Mon Guide Gratuit" > "Envoyer". |
| Gestion des erreurs | Validation inline. Messages d'erreur spécifiques. Ne pas effacer tout le formulaire sur erreur. |
| Multi-étapes | Diviser les formulaires longs en étapes avec indicateur de progression. |
| Requis vs optionnel | Marquer les champs optionnels, pas les obligatoires. |
| Remplissage auto | Activer le remplissage auto du navigateur pour les champs standard. |
| Types de champs | Utiliser les types d'entrée appropriés (email, tel, url) pour les claviers mobiles. |

### Étape 5 : Audit de Responsivité Mobile
Le mobile représente plus de 60% du trafic web. Vérifier :

- [ ] Le CTA est accessible au pouce (moitié inférieure de l'écran)
- [ ] Le texte est lisible sans zoom (16px minimum pour le corps)
- [ ] Les formulaires sont utilisables sur mobile (grandes zones de touche, claviers appropriés)
- [ ] Les images se redimensionnent correctement sans casser la mise en page
- [ ] Pas de défilement horizontal requis
- [ ] La page se charge en moins de 3 secondes sur 4G
- [ ] Bouton clic-pour-appeler pour les numéros de téléphone
- [ ] Barre CTA fixe au défilement (si applicable)

### Étape 6 : Évaluation de l'Impact de la Vitesse de Chargement
Benchmarks d'impact sur la conversion :

| Temps de Chargement | Impact sur la Conversion |
|---|---|
| 0-2 secondes | Référence (optimal) |
| 2-3 secondes | -7% taux de conversion |
| 3-5 secondes | -20% taux de conversion |
| 5-8 secondes | -35% taux de conversion |
| 8+ secondes | -50%+ taux de conversion |

Vérifier les problèmes de vitesse courants :
- Images non optimisées (utiliser WebP, lazy loading)
- JavaScript bloquant le rendu
- Absence de cache navigateur
- Pas de CDN
- Scripts tiers excessifs
- CSS/JS non minifiés

### Étape 7 : Générer des Recommandations de Tests A/B
Formater chaque test comme une hypothèse :

**Modèle :**
"Si nous [CHANGEMENT], alors [MÉTRIQUE] va [S'AMÉLIORER/AUGMENTER] parce que [RAISON]."

**Exemples de tests à considérer :**
1. Variations de titre (axé bénéfice vs axé résultat)
2. Couleur et texte du bouton CTA
3. Placement de la preuve sociale (au-dessus vs en-dessous de la ligne de flottaison)
4. Nombre de champs du formulaire (réduire de 1-2 champs)
5. Image héros vs vidéo héros
6. Page longue vs page courte
7. Ajout d'éléments d'urgence (compte à rebours, places limitées)
8. Ancrage et présentation des prix
9. Format des témoignages (texte vs vidéo)
10. Ajout d'un chatbot ou chat en direct

### Étape 8 : Guide d'Interprétation des Cartes de Chaleur
Même sans données de carte de chaleur réelles, fournir des conseils sur :

- **Zones d'attention attendues** basées sur la mise en page
- **Lecture en F vs en Z** selon la densité du contenu
- **Prédictions de profondeur de défilement** selon la longueur et les ruptures de contenu
- **Zones de probabilité de clic** selon la hiérarchie visuelle
- **Indicateurs de clics de rage** (éléments qui semblent cliquables mais ne le sont pas)
- **Zones mortes** où le contenu pourrait être ignoré

## Format de Sortie

Générer un fichier `ANALYSE-LANDING.md` dans le répertoire projet ou de sortie :

```markdown
# Analyse CRO de Page d'Atterrissage
## [URL de la Page]
### Date d'Analyse : [date]

---

## Score CRO Global : [X/100]

## Type de Page : [type identifié]
## Taux de Conversion Actuel Estimé : [estimation basée sur les observations]
## Taux de Conversion Cible : [objectif d'amélioration réaliste]

---

## Analyse Section par Section

### 1. Zone Héros [Score : X/10]
**Observations :**
- [observations spécifiques]

**Corrections (Priorité : HAUTE/MOYENNE/BASSE) :**
- [recommandations spécifiques et actionnables]

[Répéter pour les 7 sections]

---

## Score du Texte : [X/100]
| Dimension | Score | Notes |
|---|---|---|
| Clarté | X/10 | [notes] |
| Urgence | X/10 | [notes] |
| Spécificité | X/10 | [notes] |
| Preuve | X/10 | [notes] |
| Orientation Action | X/10 | [notes] |

---

## Audit du Formulaire
[observations et recommandations]

---

## Audit Mobile
[observations et recommandations]

---

## Recommandations de Tests A/B
1. [Test au format hypothèse]
2. [Test au format hypothèse]
3. [Test au format hypothèse]

---

## Liste de Corrections Priorisées

### Victoires Rapides (à mettre en œuvre cette semaine)
1. [correction avec impact attendu]

### Moyen Terme (à mettre en œuvre ce mois-ci)
1. [correction avec impact attendu]

### Stratégique (à mettre en œuvre ce trimestre)
1. [correction avec impact attendu]

---

## Suggestions de Maquette Avant/Après
[Descriptions textuelles des maquettes de mise en page actuelle vs recommandée]
```

## Principes Clés
- Toujours lier les recommandations à l'IMPACT SUR LE CA. Ne pas se contenter de dire "changez la couleur du bouton" — dire "changer le bouton CTA pour une couleur contrastée augmente typiquement les clics de 15-30%, ce qui à votre trafic actuel pourrait représenter X conversions supplémentaires par mois."
- Prioriser les corrections par ratio effort/impact. Les victoires rapides d'abord.
- Être spécifique. "Améliorez votre titre" est inutile. "Changez votre titre de 'Bienvenue sur Notre Plateforme' à 'Réduisez Votre Temps de Reporting de 75% — Analytics Automatisés pour les Équipes de Croissance' parce que ça ajoute de la spécificité, un bénéfice quantifié et cible une audience précise" est actionnable.
- Référencer les benchmarks sectoriels pour que le client comprenne sa position.
- Si vous avez accès à la page via les outils navigateur, prendre des captures d'écran et référencer des éléments spécifiques.
- Si l'utilisateur a exécuté `/market audit` précédemment, intégrer ces observations dans l'analyse CRO pour une image plus complète.
