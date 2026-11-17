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

FICHES['4e-g-t1-l2'] = {
 'materiel': ["schéma de l'administration décentralisée (schéma 1)", "schéma des sources de financement (schéma 2)",
              "budget simplifié d'une commune", "questionnaire d'enquête à la mairie"],
 'contexte': "les populations élisent les responsables des communes et des régions chargés du développement local.",
 'circonstance': "à l'occasion des élections locales, des élèves de 4e du lycée municipal d'Attécoubé s'interrogent sur le rôle des élus municipaux et régionaux et sur le financement des collectivités.",
 'taches': ["définir la décentralisation et identifier ses composantes", "décrire l'administration décentralisée et mener une enquête sur son rôle",
            "relever les sources de financement des collectivités territoriales"],
 'prerequis': ["La déconcentration administrative (leçon 1).", "Le vote et la citoyenneté (EDHC)."],
 'seances': [
  {'titre': "Présentation générale de la décentralisation (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation.", "« Que feront les élus municipaux et régionaux ? »"], ["Ils développeront la commune et la région."], "Introduction."),
   ("Développement · I. Présentation générale", 37, "Construction des définitions, tableau comparatif",
    ["Faire définir décentralisation et collectivité territoriale.", "Faire comparer déconcentration et décentralisation ; relever objectifs et étapes."],
    ["Transfert de compétences et de moyens à des collectivités dotées de la personnalité morale et d'un budget, administrées par des élus.", "Nommés / élus ; participation, proximité, développement ; 1980, 2001, 2003, 2014."], "I. 1 à 4."),
   (EVAL, 10, "Travail individuel", ["Activité d'application I."], ["Nommé / élu."], None),
  ]},
  {'titre': "Les composantes (II)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Qui dirige la région et la commune ? »"], ["Le président du conseil régional, le maire."], None),
   ("Développement · II. Les composantes", 40, "Lecture du schéma 1",
    ["Faire identifier les organes délibérants et exécutifs.", "Présenter le statut particulier du district autonome."],
    ["Région : conseil régional, président du conseil régional ; commune : conseil municipal, maire et adjoints ; district : ministre-gouverneur nommé."], "II."),
   (EVAL, 10, "Travail individuel", ["Activité d'application II."], ["Organes de la région et de la commune."], None),
  ]},
  {'titre': "Le rôle des collectivités (III)", 'etapes': [
   (PRES, 5, "Retour sur l'enquête", ["« Qu'a réalisé la mairie dans notre localité ? »"], ["Le marché, l'éclairage, des salles de classe."], None),
   ("Développement · III. Le rôle", 40, "Restitution de l'enquête, classement",
    ["Faire classer les réalisations relevées par domaine de compétence."],
    ["Urbanisme, voirie, assainissement, éducation, santé, hydraulique, action sociale, culture, sports, économie locale, état civil."], "III."),
   (EVAL, 10, "Travail individuel", ["Activité d'application III."], ["Quatre compétences."], None),
  ]},
  {'titre': "Le financement et la tutelle (IV et V)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Avec quel argent la mairie construit-elle ? »"], ["Avec les taxes, l'aide de l'État."], None),
   ("Développement · IV. et V. Financement et tutelle", 35, "Lecture du schéma 2 et d'un budget",
    ["Faire relever les cinq sources de financement.", "Faire expliquer la tutelle et le civisme fiscal."],
    ["Ressources propres, impôts rétrocédés, dotations, emprunts, dons et coopération.", "Contrôle de légalité et du budget par le ministre de l'Intérieur et le préfet ; Cour des comptes."], "IV, V, conclusion."),
   (EVAL, 15, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Organes, rôle, financement, civisme."], None),
  ]},
 ],
 'eclairage': [
  "Collectivité territoriale : personnalité morale, autonomie financière, organes élus.",
  "La région est à la fois circonscription (préfet de région) et collectivité (conseil régional).",
  "Mode de désignation du maire et du président du conseil régional : vérifier les textes électoraux en vigueur.",
  "Rester neutre : ne citer aucun parti ni candidat.",
 ],
 'difficultes': [
  ("Confusion entre préfet de région et président du conseil régional.", "Tableau nommé / élu."),
  ("Confusion entre tutelle et autorité hiérarchique.", "Contrôler n'est pas commander."),
  ("Difficulté à relier taxes et équipements.", "Partir du ticket de marché (schéma 2)."),
 ],
 'soutien': ["Fiche-lexique : collectivité, conseil, maire, tutelle, dotation.", "Schéma 1 vierge à compléter."],
 'approfondissement': ["Interview d'un conseiller municipal.", "Analyse simplifiée du budget de la commune."],
 'evaluation': {
  'activites': [
   ("Définis : décentralisation ; collectivité territoriale.", 2, "Décentralisation : transfert de compétences et de moyens de l'État à des collectivités administrées par des élus (1 pt) ; collectivité : portion du territoire dotée de la personnalité morale et d'un budget propre (1 pt)."),
   ("Nomme l'organe délibérant et l'organe exécutif de la commune et de la région.", 2, "Commune : conseil municipal, maire (1 pt) ; région : conseil régional, président du conseil régional (1 pt)."),
   ("Cite trois compétences transférées aux collectivités.", 1.5, "Voirie, assainissement, écoles, centres de santé, marchés, état civil… 0,5 pt par compétence."),
   ("Cite cinq sources de financement des collectivités.", 2.5, "Ressources propres, impôts rétrocédés, dotations de l'État, emprunts, dons et coopération. 0,5 pt par source."),
  ],
  'situation': "Dans ta commune, des commerçants refusent de payer le ticket de marché en disant que « la mairie ne fait rien ».",
  'consignes': [
   ("Identifie la collectivité concernée et son responsable.", 2, "La commune (1 pt), dirigée par le maire et le conseil municipal (1 pt)."),
   ("Explique le rôle de la commune dans le développement local.", 4, "Elle construit et entretient marchés, écoles, centres de santé (2 pts) ; voirie, éclairage, ordures, état civil (2 pts)."),
   ("Montre aux commerçants l'importance du paiement des taxes locales.", 4, "Les taxes alimentent le budget communal (2 pts) ; elles financent l'entretien du marché et les équipements dont ils profitent : civisme fiscal (2 pts)."),
  ],
 },
 'valeurs': ["Civisme fiscal et participation à la vie locale.", "Sens de l'intérêt général ; neutralité politique.",
             "Liens avec l'EDHC (citoyenneté, élections)."],
}

