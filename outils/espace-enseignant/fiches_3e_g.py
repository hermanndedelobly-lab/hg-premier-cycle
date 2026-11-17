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

# ------------------------------------------------------------------ T1-L3
FICHES['3e-g-t1-l3'] = {
 'materiel': ["schéma du cercle vicieux (schéma 1)", "graphique du recul de la forêt (graphique 1)", "affiche de sensibilisation au dépistage du VIH",
              "extrait d'un plan national de développement", "ticket de caisse montrant la TVA"],
 'contexte': "des élèves de 3e 4 du collège Ségbé, à Yopougon, constatent que la Côte d'Ivoire est une grande puissance économique d'Afrique de l'Ouest.",
 'circonstance': "pourtant, le panier de la ménagère est vide, l'accès aux soins est difficile et les revendications sociales augmentent : ils veulent comprendre ce paradoxe.",
 'taches': ["identifier et caractériser les problèmes de développement économique", "identifier les problèmes de santé publique liés au VIH/sida et montrer l'importance de la fiscalité",
            "proposer des solutions aux problèmes économiques"],
 'prerequis': ["Les atouts et les secteurs d'activités (leçons précédentes).", "La notion de PIB.", "Les notions de santé publique (SVT)."],
 'seances': [
  {'titre': "Les problèmes structurels (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation et du schéma 1",
    ["Lire la situation ; « Comment un pays riche peut-il avoir des habitants pauvres ? »", "Lire le schéma 1."], ["Les richesses sont mal réparties ; l'économie dépend des produits bruts."], "Introduction."),
   ("Développement · I. Problèmes structurels", 35, "Étude de documents, lecture du graphique 1",
    ["Faire définir le problème structurel ; faire relever les problèmes.", "Faire lire le graphique 1 (recul de la forêt)."],
    ["Dépendance aux produits bruts, industrie insuffisante, informel, chômage des jeunes, pauvreté, endettement, mauvaise gouvernance, infrastructures inégales.",
     "La forêt dense est passée d'environ 16 à environ 3 millions d'hectares en un siècle (ordres de grandeur)."], "I. 1 à 8."),
   (EVAL, 12, "Travail individuel", ["Activité d'application I."], ["Définitions et trois problèmes structurels."], None),
  ]},
  {'titre': "Problèmes conjoncturels et VIH/sida (II, III)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Qu'est-ce qui peut faire reculer l'économie d'une année à l'autre ? »"], ["Une crise, une épidémie, la chute des prix."], None),
   ("Développement · II et III. Conjoncture et VIH/sida", 38, "Exposé dialogué, étude d'une affiche",
    ["Faire relever les problèmes conjoncturels.", "Expliquer le lien entre VIH/sida et développement ; présenter les réponses."],
    ["Prix mondiaux, vie chère, crises de 1999 – 2011, Covid-19, aléas climatiques, insécurité au nord.",
     "Perte de main-d'œuvre, dépenses de santé, orphelins ; dépistage et traitements gratuits, prévention, lutte contre la stigmatisation."], "II et III."),
   (EVAL, 12, "Travail individuel", ["Activités d'application II et III."], ["Deux problèmes conjoncturels ; VIH et développement."], None),
  ]},
  {'titre': "L'importance de la fiscalité (IV)", 'etapes': [
   (PRES, 5, "Lecture d'un ticket de caisse", ["« Que représente la ligne TVA ? »"], ["Une taxe payée à l'État."], None),
   ("Développement · IV. La fiscalité", 35, "Explication, tableau impôts directs / indirects",
    ["Faire classer des impôts en directs et indirects.", "Faire expliquer ce que financent les impôts ; parler de civisme fiscal."],
    ["Directs : sur les salaires, les bénéfices, le foncier, la patente ; indirects : TVA (18 %), droits de douane, taxes sur les carburants.",
     "Les impôts financent écoles, hôpitaux, routes, salaires ; ils réduisent l'endettement ; l'informel et la fraude privent l'État de ressources."], "IV."),
   (EVAL, 15, "Travail individuel", ["Activité d'application IV."], ["Rôle de la fiscalité."], None),
  ]},
  {'titre': "Les solutions et l'évaluation (V)", 'etapes': [
   (PRES, 5, "Retour au schéma 1", ["« Comment briser le cercle vicieux ? »"], ["Transformer, former, bien gérer."], None),
   ("Développement · V. Les solutions", 25, "Travail de groupes : une solution par problème",
    ["Chaque groupe propose une solution à un problème et la justifie.", "Mise en commun et trace écrite."],
    ["Transformation locale, formation et emploi des jeunes, bonne gouvernance, CMU et filets sociaux, plans de développement, civisme fiscal, protection de l'environnement."], "V, conclusion."),
   (EVAL, 25, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Problèmes, fiscalité, solutions."], None),
  ]},
 ],
 'eclairage': [
  "Croissance n'est pas développement : la croissance mesure la production, le développement les conditions de vie (IDH).",
  "Les données sur la forêt varient selon la définition (forêt dense ou totale) et la méthode ; le graphique 1 donne des ordres de grandeur à vérifier.",
  "La prévalence du VIH chez les adultes est estimée autour de 2 % par l'ONUSIDA ; la donnée change chaque année.",
  "L'élargissement de l'assiette fiscale au secteur informel est un objectif majeur des plans nationaux de développement.",
 ],
 'difficultes': [
  ("Confusion entre problème structurel et conjoncturel.", "Critère de durée ; exemples à classer."),
  ("Vision de l'impôt comme une simple contrainte.", "Ce que l'impôt finance concrètement."),
  ("Préjugés sur le VIH/sida.", "Informations scientifiques ; refus de la stigmatisation."),
 ],
 'soutien': ["Liste de problèmes à classer en structurels et conjoncturels.", "Schéma 1 à compléter avec des étiquettes."],
 'approfondissement': ["Enquête : que finance le budget de l'État ? (loi de finances simplifiée)", "Exposé sur la déforestation et le cacao."],
 'evaluation': {
  'activites': [
   ("Définis : problème structurel ; fiscalité.", 2, "Problème structurel : difficulté durable liée à l'organisation de l'économie (1 pt) ; fiscalité : ensemble des impôts et taxes prélevés par l'État et les collectivités (1 pt)."),
   ("Classe en structurels ou conjoncturels : Covid-19 ; poids de l'informel ; chute des cours du cacao ; chômage des jeunes.", 2, "Structurels : poids de l'informel, chômage des jeunes ; conjoncturels : Covid-19, chute des cours du cacao. 0,5 pt par élément."),
   ("Explique pourquoi le VIH/sida est un problème de développement.", 2, "Il touche les adultes actifs : moins de main-d'œuvre (1 pt) ; il augmente les dépenses de santé et laisse des orphelins (1 pt)."),
   ("Cite deux impôts, un direct et un indirect.", 2, "Direct : impôt sur les salaires, sur les bénéfices ou foncier (1 pt) ; indirect : TVA ou droits de douane (1 pt)."),
  ],
  'situation': "Un commerçant du marché d'Adjamé refuse de déclarer son activité : « Les impôts ne servent à rien, l'État est assez riche avec le cacao. »",
  'consignes': [
   ("Cite deux problèmes structurels de l'économie ivoirienne.", 2, "La dépendance aux matières premières brutes (1 pt) ; le poids de l'informel ou le chômage des jeunes (1 pt)."),
   ("Explique pourquoi le cacao ne suffit pas à financer l'État.", 4, "Ses prix varient sur les marchés mondiaux et il est exporté brut, avec une faible valeur ajoutée (2 pts) ; l'État a besoin de ressources régulières, comme les impôts, pour financer les services publics (2 pts)."),
   ("Montre au commerçant l'importance de la fiscalité.", 4, "Les impôts financent les écoles, les hôpitaux et les routes, dont le commerçant profite (2 pts) ; s'ils sont bien collectés, ils réduisent l'endettement et la dépendance du pays (2 pts)."),
  ],
 },
 'valeurs': ["Civisme fiscal et refus de la corruption.", "Solidarité, lutte contre la stigmatisation des malades, protection de l'environnement.",
             "Liens avec l'EDHC (citoyenneté), les SVT (VIH, forêt) et les mathématiques (pourcentages)."],
}

