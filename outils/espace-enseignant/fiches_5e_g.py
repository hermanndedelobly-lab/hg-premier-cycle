# Fiches enseignant — Géographie 5e (lot 2 de la généralisation du modèle validé)
# Même format que fiches_h.py : étape = (moment, durée en min, stratégie, [activités du professeur],
# [réponses attendues des élèves], trace écrite)

PRES = "Présentation"
EVAL = "Évaluation"

FICHES = {}

# ------------------------------------------------------------------ T1-L1
FICHES['5e-g-t1-l1'] = {
 'materiel': ["carte du milieu physique (carte 1)", "croquis des zones de peuplement (carte 2) et carte des densités de l'INS ou du manuel",
              "résultats du RGPH 2021 (population nationale et régionale)", "calculatrice"],
 'contexte': "au cours d'une discussion en classe, des élèves de 5e du Collège moderne d'Adjamé apprennent que certaines parties du pays sont presque vides et d'autres très peuplées.",
 'circonstance': "un groupe pense que de telles différences de densité sont impossibles ; la classe se rend à l'Institut national de la statistique (INS) pour consulter des cartes et des documents.",
 'taches': ["définir le milieu physique et la densité ; décrire le milieu physique ivoirien", "localiser les zones de peuplement, lire une carte de population et effectuer des calculs",
            "établir les relations entre l'installation des hommes et le milieu naturel"],
 'prerequis': ["Le relief, le climat, les sols et la végétation de la Côte d'Ivoire (6e).", "La notion de densité de population (6e).", "La lecture d'une carte : titre, légende, orientation, échelle (6e)."],
 'seances': [
  {'titre': "Définitions et milieu physique (I et II)", 'etapes': [
   (PRES, 8, "Lecture de la situation et recueil des hypothèses",
    ["Lire la situation (élèves d'Adjamé, visite à l'INS).", "« Pourquoi certaines régions sont-elles presque vides et d'autres très peuplées ? »"],
    ["Hypothèses : le climat, l'eau, les villes, le travail."], "Introduction."),
   ("Développement · I. Définitions", 12, "Questionnement et calcul guidé",
    ["Faire définir le milieu physique à partir des leçons de 6e.", "Faire définir et calculer une densité simple."],
    ["Milieu physique : situation, relief, climat, cours d'eau, sols, végétation.", "Densité = population ÷ superficie ; 1 200 000 ÷ 15 000 = 80 hab./km²."], "I. 1 et 2."),
   ("Développement · II. Le milieu physique", 25, "Exploitation de la carte 1",
    ["Faire situer le pays et donner sa superficie.", "Faire décrire le relief, nommer les fleuves d'ouest en est, repérer la limite forêt – savane."],
    ["322 462 km², environ 520 km de côte ; plaines et plateaux, montagnes à l'ouest (mont Nimba, 1 752 m).", "Cavally, Sassandra, Bandama, Comoé ; forêt au sud, savane au nord, V baoulé au centre."], "II. 1 à 4."),
   (EVAL, 10, "Travail individuel", ["Activités d'application I et II."], ["Calcul de densité ; fleuves et point culminant."], None),
  ]},
  {'titre': "La répartition de la population : localiser, lire, calculer (III)", 'etapes': [
   (PRES, 5, "Rappel et question", ["« Où vivent les Ivoiriens ? »"], ["À Abidjan, dans les villes, dans le Sud."], None),
   ("Développement · III. 1 à 3. La répartition", 20, "Calcul et exploitation de la carte 2",
    ["Faire calculer la densité nationale à partir du RGPH 2021.", "Faire localiser les zones fortement et faiblement peuplées."],
    ["29 389 150 ÷ 322 462 ≈ 91 hab./km².", "Fortes densités : Abidjan et le littoral, Centre-Ouest, grandes villes ; faibles : Nord-Est, savanes du Nord-Ouest, parcs."], "III. 1 à 3."),
   ("Développement · III. 4 et 5. Lire une carte, calculer", 20, "Lecture guidée d'une carte des densités, calculs en binômes",
    ["Faire lire titre et légende d'une carte des densités ; repérer zones foncées et claires.", "Faire calculer des densités et des parts en pourcentage."],
    ["Couleurs foncées = fortes densités ; claires = faibles densités.", "Part = population de la région ÷ population totale × 100."], "III. 4 et 5."),
   (EVAL, 10, "Travail individuel", ["Activité d'application III."], ["Zones de peuplement et calcul."], None),
  ]},
  {'titre': "Les relations entre l'installation des hommes et le milieu (IV)", 'etapes': [
   (PRES, 5, "Comparaison des cartes 1 et 2", ["« Que remarquez-vous en comparant les deux cartes ? »"], ["Les zones peuplées sont surtout en forêt et sur le littoral."], None),
   ("Développement · IV. Les relations homme – milieu", 30, "Travail de groupes puis mise en commun",
    ["Chaque groupe explique une zone (Sud littoral, Centre-Ouest, Ouest montagneux, Nord-Est) par un facteur naturel et un facteur humain."],
    ["Milieux favorables : climat humide, sols fertiles, littoral ; milieux répulsifs : longue saison sèche, sols pauvres, marécages, aires protégées.",
     "Autres facteurs : histoire, économie (port, emplois, routes), aménagement."], "IV. 1 à 3, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Réinvestissent densité, répartition et explications."], None),
  ]},
 ],
 'eclairage': [
  "La densité est une moyenne qui lisse les contrastes : toujours la compléter par une carte.",
  "La répartition résulte de facteurs naturels, historiques et économiques : éviter le déterminisme naturel.",
  "Le peuplement du Centre-Ouest et du Sud-Ouest s'est fortement accru au XXe siècle avec l'économie de plantation ; Abidjan regroupe environ un cinquième de la population.",
  "Les recensements de l'INS (1975, 1988, 1998, 2014, 2021) sont la source officielle ; RGPH 2021 : 29 389 150 habitants.",
 ],
 'difficultes': [
  ("Division inversée dans le calcul de la densité.", "Rappeler l'unité habitants par km² : les habitants au numérateur ; refaire trois calculs guidés."),
  ("Confusion entre population et densité.", "Comparer une petite région très peuplée et une grande région peu dense."),
  ("Explication uniquement par le milieu naturel.", "Exiger un facteur naturel et un facteur humain pour chaque zone."),
 ],
 'soutien': ["Fiche-méthode du calcul de la densité avec un exemple résolu.", "Carte 2 à colorier avec une légende déjà faite."],
 'approfondissement': ["Calculer la densité de la région de l'établissement à partir du RGPH 2021 et la comparer à la moyenne nationale.", "Exposé sur un parc national ivoirien."],
 'evaluation': {
  'activites': [
   ("Définis : milieu physique ; densité de population.", 2, "Milieu physique : ensemble des éléments naturels d'un espace (situation, relief, climat, cours d'eau, sols, végétation) (1 pt) ; densité : nombre moyen d'habitants par km² (1 pt)."),
   ("Calcule la densité de la Côte d'Ivoire en 2021 (29 389 150 habitants, 322 462 km²).", 2, "29 389 150 ÷ 322 462 ≈ 91 hab./km² (opération 1 pt, résultat et unité 1 pt)."),
   ("Cite les quatre grands fleuves de Côte d'Ivoire d'ouest en est.", 2, "Cavally, Sassandra, Bandama, Comoé. 0,5 pt par fleuve bien placé."),
   ("Région A : 1 500 000 habitants sur 6 000 km² ; région B : 270 000 habitants sur 21 000 km² (données d'exercice). Calcule les deux densités.", 2, "A : 250 hab./km² (1 pt) ; B : environ 12,9 hab./km² (1 pt)."),
  ],
  'situation': "Un camarade affirme que les habitants se sont installés au hasard sur le territoire ivoirien et que la nature n'y est pour rien.",
  'consignes': [
   ("Définis la densité de population et cite une zone fortement peuplée et une zone faiblement peuplée.", 3, "Nombre moyen d'habitants par km² (1 pt) ; fortement peuplée : district d'Abidjan ou Centre-Ouest (1 pt) ; faiblement peuplée : Nord-Est (Bounkani) ou parc national (1 pt)."),
   ("Explique par deux facteurs naturels cette inégale répartition.", 4, "Au sud, climat humide et sols fertiles favorables à l'agriculture (2 pts) ; au nord-est, longue saison sèche et sols pauvres (2 pts)."),
   ("Montre à ton camarade qu'il existe aussi des facteurs humains.", 3, "Le port, les emplois et les routes attirent la population à Abidjan ; les migrations et l'économie de plantation ont peuplé le Centre-Ouest (1,5 pt par facteur, 2 attendus)."),
  ],
 },
 'valeurs': ["Connaissance et respect du territoire national.", "Protection des aires protégées.",
             "Liens avec les mathématiques (calculs, pourcentages) et les SVT (milieux naturels)."],
}

