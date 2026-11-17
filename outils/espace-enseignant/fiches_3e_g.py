# Fiches enseignant — Géographie 3e (lot 4 de la généralisation du modèle validé)
# Même format que fiches_g.py : étape = (moment, durée en min, stratégie, [activités du professeur],
# [réponses attendues des élèves], trace écrite)

PRES = "Présentation"
EVAL = "Évaluation"

FICHES = {}

# ------------------------------------------------------------------ T1-L1
FICHES['3e-g-t1-l1'] = {
 'materiel': ["croquis des atouts naturels (carte 1)", "schéma des atouts au développement (schéma 1)", "fond de carte de la Côte d'Ivoire (un par élève)",
              "tableau des résultats du RGPH 2021", "photographie du barrage de Soubré ou du port de San-Pédro"],
 'contexte': "des élèves de 3e 5 du collège moderne de Toupa regardent sur RTI 1 un documentaire sur l'économie ivoirienne.",
 'circonstance': "ils apprennent que la Côte d'Ivoire a l'une des économies les plus solides d'Afrique de l'Ouest et veulent en connaître les fondements.",
 'taches': ["identifier les atouts naturels et humains de la Côte d'Ivoire", "schématiser les milieux climatiques et expliquer l'importance des atouts et des migrations",
            "analyser le rôle des atouts dans le développement économique"],
 'prerequis': ["Les climats et la végétation de la Côte d'Ivoire (6e).", "La population de la Côte d'Ivoire (5e).", "La lecture d'une carte et d'un tableau statistique."],
 'seances': [
  {'titre': "Les atouts naturels (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation, lecture du schéma 1",
    ["Lire la situation ; « Sur quoi repose une économie solide ? »", "Faire lire rapidement le schéma 1."], ["Sur des ressources, une population au travail et de bons choix."], "Introduction."),
   ("Développement · I. Les atouts naturels", 35, "Lecture de la carte 1, schématisation sur fond de carte",
    ["Faire relever la situation, le relief, les climats, les sols, les eaux, les mines et l'énergie.", "Faire schématiser les quatre milieux climatiques sur un fond de carte."],
    ["Golfe de Guinée, 322 462 km², environ 520 km de côte ; relief peu accidenté ; climats attiéen, baouléen, soudanais, de montagne.",
     "Sols ferrallitiques ; Cavally, Sassandra, Bandama, Comoé ; barrages ; or, manganèse, pétrole et gaz (Baleine) ; ports d'Abidjan et de San-Pédro."], "I. 1 à 5."),
   (EVAL, 12, "Travail individuel", ["Activité d'application I."], ["Quatre atouts naturels, importance de l'un d'eux."], None),
  ]},
  {'titre': "Les atouts humains (II)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Les habitants sont-ils une richesse pour un pays ? »"], ["Oui, s'ils travaillent et sont formés."], None),
   ("Développement · II. Les atouts humains", 38, "Lecture d'un tableau statistique, explication",
    ["Faire lire les résultats du RGPH 2021.", "Expliquer le rôle des migrations internes, de l'immigration et de l'exode rural."],
    ["29 389 150 habitants, 75,6 % de moins de 35 ans : main-d'œuvre abondante, grand marché ; universités et grandes écoles.",
     "Migrations internes vers la zone forestière ; immigrants du Burkina Faso, du Mali, de Guinée dans les plantations ; 52,5 % de citadins."], "II. 1 à 4."),
   (EVAL, 12, "Travail individuel", ["Activité d'application II."], ["La population, atout pour l'économie."], None),
  ]},
  {'titre': "L'analyse des atouts dans le développement (III)", 'etapes': [
   (PRES, 5, "Rappel", ["« Avoir des atouts suffit-il pour se développer ? »"], ["Non, il faut les valoriser."], None),
   ("Développement · III. L'analyse des atouts", 30, "Débat dirigé à partir du schéma 1",
    ["Faire relier chaque atout à une activité économique.", "Montrer le rôle des choix politiques (miracle ivoirien, crises de 1999 – 2011)."],
    ["Agriculture d'exportation, hydroélectricité, ports, industries extractives, villes et services.",
     "Libéralisme et ouverture ont permis le « miracle ivoirien » ; les crises ont fait reculer l'économie malgré les mêmes atouts."], "III, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Atouts naturels et humains, choix politiques."], None),
  ]},
 ],
 'eclairage': [
  "Le RGPH 2021 compte 29 389 150 habitants ; 75,6 % ont moins de 35 ans ; 52,5 % vivent en ville (INS).",
  "Le gisement Baleine, découvert en 2021, est en production depuis août 2023 ; il relance l'activité pétrolière et gazière.",
  "Le barrage de Soubré (2017), sur le Sassandra, est le plus puissant du pays.",
  "La Côte d'Ivoire est premier producteur mondial de cacao et de noix de cajou brute, premier producteur africain de caoutchouc naturel.",
 ],
 'difficultes': [
  ("Confusion entre les climats.", "Croquis : attiéen au sud, baouléen au centre, soudanais au nord, montagne à l'ouest."),
  ("Confusion entre ressource et atout.", "Une ressource devient un atout lorsqu'elle est valorisée."),
  ("Vision négative de l'immigration.", "Rôle des migrants dans l'économie de plantation."),
 ],
 'soutien': ["Fond de carte avec les zones déjà tracées, à légender.", "Tableau atouts naturels / atouts humains à compléter."],
 'approfondissement': ["Exposé sur le gisement Baleine ou sur un barrage hydroélectrique.", "Comparer les atouts de la Côte d'Ivoire et du Ghana."],
 'evaluation': {
  'activites': [
   ("Définis : atout ; hydroélectricité.", 2, "Atout : avantage qui favorise le développement d'un pays (1 pt) ; hydroélectricité : électricité produite par la force de l'eau retenue par un barrage (1 pt)."),
   ("Cite trois atouts naturels de la Côte d'Ivoire.", 1.5, "Trois parmi : situation sur le golfe de Guinée, relief peu accidenté, climats variés, sols fertiles, fleuves et barrages, or, pétrole et gaz. 0,5 pt par atout."),
   ("Associe chaque climat à sa région : attiéen ; baouléen ; soudanais ; de montagne.", 2, "Sud ; centre ; nord ; ouest. 0,5 pt par association."),
   ("Explique le rôle des migrations dans l'économie ivoirienne.", 2.5, "Les migrants, venus du nord, du centre et des pays voisins, ont fourni la main-d'œuvre des plantations de cacao et de café (1,5 pt) ; ils participent aussi au commerce et au transport (1 pt)."),
  ],
  'situation': "Ton oncle affirme que la Côte d'Ivoire est riche « uniquement grâce à son sol et à son climat ».",
  'consignes': [
   ("Cite deux atouts naturels et deux atouts humains de la Côte d'Ivoire.", 2, "Naturels : climats variés, sols fertiles (ou ports, fleuves, mines) (1 pt) ; humains : population jeune et nombreuse, main-d'œuvre formée (ou migrations) (1 pt)."),
   ("Explique l'importance de deux de ces atouts pour l'économie.", 4, "Les climats et les sols permettent l'agriculture d'exportation (cacao, café, anacarde) (2 pts) ; la population jeune fournit la main-d'œuvre et un grand marché (2 pts)."),
   ("Montre à ton oncle que les atouts naturels ne suffisent pas.", 4, "Il faut des hommes pour mettre en valeur ces ressources, comme les migrants et les planteurs (2 pts) ; il faut aussi de bons choix politiques et la paix : pendant les crises de 1999 – 2011, l'économie a reculé (2 pts)."),
  ],
 },
 'valeurs': ["Amour du travail et goût de l'entreprise.", "Hospitalité et cohésion sociale ; protection des ressources naturelles.",
             "Liens avec l'histoire (économie coloniale), les SVT (sols, climats) et l'EDHC (citoyenneté)."],
}