# ------------------------------------------------------------------ T2-L1
FICHES['3e-g-t2-l1'] = {
 'materiel': ["carte des ressources de l'Afrique (carte 1)", "courbe de la population de l'Afrique (graphique 1)", "carte politique de l'Afrique",
              "tableau de la production de cacao des principaux pays producteurs", "papier millimétré"],
 'contexte': "des élèves de 3e 5 du lycée de Korhogo écoutent la radio ONUCI-FM.",
 'circonstance': "ils apprennent que la majorité des pays d'Afrique sont pauvres et endettés et veulent en connaître les raisons et les solutions.",
 'taches': ["identifier les atouts naturels et humains de l'Afrique", "caractériser les secteurs d'activités et construire des graphiques",
            "analyser les problèmes de développement et proposer des solutions"],
 'prerequis': ["L'étude économique de la Côte d'Ivoire (thème 1).", "La carte politique de l'Afrique.", "La construction d'un graphique (barres, courbe)."],
 'seances': [
  {'titre': "Les atouts naturels et humains (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation ; « L'Afrique est-elle pauvre en ressources ? »"], ["Non : elle a du pétrole, de l'or, du cacao…"], "Introduction."),
   ("Développement · I. Les atouts", 35, "Lecture de la carte 1 et du graphique 1",
    ["Faire relever les ressources et les pays producteurs sur la carte 1.", "Faire lire le graphique 1 et calculer le coefficient multiplicateur."],
    ["Pétrole et gaz (Nigeria, Angola, Algérie), or (Afrique du Sud, Ghana, Mali), cobalt et cuivre (RD Congo, Zambie), diamants, bauxite, uranium, phosphates ; terres cultivables.",
     "Environ 230 millions d'habitants en 1950 et 1,5 milliard aujourd'hui : multipliée par plus de six ; population la plus jeune du monde."], "I. 1 et 2."),
   (EVAL, 12, "Travail individuel", ["Activité d'application I."], ["Trois atouts naturels, un atout humain."], None),
  ]},
  {'titre': "Les secteurs d'activités et les graphiques (II)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Que deviennent les ressources africaines ? »"], ["Elles sont souvent exportées brutes."], None),
   ("Développement · II. Les secteurs d'activités", 38, "Exposé dialogué, construction d'un graphique",
    ["Faire caractériser les trois secteurs.", "Faire construire un diagramme en barres de la production de cacao à partir d'un tableau."],
    ["Primaire dominant (agriculture traditionnelle, cultures d'exportation) ; secondaire faible, dominé par les mines ; tertiaire en croissance mais informel.",
     "Diagramme en barres : axe gradué, une barre par pays, titre, légende, source."], "II. 1 à 4."),
   (EVAL, 12, "Travail individuel", ["Activité d'application II."], ["Caractéristiques des trois secteurs."], None),
  ]},
  {'titre': "Les problèmes de développement (III)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Pourquoi un continent riche a-t-il des populations pauvres ? »"], ["Produits exportés bruts, conflits, corruption…"], None),
   ("Développement · III. Les problèmes", 35, "Travail de groupes, tableau de synthèse",
    ["Chaque groupe étudie une famille de problèmes (économiques, politiques, sociaux, environnementaux).", "Mise en commun dans un tableau."],
    ["Économies extraverties, faible commerce intra-africain (environ 15 %), infrastructures insuffisantes, dette.",
     "Instabilité, terrorisme, corruption ; pauvreté, chômage, fuite des cerveaux ; désertification, déforestation, changement climatique."], "III. 1 à 4."),
   (EVAL, 15, "Travail individuel", ["Activité d'application III."], ["Deux problèmes expliqués."], None),
  ]},
  {'titre': "Les solutions et l'évaluation (IV)", 'etapes': [
   (PRES, 5, "Retour à la situation", ["« Que peuvent faire les Africains pour se développer ? »"], ["Transformer, s'unir, former, bien gérer."], None),
   ("Développement · IV. Les solutions", 25, "Exposé dialogué",
    ["Distinguer les solutions continentales et nationales.", "Relier chaque solution à un problème."],
    ["Continentales : Agenda 2063, ZLECAf, infrastructures, BAD ; nationales : transformation locale, agriculture modernisée, éducation, bonne gouvernance, paix, énergies renouvelables."], "IV, conclusion."),
   (EVAL, 25, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Atouts, problèmes, solutions."], None),
  ]},
 ],
 'eclairage': [
  "Les ordres de grandeur du graphique 1 (230, 420, 820 et 1 520 millions d'habitants) sont arrondis à partir de l'ONU (World Population Prospects) ; ils restent à vérifier.",
  "L'ONU compte 54 États africains ; l'Union africaine en compte 55 avec la République arabe sahraouie démocratique.",
  "Le commerce intra-africain représente environ 15 % du commerce des pays africains (CNUCED).",
  "La RD Congo fournit la majorité du cobalt mondial, indispensable aux batteries.",
 ],
 'difficultes': [
  ("Idée d'une Afrique pauvre en ressources.", "Carte 1."),
  ("Explication de la pauvreté par une seule cause.", "Tableau des quatre familles de problèmes."),
  ("Erreurs de construction des graphiques.", "Grille de vérification : titre, échelle, légende, source."),
 ],
 'soutien': ["Carte muette de l'Afrique à compléter avec cinq ressources.", "Tableau problèmes / solutions à relier."],
 'approfondissement': ["Exposé sur un pays africain qui réussit (Botswana, Rwanda, Maroc).", "Recherche sur le cobalt et les batteries."],
 'evaluation': {
  'activites': [
   ("Définis : économie extravertie ; commerce intra-africain.", 2, "Économie extravertie : tournée vers l'exportation de produits bruts et dépendante de l'extérieur (1 pt) ; commerce intra-africain : échanges entre pays africains (1 pt)."),
   ("Associe chaque ressource à un pays producteur : cobalt ; pétrole ; phosphates ; cacao.", 2, "RD Congo ; Nigeria (ou Angola, Algérie) ; Maroc ; Côte d'Ivoire (ou Ghana). 0,5 pt par association."),
   ("Calcule par combien la population de l'Afrique a été multipliée entre 1950 (230 millions) et 2025 (1 520 millions).", 2, "1 520 ÷ 230 ≈ 6,6 (1 pt pour le calcul, 1 pt pour le résultat et la phrase)."),
   ("Cite deux problèmes économiques du développement de l'Afrique.", 2, "Économies extraverties, dépendantes des prix mondiaux (1 pt) ; faible commerce intra-africain ou infrastructures insuffisantes (1 pt)."),
  ],
  'situation': "Ton cousin pense que « l'Afrique est pauvre parce qu'elle n'a pas de richesses ».",
  'consignes': [
   ("Cite trois richesses naturelles de l'Afrique et un pays producteur pour chacune.", 2, "Pétrole (Nigeria), or (Afrique du Sud ou Ghana), cobalt (RD Congo) ; on accepte d'autres associations justes (0,5 pt chacune, 0,5 pt pour la présentation)."),
   ("Explique deux raisons de la pauvreté de nombreux pays africains.", 4, "Les ressources sont exportées brutes, avec peu de valeur ajoutée (2 pts) ; l'instabilité politique, la corruption ou le manque d'infrastructures freinent le développement (2 pts)."),
   ("Propose deux solutions pour que l'Afrique profite mieux de ses richesses.", 4, "Transformer les matières premières sur place (2 pts) ; développer le commerce entre pays africains grâce à la ZLECAf (ou former la jeunesse, bonne gouvernance) (2 pts)."),
  ],
 },
 'valeurs': ["Fierté africaine et esprit d'initiative.", "Solidarité et intégration entre les peuples africains ; gestion responsable des ressources.",
             "Liens avec l'histoire (UA, colonisation), les mathématiques (graphiques) et l'EDHC (bonne gouvernance)."],
}