# ------------------------------------------------------------------ T1-L2
FICHES['5e-g-t1-l2'] = {
 'materiel': ["tableau des recensements (INS)", "papier millimétré, règle, crayons de couleur", "tableau officiel de la population par âge et par sexe (INS)",
              "photographies d'une forêt défrichée et d'un quartier précaire", "calculatrice"],
 'contexte': "des élèves de 5e du Collège moderne de Toupa suivent, au foyer de l'établissement, l'allocution de la ministre de la Famille pour la Journée mondiale de la population.",
 'circonstance': "ils apprennent que le rythme de croissance de la population ivoirienne est l'un des plus élevés du monde et s'en inquiètent.",
 'taches': ["définir la démographie et décrire la croissance et la structure de la population", "construire une courbe et une pyramide des âges ; effectuer des calculs",
            "identifier les facteurs, expliquer les conséquences sur le milieu et mener des actions de gestion de l'environnement"],
 'prerequis': ["La densité et la répartition de la population (leçon 1).", "La construction d'un graphique simple (6e).", "Le calcul d'un pourcentage (mathématiques)."],
 'seances': [
  {'titre': "Démographie, recensement et croissance (I, II. 1 et 2)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation (Journée mondiale de la population).", "« La population augmente-t-elle vraiment très vite ? Comment le savoir ? »"],
    ["En comptant la population à plusieurs dates : les recensements."], "Introduction."),
   ("Développement · I. Démographie et recensement", 12, "Questionnement",
    ["Faire définir la démographie et le recensement ; présenter l'INS et l'utilité du recensement."],
    ["Démographie : science des populations ; recensement : dénombrement complet ; utile pour prévoir écoles, santé, emplois, logements."], "I. 1 et 2."),
   ("Développement · II. 1 et 2. L'évolution de la population", 25, "Lecture d'un tableau et calculs",
    ["Faire lire le tableau des recensements.", "Faire calculer augmentations et facteur de multiplication."],
    ["6,7 millions en 1975, 29,4 millions en 2021 ; multipliée par 4,4 ; environ 3 % par an."], "II. 1 et 2."),
   (EVAL, 10, "Travail individuel", ["Activités d'application I et II."], ["Définition du recensement ; calcul d'augmentation."], None),
  ]},
  {'titre': "Construire la courbe et calculer (II. 3 et 4)", 'etapes': [
   (PRES, 5, "Rappel", ["Faire rappeler les chiffres des recensements."], ["Les cinq recensements et leurs populations."], None),
   ("Développement · II. 3 et 4. Courbe et calculs", 40, "Construction individuelle sur papier millimétré, exercices de calcul",
    ["Faire construire la courbe en respectant les intervalles entre années.", "Faire calculer un pourcentage d'augmentation et un taux d'accroissement naturel."],
    ["Courbe croissante avec titre et source ; intervalles de 13, 10, 16 et 7 ans.", "(29 389 150 − 22 671 331) ÷ 22 671 331 × 100 ≈ 29,6 % ; 35 ‰ − 10 ‰ = 25 ‰."], "II. 3 et 4."),
   (EVAL, 10, "Correction collective", ["Correction de la courbe avec le graphique 1 ; calcul de contrôle."], ["Courbes corrigées."], None),
  ]},
  {'titre': "Facteurs de la croissance et structure de la population (III et IV)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Pourquoi la population augmente-t-elle si vite ? »"], ["Beaucoup de naissances, moins de décès, arrivée de migrants."], None),
   ("Développement · III et IV. Facteurs et structure", 40, "Travail de groupes ; lecture et construction d'une pyramide",
    ["Chaque groupe explique un facteur (natalité, mortalité, immigration).", "Faire décrire puis construire une pyramide des âges à partir des données officielles."],
    ["Forte natalité ; baisse de la mortalité ; immigration (environ un habitant sur cinq de nationalité étrangère en 2021).",
     "Population jeune (75,6 % de moins de 35 ans) ; pyramide à base large et sommet étroit ; hommes à gauche, femmes à droite."], "III, IV."),
   (EVAL, 10, "Travail individuel", ["Activités d'application III et IV."], ["Facteurs ; description de la pyramide."], None),
  ]},
  {'titre': "Conséquences sur le milieu et actions (V et VI)", 'etapes': [
   (PRES, 5, "Observation de photographies", ["Montrer une forêt défrichée et un quartier précaire : « Quel lien avec la croissance de la population ? »"], ["Plus d'habitants, plus de terres et de maisons."], None),
   ("Développement · V et VI. Conséquences et actions", 30, "Chaîne de causes au tableau, propositions d'actions",
    ["Faire construire la chaîne : plus d'habitants → plus de terres, de bois, d'eau → déforestation, pollution, sols appauvris.", "Faire proposer des actions et un projet de classe."],
    ["Déforestation, biodiversité menacée, quartiers précaires, déchets, besoins en bois et en eau, jachères réduites.",
     "Planification familiale, reboisement, agriculture intensive, gestion des déchets, foyers améliorés, club environnement."], "V, VI, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Réinvestissent facteurs, conséquences et actions."], None),
  ]},
 ],
 'eclairage': [
  "La Côte d'Ivoire est dans la phase de transition démographique où la mortalité a baissé avant la natalité, d'où une croissance rapide.",
  "Croissance moyenne d'environ 3 % par an entre 1975 et 2021, calculée à partir des recensements ; éviter de comparer les taux d'une période à l'autre.",
  "L'immigration, liée à l'économie de plantation, est un facteur ancien ; selon le RGPH 2021, environ un habitant sur cinq est de nationalité étrangère.",
  "Selon l'INS (RGPH 2021) : 75,6 % de moins de 35 ans, 52,5 % d'urbains.",
 ],
 'difficultes': [
  ("Axe des années mal gradué (intervalles égaux entre recensements).", "Graduer l'axe tous les 5 ans, puis placer chaque année à sa place exacte."),
  ("Confusion entre ‰ et %.", "Exercices de conversion (25 ‰ = 2,5 %)."),
  ("Pyramide inversée ou sans légende.", "Convention hommes à gauche, femmes à droite ; liste de vérification."),
 ],
 'soutien': ["Repère gradué fourni pour la courbe.", "Pyramide à compléter : barres déjà tracées pour la moitié des tranches."],
 'approfondissement': ["Calculer le temps de doublement avec la règle de 70.", "Comparer la pyramide ivoirienne et celle d'un pays vieillissant."],
 'evaluation': {
  'activites': [
   ("Définis : démographie ; recensement.", 2, "Démographie : science qui étudie les populations humaines (effectif, structure, évolution) (1 pt) ; recensement : dénombrement complet de la population à une date donnée (1 pt)."),
   ("Calcule le pourcentage d'augmentation de la population entre 2014 (22 671 331) et 2021 (29 389 150).", 2, "(29 389 150 − 22 671 331) ÷ 22 671 331 × 100 ≈ 29,6 % (opération 1 pt, résultat 1 pt)."),
   ("Dans une région, le taux de natalité est de 35 ‰ et le taux de mortalité de 10 ‰ (données d'exercice). Calcule le taux d'accroissement naturel et exprime-le en %.", 2, "35 − 10 = 25 ‰ (1 pt), soit 2,5 % (1 pt)."),
   ("Cite les trois facteurs de la croissance démographique ivoirienne.", 2, "Forte natalité, baisse de la mortalité, immigration (0,5 pt chacun ; 0,5 pt si les trois sont exacts)."),
  ],
  'situation': "Dans ton village, la forêt a presque disparu en vingt ans et les familles cherchent de nouvelles terres. Ton oncle pense que « c'est la faute du climat ».",
  'consignes': [
   ("Définis la démographie et décris la forme de la pyramide des âges ivoirienne.", 3, "Science des populations humaines (1 pt) ; base large et sommet étroit (1 pt) : population jeune (1 pt)."),
   ("Explique à ton oncle le lien entre la croissance de la population et la disparition de la forêt.", 4, "La population augmente vite (1 pt) ; il faut plus de terres à cultiver, de bois et d'espace pour construire (2 pts) ; la forêt est donc défrichée et les jachères réduites (1 pt)."),
   ("Propose deux actions pour une gestion rationnelle de l'environnement.", 3, "Reboiser les terres dégradées ; pratiquer une agriculture plus productive sur moins d'espace ; utiliser des foyers améliorés ; planification familiale (1,5 pt par action, 2 attendues)."),
  ],
 },
 'valeurs': ["Responsabilité envers l'environnement et les générations futures.", "Santé et éducation des filles.",
             "Liens avec les mathématiques (pourcentages, graphiques), les SVT et l'EDHC."],
}