FICHES['4e-g-t1-l3'] = {
 'materiel': ["schéma des obstacles et des conséquences (schéma 1)", "schéma du cercle vertueux du civisme (schéma 2)",
              "article de presse sur une route dégradée", "tableau comparatif vierge déconcentration / décentralisation"],
 'contexte': "l'état des routes et des équipements révèle les insuffisances de l'organisation administrative dans certaines localités.",
 'circonstance': "les routes du département se dégradent ; des élèves de 4e du collège moderne de Béoumi s'interrogent sur le rôle de la sous-préfecture et du conseil régional et sur les obstacles au fonctionnement de l'administration.",
 'taches': ["définir l'organisation administrative et expliquer son rôle dans le développement", "identifier les obstacles et réaliser un tableau comparatif",
            "proposer des solutions et initier des actions de développement"],
 'prerequis': ["La déconcentration (leçon 1).", "La décentralisation (leçon 2)."],
 'seances': [
  {'titre': "L'organisation administrative et son rôle (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation.", "« Qui doit réparer nos routes ? »"], ["L'État, le conseil régional, la mairie."], "Introduction."),
   ("Développement · I. Organisation et rôle", 37, "Rappel des leçons 1 et 2, tableau comparatif",
    ["Faire définir l'organisation administrative.", "Faire expliquer les rôles et réaliser le tableau comparatif."],
    ["Administration centrale, déconcentrée, décentralisée.", "Nommés / élus ; État / populations ; sans budget propre / autonomie financière ; hiérarchie / tutelle."], "I. 1 à 4."),
   (EVAL, 10, "Travail individuel", ["Activité d'application I."], ["Un rôle de chaque administration."], None),
  ]},
  {'titre': "Les obstacles (II)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Pourquoi les routes restent-elles dégradées ? »"], ["Manque d'argent, mauvaise gestion."], None),
   ("Développement · II. Les obstacles", 40, "Travail de groupes sur documents",
    ["Chaque groupe étudie un type d'obstacle et présente des exemples."],
    ["Financiers, humains et matériels, institutionnels, de gouvernance, liés aux populations."], "II. 1 à 5."),
   (EVAL, 10, "Travail individuel", ["Activité d'application II."], ["Classement des obstacles."], None),
  ]},
  {'titre': "Conséquences et solutions (III et IV)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Quelles conséquences pour nous ? »"], ["Routes impraticables, écoles insuffisantes."], None),
   ("Développement · III. et IV. Conséquences et solutions", 40, "Lecture du schéma 1, propositions",
    ["Faire relier obstacles et conséquences.", "Faire proposer des solutions pour l'État, les collectivités et les citoyens."],
    ["Routes dégradées, équipements insuffisants, projets inachevés, inégalités, méfiance.", "Transfert des moyens, formation, numérisation, lutte contre la corruption ; collecte des taxes ; civisme fiscal."], "III, IV."),
   (EVAL, 10, "Travail individuel", ["Activités d'application III et IV."], ["Conséquences ; solutions à trois niveaux."], None),
  ]},
  {'titre': "Des actions de développement (V)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Que pouvons-nous faire ? »"], ["Sensibiliser, nettoyer, proposer."], None),
   ("Développement · V. Actions de développement", 35, "Lecture du schéma 2, atelier",
    ["Faire expliquer le cercle vertueux.", "Faire concevoir des slogans et un projet de club de développement."],
    ["Civisme → budget → équipements → développement → confiance.", "Journées de salubrité, slogans, enquête, club de développement."], "V, conclusion."),
   (EVAL, 15, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Rôle, obstacles, solutions, actions."], None),
  ]},
 ],
 'eclairage': [
  "Cinq familles d'obstacles : financiers, humains et matériels, institutionnels, de gouvernance, liés aux populations.",
  "Le transfert des compétences a été plus rapide que le transfert des ressources.",
  "La Haute Autorité pour la Bonne Gouvernance (2013) et la Cour des comptes contrôlent l'usage des fonds publics.",
  "Évoquer la corruption sans mettre en cause de personne ni d'institution précise.",
 ],
 'difficultes': [
  ("Confusion entre obstacle et conséquence.", "Tableau cause / effet."),
  ("Tendance à tout attribuer à l'État.", "Schéma 2 et rôle des citoyens."),
  ("Solutions trop vagues.", "Grille acteur – action – résultat."),
 ],
 'soutien': ["Fiche-lexique : gouvernance, corruption, incivisme fiscal, disparités.", "Tableau comparatif à compléter."],
 'approfondissement': ["Enquête sur un projet inachevé de la localité.", "Projet de budget participatif simulé en classe."],
 'evaluation': {
  'activites': [
   ("Définis : organisation administrative.", 1, "Ensemble des structures, règles et personnes par lesquelles l'État et les collectivités administrent le territoire (1 pt)."),
   ("Complète le tableau : responsables et relation avec l'État de l'administration déconcentrée et de l'administration décentralisée.", 2, "Déconcentrée : nommés, autorité hiérarchique (1 pt) ; décentralisée : élus, tutelle (1 pt)."),
   ("Cite trois obstacles au fonctionnement de l'administration.", 1.5, "Ressources faibles, manque de personnel, chevauchement des compétences, corruption, incivisme fiscal. 0,5 pt par obstacle."),
   ("Donne deux conséquences de ces obstacles sur le développement.", 2, "Routes dégradées, équipements insuffisants, projets inachevés, inégalités régionales. 1 pt par conséquence."),
   ("Propose une solution au niveau de l'État et une au niveau des citoyens.", 1.5, "État : transférer les moyens, lutter contre la corruption (0,75 pt) ; citoyens : payer ses taxes, respecter les biens publics (0,75 pt)."),
  ],
  'situation': "Dans ta localité, le centre de santé construit par le conseil régional est inachevé depuis trois ans et les habitants accusent l'administration de ne rien faire.",
  'consignes': [
   ("Identifie la structure responsable du projet et le type d'administration auquel elle appartient.", 2, "Le conseil régional (1 pt) ; l'administration décentralisée (1 pt)."),
   ("Explique deux obstacles qui peuvent expliquer l'inachèvement du projet.", 4, "Manque de ressources ou retard des dotations (2 pts) ; mauvaise gestion, manque de personnel ou incivisme fiscal (2 pts)."),
   ("Propose deux actions que les habitants et les élèves peuvent mener.", 4, "Payer les taxes, participer aux réunions et suivre le projet, sensibiliser, proposer un comité de suivi (2 pts par action, 2 attendues)."),
  ],
 },
 'valeurs': ["Civisme fiscal, intégrité et sens de l'intérêt général.", "Participation citoyenne et responsabilité partagée.",
             "Liens avec l'EDHC (bonne gouvernance, citoyenneté)."],
}