# ------------------------------------------------------------------ T2-L2
FICHES['3e-g-t2-l2'] = {
 'materiel': ["carte des échanges de l'Afrique (carte 1)", "graphique du poids de l'Afrique dans le monde (graphique 1)", "planisphère",
              "étiquettes de produits courants indiquant leur pays d'origine", "tableau des principaux partenaires commerciaux de l'Afrique"],
 'contexte': "des élèves de 3e 2 suivent à la télévision un sommet du G8, où aucun État africain n'est présent.",
 'circonstance': "surpris, ils s'interrogent sur la place de l'Afrique dans les échanges mondiaux et décident de mener des recherches sur la mondialisation.",
 'taches': ["définir la mondialisation, identifier ses facteurs et décrire son fonctionnement", "apprécier la place de l'Afrique dans les échanges et construire des graphiques",
            "expliquer les opportunités et proposer des solutions pour améliorer la place de l'Afrique"],
 'prerequis': ["L'étude économique de l'Afrique (leçon précédente).", "La lecture d'un planisphère.", "La construction d'un diagramme."],
 'seances': [
  {'titre': "Définition et facteurs de la mondialisation (I)", 'etapes': [
   (PRES, 8, "Observation d'objets du quotidien",
    ["Faire lire l'origine de quelques produits (téléphone, vêtement, riz).", "« Pourquoi ces produits viennent-ils de si loin ? »"], ["Parce que les pays échangent dans le monde entier."], "Introduction."),
   ("Développement · I. Définition et facteurs", 35, "Exposé dialogué",
    ["Faire définir la mondialisation.", "Faire relever les facteurs."],
    ["Intégration de toutes les régions du monde dans un espace unique d'échanges.",
     "Facteurs : Grandes Découvertes, révolution industrielle, transports (conteneurs), NTIC, OMC (1995), fin de la guerre froide (1991)."], "I. 1 et 2."),
   (EVAL, 12, "Travail individuel", ["Activité d'application I."], ["Définition et trois facteurs."], None),
  ]},
  {'titre': "Le fonctionnement de la mondialisation (II)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Qui organise les échanges mondiaux ? »"], ["Les États, les entreprises, les organisations internationales."], None),
   ("Développement · II. Le fonctionnement", 38, "Lecture d'un planisphère, tableau acteurs – flux – espaces",
    ["Faire classer acteurs, flux et espaces.", "Faire localiser les pôles dominants et les espaces en marge."],
    ["Acteurs : États, firmes multinationales, OMC, FMI, Banque mondiale, regroupements régionaux, ONG.",
     "Flux : marchandises, capitaux, informations, personnes ; pôles : Amérique du Nord, Europe, Asie orientale ; émergents ; marges."], "II. 1 à 3."),
   (EVAL, 12, "Travail individuel", ["Activité d'application II."], ["Trois acteurs, trois pôles."], None),
  ]},
  {'titre': "La place de l'Afrique dans les échanges (III)", 'etapes': [
   (PRES, 5, "Retour à la situation", ["« Pourquoi aucun État africain n'était-il au G8 ? »"], ["Parce que leur poids économique est faible."], None),
   ("Développement · III. La place de l'Afrique", 38, "Lecture de la carte 1 et du graphique 1, construction d'un graphique",
    ["Faire relever ce que l'Afrique exporte et importe, et ses partenaires.", "Faire construire un diagramme à partir d'un tableau (partenaires ou part des continents)."],
    ["Environ 3 % du commerce mondial pour près d'un habitant sur cinq ; exportations de matières premières, importations de produits manufacturés ; UE, Chine, États-Unis, Inde.",
     "Diagramme avec titre, légende, source."], "III. 1 à 5."),
   (EVAL, 12, "Travail individuel", ["Activité d'application III."], ["Place marginale, échange inégal."], None),
  ]},
  {'titre': "Opportunités, solutions et évaluation (IV, V)", 'etapes': [
   (PRES, 5, "Question-problème", ["« La mondialisation peut-elle aider l'Afrique ? »"], ["Oui, si elle transforme ses produits et s'unit."], None),
   ("Développement · IV et V. Opportunités et solutions", 25, "Tableau à deux colonnes",
    ["Faire relever les opportunités.", "Faire proposer des solutions et les justifier."],
    ["Nouveaux partenaires, investissements, mobile et Internet, diaspora, UA au G20.",
     "Transformer sur place, ZLECAf, infrastructures, formation, bonne gouvernance, parler d'une seule voix."], "IV, V, conclusion."),
   (EVAL, 25, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Place de l'Afrique, opportunités, solutions."], None),
  ]},
 ],
 'eclairage': [
  "Le G8 (G7 + Russie) n'existe plus depuis 2014 ; l'Afrique du Sud et, depuis 2023, l'Union africaine sont membres du G20.",
  "La part de l'Afrique dans le commerce mondial se situe autour de 2 à 3 % selon les années et les sources (OMC, CNUCED).",
  "La Chine est devenue, dans les années 2000, l'un des premiers partenaires commerciaux du continent.",
  "Ngozi Okonjo-Iweala (Nigeria) dirige l'OMC depuis 2021 : première femme et première Africaine à ce poste.",
 ],
 'difficultes': [
  ("Confusion entre G7, G8 et G20.", "Tableau comparatif."),
  ("Idée que l'Afrique est hors de la mondialisation.", "Carte 1 : elle y participe, en position dépendante."),
  ("Confusion entre acteurs et flux.", "Exemples à classer."),
 ],
 'soutien': ["Planisphère à compléter (pôles, Afrique, flèches).", "Liste de mots à classer : acteurs, flux, espaces."],
 'approfondissement': ["Enquête : d'où viennent les produits du marché le plus proche ?", "Exposé sur la ZLECAf ou sur les relations Chine – Afrique."],
 'evaluation': {
  'activites': [
   ("Définis : mondialisation ; firme multinationale.", 2, "Mondialisation : intégration de toutes les régions du monde dans un espace unique d'échanges (1 pt) ; firme multinationale : entreprise qui a des filiales dans plusieurs pays (1 pt)."),
   ("Cite trois facteurs de la mondialisation.", 1.5, "Révolution des transports, NTIC, libéralisation des échanges (OMC) ou fin de la guerre froide. 0,5 pt par facteur."),
   ("Cite les trois pôles dominants de la mondialisation.", 1.5, "Amérique du Nord, Europe occidentale, Asie orientale. 0,5 pt par pôle."),
   ("Explique pourquoi on parle d'échange inégal pour l'Afrique.", 3, "Elle exporte surtout des matières premières, aux prix bas et variables (1,5 pt) ; elle importe des produits manufacturés plus chers, ce qui la rend dépendante (1,5 pt)."),
  ],
  'situation': "Un camarade affirme : « La mondialisation, ce n'est que pour les pays riches ; l'Afrique n'a rien à y gagner. »",
  'consignes': [
   ("Indique la place de l'Afrique dans le commerce mondial.", 2, "Environ 3 % des échanges mondiaux (1 pt) pour près d'un habitant sur cinq de la planète (1 pt)."),
   ("Montre que la mondialisation offre des opportunités à l'Afrique.", 4, "Nouveaux partenaires et investissements (Chine, Inde) (2 pts) ; diffusion du téléphone mobile, d'Internet et du paiement mobile, ou entrée de l'UA au G20 (2 pts)."),
   ("Propose deux solutions pour améliorer la place de l'Afrique et réponds à ton camarade.", 4, "Transformer sur place les matières premières (1,5 pt) ; développer le commerce intra-africain grâce à la ZLECAf (1,5 pt) ; conclusion : l'Afrique peut y gagner si elle change sa place (1 pt)."),
  ],
 },
 'valeurs': ["Ouverture au monde et esprit critique face à la consommation.", "Solidarité africaine et fierté de produire et transformer localement.",
             "Liens avec l'histoire (colonisation, ONU, UA), les mathématiques (graphiques) et l'anglais (vocabulaire du commerce)."],
}