# ------------------------------------------------------------------ T1-L3
FICHES['5e-g-t1-l3'] = {
 'materiel': ["carte des ressources en eau (carte 1)", "rapporteur, compas, crayons de couleur", "document sur la pollution de la lagune Ébrié ou sur l'orpaillage",
              "verre doseur et montre (mesure d'une fuite)", "papier et feutres pour les affiches"],
 'contexte': "après une visite des sanitaires du Lycée municipal d'Attécoubé, le proviseur constate que beaucoup de robinets restent ouverts.",
 'circonstance': "il réunit les élèves et leur recommande une utilisation rationnelle de l'eau, « source de vie et de développement » ; des élèves de 5e décident de faire des recherches.",
 'taches': ["identifier et localiser les ressources en eau", "expliquer l'importance de l'eau ; construire un diagramme et effectuer des calculs",
            "identifier les problèmes liés à l'eau ; produire des supports et proposer des actions de gestion rationnelle"],
 'prerequis': ["Le cycle de l'eau (6e).", "Le relief et l'hydrographie (leçon 1).", "La mesure d'un angle au rapporteur (mathématiques)."],
 'seances': [
  {'titre': "Les ressources en eau et leurs usages (I, II. 1 et 2)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation d'Attécoubé.", "« L'eau est-elle vraiment source de vie et de développement ? »"], ["On en a besoin pour boire, se laver, cultiver, produire de l'électricité."], "Introduction."),
   ("Développement · I. Les ressources en eau", 25, "Exploitation de la carte 1",
    ["Faire classer les ressources (marines, de surface, souterraines).", "Faire localiser fleuves, lagunes, lacs de barrage et ports ; rappeler le régime des cours d'eau."],
    ["Océan Atlantique ; Comoé, Bandama, Cavally, Sassandra ; lagunes Ébrié, Aby, Grand-Lahou ; lacs Kossou, Taabo, Buyo, Soubré, Ayamé ; nappes.", "Hautes eaux en saison des pluies, basses eaux en saison sèche."], "I. 1 à 4."),
   ("Développement · II. 1 et 2. L'importance de l'eau", 12, "Brainstorming et classement",
    ["Faire citer les usages de l'eau et les classer en usages quotidiens et économiques."],
    ["Boire, cuisiner, se laver ; irrigation, hydroélectricité, pêche, transports, industrie, tourisme."], "II. 1 et 2."),
   (EVAL, 10, "Travail individuel", ["Activité d'application I."], ["Fleuves et lacs de barrage."], None),
  ]},
  {'titre': "Diagramme, calculs et problèmes liés à l'eau (II. 3 et 4, III)", 'etapes': [
   (PRES, 5, "Rappel", ["Faire rappeler les usages de l'eau."], ["Usages quotidiens et économiques."], None),
   ("Développement · II. 3 et 4. Diagramme et calculs", 30, "Construction individuelle au rapporteur ; calculs",
    ["Faire construire un diagramme circulaire (60 %, 25 %, 15 %).", "Faire calculer consommation et pertes dues à une fuite."],
    ["Angles : 216°, 90°, 54° ; total 360° ; titre, légende, source.", "10 L/h → 240 L/jour → 87 600 L/an."], "II. 3 et 4."),
   ("Développement · III. Les problèmes liés à l'eau", 10, "Étude d'un document",
    ["Faire relever dans un document les problèmes liés à l'eau."],
    ["Pollution (déchets, engrais, orpaillage), gaspillage, inégal accès, maladies hydriques, végétaux envahissants."], "III."),
   (EVAL, 10, "Travail individuel", ["Activités d'application II et III."], ["Angle d'un secteur ; causes de pollution."], None),
  ]},
  {'titre': "La gestion rationnelle de l'eau (IV)", 'etapes': [
   (PRES, 5, "Retour à la situation", ["« Que faire dans notre établissement ? »"], ["Fermer les robinets, réparer les fuites, sensibiliser."], None),
   ("Développement · IV. La gestion rationnelle", 30, "Questionnement puis production en groupes",
    ["Faire relier chaque action à une valeur.", "Faire produire affiches et slogans pour les sanitaires."],
    ["Actions : fermer les robinets, réparer les fuites, récupérer l'eau de pluie, protéger les puits, ne pas polluer, traiter l'eau.",
     "Valeurs : responsabilité, solidarité et partage, respect du bien commun ; slogan « Ferme le robinet, l'eau est précieuse »."], "IV, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Identifient un problème, ses conséquences et des actions."], None),
  ]},
 ],
 'eclairage': [
  "Le principal défi ivoirien est la qualité de l'eau et l'inégal accès, plus que la quantité.",
  "Loi n° 98-755 du 23 décembre 1998 portant Code de l'eau ; droit à l'eau reconnu par l'ONU en 2010 ; ODD 6.",
  "Barrages : Ayamé (Bia), Kossou et Taabo (Bandama), Buyo et Soubré (Sassandra, Soubré mis en service en 2017).",
  "Le diagramme circulaire du cours est construit avec des données d'exercice.",
 ],
 'difficultes': [
  ("Confusion entre lagune et lac.", "La lagune communique avec la mer (eau saumâtre) ; le lac est entouré de terre."),
  ("Erreurs d'angles dans le diagramme circulaire.", "Vérifier que la somme fait 360° ; exercice guidé au rapporteur."),
  ("Erreurs d'unités dans les calculs de pertes.", "Écrire systématiquement l'unité à chaque étape (L/h, L/jour, L/an)."),
 ],
 'soutien': ["Carte muette à compléter avec une liste de noms.", "Diagramme circulaire pré-gradué tous les 10 %."],
 'approfondissement': ["Faire l'inventaire des fuites de l'établissement avec le club environnement.", "Exposé sur un barrage hydroélectrique ivoirien."],
 'evaluation': {
  'activites': [
   ("Cite les quatre grands fleuves de Côte d'Ivoire, d'ouest en est.", 2, "Cavally, Sassandra, Bandama, Comoé. 0,5 pt par fleuve bien placé."),
   ("L'eau d'une région est utilisée ainsi : agriculture 60 %, usages domestiques 25 %, industrie 15 % (données d'exercice). Calcule les angles du diagramme circulaire.", 3, "Agriculture 216° ; domestique 90° ; industrie 54°. 1 pt par angle."),
   ("Relie chaque plan d'eau à une activité : a) océan Atlantique ; b) lac de Kossou ; c) lagune Ébrié — 1) production d'électricité ; 2) transport lagunaire ; 3) pêche industrielle et commerce maritime.", 1.5, "a-3 ; b-1 ; c-2. 0,5 pt par association."),
   ("Un robinet fuit de 6 litres par heure. Calcule la perte en une semaine.", 1.5, "6 × 24 × 7 = 1 008 litres (opération 1 pt, résultat 0,5 pt)."),
  ],
  'situation': "Dans ton village, des orpailleurs lavent leur minerai dans la rivière, et les habitants qui y puisent leur eau tombent malades.",
  'consignes': [
   ("Identifie le problème lié à l'eau.", 2, "La pollution de la rivière par l'orpaillage clandestin (mercure, boue) (2 pts)."),
   ("Montre deux conséquences pour la population.", 4, "Des maladies (diarrhées, intoxications) (2 pts) ; la disparition des poissons et la perte d'une source d'eau pour les cultures et le bétail (2 pts)."),
   ("Propose deux actions de gestion rationnelle de l'eau et la valeur liée à chacune.", 4, "Signaler l'orpaillage illégal aux autorités et sensibiliser (respect du bien commun) ; installer un forage, faire bouillir et filtrer l'eau (responsabilité, solidarité) (2 pts par action avec sa valeur)."),
  ],
 },
 'valeurs': ["Responsabilité, solidarité et respect du bien commun dans l'usage de l'eau.", "Santé et hygiène.",
             "Liens avec les SVT (cycle de l'eau, maladies), les mathématiques (angles, calculs) et l'EDHC."],
}

