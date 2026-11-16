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

# ------------------------------------------------------------------ T1-L2
FICHES['5e-h-t1-l2'] = {
 'materiel': ["schéma des traits d'une civilisation (schéma 1)", "carte des expressions du patrimoine culturel (carte 1)",
              "photos ou objets : pagne, masque, instrument de musique, ustensiles", "papier, feutres pour les affiches"],
 'contexte': "l'intronisation du nouveau roi de Sakassou réunit, au village du Warêbo, des délégations de toute la région du Gbêkê.",
 'circonstance': "impressionnés par les danses et les tenues des délégations, des élèves de 5e du Lycée moderne de Sakassou décident de faire des recherches de retour en classe.",
 'taches': ["définir la civilisation et identifier les aires culturelles de la région", "localiser les groupes culturels et distinguer leurs traits",
            "produire des supports de sensibilisation et proposer des actions de préservation du patrimoine"],
 'prerequis': ["Les grands groupes culturels de Côte d'Ivoire (leçon 1).", "Les peuples de la région de l'établissement (leçon 1).", "Les sources de l'histoire (6e)."],
 'seances': [
  {'titre': "Civilisation et aire culturelle (I)", 'etapes': [
   (PRES, 10, "Lecture de la situation et description d'une cérémonie vécue",
    ["Lire la situation (intronisation du roi à Sakassou).", "« Décrivez une cérémonie à laquelle vous avez assisté : danses, tenues, musiques, plats. »"],
    ["Les élèves décrivent des danses, des pagnes, des tambours, des repas, la présence du roi ou du chef."], "Introduction."),
   ("Développement · I. Les notions", 35, "Classement au tableau, construction du schéma 1",
    ["Faire classer les éléments notés au tableau en catégories.", "Faire formuler la définition de la civilisation et du trait culturel, puis de l'aire culturelle."],
    ["Catégories : organisation, économie, croyances, langue, arts, alimentation, habitat et costume, coutumes.",
     "Civilisation : ensemble des caractères propres à la vie d'un peuple ; aire culturelle : espace de peuples aux origines et aux langues proches ; cinq aires en Côte d'Ivoire."], "I. 1 et 2."),
   (EVAL, 10, "Travail individuel", ["Activité d'application I."], ["Définitions et trois traits culturels."], None),
  ]},
  {'titre': "Les aires de la région ; organisation et activités (II, III. 1 et 2)", 'etapes': [
   (PRES, 5, "Rappel", ["« À quelle aire culturelle appartient notre région ? »"], ["Réponse selon la région (Gôh : aire krou et mandé du Sud)."], None),
   ("Développement · II. Les aires et groupes culturels de la région", 20, "Travail sur carte, en binômes",
    ["Faire identifier les aires de la région et localiser les groupes.", "Comparer avec l'exemple du Gbêkê (aire akan, Sakassou)."],
    ["Gôh : Bété (krou), Gban (mandé du Sud), groupes venus d'ailleurs ; Gbêkê : Baoulé (akan), groupe warêbo autour de Sakassou."], "II. 1 et 2."),
   ("Développement · III. 1 et 2. Organisation et activités", 20, "Lecture guidée d'un tableau comparatif",
    ["Faire relever deux différences entre l'organisation krou et l'organisation akan.", "Faire relier les activités au milieu (forêt, savane, lagune)."],
    ["Krou : lignages, pas de pouvoir centralisé, parenté patrilinéaire ; Akan : royaumes, reine mère, succession surtout matrilinéaire.",
     "Igname, riz, plantain, cultures d'exportation, chasse, pêche, élevage au Nord, artisanat, commerce."], "III. 1 et 2."),
   (EVAL, 10, "Travail individuel", ["Activité d'application II."], ["Associent chaque peuple à son aire."], None),
  ]},
  {'titre': "Croyances, arts, alimentation, habitat et costume (III. 3 à 5)", 'etapes': [
   (PRES, 5, "Écoute ou description d'une musique traditionnelle", ["Faire écouter ou décrire une musique traditionnelle connue des élèves."], ["Les élèves nomment l'instrument, le peuple, l'occasion."], None),
   ("Développement · III. 3 à 5. Croyances, arts, alimentation, habitat, costume", 40, "Travail de groupes, mise en commun, exploitation de la carte 1",
    ["Chaque groupe remplit une fiche sur un peuple de la région : croyances, fêtes, danse, plat, habitat, costume.", "Exploiter la carte 1 : relever les éléments inscrits par l'UNESCO."],
    ["Ancêtres et génies, christianisme, islam ; fête des ignames, fêtes de génération, Poro.",
     "Tohourou et Alloukou (Bété), Goli (Baoulé), Zaouli (Gouro, UNESCO 2017), échassiers (Dan), Boloye et balafon (Sénoufo).",
     "Foutou, attiéké, placali, tô ; cases rondes au Nord, rectangulaires en forêt ; pagne kita."], "III. 3 à 5."),
   (EVAL, 10, "Travail individuel", ["Activité d'application III."], ["Relient chaque expression culturelle à son peuple."], None),
  ]},
  {'titre': "Patrimoine et diversité culturelle (IV)", 'etapes': [
   (PRES, 5, "Situation-problème", ["« Un oncle veut vendre un vieux masque du village à un touriste. Qu'en penses-tu ? »"], ["Avis partagés ; certains évoquent le caractère sacré du masque."], None),
   ("Développement · IV. Patrimoine et diversité culturelle", 30, "Questionnement puis production en groupes",
    ["Faire distinguer patrimoine matériel et immatériel ; relever les menaces.", "Faire proposer des actions de préservation ; faire produire une affiche ou un slogan."],
    ["Matériel : masques, sièges royaux, sites ; immatériel : langues, danses, contes, savoir-faire.",
     "Menaces : oubli des langues, vente d'objets sacrés, abandon des savoir-faire, mépris des autres cultures.",
     "Actions : transmettre les langues, fêtes culturelles, musées, clubs ; slogan « Nos cultures sont différentes, notre nation est une »."], "IV. 1 à 4, conclusion."),
   (EVAL, 20, "Présentation des productions et travail individuel", ["Présentation des affiches ; situation d'évaluation."], ["Productions présentées ; réponses à la situation."], None),
  ]},
 ],
 'eclairage': [
  "La civilisation s'emploie au pluriel et sans hiérarchie : chaque peuple a la sienne ; le sens ancien, au singulier, a servi à justifier la colonisation.",
  "Les aires culturelles sont des ensembles dominants, aux limites floues ; les traits circulent d'une aire à l'autre (le Goli des Baoulé, emprunté aux Wan).",
  "La règle matrilinéaire akan est très nette chez les Agni ; chez les Baoulé, le système de parenté est plus souple.",
  "La Convention de l'UNESCO de 2003 définit le patrimoine culturel immatériel ; le Zaouli des Gouro a été inscrit en 2017.",
 ],
 'difficultes': [
  ("Confusion entre aire culturelle et région administrative.", "Comparer la carte des aires et la carte des régions : les aires débordent les limites administratives."),
  ("Confusion entre patrilinéaire et matrilinéaire.", "Exemple concret de l'héritage d'un chef ; mnémotechnique pater / mater."),
  ("Confusion entre patrimoine matériel et immatériel.", "Classer dix exemples (masque, danse, conte, siège royal, langue…) en deux colonnes."),
 ],
 'soutien': ["Fiche à trous sur la définition de la civilisation et le schéma 1.", "Tableau à compléter : peuple, aire, une danse, un plat."],
 'approfondissement': ["Préparer un exposé sur une fête traditionnelle de la région.", "Réaliser une petite exposition de photographies sur le patrimoine de la région."],
 'evaluation': {
  'activites': [
   ("Définis la civilisation et l'aire culturelle.", 2, "Civilisation : ensemble des caractères propres à la vie d'un peuple (1 pt). Aire culturelle : espace de peuples aux origines communes, aux langues apparentées et aux traits culturels voisins (1 pt)."),
   ("Relie chaque expression culturelle à son peuple : Zaouli, Goli, Tohourou, Boloye — Bété, Gouro, Sénoufo, Baoulé.", 2, "Zaouli → Gouro ; Goli → Baoulé ; Tohourou → Bété ; Boloye → Sénoufo. 0,5 pt par association."),
   ("Distingue l'organisation politique des Bété et celle des Baoulé.", 2, "Bété : sociétés lignagères sans pouvoir centralisé, chef de village et conseil des anciens (1 pt) ; Baoulé : royaumes et chefferies, roi ou chef, reine mère, notables (1 pt)."),
   ("Cite deux éléments du patrimoine matériel et deux éléments du patrimoine immatériel.", 2, "Matériel : masque, siège royal, site, objet en or… ; immatériel : langue, danse, conte, savoir-faire… 0,5 pt par élément."),
  ],
  'situation': "Dans ta famille, les jeunes ne parlent plus la langue de leurs parents, et un oncle veut vendre à un touriste un vieux masque du village. Ton petit frère pense que « les cultures des autres régions ne valent rien ».",
  'consignes': [
   ("Définis la civilisation et cite trois traits culturels de ta région.", 3, "Ensemble des caractères propres à la vie d'un peuple (1,5 pt) ; trois traits culturels exacts de la région : langue, danse, plat, fête… (0,5 pt chacun)."),
   ("Montre deux dangers qui menacent le patrimoine culturel de ta région.", 3, "L'abandon de la langue maternelle par les jeunes (1,5 pt) ; la vente d'objets sacrés qui quittent la région et le pays (1,5 pt)."),
   ("Propose deux actions pour préserver ce patrimoine et réponds à ton petit frère par un slogan.", 4, "Parler la langue en famille, organiser des concours de contes, garder le masque au village ou le confier à un musée (1,5 pt par action, 2 attendues) ; slogan en faveur de la diversité culturelle (1 pt)."),
  ],
 },
 'valeurs': ["Respect et valorisation de la diversité culturelle.", "Protection du patrimoine culturel national.",
             "Liens avec l'EDHC (vivre ensemble), les arts plastiques (affiches, masques) et l'éducation musicale."],
}
