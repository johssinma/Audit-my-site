#!/usr/bin/env python3
"""
Générateur de Calendrier de Contenu Social — Script utilitaire pour claude-mark2
Génère un calendrier structuré de contenu réseaux sociaux sur 30 jours avec des posts
spécifiques à chaque plateforme.
"""

import sys
import json
from datetime import datetime, timedelta


# Modèles de piliers de contenu
CONTENT_PILLARS = {
    "educatif": {
        "name": "Éducatif",
        "description": "Enseigner quelque chose de précieux à votre audience",
        "formats": ["Thread comment faire", "Conseil rapide", "Démystification", "Partage de cadre",
                     "Recommandation d'outil", "Insight sectoriel", "Analyse de données"],
        "platforms": {
            "linkedin": "Post long format avec puces, partager cadres et données",
            "twitter": "Format thread (5-10 tweets), commencer par une prise de position ou statistique surprenante",
            "instagram": "Carrousel (5-10 diapositives), design épuré, un insight par diapositive",
            "tiktok": "Parlant face caméra 60-90s ou capture d'écran, accroche dans les 2 premières secondes",
            "youtube": "Analyse approfondie 8-15 min, titre optimisé pour la recherche, miniature forte"
        }
    },
    "coulisses": {
        "name": "Dans les Coulisses",
        "description": "Montrer le processus réel et non filtré",
        "formats": ["Journée type", "Révélation du stack d'outils", "Présentation du processus",
                     "Erreur/leçon apprise", "Partage CA/métriques", "Équipe/espace de travail"],
        "platforms": {
            "linkedin": "Format histoire personnelle, vulnérabilité + leçon apprise",
            "twitter": "Tweet unique avec photo ou court thread, brut et authentique",
            "instagram": "Stories ou Reels, décontracté et authentique, footage dans les coulisses",
            "tiktok": "Footage brut, audio tendance, ambiance authentique",
            "youtube": "Style vlog, 5-10 min, journée type ou révélation de processus"
        }
    },
    "preuve_sociale": {
        "name": "Preuve Sociale",
        "description": "Montrer résultats, témoignages et crédibilité",
        "formats": ["Victoire client/étude de cas", "Partage témoignage", "Avant/après",
                     "Jalon CA", "Contenu généré par utilisateurs", "Récompense/reconnaissance"],
        "platforms": {
            "linkedin": "Format étude de cas avec chiffres précis, taguer le client",
            "twitter": "Capture d'écran résultat + contexte bref, célébrer publiquement",
            "instagram": "Visuel témoignage designé ou extrait vidéo témoignage",
            "tiktok": "Révélation avant/après, contenu transformation",
            "youtube": "Présentation complète étude de cas, 10-15 min"
        }
    },
    "engagement": {
        "name": "Engagement",
        "description": "Lancer des conversations et construire la communauté",
        "formats": ["Prise de position/opinion", "Post question", "Sondage", "Ça ou ça",
                     "Opinion impopulaire", "D'accord ou pas", "Complétez la phrase"],
        "platforms": {
            "linkedin": "Commencer par une affirmation percutante, demander des avis en commentaires",
            "twitter": "Prise de position courte et punchy ou sondage, répondre à chaque commentaire",
            "instagram": "Sondages/questions en stories, stickers interactifs",
            "tiktok": "Format stitch ou duet, répondre aux commentaires",
            "youtube": "Post communauté avec sondage, ou vidéo demandant des avis"
        }
    },
    "promotionnel": {
        "name": "Promotionnel",
        "description": "Promotion directe du produit/service (à utiliser avec parcimonie)",
        "formats": ["Démo produit", "Mise en avant de fonctionnalité", "Offre spéciale",
                     "Promo webinaire/événement", "Ressource gratuite", "Invitation communauté"],
        "platforms": {
            "linkedin": "Approche valeur d'abord, commencer par le problème que vous résolvez",
            "twitter": "Pitch court avec lien, ou thread montrant l'outil en action",
            "instagram": "Démo Reel ou carrousel montrant les bénéfices, lien en bio",
            "tiktok": "Démo produit avec format tendance, vente douce",
            "youtube": "Tutoriel utilisant votre produit, pas un pitch commercial"
        }
    }
}

# Recommandations de fréquence de publication
POSTING_FREQUENCY = {
    "linkedin": {"ideal": "3-5x/semaine", "minimum": "2x/semaine", "meilleurs_horaires": "Mar-Jeu 8-10h, 12h"},
    "twitter": {"ideal": "3-5x/jour", "minimum": "1x/jour", "meilleurs_horaires": "9h, 12h, 17h"},
    "instagram": {"ideal": "4-7x/semaine (feed+reels)", "minimum": "3x/semaine", "meilleurs_horaires": "11h-13h, 19h-21h"},
    "tiktok": {"ideal": "1-3x/jour", "minimum": "3x/semaine", "meilleurs_horaires": "7h-9h, 12h-15h, 19h-23h"},
    "youtube": {"ideal": "2-3x/semaine", "minimum": "1x/semaine", "meilleurs_horaires": "Jeu-Sam 14h-16h"},
    "facebook": {"ideal": "3-5x/semaine", "minimum": "2x/semaine", "meilleurs_horaires": "Mer 11h, Ven 10h-11h"}
}