# ------------------------------------------------------------------ T2-L1
FICHES['5e-g-t2-l1'] = {
 'materiel': ["schémas du cycle du brûlis et de l'agroforesterie (schémas 1 et 2)", "photographies d'une plantation industrielle, d'un champ associé et de cacao sous ombrage",
              "outils agricoles ou leurs images (daba, houe, machette, pulvérisateur)", "grande feuille pour le tableau des avantages et inconvénients"],
 'contexte': "un élève de 5e du Collège moderne de Koumassi passe ses vacances au village.",
 'circonstance': "son grand-père s'inquiète de l'insuffisance des récoltes ces dernières années ; de retour au collège, la classe décide de chercher des explications et des solutions.",
 'taches': ["définir méthode et technique agricoles ; identifier les méthodes et distinguer les techniques", "répertorier les outils ; relever avantages et inconvénients et construire un tableau",
            "traiter une situation relative au choix des méthodes et techniques"],
 'prerequis': ["Les sols, le climat et la végétation (6e).", "La croissance démographique et la pression sur la terre (leçon 2 du thème 1)."],
 'seances': [
  {'titre': "Définitions et méthodes agricoles (I et II)", 'etapes': [
   (PRES, 8, "Lecture de la situation et hypothèses",
    ["Lire la situation du grand-père.", "« Pourquoi les récoltes baissent-elles ? »"], ["Manque de pluie, sol fatigué, maladies."], "Introduction."),
   ("Développement · I. Définitions", 10, "Construction des définitions par des exemples",
    ["Faire définir méthode et technique ; classer quelques exemples."],
    ["Méthode : organisation générale de la production ; technique : procédé concret pour travailler la terre."], "I. 1 et 2."),
   ("Développement · II. Les méthodes", 27, "Étude du schéma 1 et de photographies",
    ["Faire expliquer le cycle du brûlis et le rôle de la jachère.", "Faire décrire les autres méthodes à partir de photographies."],
    ["Défrichement, brûlis, cultures, jachère ; si la jachère raccourcit, le sol s'épuise.", "Intensive, monoculture, polyculture et cultures associées, agroforesterie."], "II. 1 à 5."),
   (EVAL, 10, "Travail individuel", ["Activités d'application I et II."], ["Définitions ; agriculture itinérante."], None),
  ]},
  {'titre': "Techniques, outils, avantages et inconvénients (III et IV)", 'etapes': [
   (PRES, 5, "Questionnement", ["« Avec quels outils travaillent vos parents ou vos grands-parents ? »"], ["Daba, machette, houe ; parfois tracteur, pulvérisateur."], None),
   ("Développement · III. Techniques et outils", 15, "Inventaire et classement",
    ["Faire lister les techniques ; faire classer les outils en traditionnels et modernes."],
    ["Défrichement, brûlis, labour, billonnage, engrais, pesticides, irrigation, jachère, rotation, mécanisation.", "Traditionnels : daba, houe, machette ; modernes : tracteur, motopompe, pulvérisateur."], "III. 1 à 3."),
   ("Développement · IV. Avantages et inconvénients", 25, "Construction du tableau en groupes ; exploitation du schéma 2",
    ["Chaque groupe remplit une ligne du tableau.", "Faire comparer monoculture et agroforesterie (schéma 2)."],
    ["Chaque pratique a des avantages (rendements, revenus) et des inconvénients (déforestation, sols épuisés, pollution).", "Agroforesterie : ombrage, humus, sol protégé ; sol nu : érosion."], "IV."),
   (EVAL, 10, "Travail individuel", ["Activités d'application III et IV."], ["Classement des outils ; avantage et inconvénient des engrais."], None),
  ]},
  {'titre': "Choisir des pratiques durables (V)", 'etapes': [
   (PRES, 5, "Retour au problème", ["« Que conseiller au grand-père ? »"], ["Premières idées de solutions."], None),
   ("Développement · V. Les pratiques durables", 30, "Recherche de solutions et rédaction d'une lettre de conseils",
    ["Faire proposer des solutions et vérifier, pour chacune, qu'elle améliore la récolte et protège l'environnement.", "Faire rédiger une lettre de conseils au grand-père."],
    ["Abandonner le brûlis répété, compost et fumier, rotation, agroforesterie, semences améliorées, engrais raisonnés, lutte contre les feux, conseils de l'ANADER."], "V, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Identifient méthode et technique, expliquent la baisse des récoltes, proposent des solutions."], None),
  ]},
 ],
 'eclairage': [
  "Le modèle ivoirien du cacao s'est construit sur l'avancée d'un front pionnier en forêt (la « rente forêt » analysée par François Ruf).",
  "Les sols ferrallitiques tirent leur fertilité de l'humus forestier : sa destruction fait chuter rapidement les rendements.",
  "Réponses actuelles : agroforesterie, intensification écologique, Code forestier de 2019, exigences des marchés contre la déforestation.",
  "Les pratiques extensives étaient adaptées à de faibles densités : ne pas culpabiliser les paysans.",
 ],
 'difficultes': [
  ("Confusion entre méthode et technique.", "Classement d'exemples avec la question-test : organiser ou travailler la terre ?"),
  ("Idée que le moderne est toujours meilleur.", "Relire le tableau : chaque pratique a des avantages et des inconvénients."),
  ("Solutions irréalistes.", "Exiger des solutions applicables par un paysan de la région, avec leur effet sur la récolte et sur l'environnement."),
 ],
 'soutien': ["Tableau à compléter avec une liste d'avantages et d'inconvénients à placer.", "Images d'outils à classer."],
 'approfondissement': ["Enquête auprès d'un agriculteur de la famille sur ses méthodes et ses difficultés.", "Exposé sur l'agroforesterie dans les plantations de cacao."],
 'evaluation': {
  'activites': [
   ("Définis : méthode agricole ; technique agricole.", 2, "Méthode : manière générale d'organiser la production (1 pt) ; technique : procédé concret pour travailler la terre (1 pt)."),
   ("Classe en outils traditionnels ou modernes : daba, tracteur, machette, pulvérisateur, houe, motoculteur.", 1.5, "Traditionnels : daba, machette, houe ; modernes : tracteur, pulvérisateur, motoculteur. 0,25 pt par outil."),
   ("Dis si chaque élément est une méthode ou une technique : monoculture, irrigation, agriculture itinérante, labour.", 2, "Méthodes : monoculture, agriculture itinérante ; techniques : irrigation, labour. 0,5 pt par réponse."),
   ("Donne un avantage et un inconvénient de la monoculture d'exportation et de l'agroforesterie.", 2.5, "Monoculture : revenus élevés / déforestation et sols épuisés ; agroforesterie : sol protégé et enrichi / rendements plus lents, formation nécessaire. 0,5 pt par élément ; 0,5 pt pour la cohérence."),
  ],
  'situation': "Ton grand-père pratique depuis trente ans la culture sur brûlis sur la même zone ; les jachères sont de plus en plus courtes et les récoltes baissent.",
  'consignes': [
   ("Identifie la méthode et la technique utilisées par ton grand-père.", 2, "Agriculture extensive itinérante (1 pt) ; culture sur brûlis (1 pt)."),
   ("Explique pourquoi les récoltes baissent.", 4, "Le feu détruit l'humus et les êtres vivants du sol (2 pts) ; les jachères trop courtes ne laissent plus au sol le temps de se reconstituer : il s'épuise et s'érode (2 pts)."),
   ("Propose deux solutions adaptées et justifie-les.", 4, "Utiliser du compost ou du fumier et pratiquer la rotation des cultures ; planter des arbres sur les parcelles (agroforesterie) et éviter les feux (2 pts par solution justifiée)."),
  ],
 },
 'valeurs': ["Respect de la terre nourricière et de la forêt.", "Valorisation du travail agricole et des savoirs paysans.",
             "Liens avec les SVT (sol, humus, biodiversité) et l'EDHC (développement durable)."],
}

