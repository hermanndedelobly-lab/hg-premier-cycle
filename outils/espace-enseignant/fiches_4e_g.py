# Fiches enseignant — Géographie 4e (lot 3 de la généralisation du modèle validé)
# Même format que fiches_h.py : étape = (moment, durée en min, stratégie, [activités du professeur],
# [réponses attendues des élèves], trace écrite)

PRES = "Présentation"
EVAL = "Évaluation"

FICHES = {}

FICHES['4e-g-t1-l1'] = {
 'materiel': ["carte des districts autonomes et de leurs chefs-lieux (carte 1)", "organigramme de l'administration déconcentrée (schéma 1)",
              "extrait de la loi n° 2014-451 du 5 août 2014", "questionnaire d'enquête préparé en classe"],
 'contexte': "l'État ivoirien est représenté sur tout le territoire par des autorités qu'il nomme.",
 'circonstance': "lors de l'inauguration de la salle multimédia du lycée moderne d'Alépé, des ministres se font représenter par le préfet de région ; des élèves de 4e veulent comprendre la déconcentration.",
 'taches': ["définir la déconcentration et identifier ses composantes", "décrire et schématiser l'administration déconcentrée",
            "mener une enquête sur son rôle et promouvoir le respect des institutions de l'État"],
 'prerequis': ["Les institutions de la République (EDHC).", "La carte de la Côte d'Ivoire (6e)."],
 'seances': [
  {'titre': "Présentation générale de la déconcentration (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation.", "« Pourquoi le préfet de région représente-t-il des ministres ? »"], ["Parce qu'il représente l'État et le Gouvernement dans la région."], "Introduction."),
   ("Développement · I. Présentation générale", 37, "Lecture d'un extrait de loi, construction des définitions",
    ["Faire définir la déconcentration et la circonscription administrative.", "Faire relever les raisons, les principes et les composantes."],
    ["Système fondé sur des circonscriptions dirigées par des responsables nommés par le pouvoir central.", "Encadrer, développer, unir, rapprocher l'administration ; circonscriptions hiérarchisées ; circonscriptions et services extérieurs."], "I. 1 à 3."),
   (EVAL, 10, "Travail individuel", ["Activité d'application I."], ["Définitions."], None),
  ]},
  {'titre': "Les circonscriptions administratives (II)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Quelles circonscriptions et quels responsables ? »"], ["Préfecture, sous-préfecture ; préfet, sous-préfet."], None),
   ("Développement · II. Les circonscriptions", 40, "Lecture de la carte 1, tableau",
    ["Faire localiser le district de l'établissement sur la carte 1.", "Faire compléter un tableau : circonscription, nombre, responsable, missions."],
    ["District autonome (14, ministre-gouverneur), région (31, préfet de région), département (plus de 100, préfet), sous-préfecture (environ 510, sous-préfet), village (plus de 8 000, chef de village)."], "II. 1 à 5."),
   (EVAL, 10, "Travail individuel", ["Activité d'application II."], ["Classement et responsables."], None),
  ]},
  {'titre': "Les services extérieurs et le schéma (III et IV)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Qui représente les ministères dans notre ville ? »"], ["La DRENA, la direction de la santé, la gendarmerie."], None),
   ("Développement · III. et IV. Services extérieurs et schéma", 40, "Recensement, construction du schéma 1",
    ["Faire recenser les services extérieurs de la localité.", "Faire construire le schéma de l'administration déconcentrée avec l'exemple local."],
    ["Directions régionales et départementales, police, gendarmerie, impôts, sous l'autorité du préfet.", "Pouvoir central → district → région → département → sous-préfecture → village."], "III, IV."),
   (EVAL, 10, "Travail individuel", ["Activités d'application III et IV."], ["Définition du service extérieur ; schéma."], None),
  ]},
  {'titre': "Le rôle de l'administration déconcentrée et le respect des institutions (V et VI)", 'etapes': [
   (PRES, 5, "Retour sur l'enquête", ["« Qu'avez-vous appris à la préfecture ? »"], ["Le préfet assure la sécurité, délivre des documents."], None),
   ("Développement · V. et VI. Rôle et respect des institutions", 35, "Restitution de l'enquête, synthèse",
    ["Faire restituer l'enquête par groupes.", "Faire dégager les règles de comportement civique."],
    ["Représenter l'État, appliquer les lois, sécurité, documents, coordination, suivi des projets.", "Respect des autorités, protection des biens publics, état civil, impôts, participation."], "V, VI, conclusion."),
   (EVAL, 15, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Définition, structures, rôle, comportements."], None),
  ]},
 ],
 'eclairage': [
  "La loi n° 2014-451 du 5 août 2014 fonde l'administration territoriale sur la déconcentration et la décentralisation.",
  "14 districts autonomes depuis 2021 ; 31 régions ; les nombres de départements et de sous-préfectures évoluent : vérifier les chiffres récents.",
  "La circonscription administrative n'a ni budget propre ni organe élu : c'est la différence avec la collectivité territoriale.",
  "Le chef de village est désigné selon la coutume et reconnu par l'administration.",
 ],
 'difficultes': [
  ("Confusion entre circonscription et collectivité.", "Opposer le responsable nommé et l'élu."),
  ("Difficulté à hiérarchiser les circonscriptions.", "Jeu de classement avec le schéma 1."),
  ("Confusion entre circonscription et service extérieur.", "Territoire / relais d'un ministère."),
 ],
 'soutien': ["Fiche-lexique : déconcentration, circonscription, préfet, service extérieur.", "Schéma 1 vierge à compléter."],
 'approfondissement': ["Interview d'un agent de la préfecture ou de la sous-préfecture.", "Recherche sur l'histoire du découpage administratif de la région."],
 'evaluation': {
  'activites': [
   ("Définis : déconcentration ; circonscription administrative.", 2, "Déconcentration : système fondé sur des circonscriptions dirigées par des responsables nommés par le pouvoir central (1 pt) ; circonscription : portion du territoire créée pour la gestion administrative (1 pt)."),
   ("Cite les deux composantes de l'administration déconcentrée.", 1, "Les circonscriptions administratives (0,5 pt) et les services extérieurs de l'État (0,5 pt)."),
   ("Range du plus grand au plus petit et nomme le responsable : sous-préfecture, région, village, district autonome, département.", 3, "District autonome (ministre-gouverneur) → région (préfet de région) → département (préfet) → sous-préfecture (sous-préfet) → village (chef de village). 0,5 pt pour l'ordre, 0,5 pt par responsable exact (5 attendus, plafonné à 2,5)."),
   ("Donne deux exemples de services extérieurs de l'État.", 2, "Direction régionale de l'Éducation nationale, direction régionale de la Santé, direction départementale de l'Agriculture, brigade de gendarmerie, centre des impôts. 1 pt par exemple."),
  ],
  'situation': "Dans ton quartier, des jeunes affirment que le sous-préfet est « un simple fonctionnaire » et refusent de participer à une réunion qu'il a convoquée.",
  'consignes': [
   ("Identifie le système d'administration auquel appartient le sous-préfet et son supérieur hiérarchique.", 2, "La déconcentration (1 pt) ; le préfet (1 pt)."),
   ("Explique le rôle du sous-préfet dans sa circonscription.", 4, "Il représente l'État (1 pt), maintient l'ordre et la sécurité (1 pt), assure l'état civil là où il n'y a pas de commune (1 pt), encadre les chefs de village et règle les litiges (1 pt)."),
   ("Propose deux attitudes qui montrent le respect des institutions de l'État.", 4, "Répondre aux convocations des autorités, respecter les lois, protéger les biens publics, déclarer les naissances (2 pts par attitude, 2 attendues)."),
  ],
 },
 'valeurs': ["Respect des institutions et des autorités de l'État.", "Sens du service public et civisme.",
             "Liens avec l'EDHC (institutions, citoyenneté)."],
}