# Formules d'accroche par plateforme
HOOK_FORMULAS = {
    "linkedin": [
        "J'ai {fait X} et {résultat inattendu}. Voici ce que j'ai appris :",
        "La plupart des gens pensent {croyance courante}. Ils ont tort. Voici pourquoi :",
        "{Nombre} choses que j'aurais aimé savoir avant {action} :",
        "J'ai passé {temps} à analyser {sujet}. Voici {nombre} découvertes :",
        "Arrêtez {erreur courante}. Faites ça à la place :",
        "Le {secteur} est en train de changer. Voici ce dont personne ne parle :"
    ],
    "twitter": [
        "{Sujet} est cassé. Voici un thread sur comment le réparer 🧵",
        "J'ai étudié {nombre} {choses}. Voici ce qui sépare les meilleurs du reste :",
        "Opinion impopulaire : {affirmation percutante}",
        "Vous n'avez pas besoin de {chose}. Vous avez besoin de {mieux}. Voici pourquoi :",
        "{Nombre} {choses} qui vont {bénéfice} (thread) :",
        "La plus grande erreur en {sujet} ? {Erreur}. Laissez-moi expliquer :"
    ],
    "instagram": [
        "Sauvegardez ça pour plus tard ↓",
        "POV : Vous atteignez enfin {résultat souhaité}",
        "{Nombre} choses sur {sujet} qui vont vous épater",
        "L'antisèche {sujet} dont vous ignoriez avoir besoin",
        "Si vous luttez avec {problème}, essayez ça →",
        "J'ai transformé {entrée} en {sortie impressionnante}. Voici comment :"
    ],
    "tiktok": [
        "Attendez la fin... (révélation transformation)",
        "Des choses qui font sens en {niche}",
        "POV : Vous découvrez {chose utile}",
        "Je n'arrive pas à croire que {chose surprenante} marche vraiment",
        "En réponse à @utilisateur — voici comment je {fais cette chose}",
        "Jour {X} de {défi/série}"
    ]
}


def generate_calendar(topic, platforms=None, days=30, brand_name=None):
    """Générer un calendrier de contenu réseaux sociaux."""
    if platforms is None:
        platforms = ["linkedin", "twitter", "instagram"]

    start_date = datetime.now()
    calendar = {
        "sujet": topic,
        "marque": brand_name or topic,
        "plateformes": platforms,
        "duree_jours": days,
        "date_debut": start_date.strftime("%Y-%m-%d"),
        "date_fin": (start_date + timedelta(days=days)).strftime("%Y-%m-%d"),
        "planning_publication": {p: POSTING_FREQUENCY.get(p, {}) for p in platforms},
        "piliers_contenu": {
            k: {"nom": v["name"], "description": v["description"], "frequence": ""}
            for k, v in CONTENT_PILLARS.items()
        },
        "distribution_piliers": {
            "educatif": "40%",
            "coulisses": "15%",
            "preuve_sociale": "15%",
            "engagement": "20%",
            "promotionnel": "10%"
        },
        "formules_accroche": {p: HOOK_FORMULAS.get(p, []) for p in platforms},
        "calendrier": []
    }

    # Générer 30 jours d'idées de contenu
    pillar_rotation = ["educatif", "engagement", "educatif", "coulisses",
                       "educatif", "preuve_sociale", "promotionnel",
                       "educatif", "engagement", "educatif"]

    jours_semaine_fr = {
        "Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi",
        "Thursday": "Jeudi", "Friday": "Vendredi", "Saturday": "Samedi", "Sunday": "Dimanche"
    }

    for day in range(days):
        date = start_date + timedelta(days=day)
        day_of_week_en = date.strftime("%A")
        day_of_week = jours_semaine_fr.get(day_of_week_en, day_of_week_en)

        pillar_key = pillar_rotation[day % len(pillar_rotation)]
        pillar = CONTENT_PILLARS[pillar_key]

        format_idx = day % len(pillar["formats"])
        content_format = pillar["formats"][format_idx]

        day_entry = {
            "jour": day + 1,
            "date": date.strftime("%Y-%m-%d"),
            "jour_semaine": day_of_week,
            "pilier": pillar["name"],
            "format": content_format,
            "angle_sujet": f"{content_format} sur {topic}",
            "plateformes": {}
        }

        for platform in platforms:
            if platform in pillar["platforms"]:
                day_entry["plateformes"][platform] = {
                    "conseils": pillar["platforms"][platform],
                    "publier": True
                }

        calendar["calendrier"].append(day_entry)

    # Ajouter la stratégie de réutilisation
    calendar["strategie_reutilisation"] = {
        "description": "Transformer 1 pièce de contenu en 10+ posts sur les plateformes",
        "workflow": [
            f"1. Créer un contenu long format sur {topic} (article de blog ou vidéo YouTube)",
            "2. Extraire 5-7 insights clés comme posts individuels",
            "3. Adapter chaque insight au format spécifique de la plateforme",
            "4. Créer un carrousel/thread à partir du contenu complet",
            "5. Filmer un résumé de 60s comme Reel/TikTok",
            "6. Extraire des citations pour des posts images",
            "7. Créer un sondage ou question à partir d'un insight",
            "8. Partager les coulisses de la création du contenu",
            "9. Repartager les posts les plus performants 2-4 semaines plus tard",
            "10. Créer une compilation 'best of' mensuellement"
        ]
    }

    return calendar


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "utilisation": "python3 social_calendar.py <sujet> [plateforme1,plateforme2,...] [jours]",
            "exemple": "python3 social_calendar.py 'automatisation IA' linkedin,twitter,instagram 30",
            "description": "Génère un calendrier de contenu réseaux sociaux",
            "plateformes_disponibles": list(POSTING_FREQUENCY.keys())
        }, indent=2, ensure_ascii=False))
        return

    topic = sys.argv[1]
    platforms = sys.argv[2].split(",") if len(sys.argv) > 2 else ["linkedin", "twitter", "instagram"]
    days = int(sys.argv[3]) if len(sys.argv) > 3 else 30

    calendar = generate_calendar(topic, platforms, days)
    print(json.dumps(calendar, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
