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
