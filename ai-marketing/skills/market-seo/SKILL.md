# Audit SEO de Contenu

## Objectif du Skill
Effectuer un audit SEO complet d'une page web ou d'un site, couvrant le SEO on-page, la qualité du contenu (E-E-A-T), l'analyse de mots-clés, le SEO technique et la stratégie de contenu. Ce skill combine une analyse automatisée via `scripts/analyze_page.py` avec une revue manuelle de niveau expert pour produire un document d'audit SEO actionnable.

**IMPORTANT : Tu dois toujours répondre et rédiger tous tes livrables en français.**

## Quand Utiliser
- L'utilisateur fournit une URL et demande une analyse, un audit ou des recommandations SEO
- L'utilisateur veut améliorer les classements en recherche organique et le trafic
- L'utilisateur pose des questions sur le SEO on-page, les balises méta, la qualité du contenu ou le SEO technique
- L'utilisateur veut une analyse des lacunes de contenu ou des recommandations de stratégie de contenu
- Déclenché par `/market seo <url>` ou `/market seo`

## Comment Exécuter

### Étape 1 : Lancer l'Analyse Automatisée
Utiliser le script Python pour collecter les données de base :

```bash
python3 scripts/analyze_page.py <url>
```

Ce script extrait :
- Balise titre et méta description
- Balises Open Graph
- Hiérarchie des titres (H1-H6)
- Liens (internes et externes)
- Images et statut du alt text
- Formulaires et CTAs
- Données structurées Schema
- Liens réseaux sociaux
- Scripts de tracking
- Balise meta viewport (indicateur de compatibilité mobile)
- Balise canonique
- Directives meta robots

Capturer la sortie JSON et l'utiliser comme base pour l'analyse manuelle.

### Étape 2 : Checklist SEO On-Page
Évaluer chaque élément et le noter Conforme, À Améliorer ou Non Conforme.

