# Fiches enseignant — Histoire 5e (lot 2 de la généralisation du modèle validé)
# Même format que fiches_h.py : étape = (moment, durée en min, stratégie, [activités du professeur],
# [réponses attendues des élèves], trace écrite)

PRES = "Présentation"
EVAL = "Évaluation"

FICHES = {}

# ------------------------------------------------------------------ T1-L1
FICHES['5e-h-t1-l1'] = {
 'materiel': ["carte administrative de la Côte d'Ivoire (districts et régions)", "carte des grands groupes culturels (carte 1 de la leçon)",
              "texte d'un mythe d'origine (récit d'Abla Pokou ou récit local)", "fiche sur la région de l'établissement (chef-lieu, départements, peuples)"],
 'contexte': "l'intronisation du roi des Agni de l'Indénié, à Abengourou, réunit les danses des différents peuples de la région ; des élèves de 5e y ont assisté.",
 'circonstance': "pendant la récréation, une discussion éclate entre camarades au sujet du processus de peuplement de la région.",
 'taches': ["nommer les peuples de la région et situer la région en Côte d'Ivoire", "localiser les peuples de la région",
            "expliquer le peuplement de la région", "collecter et exploiter des informations sur ce peuplement"],
 'prerequis': ["Les sources de l'histoire, en particulier la tradition orale (6e).", "La lecture d'une carte de la Côte d'Ivoire (6e).",
               "La construction d'un axe chronologique (6e)."],
 'seances': [
  {'titre': "La région et ses peuples (I et II)", 'etapes': [
   (PRES, 10, "Lecture de la situation et émergence des représentations",
    ["Lire la situation (intronisation du roi des Agni de l'Indénié).", "« Quels peuples vivent dans notre région ? Sont-ils tous arrivés en même temps ? »"],
    ["Les élèves citent les peuples qu'ils connaissent ; certains pensent que tous sont arrivés en même temps."], "Introduction."),
   ("Développement · I. La région et sa situation", 15, "Travail sur la carte administrative, en binômes",
    ["Faire trouver la région de l'établissement, son chef-lieu, ses départements, son district et ses voisins.",
     "Faire construire la hiérarchie district → région → département → sous-préfecture → village."],
    ["14 districts autonomes et 31 régions.", "Exemple : région du Gôh, chef-lieu Gagnoa, départements de Gagnoa et d'Oumé, district du Gôh-Djiboua, Centre-Ouest."], "I. 1 et 2."),
   ("Développement · II. Les peuples de Côte d'Ivoire et de la région", 20, "Étude de la carte 1, puis questionnement",
    ["Faire relever deux villes et une position dans le pays pour chaque grand groupe.",
     "Faire nommer les autochtones de la région, puis distinguer allochtones et allogènes (schéma 1)."],
    ["Akan à l'Est et au Centre ; Krou à l'Ouest et au Sud-Ouest ; Mandé du Nord au Nord-Ouest ; Mandé du Sud à l'Ouest et au Centre-Ouest ; Gour au Nord et au Nord-Est.",
     "Autochtones du Gôh : Bété (krou), Gban (mandé du Sud) ; allochtones : Baoulé, Malinké, Sénoufo… ; allogènes : Burkinabè, Maliens…"], "II. 1 à 3."),
   (EVAL, 10, "Travail individuel", ["Activités d'application I et II."], ["Situent la région et distinguent autochtone, allochtone et allogène."], None),
  ]},
  {'titre': "Le peuplement de la région (III)", 'etapes': [
   (PRES, 8, "Rappel et question-problème",
    ["Faire rappeler les grands groupes et le sens d'allochtone et d'allogène.", "« Comment ces peuples se sont-ils installés ? »"],
    ["Grands groupes ; allochtone : Ivoirien d'une autre région ; allogène : originaire d'un autre pays."], None),
   ("Développement · III. Le peuplement de la région", 35, "Étude d'un mythe d'origine, construction de la frise, travail de groupes",
    ["Lire le récit d'Abla Pokou (ou un récit local) : faire distinguer le vraisemblable et le merveilleux.",
     "Construire la frise des grandes étapes du peuplement, puis le tableau des étapes du peuplement de la région.",
     "Groupes : modes d'installation et conséquences du peuplement."],
    ["Le mythe garde le souvenir d'une migration venue de l'Est ; le sacrifice relève de la légende.",
     "Peuplement ancien ; Mandé du Nord (XVe – XVIIIe s.) ; Akan (XVIIe – XVIIIe s.) ; Lobi (XIXe s.) ; migrations du XXe siècle.",
     "Accueil par un tuteur, alliances matrimoniales, plus rarement conquête ; brassages, diversité, parfois conflits fonciers."], "III. 1 à 5."),
   (EVAL, 12, "Travail individuel et correction collective", ["Activité d'application III."], ["Citent trois modes d'installation et une conséquence."], None),
  ]},
  {'titre': "Collecter et exploiter des informations sur le peuplement (IV)", 'etapes': [
   (PRES, 7, "Question-problème",
    ["« Comment l'historien retrouve-t-il l'histoire du peuplement d'un village qui n'a pas d'archives ? »"],
    ["En interrogeant les anciens, en comparant les récits et les documents."], None),
   ("Développement · IV. Collecter et exploiter", 28, "Élaboration collective d'un questionnaire, mise en commun d'une enquête",
    ["Faire rédiger un questionnaire d'enquête (premiers occupants, origine des autres peuples, époque, accès à la terre).",
     "Si l'enquête a été menée, faire confronter les versions, classer les informations et les présenter en tableau."],
    ["Questions ouvertes, informateurs identifiés (nom, âge, village).", "Tableau : étape, peuples, groupe culturel, mode d'installation."], "IV. 1 et 2, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Réinvestissent les savoirs sur l'exemple de la région."], None),
  ]},
 ],
 'eclairage': [
  "Les grands groupes du programme sont d'abord des familles de langues : krou, mandé et gour d'une part, akan et langues lagunaires (branche kwa) d'autre part.",
  "La chronologie par vagues (peuplement ancien, Mandé du Nord, Akan, migrations tardives et contemporaines) est une synthèse des historiens ivoiriens à partir des traditions orales ; les dates sont approximatives.",
  "Le tutorat, relation coutumière entre l'autochtone qui accueille et l'étranger accueilli, a été étudié en pays gban (région du Gôh) par l'anthropologue Jean-Pierre Chauveau.",
  "Les mots autochtone, allochtone et allogène sont relatifs à une région et ont une charge politique : les présenter comme descriptifs et rappeler l'égalité des citoyens.",
 ],
 'difficultes': [
  ("Confusion entre allochtone et allogène.", "Reprendre le schéma 1 avec des exemples locaux ; faire classer cinq cas concrets."),
  ("Confusion entre région, district et département.", "Reconstruire la hiérarchie au tableau à partir de l'exemple de la région de l'établissement."),
  ("Idée d'un peuplement « d'un seul coup ».", "Relire la frise 1 et le tableau des étapes ; souligner les petits groupes familiaux successifs."),
 ],
 'soutien': ["Lexique illustré : autochtone, allochtone, allogène, migration, lignage.", "Carte de la région à compléter avec les noms déjà écrits dans une liste."],
 'approfondissement': ["Mener l'enquête auprès d'un ancien et présenter les résultats à la classe.", "Comparer le mythe d'origine de deux peuples de la région."],
 'evaluation': {
  'activites': [
   ("Définis : allochtone, allogène.", 2, "Allochtone : Ivoirien venu d'une autre région du pays (1 pt). Allogène : personne originaire d'un autre pays (1 pt)."),
   ("Cite les cinq grands groupes culturels de Côte d'Ivoire.", 2.5, "Akan, Krou, Mandé du Nord, Mandé du Sud, Gour ou voltaïques. 0,5 pt par groupe."),
   ("Situe la région du Gôh : chef-lieu, départements, district, position dans le pays.", 2, "Gagnoa ; Gagnoa et Oumé ; district du Gôh-Djiboua ; Centre-Ouest. 0,5 pt par élément."),
   ("Cite trois modes d'installation des migrants.", 1.5, "Accueil par un tuteur, alliances matrimoniales, conquête. 0,5 pt par mode."),
  ],
  'situation': "Ton correspondant de Korhogo t'écrit : « Dans ta région du Gôh, il n'y a qu'un seul peuple, arrivé d'un seul coup ; d'ailleurs, les mythes d'origine racontent toute la vérité. »",
  'consignes': [
   ("Nomme deux peuples autochtones de la région du Gôh et leur groupe culturel.", 2, "Les Bété, groupe krou (1 pt) ; les Gban ou Gagou, groupe mandé du Sud (1 pt)."),
   ("Explique en trois étapes le peuplement de la région.", 4.5, "Peuplement ancien : lignages bété autochtones, Gban (1,5 pt) ; migrations précoloniales de lignages bété venus de l'Ouest et du Sud-Ouest (1,5 pt) ; migrations du XXe siècle liées au café et au cacao : Baoulé, Malinké, Dioula, migrants de la sous-région (1,5 pt)."),
   ("Réponds à ton correspondant au sujet des mythes d'origine et propose deux sources pour vérifier les informations.", 3.5, "Les mythes gardent le souvenir de faits réels mais mêlent faits et merveilleux ; il faut les comparer avec d'autres sources (1,5 pt). Sources : interroger les anciens et les chefs, consulter les monographies et archives de la sous-préfecture, des ouvrages d'histoire (1 pt par source, 2 attendues)."),
  ],
 },
 'valeurs': ["Respect de la diversité des peuples et égalité des citoyens.", "Dialogue et respect des accords pour prévenir les conflits fonciers.",
             "Liens avec l'éducation aux droits de l'homme et à la citoyenneté (EDHC) et le français (enquête, compte rendu)."],
}