# ------------------------------------------------------------------ T1-L2
FICHES['3e-g-t1-l2'] = {
 'materiel': ["diagramme circulaire de la part des secteurs (graphique 1)", "croquis des activités économiques (carte 1)", "rapporteur, compas et crayons de couleur",
              "tableau des principales productions agricoles", "photographies du port d'Abidjan et d'une usine de transformation du cacao"],
 'contexte': "des élèves de 3e 5 du lycée moderne de Treichville écoutent « Le journal de l'économie » à la radio.",
 'circonstance': "ils apprennent que le primaire ne représente qu'environ un quart du PIB, derrière le tertiaire ; certains contestent, car pour eux l'agriculture est la base de l'économie.",
 'taches': ["identifier et caractériser les secteurs d'activités", "représenter la part de chaque secteur et montrer sa place dans l'économie",
            "identifier les problèmes de chaque secteur et apprécier les progrès réalisés"],
 'prerequis': ["Les atouts du développement économique (leçon précédente).", "Le calcul d'un pourcentage (mathématiques).", "La lecture d'une carte de la Côte d'Ivoire."],
 'seances': [
  {'titre': "Les secteurs et leur place dans l'économie (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation et débat",
    ["Lire la situation ; « L'agriculture est-elle la base de l'économie ivoirienne ? » ; noter les arguments."], ["Oui pour certains (emploi, cacao) ; non pour d'autres (part du PIB)."], "Introduction."),
   ("Développement · I. Les secteurs et leur place", 35, "Exposé dialogué, lecture du graphique 1",
    ["Faire définir les trois secteurs et le PIB.", "Faire lire le graphique 1 et classer les secteurs selon leur part."],
    ["Primaire : nature ; secondaire : transformation ; tertiaire : services ; PIB : richesses produites en un an.",
     "2025 : primaire 16,8 % ; secondaire 23,9 % ; services marchands 43,8 % ; le tertiaire est le premier secteur."], "I. 1 à 3."),
   (EVAL, 12, "Travail individuel", ["Activité d'application I (calcul des angles)."], ["60° ; 86° ; 158° ; 56°."], None),
  ]},
  {'titre': "Représenter la part des secteurs (I. 4)", 'etapes': [
   (PRES, 5, "Rappel de méthode", ["« Combien de degrés représente 1 % ? »"], ["3,6°."], None),
   ("Développement · Construction du diagramme circulaire", 40, "Travail individuel guidé",
    ["Faire tracer un cercle et reporter les angles au rapporteur.", "Faire colorier, légender, titrer et indiquer la source."],
    ["Cercle de 4 cm de rayon ; secteurs de 60°, 86°, 158° et 56° ; légende ; titre ; source."], "I. 4."),
   (EVAL, 10, "Correction collective", ["Comparer les diagrammes au graphique 1."], ["Somme des angles égale à 360°."], None),
  ]},
  {'titre': "Le secteur primaire (II)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Pourquoi le cacao est-il si important pour la Côte d'Ivoire ? »"], ["Premier producteur mondial, exportations, emplois."], None),
   ("Développement · II. Le secteur primaire", 38, "Lecture de la carte 1 et d'un tableau de productions",
    ["Faire localiser les zones agricoles.", "Faire distinguer cultures d'exportation et vivrières ; relever les problèmes."],
    ["Cacao (environ 40 % de la production mondiale), anacarde (premier mondial), café, hévéa, palmier, coton ; vivrier : igname, manioc, riz.",
     "Problèmes : vergers vieillis, swollen shoot, déforestation, prix mondiaux, faible mécanisation."], "II. 1 à 3."),
   (EVAL, 12, "Travail individuel", ["Activité d'application II."], ["Emploi et exportations."], None),
  ]},
  {'titre': "Les secteurs secondaire et tertiaire (III, IV)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Que deviennent les fèves de cacao après la récolte ? »"], ["Elles sont exportées ou transformées en usine."], None),
   ("Développement · III et IV. Secondaire et tertiaire", 38, "Étude de photographies, tableau",
    ["Faire relever les branches du secondaire et leur localisation.", "Faire relever les activités du tertiaire ; problèmes de chaque secteur."],
    ["Agro-industrie, mines et pétrole, énergie, BTP ; surtout à Abidjan, puis San-Pédro.",
     "Commerce, transports (ports, chemin de fer), télécommunications, paiement mobile, banques, BRVM ; poids de l'informel."], "III et IV."),
   (EVAL, 12, "Travail individuel", ["Activités d'application III et IV."], ["Trois branches ; moteur de la croissance."], None),
  ]},
  {'titre': "Les progrès réalisés et l'évaluation (V)", 'etapes': [
   (PRES, 5, "Retour au débat initial", ["« Qui avait raison dans la classe ? »"], ["Les deux camps, chacun en partie."], None),
   ("Développement · V. Les progrès", 25, "Tableau de synthèse",
    ["Faire compléter un tableau des progrès par secteur.", "Conclure le débat."],
    ["Primaire : hausse de l'anacarde et du caoutchouc ; secondaire : transformation locale, or, pétrole et gaz, électricité ; tertiaire : infrastructures, numérique, finance."], "V, conclusion."),
   (EVAL, 25, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Place et problèmes des secteurs."], None),
  ]},
 ],
 'eclairage': [
  "Les parts du PIB en 2025 (16,8 % ; 23,9 % ; 43,8 %) sont attribuées à la Direction générale de l'économie ; elles n'ont pas encore été confirmées automatiquement.",
  "Le primaire pèse peu dans le PIB mais reste le premier employeur et la principale source de devises.",
  "Le programme range les mines dans le secondaire (industries extractives) ; d'autres classifications les placent dans le primaire.",
  "La Côte d'Ivoire est l'un des premiers broyeurs mondiaux de cacao, mais la plus grande partie de la valeur du chocolat reste réalisée à l'étranger.",
 ],
 'difficultes': [
  ("Erreurs dans la construction du diagramme.", "Vérifier la somme des angles (360°) ; démonstration au tableau."),
  ("Confusion entre part du PIB et part de l'emploi.", "Comparer deux tableaux (PIB / emploi)."),
  ("Classement des mines ou du BTP.", "Rappeler la convention du programme : secondaire."),
 ],
 'soutien': ["Diagramme pré-tracé à colorier et légender.", "Liste d'activités à classer dans les trois secteurs."],
 'approfondissement': ["Exposé sur la filière cacao, de la plantation au chocolat.", "Comparer la structure du PIB de la Côte d'Ivoire et du Ghana."],
 'evaluation': {
  'activites': [
   ("Définis : secteur primaire ; PIB.", 2, "Secteur primaire : activités qui tirent leur production de la nature (agriculture, élevage, pêche, forêt) (1 pt) ; PIB : valeur des richesses produites dans un pays en un an (1 pt)."),
   ("Classe dans leur secteur : cacaoculture ; BTP ; banque ; pêche ; raffinage du pétrole ; téléphonie mobile.", 1.5, "Primaire : cacaoculture, pêche ; secondaire : BTP, raffinage ; tertiaire : banque, téléphonie mobile. 0,25 pt par activité."),
   ("Calcule l'angle correspondant à 23,9 % dans un diagramme circulaire.", 1.5, "23,9 × 3,6 ≈ 86° (1 pt pour le calcul, 0,5 pt pour le résultat)."),
   ("Cite un problème du secteur primaire et un problème du secteur secondaire.", 3, "Primaire : vieillissement des vergers, swollen shoot ou dépendance aux prix mondiaux (1,5 pt) ; secondaire : faible transformation locale, coût de l'énergie ou concentration à Abidjan (1,5 pt)."),
  ],
  'situation': "Pendant un exposé, un camarade affirme : « En Côte d'Ivoire, seule l'agriculture compte ; l'industrie et les services ne servent à rien. »",
  'consignes': [
   ("Indique la part de chaque secteur dans le PIB en 2025.", 2, "Primaire 16,8 % ; secondaire 23,9 % ; services marchands 43,8 % ; le reste : administration et taxes (0,5 pt par donnée)."),
   ("Montre l'importance du secteur primaire.", 4, "Il emploie une grande partie des actifs (2 pts) et fournit l'essentiel des exportations, comme le cacao dont le pays est premier producteur mondial (2 pts)."),
   ("Réponds à ton camarade en montrant le rôle des autres secteurs.", 4, "Le secondaire transforme les produits et crée des emplois industriels (agro-industrie, énergie, BTP) (2 pts) ; le tertiaire produit la plus grande part des richesses (commerce, transports, banques, télécommunications) (2 pts)."),
  ],
 },
 'valeurs': ["Valorisation du travail agricole et de l'esprit d'entreprise.", "Consommer local et soutenir la transformation des produits.",
             "Liens avec les mathématiques (pourcentages, angles), les SVT (cacaoyer) et l'EDHC (civisme fiscal)."],
}