FICHES['4e-g-t2-l1'] = {
 'materiel': ["carte de l'espace CEDEAO (carte 1)", "organigramme des institutions (schéma 1)",
              "tableau statistique des États membres (population, productions)", "extrait du protocole de 1979 sur la libre circulation"],
 'contexte': "la CEDEAO intervient dans l'économie, la paix et la démocratie en Afrique de l'Ouest.",
 'circonstance': "des élèves de 4e du lycée Sainte-Marie de Cocody apprennent à la télévision l'implication de la CEDEAO dans le conflit malien et veulent comprendre son espace, ses potentialités et son fonctionnement.",
 'taches': ["définir la CEDEAO, localiser son espace et identifier ses potentialités", "expliquer et schématiser le fonctionnement de ses institutions et sa politique d'intégration",
            "apprécier ses actions et initier des actions en faveur de l'intégration"],
 'prerequis': ["La carte politique de l'Afrique (6e).", "L'organisation administrative de la Côte d'Ivoire (thème 1)."],
 'seances': [
  {'titre': "Présentation et potentialités (I et II)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation.", "« Pourquoi la CEDEAO s'occupe-t-elle d'un conflit ? »"], ["Pour ramener la paix entre ses membres."], "Introduction."),
   ("Développement · I. et II. Présentation et potentialités", 37, "Lecture de la carte 1 et d'un tableau statistique",
    ["Faire définir la CEDEAO et retracer l'évolution des membres.", "Faire identifier les potentialités par pays."],
    ["Organisation d'intégration créée à Lagos en 1975 ; 12 membres depuis janvier 2025 ; Commission à Abuja.", "Population, cacao (Côte d'Ivoire), pétrole (Nigeria), or (Ghana), bauxite (Guinée), phosphates (Togo), ports."], "I, II."),
   (EVAL, 10, "Travail individuel", ["Activités d'application I et II."], ["Création ; potentialités."], None),
  ]},
  {'titre': "Les institutions (III)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Qui décide à la CEDEAO ? »"], ["Les présidents."], None),
   ("Développement · III. Les institutions", 40, "Lecture d'un tableau, construction du schéma 1",
    ["Faire relever objectifs et principes.", "Faire construire le schéma des institutions."],
    ["Libre circulation, union économique et monétaire, paix ; égalité, solidarité, démocratie.", "Conférence (décide), Conseil des ministres (prépare), Commission (exécute), Parlement, Cour de justice, BIDC."], "III."),
   (EVAL, 10, "Travail individuel", ["Activité d'application III."], ["Organe suprême ; rôle de la Commission."], None),
  ]},
  {'titre': "Politique d'intégration et succès (IV et V)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Comment la CEDEAO rapproche-t-elle ses membres ? »"], ["Par la libre circulation."], None),
   ("Développement · IV. et V. Intégration et succès", 40, "Étude de documents, étude de cas",
    ["Faire expliquer libre circulation, TEC, Eco, paix, infrastructures.", "Étudier le cas de la Gambie (2017)."],
    ["Protocole de 1979, TEC de 2015, Eco reporté, mécanisme de 1999, corridor Abidjan – Lagos.", "ECOMOG au Libéria et en Sierra Leone ; Gambie 2017."], "IV, V."),
   (EVAL, 10, "Travail individuel", ["Activités d'application IV et V."], ["Protocole de 1979 ; succès pour la paix."], None),
  ]},
  {'titre': "Limites et actions pour l'intégration (VI et VII)", 'etapes': [
   (PRES, 5, "Question-problème", ["« La CEDEAO a-t-elle réussi ? »"], ["Oui et non."], None),
   ("Développement · VI. et VII. Limites et actions", 35, "Débat argumenté, propositions",
    ["Organiser un débat succès / limites.", "Faire proposer des actions d'élèves."],
    ["Instabilité, retrait de l'AES, faibles échanges, tracasseries, retard de l'Eco, insécurité.", "Accueil, langues, consommation locale, échanges, refus de la xénophobie."], "VI, VII, conclusion."),
   (EVAL, 15, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Institutions, succès, limites, actions."], None),
  ]},
 ],
 'eclairage': [
  "12 États membres depuis le retrait du Mali, du Burkina Faso et du Niger (janvier 2025).",
  "Ne pas confondre la CEDEAO (Abuja, 12 membres) et l'UEMOA (Ouagadougou, franc CFA).",
  "Présidences en novembre 2026 (site officiel) : Bassirou Diomaye Faye (Conférence), général Birame Diop (Commission) ; à revérifier, elles changent régulièrement.",
  "Traiter l'actualité (AES, coups d'État) avec neutralité.",
 ],
 'difficultes': [
  ("Confusion entre CEDEAO et UEMOA.", "Tableau comparatif membres, monnaie, sièges."),
  ("Confusion entre Conférence et Commission.", "Schéma 1 : décider / exécuter."),
  ("Difficulté à localiser les États membres.", "Carte 1 muette à compléter."),
 ],
 'soutien': ["Fiche-lexique : intégration, libre circulation, TEC, monnaie unique.", "Carte muette de l'Afrique de l'Ouest."],
 'approfondissement': ["Exposé sur le corridor Abidjan – Lagos.", "Comparaison CEDEAO – UEMOA."],
 'evaluation': {
  'activites': [
   ("Définis : CEDEAO.", 1, "Communauté économique des États de l'Afrique de l'Ouest, organisation régionale d'intégration créée en 1975 (1 pt)."),
   ("Donne la date et le lieu de création de la CEDEAO et le siège de sa Commission.", 1.5, "28 mai 1975 (0,5 pt), Lagos (0,5 pt) ; Abuja (0,5 pt)."),
   ("Cite trois potentialités économiques de la CEDEAO avec un pays pour chacune.", 1.5, "Cacao (Côte d'Ivoire), pétrole (Nigeria), bauxite (Guinée), or (Ghana), phosphates (Togo). 0,5 pt par couple."),
   ("Indique le rôle de la Conférence des chefs d'État et de la Commission.", 2, "Conférence : organe suprême qui décide (1 pt) ; Commission : organe exécutif qui met en œuvre (1 pt)."),
   ("Cite deux succès et deux limites de la CEDEAO.", 2, "Succès : libre circulation, TEC, ECOMOG, Gambie 2017 ; limites : instabilité, faibles échanges, tracasseries, retard de l'Eco. 0,5 pt par élément."),
  ],
  'situation': "Ton oncle, transporteur entre Abidjan et Accra, se plaint des contrôles routiers et affirme que « la CEDEAO ne sert à rien ».",
  'consignes': [
   ("Identifie le texte de la CEDEAO qui garantit la libre circulation des personnes.", 2, "Le protocole de 1979 sur la libre circulation (2 pts)."),
   ("Montre que la CEDEAO a obtenu des succès.", 4, "Libre circulation sans visa (1 pt), TEC (1 pt), maintien de la paix : ECOMOG, Gambie (1 pt), infrastructures : corridor Abidjan – Lagos (1 pt)."),
   ("Explique deux limites qui justifient en partie la plainte de ton oncle et propose une solution.", 4, "Tracasseries aux frontières, faibles échanges ou instabilité (2 pts) ; dénoncer les rackets, appliquer les protocoles, sensibiliser les agents (2 pts)."),
  ],
 },
 'valeurs': ["Solidarité africaine et refus de la xénophobie.", "Paix et respect de la démocratie.",
             "Liens avec l'anglais (communication avec les pays voisins) et l'EDHC."],
}