# ------------------------------------------------------------------ T2-L2
FICHES['5e-g-t2-l2'] = {
 'materiel': ["schéma des sources de pollution dans un quartier (schéma 1)", "schéma d'interrelation (schéma 2)",
              "article ou résumé sur l'affaire du Probo Koala (2006)", "papier et feutres pour les slogans"],
 'contexte': "un industriel projette de construire une usine et un marché dans le quartier d'élèves de 5e du Collège moderne de Tanda.",
 'circonstance': "les jeunes du quartier se divisent : les uns approuvent le projet pour les emplois, les autres le combattent parce qu'il va dégrader l'environnement.",
 'taches': ["identifier les composantes de l'environnement ; connaître les formes de pollution et leurs causes", "distinguer les conséquences ; réaliser un schéma d'interrelation",
            "formuler un slogan de sensibilisation en faveur de l'environnement"],
 'prerequis': ["Population et environnement local (6e).", "L'eau et ses problèmes (leçon 3 du thème 1)."],
 'seances': [
  {'titre': "Environnement, formes et causes de la pollution (I et II)", 'etapes': [
   (PRES, 8, "Lecture de la situation et formulation des deux positions",
    ["Lire la situation de Tanda.", "Faire formuler les arguments des deux groupes de jeunes."], ["Pour : emplois, revenus ; contre : fumées, déchets, bruit."], "Introduction."),
   ("Développement · I. Environnement et pollution", 10, "Observation du quartier et définitions",
    ["Faire distinguer composantes naturelles et humaines ; définir la pollution."],
    ["Naturelles : air, eau, sol, végétation, faune ; humaines : habitations, routes, usines, marchés.", "Pollution : dégradation de l'environnement par des substances ou nuisances dangereuses."], "I. 1 et 2."),
   ("Développement · II. Formes et causes de la pollution", 27, "Exploitation du schéma 1 ; tableau source – polluant – milieu ; étude d'un document",
    ["Faire associer chaque numéro du schéma 1 à une forme de pollution.", "Faire remplir un tableau source, polluant, milieu touché ; présenter l'affaire du Probo Koala."],
    ["Air : fumées, gaz d'échappement ; eau : eaux usées, rejets chimiques, déchets ; sols : déchets toxiques, sachets ; sonore et visuelle : bruit, ordures.", "Probo Koala, Abidjan, août 2006 : déchets toxiques, décès, milliers d'intoxications."], "II. 1 à 5."),
   (EVAL, 10, "Travail individuel", ["Activités d'application I et II."], ["Définition ; association des pollutions."], None),
  ]},
  {'titre': "Conséquences, schéma d'interrelation et préservation (III et IV)", 'etapes': [
   (PRES, 5, "Questionnement", ["« Quelles sont les conséquences de ces pollutions pour nous ? »"], ["Maladies, inondations, poissons morts."], None),
   ("Développement · III. Conséquences et schéma d'interrelation", 20, "Relevé des conséquences ; construction du schéma en binômes",
    ["Faire classer les conséquences (santé, nature, économie).", "Faire construire le schéma d'interrelation."],
    ["Santé : maladies respiratoires, diarrhées, intoxications ; nature : poissons morts, sols stériles ; économie : pêche, inondations, tourisme.",
     "Activités → rejets → pollutions → conséquences → solutions, avec retour vers les activités."], "III. 1 à 4."),
   ("Développement · IV. Préservation", 15, "Atelier de slogans et débat final",
    ["Faire relever les moyens de lutte ; faire écrire des slogans.", "Débat : à quelles conditions accepter l'usine et le marché ?"],
    ["Lois et contrôles (étude d'impact), traitement et tri des déchets, ANAGED, sensibilisation.", "« Une usine propre, un quartier sain » ; accepter le projet avec étude d'impact et traitement des rejets."], "IV, conclusion."),
   (EVAL, 15, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Formes de pollution, conséquences, slogan et mesure."], None),
  ]},
 ],
 'eclairage': [
  "Cadre légal : loi n° 96-766 du 3 octobre 1996 portant Code de l'environnement (étude d'impact) ; sachets plastiques non biodégradables interdits depuis 2013.",
  "Acteurs : CIAPOL (surveillance des eaux, installations classées), ANAGED (déchets, créée en 2017), ANDE (études d'impact).",
  "Probo Koala (août 2006) : déchets toxiques déversés à Abidjan, décès et dizaines de milliers de consultations.",
  "Le débat de la situation doit aboutir à des conditions d'acceptation du projet, pas à un refus de tout développement.",
 ],
 'difficultes': [
  ("Confusion entre source et forme de pollution.", "Tableau à trois colonnes : source, polluant, milieu touché."),
  ("Schéma d'interrelation sans logique.", "Chaque flèche doit se lire « entraîne » ; lecture à voix haute du schéma."),
  ("Slogans négatifs ou vagues.", "Critères : court, positif, message et action clairs."),
 ],
 'soutien': ["Schéma d'interrelation à compléter avec des étiquettes fournies.", "Liste de mots pour écrire un slogan."],
 'approfondissement': ["Réaliser le schéma d'interrelation du quartier de l'établissement.", "Exposé sur l'affaire du Probo Koala et la Convention de Bamako."],
 'evaluation': {
  'activites': [
   ("Définis : environnement ; pollution.", 2, "Environnement : ensemble des éléments naturels et humains qui entourent les êtres vivants (1 pt) ; pollution : dégradation de l'environnement par des substances ou nuisances dangereuses (1 pt)."),
   ("Indique la forme de pollution : a) fumée noire d'une usine ; b) sachets plastiques dans un champ ; c) huile usée déversée dans la lagune ; d) haut-parleurs d'un marché.", 2, "a) air ; b) sol ; c) eau ; d) sonore. 0,5 pt par réponse."),
   ("Explique comment les sachets plastiques provoquent des inondations en ville.", 2, "Jetés dans la rue, ils bouchent les caniveaux (1 pt) ; l'eau de pluie ne peut plus s'écouler et déborde (1 pt)."),
   ("Que s'est-il passé à Abidjan en août 2006 avec le Probo Koala ?", 2, "Des déchets toxiques venus d'un navire ont été déversés dans plusieurs sites d'Abidjan (1 pt), provoquant des décès et des milliers d'intoxications (1 pt)."),
  ],
  'situation': "Un industriel projette de construire une usine et un marché dans ton quartier ; les jeunes se divisent entre ceux qui veulent les emplois et ceux qui craignent la pollution.",
  'consignes': [
   ("Cite deux formes de pollution que ce projet pourrait provoquer.", 2, "Pollution de l'air par les fumées de l'usine ; pollution des sols et de l'eau par les déchets du marché et les eaux usées (1 pt par forme)."),
   ("Montre une conséquence sur la santé et une sur la nature.", 4, "Santé : maladies respiratoires, diarrhées, intoxications (2 pts) ; nature : mort des poissons et des plantes, sols stériles (2 pts)."),
   ("Propose un slogan et une mesure pour concilier emplois et environnement.", 4, "Slogan court et positif, par exemple « Des emplois oui, la pollution non ! » (1,5 pt) ; mesure : étude d'impact environnemental, traitement des eaux usées et des déchets, poubelles au marché (2,5 pts)."),
  ],
 },
 'valeurs': ["Respect du cadre de vie et de la santé de tous.", "Sens de la responsabilité individuelle et collective (salubrité).",
             "Liens avec les SVT (santé, écosystèmes), l'EDHC (droit à un environnement sain) et le français (débat, slogan)."],
}
