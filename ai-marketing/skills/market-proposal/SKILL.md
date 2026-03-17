# Générateur de Proposition Commerciale pour Services Marketing

## Objectif du Skill
Générer une proposition de services marketing professionnelle et prête pour le client. Ce skill produit un document de proposition complet qui positionne l'agence/consultant comme le choix évident, cadre la tarification avec ancrage et options à paliers, et inclut des projections ROI pour justifier l'investissement.

**IMPORTANT : Tu dois toujours répondre et rédiger tous tes livrables en français.**

## Quand Utiliser
- L'utilisateur souhaite créer une proposition pour un prospect marketing
- L'utilisateur a terminé un appel de découverte et doit formaliser la mission
- L'utilisateur veut un modèle pour les propositions de son agence
- Déclenché par `/market proposal` ou `/market proposal <nom du client>`

## Comment Exécuter

### Étape 1 : Recueillir les Informations pour la Proposition
Collecter ces informations auprès de l'utilisateur (demander si non fournies) :

**Sur le Client :**
1. Nom du client et de l'entreprise
2. Secteur et modèle commercial
3. Situation marketing actuelle (ce qu'il fait maintenant)
4. Principaux points de douleur ou défis
5. Objectifs (chiffre d'affaires, croissance, leads, notoriété)
6. Budget estimé (si connu)
7. Calendrier de décision
8. Parties prenantes et décideurs clés

**Sur les Services :**
1. Quels services proposez-vous ? (SEO, publicité payante, contenu, social, email, full-stack)
2. Modèle d'engagement (retainer, projet, basé sur la performance)
3. Calendrier proposé
4. Vos études de cas ou résultats pertinents

**Si des données d'audit existent :** Vérifier s'il y a des résultats d'un `/market audit` précédent. Si trouvés, les intégrer automatiquement dans la section Analyse de la Situation pour une proposition étayée par les données.

### Étape 2 : Cadre de Questions pour l'Appel de Découverte
Si l'utilisateur n'a pas encore eu l'appel de découverte, fournir ces 10 questions essentielles :

**Compréhension du Business :**
1. "Décrivez-moi votre modèle commercial. Comment gagnez-vous de l'argent ?"
2. "Qui est votre client idéal ? Décrivez-le en détail."
3. "À quoi ressemble votre processus de vente du premier contact à la signature ?"

**Marketing Actuel :**
4. "Quel marketing faites-vous aujourd'hui, et qu'est-ce qui fonctionne ou non ?"
5. "Quelle est votre dépense marketing mensuelle actuelle, et quel est le ROI ?"
6. "Quels outils et plateformes utilisez-vous ?"

**Objectifs et Attentes :**
7. "Si nous réussissons pleinement, à quoi ressemble la situation dans 6 mois ? 12 mois ?"
8. "Quels chiffres précis cherchez-vous à atteindre ? (CA, leads, trafic)"
9. "Quelle est la valeur vie client pour vous ?"

**Décision et Processus :**
10. "Qui d'autre est impliqué dans cette décision, et quel est votre calendrier pour choisir un partenaire ?"

**Questions Bonus :**
- "Quelle est votre plus grande frustration en matière de marketing en ce moment ?"
- "Avez-vous déjà travaillé avec des agences ou consultants ? Qu'est-ce qui s'est bien ou mal passé ?"
- "Y a-t-il quelque chose qui vous ferait dire 'non' à une collaboration ?"

### Étape 3 : Construire le Document de Proposition

#### Section 1 : Page de Couverture
```
[Logo de votre entreprise]

Proposition de Stratégie Marketing
Préparée pour : [Nom du Client]
Préparée par : [Votre Nom / Agence]
Date : [Date]
Valable jusqu'au : [Date + 30 jours]

CONFIDENTIEL
```

#### Section 2 : Résumé Exécutif (1 page max)
Rédiger un résumé concis qui :
- Reconnaît la situation et les objectifs du client
- Énonce le problème central que vous allez résoudre
- Présente votre approche recommandée
- Laisse entrevoir le résultat attendu
- Crée un sentiment d'urgence à agir

**Modèle :**
```
[Nom du Client] est à un moment charnière. Avec [situation actuelle — ex. : forte adéquation produit-marché mais génération de leads irrégulière], il existe une opportunité significative de [résultat souhaité — ex. : accélérer l'acquisition clients pour soutenir vos objectifs de croissance].

Sur la base de notre analyse de [ce que vous avez examiné — site, pubs, concurrents, etc.], nous avons identifié [X] domaines clés où des améliorations stratégiques pourraient générer [résultat spécifique — ex. : une augmentation de 40-60% des leads qualifiés en 6 mois].

Cette proposition présente une mission de [durée] axée sur [domaines de service principaux], conçue pour [résultat principal]. Notre approche repose sur [votre différenciateur — ex. : méthodologie data-driven, expertise sectorielle, frameworks éprouvés].

Nous recommandons de commencer par [première phase] pour établir des bases solides et des victoires rapides, puis d'intensifier les efforts en fonction des données de performance.
```

#### Section 3 : Analyse de la Situation (2-3 pages)
Présenter votre analyse du marketing actuel du client. C'est là que les données d'audit de `/market audit` sont précieuses.

**Structure :**
1. **État Actuel** — Ce qu'il fait maintenant et ses performances
2. **Opportunités Identifiées** — Domaines spécifiques où une amélioration est possible
3. **Paysage Concurrentiel** — Comment il se compare aux concurrents (via `/market competitors` si disponible)
4. **Défis Clés** — Obstacles à surmonter
5. **Contexte de Marché** — Tendances sectorielles et benchmarks

**Important :** Formuler tout en termes d'opportunités, pas d'échecs. Le client doit se sentir compris, pas critiqué.

Bien : "Votre site web convertit à environ 1,8%, en dessous du benchmark sectoriel de 3,2%. Nous voyons un chemin clair pour combler cet écart grâce à des initiatives CRO ciblées."

Mal : "Votre site web a un taux de conversion terrible et nécessite une refonte complète."

#### Section 4 : Stratégie et Approche (2-3 pages)
Présenter votre stratégie recommandée. Soyez assez spécifique pour démontrer votre expertise sans donner un manuel d'exécution.

**Structure :**
1. **Cadre Stratégique** — Votre approche et méthodologie globale
2. **Phase 1 : Fondation** (Mois 1-2) — Configuration, audits, bases, victoires rapides
3. **Phase 2 : Croissance** (Mois 3-4) — Exécution des campagnes principales, optimisation
4. **Phase 3 : Scale** (Mois 5-6) — Développer ce qui fonctionne, couper ce qui ne marche pas
5. **Continu : Optimiser** — Amélioration continue, reporting, affinage de la stratégie

Pour chaque phase, inclure :
- Activités et livrables spécifiques
- Résultats attendus
- Comment le succès sera mesuré

#### Section 5 : Périmètre d'Intervention (1-2 pages)
Détailler exactement ce qui est inclus (et ce qui ne l'est pas).

**Inclure :**
- Livrables spécifiques avec quantités (ex. : "8 articles de blog par mois, 1 500-2 000 mots chacun")
- Rythme des réunions (ex. : "Appels stratégiques bimensuels, reporting mensuel")
- Engagements de délai de réponse (ex. : "Réponse en 24h les jours ouvrés")
- Outils et plateformes inclus
- Format et fréquence des rapports

**Exclure explicitement :**
- Éléments hors périmètre pour éviter le scope creep
- Coûts supplémentaires (budget publicitaire, logiciels, photos)
- Hypothèses sur les responsabilités du client

**Section Responsabilités du Client :**
Lister ce dont vous avez besoin du client pour réussir :
- Retours et validations rapides (préciser SLA)
- Accès aux comptes, outils et données
- Interlocuteur désigné
- Validation des contenus sous X jours ouvrés
- Budget publicitaire (séparé des honoraires de gestion)

#### Section 6 : Calendrier (1 page)
Calendrier visuel montrant les phases, jalons et livrables.

```
Mois 1     | Mois 2     | Mois 3     | Mois 4     | Mois 5     | Mois 6
-----------|------------|------------|------------|------------|----------
FONDATION  | FONDATION  | CROISSANCE | CROISSANCE | SCALE      | SCALE
Audit &    | Victoires  | Lancement  | Optim &    | Développer | Pleine
Setup      | rapides    | campagnes  | itérations | gagnants   | vitesse

Jalons Clés :
- Semaine 2 : Audit et document de stratégie finalisés
- Semaine 4 : Premières campagnes en ligne
- Mois 2 : Premier rapport de performance
- Mois 3 : Recommandations d'optimisation
- Mois 6 : Bilan complet et actualisation de la stratégie
```

#### Section 7 : Investissement (1-2 pages)
Présenter la tarification avec la structure Bon-Mieux-Excellence.

**Modèle de Tarification à Trois Paliers :**

| Composant | Démarrage | Accélération | Domination |
|-----------|-----------|--------------|------------|
| Stratégie & Planning | Révision trimestrielle | Stratégie mensuelle | Stratégie hebdomadaire |
| Création de contenu | 4 pièces/mois | 8 pièces/mois | 16 pièces/mois |
| Réseaux sociaux | 3 plateformes | 5 plateformes | Toutes plateformes |
| Gestion pubs | Jusqu'à 5K€ de budget | Jusqu'à 15K€ de budget | Jusqu'à 50K€ de budget |
| SEO | On-page de base | Programme SEO complet | SEO complet + link building |
| Email Marketing | — | Newsletter mensuelle | Automatisation complète |
| Reporting | Rapport mensuel | Rapport bimensuel | Dashboard hebdomadaire |
| Réunions | Appel mensuel | Appel bimensuel | Appel hebdomadaire |
| **Investissement Mensuel** | **X XXX€** | **X XXX€** | **X XXX€** |

**Conseils de Psychologie des Prix :**
- Présenter trois options ; la plupart des clients choisissent le palier du milieu
- Nommer les paliers avec des labels aspirationnels (pas Bronze/Argent/Or)
- Ancrer le palier le plus élevé en premier pour que le milieu semble raisonnable
- Inclure un badge "Le Plus Populaire" ou "Recommandé" sur le palier du milieu
- Montrer le calcul : "Avec une [LTV client], vous n'avez besoin que de [X] nouveaux clients par mois pour voir un ROI positif"

**Référence des Modèles de Tarification :**

| Modèle | Quand l'Utiliser | Fourchette Typique |
|--------|-----------------|-------------------|
| Retainer mensuel | Services continus, relation long terme | 2 000-25 000€/mois |
| Basé sur le projet | Périmètre défini, livrable unique | 5 000-100 000€ par projet |
| Basé sur la performance | Le client veut partager le risque, vous êtes confiant | Base + % du CA/leads |
| Hybride | Missions complexes | Retainer de base + bonus de performance |
| Horaire | Conseil, advisory, ad hoc | 150-500€/heure |

#### Section 8 : Projection ROI
Montrer au client le retour attendu sur son investissement.

**Cadre de Calcul ROI :**
```
État Actuel :
- Trafic mensuel : [X]
- Taux de conversion actuel : [X%]
- Leads/mois actuels : [X]
- Taux de closing : [X%]
- Valeur moyenne d'un contrat : [X]€
- CA mensuel actuel issu du marketing : [X]€

État Projeté (6 mois) :
- Augmentation de trafic projetée : [X%] → [nouveau trafic]
- Taux de conversion projeté : [X%] → [nouveaux leads/mois]
- Augmentation des leads projetée : [X%]
- Augmentation de CA projetée : [X]€/mois
- ROI projeté sur 6 mois : [X]x

Investissement : [coût total 6 mois]€
Retour projeté : [augmentation CA projetée]€
ROI : [X]x de retour
```

**Important :** Soyez conservateur dans vos projections. Sous-promettre et sur-délivrer. Utiliser des fourchettes plutôt que des chiffres précis. Ajouter des clauses indiquant que les résultats dépendent de multiples facteurs.

#### Section 9 : L'Équipe (0,5-1 page)
Présenter les membres de l'équipe qui travailleront sur ce compte.

Pour chaque membre :
- Nom et titre
- Expérience et expertise pertinentes
- Rôle dans cette mission
- Bio courte (2-3 phrases max)

#### Section 10 : Études de Cas (1-2 pages)
Inclure 2-3 études de cas pertinentes démontrant des résultats similaires à ceux promis.

**Format d'Étude de Cas :**
```
Client : [Secteur et type d'entreprise — anonymiser si nécessaire]
Défi : [1-2 phrases sur leur situation]
Solution : [1-2 phrases sur ce que vous avez fait]
Résultats :
- [Métrique spécifique 1 : ex. "Trafic organique augmenté de 287% en 6 mois"]
- [Métrique spécifique 2 : ex. "Coût par lead réduit de 45€ à 12€"]
- [Métrique spécifique 3 : ex. "180 000€ de nouveau CA généré"]
```

#### Section 11 : Prochaines Étapes (0,5 page)
Rendre le processus cristallin. Réduire la friction.

```
Prêt à avancer ? Voici ce qui se passe ensuite :

1. Signez cette proposition (lien signature électronique inclus)
2. Nous planifierons un appel de lancement dans les 48 heures
3. Vous recevrez notre questionnaire d'onboarding et le formulaire de demande d'accès
4. Nous démarrons la phase de Fondation immédiatement

Des questions ? Contactez [Nom] à [email] ou [téléphone].

Cette proposition est valable jusqu'au [date — 30 jours à partir d'aujourd'hui].
```

### Étape 4 : Design et Mise en Forme de la Proposition

**Bonnes Pratiques :**
- Garder la proposition totale sous 15 pages (hors annexe)
- Utiliser des en-têtes, polices et couleurs cohérents
- Inclure le logo du client à côté du vôtre sur la page de couverture
- Utiliser des graphiques et visuels plutôt que du texte dense
- Mettre en gras les chiffres et résultats clés
- Utiliser les espaces blancs généreusement
- Inclure numéros de page et table des matières pour les propositions longues
- Sauvegarder en PDF pour une présentation professionnelle

### Étape 5 : Séquence de Relance Après Envoi

**Jour 0 (Envoi) :**
Envoyer la proposition par email avec une courte note d'accompagnement. Objet : "Votre Plan de Croissance Marketing — [Nom du Client]"

**Jour 2 :**
Email de relance : "Je voulais m'assurer que vous aviez bien reçu la proposition. Je suis disponible pour un appel rapide afin de la présenter si cela vous aide."

**Jour 5 :**
Relance avec valeur ajoutée : Partager un article, étude de cas ou insight pertinent pour leur secteur. Référencer subtilement la proposition.

**Jour 7 :**
Relance directe : "J'aimerais avoir votre avis sur la proposition. Avez-vous des questions auxquelles je peux répondre ? Je suis disponible [créneaux précis] cette semaine."

**Jour 14 :**
Dernière relance : "Je souhaitais vous contacter une dernière fois au sujet de la proposition. Je comprends que le timing n'est peut-être pas idéal — si c'est le cas, je serai heureux de reprendre contact quand le moment sera venu."

**Jour 21 :**
Email de rupture : "Sans nouvelles de votre part, je suppose que le timing n'est pas opportun. Je vais clore cette proposition le [date d'expiration]. Si les choses changent, ma porte reste ouverte. Je vous souhaite, ainsi qu'à [Entreprise], tout le succès possible."

### Étape 6 : Gestion des Objections

Préparer des réponses aux objections courantes des clients :

| Objection | Cadre de Réponse |
|-----------|-----------------|
| "Trop cher" | Recadrer comme investissement, montrer le ROI, proposer un périmètre de départ plus petit, comparer au coût de l'inaction |
| "On peut le faire en interne" | Mettre en avant le coût d'opportunité, l'expertise spécialisée, la rapidité de résultats et le vrai coût complet en interne |
| "On a essayé ça avant et ça n'a pas marché" | Demander ce qui n'a pas fonctionné précisément, différencier votre approche, proposer un projet pilote avec critères de succès clairs |
| "On doit y réfléchir" | Fixer une date de relance précise, proposer d'adresser des préoccupations spécifiques, fournir des références supplémentaires |
| "Pouvez-vous garantir les résultats ?" | Expliquer pourquoi les garanties sont irréalistes en marketing mais partager les résultats historiques, proposer une composante basée sur la performance |
| "On parle avec d'autres agences" | L'accueillir favorablement, se différencier sur la méthodologie pas le prix, proposer une période d'essai, souligner la compatibilité culturelle |
| "Le calendrier est trop long" | Expliquer pourquoi les raccourcis échouent, proposer une phase de victoires rapides, montrer l'approche par phases avec une valeur précoce |
| "On n'a pas le budget maintenant" | Proposer une mission de départ plus petite, différer certains paiements, montrer le coût de l'attente |

### Étape 7 : Éléments Essentiels des Conditions Générales

À inclure en annexe de la proposition ou en document séparé :

1. **Conditions de Paiement :** 15 ou 30 jours nets, modes de paiement, pénalités de retard
2. **Durée du Contrat :** Période d'engagement minimale, conditions de renouvellement automatique
3. **Politique d'Annulation :** Préavis requis (typiquement 30 jours), processus de sortie
4. **Modifications de Périmètre :** Processus de gestion des changements et coûts supplémentaires
5. **Propriété Intellectuelle :** Propriétaire du travail produit, conditions de licence
6. **Confidentialité :** Termes NDA, gestion des données client
7. **Limitation de Responsabilité :** Plafonds de responsabilité, cas de force majeure
8. **Reporting et Communication :** Rythme et format convenus
9. **Coûts Tiers :** Responsabilité client pour budget pub, logiciels, images
10. **Clause de Non-Garantie des Résultats :** Les résultats marketing ne sont pas garantis

## Format de Sortie

Générer un fichier `PROPOSITION-CLIENT.md` avec :

```markdown
# Proposition de Services Marketing

## Préparée pour : [Nom du Client]
## Préparée par : [Nom de l'Agence]
## Date : [Date]

---

## Table des Matières
1. Résumé Exécutif
2. Analyse de la Situation
3. Stratégie & Approche
4. Périmètre d'Intervention
5. Calendrier
6. Investissement
7. Projection ROI
8. Notre Équipe
9. Études de Cas
10. Prochaines Étapes

---

[Contenu complet de la proposition avec toutes les sections remplies selon les détails du client]

---

## Annexe
- Conditions Générales
- Description Détaillée des Livrables
- Stack d'Outils
```

## Principes Clés
- La proposition est un document de vente, pas un cahier des charges. Elle doit VENDRE, pas seulement décrire.
- Commencer par les problèmes et objectifs du client, pas par vos services. Faites-le se sentir compris avant de présenter les solutions.
- Chaque prix doit être ancré au ROI qu'il va générer. Ne jamais présenter un coût sans contexte.
- Utiliser le langage propre au client issu de l'appel de découverte. Lui renvoyer ses propres mots.
- Si des données d'audit sont disponibles via des skills précédents, les utiliser abondamment — les propositions étayées par des données se concluent 2-3x plus souvent que les propositions génériques.
- Rester concis. Les dirigeants survolent. Utiliser le gras, les en-têtes et les tableaux pour rendre les informations clés facilement lisibles.
- Toujours inclure une prochaine étape spécifique et limitée dans le temps. L'ambiguïté tue les deals.