FICHES['4e-g-t2-l2'] = {
 'materiel': ["carte de l'Union européenne et de la zone euro (carte 1)", "graphique de l'évolution du nombre de membres (graphique 1)",
              "tableau des institutions de l'UE", "données statistiques (population, PIB, commerce)"],
 'contexte': "l'Union européenne est le regroupement régional le plus intégré du monde, mais elle traverse aussi des crises.",
 'circonstance': "des élèves de 4e du lycée moderne de Bondoukou apprennent au journal télévisé que des pays de l'UE connaissent une crise financière et veulent comprendre la construction et le fonctionnement de l'UE.",
 'taches': ["définir l'UE et localiser son espace", "décrire la construction européenne et identifier ses potentialités",
            "schématiser son fonctionnement et apprécier les politiques communes"],
 'prerequis': ["La CEDEAO (leçon précédente).", "La Révolution industrielle en Europe (histoire)."],
 'seances': [
  {'titre': "Définition et espace de l'UE (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation.", "« Qu'est-ce que l'UE ? »"], ["Une union de pays européens."], "Introduction."),
   ("Développement · I. Définition et espace", 37, "Lecture de la carte 1",
    ["Faire définir l'UE.", "Faire localiser les 27 membres et distinguer la zone euro."],
    ["Union économique et politique d'États qui partagent une partie de leur souveraineté.", "27 membres, environ 450 millions d'habitants, 21 pays de la zone euro, espace Schengen."], "I."),
   (EVAL, 10, "Travail individuel", ["Activité d'application I."], ["27 membres ; 21 pays de la zone euro."], None),
  ]},
  {'titre': "La construction européenne (II)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Comment est-on passé de 6 à 27 ? »"], ["Par des élargissements."], None),
   ("Développement · II. La construction", 40, "Tableau des étapes, lecture du graphique 1",
    ["Faire relever les raisons et les étapes.", "Faire lire le graphique 1."],
    ["Paix, reconstruction, poids face aux grandes puissances.", "CECA 1951, Rome 1957, Maastricht 1992, euro 1999 – 2002, 2004, Brexit 2020."], "II."),
   (EVAL, 10, "Travail individuel", ["Activité d'application II."], ["Ordre chronologique."], None),
  ]},
  {'titre': "Potentialités et fonctionnement (III et IV)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Quelles sont les forces de l'UE ? Qui décide ? »"], ["Industrie, agriculture ; Bruxelles."], None),
   ("Développement · III. et IV. Potentialités et fonctionnement", 40, "Exploitation de données, schéma",
    ["Faire identifier les potentialités à partir de données.", "Faire schématiser le fonctionnement des institutions."],
    ["Grand marché, agriculture moderne, industries, services, ports.", "Conseil européen oriente ; Commission propose ; Parlement et Conseil de l'UE votent ; Commission exécute ; Cour de justice, BCE."], "III, IV."),
   (EVAL, 10, "Travail individuel", ["Activités d'application III et IV."], ["Potentialités ; qui propose, qui vote."], None),
  ]},
  {'titre': "Politiques communes, résultats et limites (V)", 'etapes': [
   (PRES, 5, "Retour à la situation", ["« Pourquoi parle-t-on de crise ? »"], ["Des pays sont endettés."], None),
   ("Développement · V. Politiques communes", 35, "Tableau, débat, comparaison avec la CEDEAO",
    ["Faire relever les politiques communes.", "Faire apprécier résultats et limites ; comparer avec la CEDEAO."],
    ["PAC, marché unique, Schengen, euro, politique régionale, Erasmus.", "Paix, niveau de vie ; Brexit, dette, désaccords, dépendance énergétique."], "V, conclusion."),
   (EVAL, 15, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Construction, institutions, politiques, comparaison."], None),
  ]},
 ],
 'eclairage': [
  "27 membres depuis le Brexit (2020) ; 21 pays de la zone euro depuis l'entrée de la Bulgarie (1er janvier 2026).",
  "Ne pas confondre Conseil européen, Conseil de l'UE et Conseil de l'Europe.",
  "La « crise financière » de la situation renvoie surtout à la crise de la dette de la zone euro (Grèce, à partir de 2010).",
  "Accord de partenariat économique Côte d'Ivoire – UE appliqué depuis 2016.",
 ],
 'difficultes': [
  ("Confusion entre Europe et Union européenne.", "Carte 1 : pays non membres."),
  ("Confusion entre les trois « conseils ».", "Tableau comparatif."),
  ("Difficulté à retenir les étapes.", "Graphique 1 et frise à compléter."),
 ],
 'soutien': ["Fiche-lexique : marché unique, zone euro, élargissement, Brexit.", "Carte muette de l'Europe."],
 'approfondissement': ["Exposé sur le programme Erasmus.", "Tableau comparatif UE – CEDEAO."],
 'evaluation': {
  'activites': [
   ("Définis : Union européenne.", 1, "Union économique et politique d'États européens qui partagent une partie de leur souveraineté (1 pt)."),
   ("Range dans l'ordre chronologique : euro ; CECA ; Brexit ; traités de Rome ; traité de Maastricht.", 2.5, "CECA (1951) → traités de Rome (1957) → Maastricht (1992) → euro (1999 – 2002) → Brexit (2020). 0,5 pt par position exacte."),
   ("Indique le nombre d'États membres et de pays de la zone euro en 2026.", 1, "27 membres (0,5 pt) ; 21 pays de la zone euro (0,5 pt)."),
   ("Indique quelle institution propose les lois et lesquelles les votent.", 1.5, "La Commission propose (0,5 pt) ; le Parlement européen et le Conseil de l'UE votent (1 pt)."),
   ("Cite deux politiques communes de l'UE.", 2, "PAC, marché unique, Schengen, euro, politique régionale, Erasmus. 1 pt par politique."),
  ],
  'situation': "Lors d'un débat, un camarade affirme que la CEDEAO devrait copier exactement l'Union européenne pour réussir.",
  'consignes': [
   ("Identifie deux étapes de la construction européenne.", 2, "CECA (1951), traités de Rome (1957), Maastricht (1992), euro (1999 – 2002)… 1 pt par étape."),
   ("Montre que l'UE est un exemple d'intégration réussie.", 4, "Paix entre membres (1 pt), marché unique et euro (1 pt), politiques communes : PAC, politique régionale (1 pt), élévation du niveau de vie (1 pt)."),
   ("Explique pourquoi la CEDEAO ne peut pas copier exactement l'UE.", 4, "Limites de l'UE elle-même : Brexit, crises (1 pt) ; différences de développement, faibles échanges, instabilité en Afrique de l'Ouest (2 pts) ; s'inspirer en adaptant (1 pt)."),
  ],
 },
 'valeurs': ["Paix, solidarité et coopération entre les peuples.", "Esprit critique face aux modèles étrangers.",
             "Liens avec l'histoire (guerres mondiales, Révolution industrielle) et l'anglais."],
}
