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