#### Balise Titre
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Existence | Chaque page doit avoir une balise titre unique | Conforme/Non conforme |
| Longueur | 50-60 caractères (s'affiche entièrement dans les SERPs) | Conforme/À Améliorer/Non conforme |
| Mot-clé principal | Contient le mot-clé cible principal | Conforme/À Améliorer/Non conforme |
| Position du mot-clé | Le mot-clé principal apparaît en début de titre | Conforme/À Améliorer/Non conforme |
| Nom de marque | Inclut le nom de marque (typiquement à la fin, séparé par | ou –) | Conforme/À Améliorer/Non conforme |
| Unicité | Différent des autres pages du site | Conforme/Non conforme |
| Attrayant | Un internaute voudrait-il cliquer dessus ? | Conforme/À Améliorer/Non conforme |

**Erreurs courantes de balise titre :**
- Trop longue (tronquée dans les résultats de recherche)
- Mot-clé principal absent
- Bourrage de mots-clés ("Meilleur Outil SEO | Top Outil SEO | Logiciel SEO | Plateforme SEO")
- Même titre sur plusieurs pages
- Titres génériques ("Accueil", "Bienvenue", "Page 1")
- Nom de marque absent

#### Méta Description
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Existence | Chaque page devrait avoir une méta description | Conforme/Non conforme |
| Longueur | 150-160 caractères | Conforme/À Améliorer/Non conforme |
| Mot-clé principal | Inclut naturellement le mot-clé cible | Conforme/À Améliorer/Non conforme |
| Appel à l'action | Inclut une raison de cliquer | Conforme/À Améliorer/Non conforme |
| Unicité | Différente des autres pages | Conforme/Non conforme |
| Attrayante | Agit comme texte publicitaire pour le résultat de recherche | Conforme/À Améliorer/Non conforme |

#### Hiérarchie des Titres (H1-H6)
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| H1 présent | Exactement un H1 par page | Conforme/Non conforme |
| H1 contient le mot-clé | Mot-clé principal dans le H1 | Conforme/À Améliorer/Non conforme |
| H1 différent du titre | H1 et balise titre différents (mais liés) | Conforme/À Améliorer/Non conforme |
| Hiérarchie logique | H2 sous H1, H3 sous H2 (pas de niveaux sautés) | Conforme/À Améliorer/Non conforme |
| Sous-titres descriptifs | H2s et H3s décrivent clairement les sections de contenu | Conforme/À Améliorer/Non conforme |
| Mots-clés dans sous-titres | Mots-clés secondaires apparaissent naturellement dans H2s/H3s | Conforme/À Améliorer/Non conforme |
| Pas surchargé | Titres utilisés pour la structure, pas le style | Conforme/À Améliorer/Non conforme |

#### Optimisation des Images
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Alt text | Chaque image a un alt text descriptif | Conforme/À Améliorer/Non conforme |
| Qualité de l'alt text | L'alt text décrit l'image et inclut naturellement des mots-clés | Conforme/À Améliorer/Non conforme |
| Noms de fichiers | Noms de fichiers descriptifs (pas IMG_001.jpg) | Conforme/À Améliorer/Non conforme |
| Taille de fichier | Images optimisées pour le web (WebP préféré, compressées) | Conforme/À Améliorer/Non conforme |
| Lazy loading | Images sous la ligne de flottaison utilisent le lazy loading | Conforme/À Améliorer/Non conforme |
| Images responsives | Utilise srcset ou l'élément picture pour différentes tailles | Conforme/À Améliorer/Non conforme |
| Images décoratives | Les images décoratives ont alt="" vide (pas alt absent) | Conforme/À Améliorer/Non conforme |

#### Liens Internes
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Liens internes présents | La page renvoie vers d'autres pages pertinentes du site | Conforme/À Améliorer/Non conforme |
| Texte d'ancre | Le texte d'ancre des liens internes est descriptif (pas "cliquez ici") | Conforme/À Améliorer/Non conforme |
| Deep linking | Les liens pointent vers des pages spécifiques, pas seulement la page d'accueil | Conforme/À Améliorer/Non conforme |
| Contexte pertinent | Les liens sont contextuellement pertinents au contenu environnant | Conforme/À Améliorer/Non conforme |
| Nombre raisonnable | 3-10 liens internes par 1 000 mots de contenu | Conforme/À Améliorer/Non conforme |
| Liens cassés | Pas de liens internes cassés (erreurs 404) | Conforme/Non conforme |

#### Structure d'URL
| Critère | Bonne Pratique | Vérification |
|---|---|---|
| Lisible | L'URL est lisible et descriptive | Conforme/À Améliorer/Non conforme |
| Mots-clés | L'URL contient des mots-clés pertinents | Conforme/À Améliorer/Non conforme |
| Longueur | Moins de 75 caractères (idéalement moins de 60) | Conforme/À Améliorer/Non conforme |
| Tirets | Mots séparés par des tirets (pas des underscores) | Conforme/Non conforme |
| Minuscules | Tous les caractères en minuscules | Conforme/Non conforme |
| Pas de paramètres | URLs propres sans paramètres de requête inutiles | Conforme/À Améliorer/Non conforme |
| Slashes finaux | Utilisation cohérente (toujours ou jamais) | Conforme/À Améliorer/Non conforme |

### Étape 3 : Évaluation de la Qualité du Contenu (E-E-A-T)

Évaluer le contenu selon le cadre E-E-A-T de Google :

#### Expérience
Le contenu démontre-t-il une expérience directe avec le sujet ?

**Vérifier :**
- Anecdotes personnelles, études de cas ou exemples concrets
- Captures d'écran, photos ou preuves d'expérience pratique
- Détails spécifiques que seule une personne expérimentée connaîtrait
- Contenu de type "J'ai fait X et voici ce qui s'est passé"

**Score :** Fort / Présent / Faible / Absent

#### Expertise
L'auteur démontre-t-il une vraie connaissance du sujet ?

**Vérifier :**
- Bio de l'auteur avec références pertinentes
- Profondeur du contenu (pas superficiel)
- Informations et données précises
- Utilisation correcte de la terminologie du secteur
- Liens vers des sources d'autorité

**Score :** Fort / Présent / Faible / Absent

#### Autorité
Le site et l'auteur sont-ils reconnus comme une autorité sur ce sujet ?

**Vérifier :**
- Signatures d'auteur avec vrais noms et bios
- Page À propos avec historique de l'entreprise
- Récompenses ou certifications sectorielles
- Backlinks de sites d'autorité
- Mentions médias ou couverture presse
- Articles invités dans des publications du secteur

**Score :** Fort / Présent / Faible / Absent

#### Fiabilité
Les utilisateurs peuvent-ils faire confiance à ce contenu et ce site ?

**Vérifier :**
- HTTPS (certificat SSL)
- Politique de confidentialité et conditions d'utilisation
- Adresse physique et coordonnées
- Avis et témoignages clients
- Badges de sécurité et certifications
- Pratiques commerciales transparentes
- Informations exactes et à jour
- Sources et statistiques correctement citées

**Score :** Fort / Présent / Faible / Absent

### Étape 4 : Analyse des Mots-Clés

#### Évaluation du Mot-Clé Principal
| Élément | Évaluation |
|---|---|
| Mot-clé principal identifié | Quel mot-clé cette page cible-t-elle ? |
| Alignement de l'intention de recherche | Le contenu correspond-il à ce qu'attendent les internautes ? (informationnel, commercial, transactionnel, navigationnel) |
| Mot-clé dans le titre | Présent, position, utilisation naturelle |
| Mot-clé dans H1 | Présent, utilisation naturelle |
| Mot-clé dans les 100 premiers mots | Apparaît tôt dans le contenu |
| Mot-clé dans les sous-titres | Apparaît dans au moins un H2 ou H3 |
| Mot-clé dans la méta description | Présent et naturel |
| Mot-clé dans l'URL | Présent |
| Densité du mot-clé | 1-2% est idéal. Plus de 3% est du bourrage de mots-clés. |

#### Mots-Clés Secondaires
Identifier 5-10 mots-clés connexes à inclure naturellement dans le contenu :
- Synonymes et variations du mot-clé principal
- Variations longue traîne
- Questions connexes (Les Gens Demandent Aussi)
- Mots-clés LSI (Indexation Sémantique Latente)

#### Analyse de l'Intention de Recherche
Déterminer l'intention derrière le mot-clé cible et évaluer si le contenu correspond :

| Type d'Intention | Objectif Utilisateur | Le Contenu Devrait Être |
|---|---|---|
| Informationnel | Apprendre quelque chose | Article de blog, guide, tutoriel, FAQ |
| Commercial | Comparer des options | Page de comparaison, avis, liste |
| Transactionnel | Acheter quelque chose | Page produit, page tarification, checkout |
| Navigationnel | Trouver une page spécifique | Page d'accueil, page de connexion, outil spécifique |

**Le désalignement est un frein au classement.** Si l'internaute cherche "comment faire X" (informationnel) et atterrit sur une page de vente (transactionnel), il repart — et Google le remarque.

### Étape 5 : Vérification Rapide du SEO Technique

#### Robots.txt
```
Vérifier : /robots.txt existe-t-il et est-il correctement configuré ?
```
- [ ] robots.txt accessible
- [ ] Ne bloque pas les pages ou ressources importantes
- [ ] Pointe vers sitemap.xml
- [ ] Ne bloque pas CSS/JS (nécessaire pour le rendu)

#### Sitemap XML
```
Vérifier : /sitemap.xml existe-t-il ?
```
- [ ] Sitemap présent et accessible
- [ ] Contient toutes les pages importantes
- [ ] Pas d'URLs cassées dans le sitemap
- [ ] Soumis à Google Search Console
- [ ] Les dates de dernière modification sont exactes

#### Balises Canoniques
- [ ] Balise canonique présente sur la page
- [ ] Pointe vers l'URL correcte (auto-référente ou vers la version canonique)
- [ ] Cohérente avec robots.txt et sitemap

#### Vitesse de Page
Benchmarks de référence :

| Métrique | Bon | À Améliorer | Mauvais |
|---|---|---|---|
| Largest Contentful Paint (LCP) | Moins de 2,5s | 2,5-4,0s | Plus de 4,0s |
| First Input Delay (FID) | Moins de 100ms | 100-300ms | Plus de 300ms |
| Cumulative Layout Shift (CLS) | Moins de 0,1 | 0,1-0,25 | Plus de 0,25 |
| Time to First Byte (TTFB) | Moins de 200ms | 200-500ms | Plus de 500ms |
| First Contentful Paint (FCP) | Moins de 1,8s | 1,8-3,0s | Plus de 3,0s |

**Problèmes de vitesse courants à signaler :**
- Images non optimisées (recommander format WebP, compression)
- JavaScript ou CSS bloquant le rendu
- Pas d'en-têtes de cache navigateur
- Pas de CDN détecté
- Scripts tiers excessifs (tracking, widgets, polices)
- CSS et JavaScript non minifiés
- Compression manquante (gzip ou brotli)

#### Compatibilité Mobile
- [ ] Balise meta viewport présente (`<meta name="viewport" content="width=device-width, initial-scale=1">`)
- [ ] Texte lisible sans zoom (minimum 16px pour le corps)
- [ ] Zones de touche suffisamment grandes et espacées (minimum 48x48px)
- [ ] Pas de défilement horizontal requis
- [ ] Images responsives
- [ ] Formulaires utilisables sur mobile

### Étape 6 : Analyse des Lacunes de Contenu

Méthodologie pour identifier les lacunes :

1. **Identifier le cluster thématique :** Quel est le sujet principal couvert par cette page/ce site ?
2. **Cartographier le contenu existant :** Quels sous-thèmes sont déjà couverts ?
3. **Identifier les sous-thèmes manquants :** Quels sujets connexes les concurrents couvrent-ils que ce site ne couvre pas ?
4. **Analyser "Les Gens Demandent Aussi" :** Quelles questions les internautes posent-ils sur ce sujet ?
5. **Vérifier les recherches associées :** Que suggère Google en bas de la SERP ?

**Modèle de Lacune de Contenu :**
| Sujet Manquant | Potentiel Volume de Recherche | Concurrence | Type de Contenu Nécessaire | Priorité |
|---|---|---|---|---|
| [Sujet] | Fort/Moyen/Faible | Forte/Moyenne/Faible | Blog/Guide/Outil/Page | 1-5 |

### Étape 7 : Optimisation des Featured Snippets

Identifier les opportunités de capturer des featured snippets :

**Types de featured snippets :**
1. **Snippet paragraphe** — Réponse en 40-60 mots. Utiliser une question claire en H2/H3 suivie d'une réponse concise.
2. **Snippet liste** — Utiliser des listes ordonnées ou non ordonnées avec un H2 contenant la requête cible.
3. **Snippet tableau** — Utiliser des tableaux HTML avec des en-têtes clairs.
4. **Snippet vidéo** — Inclure une vidéo avec titre descriptif et horodatages.

**Checklist d'optimisation :**
- [ ] Cibler les requêtes en forme de question ("comment", "qu'est-ce que", "pourquoi")
- [ ] Placer la réponse immédiatement après le titre-question
- [ ] Garder les réponses en paragraphe entre 40-60 mots
- [ ] Utiliser des listes structurées et des tableaux quand c'est approprié
- [ ] Inclure la requête cible dans un H2 ou H3

### Étape 8 : Audit du Balisage Schema

Vérifier l'implémentation des données structurées :

| Type de Schema | Applicable À | Statut |
|---|---|---|
| Organization | Page d'accueil, page À propos | Présent/Absent |
| LocalBusiness | Commerces locaux | Présent/Absent/N/A |
| Product | Pages produit | Présent/Absent/N/A |
| Article | Articles de blog, actualités | Présent/Absent/N/A |
| FAQ | Sections FAQ | Présent/Absent |
| HowTo | Contenu tutoriel | Présent/Absent/N/A |
| Review/AggregateRating | Avis, témoignages | Présent/Absent/N/A |
| BreadcrumbList | Toutes les pages avec fil d'Ariane | Présent/Absent |
| WebSite/SearchAction | Page d'accueil (sitelinks search box) | Présent/Absent |
| Event | Pages d'événements | Présent/Absent/N/A |

**Conseils d'implémentation :**
- Utiliser le format JSON-LD (format préféré de Google)
- Valider avec le Test des Résultats Enrichis de Google
- Ne pas baliser du contenu qui n'est pas visible sur la page
- Garder les données schema cohérentes avec le contenu on-page

### Étape 9 : Opportunités de Liens Internes

Identifier des améliorations spécifiques de liens internes :

1. **Pages orphelines** — Pages sans liens internes pointant vers elles
2. **Pages hub** — Pages à forte autorité qui devraient lier vers du contenu connexe
3. **Clusters thématiques** — Grouper le contenu connexe et créer des structures de liens
4. **Liens CTA** — Le contenu de blog devrait lier vers les pages produit/service pertinentes
5. **Liens footer/sidebar** — Liens sitewide vers les pages importantes

**Évaluation de l'Architecture de Liens :**
```
Page d'accueil
  |-- Pages Catégorie/Service (Contenu Pilier)
       |-- Articles de Blog individuels (Contenu Cluster)
            |-- Liens retour vers le Contenu Pilier
  |-- Pages de Conversion Clés (Tarification, Inscription, Contact)
       |-- Liées depuis le contenu pertinent
```

### Étape 10 : Évaluation de l'Impact des Core Web Vitals

Évaluer l'impact sur le CA des performances Core Web Vitals :

**Impacts prouvés par la recherche :**
- Les sites passant tous les Core Web Vitals voient 24% moins d'abandons de page
- Une diminution de 100ms du LCP correspond à une augmentation de 1,1% du taux de conversion
- Réduire le CLS de 0,1 correspond à une diminution de 15% du taux de rebond
- Les pages se chargeant en moins de 2 secondes ont un taux de rebond moyen de 9%, contre 38% pour les pages prenant 5 secondes

**Recommandations par métrique :**
| Métrique | Si Échoue | Correctifs Typiques |
|---|---|---|
| LCP | Plus de 2,5s | Optimiser l'image héros, précharger les ressources critiques, utiliser un CDN, réduire le temps de réponse serveur |
| FID/INP | Plus de 100ms | Réduire l'exécution JavaScript, différer les scripts non critiques, utiliser les web workers |
| CLS | Plus de 0,1 | Définir les dimensions des images, réserver l'espace pour les pubs/intégrations, éviter d'insérer du contenu au-dessus du contenu existant |

### Étape 11 : Recommandations de Stratégie de Contenu

Sur la base des observations de l'audit, recommander :

1. **Rythme de publication** — À quelle fréquence publier selon la concurrence et les ressources
2. **Types de contenu** — Articles de blog, guides, outils, vidéos, infographies
3. **Stratégie de ciblage de mots-clés** — Équilibre entre volume élevé et longue traîne
4. **Longueur du contenu** — Benchmark vs le contenu top-classé pour les mots-clés cibles
5. **Stratégie de mise à jour du contenu** — À quelle fréquence rafraîchir le contenu existant
6. **Plan de distribution** — Comment promouvoir le contenu au-delà de la recherche organique

**Matrice de Priorisation du Contenu :**
| Idée de Contenu | Volume de Recherche | Concurrence | Valeur Business | Score Priorité |
|---|---|---|---|---|
| [Sujet] | Fort/Moyen/Faible | Forte/Moyenne/Faible | Forte/Moyenne/Faible | 1-10 |

Score : Fort volume + Faible concurrence + Forte valeur business = Priorité maximale

## Format de Sortie

Générer un fichier `AUDIT-SEO.md` avec :

```markdown
# Audit SEO de Contenu
## [URL]
### Date : [Date]

---

## Score Santé SEO : [X/100]

---

## Checklist SEO On-Page

### Balise Titre
- Statut : [Conforme/À Améliorer/Non Conforme]
- Actuel : "[titre actuel]"
- Recommandé : "[titre amélioré]"
- Problèmes : [liste des problèmes]

### Méta Description
- Statut : [Conforme/À Améliorer/Non Conforme]
- Actuel : "[méta actuelle]"
- Recommandé : "[méta améliorée]"

### Hiérarchie des Titres
[Analyse de la structure H1-H6]

### Optimisation des Images
[Résultats de l'audit alt text]

### Liens Internes
[Analyse des liens]

### Structure d'URL
[Évaluation de l'URL]

---

## Qualité du Contenu (E-E-A-T)
| Dimension | Score | Preuves |
|---|---|---|
| Expérience | [Fort/Présent/Faible/Absent] | [détails] |
| Expertise | [Fort/Présent/Faible/Absent] | [détails] |
| Autorité | [Fort/Présent/Faible/Absent] | [détails] |
| Fiabilité | [Fort/Présent/Faible/Absent] | [détails] |

---

## Analyse des Mots-Clés
- Mot-Clé Principal : [mot-clé]
- Intention de Recherche : [type]
- Placement du Mot-Clé : [résultats checklist]
- Mots-Clés Secondaires : [liste]

---

## SEO Technique
[Résultats de la vérification rapide]

---

## Analyse des Lacunes de Contenu
[Tableau des sujets manquants]

---

## Opportunités Featured Snippets
[Opportunités spécifiques]

---

## Balisage Schema
[Actuel vs recommandé]

---

## Opportunités de Liens Internes
[Recommandations spécifiques]

---

## Core Web Vitals
[Évaluation de la performance avec impact CA]

---

## Recommandations de Stratégie de Contenu
[Plan de publication, priorités de contenu]

---

## Recommandations Priorisées

### Critique (Corriger Immédiatement)
1. [recommandation avec impact attendu]

### Haute Priorité (Ce Mois-ci)
1. [recommandation]

### Priorité Moyenne (Ce Trimestre)
1. [recommandation]

### Faible Priorité (Quand les Ressources le Permettent)
1. [recommandation]
```

## Principes Clés
- Les audits SEO doivent être éducatifs, pas juste diagnostiques. Expliquer POURQUOI chaque élément est important pour que le client comprenne la valeur.
- Toujours fournir l'"avant" (état actuel) et l'"après" (changement recommandé) pour que le client voie exactement ce qui doit changer.
- Relier les améliorations SEO aux résultats business. "Optimiser votre balise titre" ne veut rien dire pour un chef d'entreprise. "Optimiser votre balise titre pourrait augmenter votre taux de clic de 20-35%, ramenant environ 500 visiteurs supplémentaires par mois sur cette page" est actionnable.
- Utiliser les données du script automatisé comme point de départ, mais ajouter une analyse experte par-dessus. Le script trouve les données ; le skill interprète ce qu'elles signifient.
- Prioriser les recommandations par ratio effort/impact. Changer une balise titre prend 5 minutes mais peut impacter chaque impression de recherche. Réécrire tout le contenu prend des semaines.
- Si l'utilisateur a exécuté `/market audit` ou `/market landing` précédemment, croiser ces observations avec l'audit SEO pour une image plus complète.
