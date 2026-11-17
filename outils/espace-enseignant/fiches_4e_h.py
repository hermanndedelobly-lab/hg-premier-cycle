# Fiches enseignant — Histoire 4e (lot 3 de la généralisation du modèle validé)
# Même format que fiches_h.py : étape = (moment, durée en min, stratégie, [activités du professeur],
# [réponses attendues des élèves], trace écrite)

PRES = "Présentation"
EVAL = "Évaluation"

FICHES = {}

# ------------------------------------------------------------------ T1-L1
FICHES['4e-h-t1-l1'] = {
 'materiel': ["fond de carte de la Côte d'Ivoire (un par groupe)", "frise des arrivées et des royaumes (frise 1)", "carte des royaumes (carte 1)",
              "texte de la tradition baoulé (Abla Pokou)", "paroles de la chanson « Cours d'histoire » (extrait)"],
 'contexte': "lors d'une kermesse, des élèves de 4e du Lycée moderne d'Abobo écoutent la chanson de Tiken Jah Fakoly « Cours d'histoire ».",
 'circonstance': "l'artiste chante que les Baoulé se sont installés au XVIIIe siècle alors que les Krou étaient là avant le XVIe siècle ; une discussion éclate entre les élèves.",
 'taches': ["identifier et localiser les aires culturelles", "expliquer les causes des migrations et caractériser les mouvements de populations",
            "expliquer le fonctionnement des structures sociales et apprécier l'impact des contacts entre les peuples"],
 'prerequis': ["Les premiers habitants et les premiers mouvements migratoires (5e).", "L'empire du Mali (5e).", "La lecture d'une carte et d'une frise (6e)."],
 'seances': [
  {'titre': "Les aires culturelles (I)", 'etapes': [
   (PRES, 8, "Écoute d'un extrait et questionnement",
    ["Lire la situation (chanson de Tiken Jah Fakoly).", "« Les Baoulé et les Krou sont-ils arrivés en même temps ? »"], ["Non : les Krou étaient là avant, les Baoulé sont arrivés plus tard."], "Introduction."),
   ("Développement · I. Les aires culturelles", 35, "Travail de groupes sur fond de carte, mise en commun",
    ["Faire définir l'aire culturelle.", "Chaque groupe localise une aire et ses peuples ; construire collectivement la carte des aires."],
    ["Ensemble de peuples d'un même espace aux origines, langues et coutumes voisines ; cinq grands groupes.",
     "Akan à l'est et au centre ; Krou à l'ouest et au sud-ouest ; Mandé du Nord au nord-ouest ; Mandé du Sud à l'ouest ; Gour au nord et au nord-est."], "I. 1 à 3."),
   (EVAL, 12, "Travail individuel", ["Activité d'application I."], ["Cinq groupes, un peuple et une région pour chacun."], None),
  ]},
  {'titre': "La mise en place des peuples (II)", 'etapes': [
   (PRES, 5, "Rappel et question-problème", ["« Pourquoi ces peuples ont-ils quitté leur région d'origine ? »"], ["Guerres, recherche de terres, commerce."], None),
   ("Développement · II. La mise en place des peuples", 40, "Lecture d'un récit de tradition, d'un tableau, de la frise 1 et de la carte 1",
    ["Faire relever les causes générales et particulières des migrations (récit d'Abla Pokou).", "Faire lire le tableau et la frise ; caractériser les formes des migrations ; localiser les royaumes."],
    ["Guerres, querelles de succession, terres, calamités, commerce, islam ; départ des Baoulé après la mort d'Opoku Ware (vers 1750), selon la tradition la plus répandue.",
     "Migrations lentes, par lignages, le long des fleuves et des pistes ; installation pacifique ou par la force.", "Gyaman, Sanwi, Indénié, Kong, royauté baoulé."], "II. 1 à 3."),
   (EVAL, 10, "Travail individuel", ["Activité d'application II."], ["Provenances, périodes et deux royaumes."], None),
  ]},
  {'titre': "Structures sociales et impact des contacts (III)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Comment des étrangers pouvaient-ils obtenir une terre ? »"], ["En la demandant au chef ou aux premiers occupants."], None),
   ("Développement · III. Structures sociales et impact des contacts", 35, "Explication, recherche d'exemples, débat dirigé",
    ["Expliquer le rôle du lignage, du chef de terre, du tuteur, des classes d'âge.", "Faire chercher des exemples de brassages et d'échanges ; débat sur la cohésion nationale ; slogans."],
    ["Le chef de terre autorise l'installation ; le tuteur cède une terre et protège l'étranger ; les classes d'âge intègrent les jeunes.",
     "Mariages, alliances à plaisanterie, emprunts culturels, commerce de la cola, de l'or et du sel ; aucun peuple n'est plus ivoirien qu'un autre."], "III, conclusion."),
   (EVAL, 15, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Chronologie, causes, cohésion nationale."], None),
  ]},
 ],
 'eclairage': [
  "Les migrations akan sont liées à la compétition entre États akan (Denkyira, Akwamu, puis Ashanti, vainqueur à Feyiase en 1701) et aux crises de succession.",
  "L'État de Kong, fondé par les Dioula au début du XVIIIe siècle, est né des réseaux marchands de l'or et de la cola.",
  "Les peuples lagunaires sont rattachés à l'aire akan par l'usage scolaire ; certaines langues du littoral (ega, krobou) témoignent d'un peuplement plus ancien.",
  "Dates approximatives : départ des Baoulé vers 1750 selon la version la plus répandue de la tradition.",
 ],
 'difficultes': [
  ("Confusion entre Mandé du Nord et Mandé du Sud.", "Comparer leurs régions sur la carte des aires (Nord-Ouest / Ouest et Centre-Ouest)."),
  ("Idée de migrations rapides et massives.", "Relire la frise 1 et les formes des migrations (lignages, plusieurs générations)."),
  ("Confusion entre chef de terre et roi.", "Tableau : autorité religieuse sur la terre / pouvoir politique."),
 ],
 'soutien': ["Carte muette avec liste des peuples à placer.", "Tableau des provenances à compléter."],
 'approfondissement': ["Exposé sur un royaume ivoirien (Gyaman, Sanwi, Indénié, Kong).", "Recueillir le récit d'installation d'un village de la région."],
 'evaluation': {
  'activites': [
   ("Définis : aire culturelle ; migration.", 2, "Aire culturelle : ensemble de peuples d'un même espace, aux origines, langues et coutumes voisines (1 pt) ; migration : déplacement d'un groupe vers une autre région pour s'y installer (1 pt)."),
   ("Cite les cinq grands groupes culturels et localise-les.", 2.5, "Akan (Est, Centre), Krou (Ouest, Sud-Ouest), Mandé du Nord (Nord-Ouest), Mandé du Sud (Ouest, Centre-Ouest), Gour (Nord, Nord-Est). 0,5 pt par groupe localisé."),
   ("Réponds : a) Quel peuple akan fonde le royaume du Gyaman ? b) Quelle reine conduit les Baoulé selon la tradition ? c) Qui fonde la puissance de Kong ?", 1.5, "a) les Abron ; b) Abla Pokou ; c) les Dioula, sous Sékou Ouattara. 0,5 pt par réponse."),
   ("Explique le rôle du tuteur dans l'installation des migrants.", 2, "Il accueille l'étranger, lui cède une terre à cultiver et le protège (1,5 pt) ; en retour l'étranger lui doit respect et reconnaissance (0,5 pt)."),
  ],
  'situation': "Lors d'un débat, un élève soutient que les peuples « arrivés en dernier » ne sont pas de vrais Ivoiriens.",
  'consignes': [
   ("Classe chronologiquement l'arrivée des Krou et des Akan.", 2, "Les Krou sont présents avant le XVIe siècle (1 pt) ; les Akan arrivent surtout à la fin du XVIIe et au XVIIIe siècle (1 pt)."),
   ("Explique deux causes des migrations akan.", 4, "Les querelles de succession au trône, comme celle qui suit la mort d'Opoku Ware selon la tradition baoulé (2 pts) ; les guerres entre royaumes akan (Denkyira, Ashanti) (2 pts)."),
   ("Montre, par deux arguments, que les migrations ont favorisé la cohésion nationale.", 4, "Les mariages et les alliances ont mêlé les peuples (2 pts) ; les échanges commerciaux et culturels ont créé une histoire commune partagée par tous les Ivoiriens (2 pts)."),
  ],
 },
 'valeurs': ["Cohésion nationale et vivre-ensemble.", "Refus du tribalisme et de la xénophobie.",
             "Liens avec l'EDHC (citoyenneté), la géographie (carte) et l'éducation musicale (chanson engagée)."],
}

# ------------------------------------------------------------------ T1-L2
FICHES['4e-h-t1-l2'] = {
 'materiel': ["schéma de la filiation (schéma 1)", "schéma des trois systèmes politiques (schéma 2)", "grandes feuilles pour les organigrammes de groupe",
              "photographie d'une cérémonie royale akan ou d'une fête de génération"],
 'contexte': "le professeur de français d'une classe de 4e du Collège moderne d'Adzopé annonce qu'il sera intronisé chef de son village, Anono, dans la commune de Cocody.",
 'circonstance': "pendant la récréation, les élèves discutent du rôle de la chefferie alors qu'il existe des autorités administratives.",
 'taches': ["identifier et distinguer les organisations sociales et les systèmes politiques", "schématiser les systèmes politiques et expliquer le fonctionnement des structures sociales",
            "proposer des activités de promotion de la paix"],
 'prerequis': ["La mise en place des peuples et les aires culturelles (leçon 1).", "Les traits de civilisation (5e)."],
 'seances': [
  {'titre': "Les organisations sociales (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation d'Anono.", "« À quoi sert un chef de village alors qu'il y a un maire et un sous-préfet ? »"], ["Il garde les traditions, règle les palabres."], "Introduction."),
   ("Développement · I. Les organisations sociales", 35, "Construction collective, exploitation du schéma 1",
    ["Faire construire la hiérarchie famille, lignage, clan, village, tribu.", "Expliquer la filiation avec le schéma 1 ; présenter hiérarchie sociale, classes d'âge et initiation."],
    ["Lignage : descendants d'un ancêtre connu ; clan : ancêtre lointain, souvent mythique.",
     "Matrilinéaire : héritage de l'oncle maternel au neveu (Agni, Abron, Sénoufo) ; patrilinéaire : du père au fils (Krou, Mandé).",
     "Sociétés hiérarchisées (Akan, Mandé du Nord) et égalitaires (Krou, Mandé du Sud) ; classes d'âge lagunaires ; Poro sénoufo."], "I. 1 à 4."),
   (EVAL, 12, "Travail individuel", ["Activité d'application I."], ["Distinction lignage – clan."], None),
  ]},
  {'titre': "Les systèmes politiques (II)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Tous les peuples avaient-ils un roi ? »"], ["Non, certains étaient dirigés par les anciens."], None),
   ("Développement · II. Les systèmes politiques", 40, "Travail de groupes : organigramme d'un système, mise en commun avec le schéma 2",
    ["Chaque groupe étudie un système (royaume akan, société krou, société lagunaire) et en fait l'organigramme."],
    ["Centralisé : roi, conseil royal, chefs de provinces et de villages, regalia.", "Lignager : villages autonomes, chef du lignage fondateur, conseil des anciens, palabre.",
     "Classes d'âge : le pouvoir passe d'une génération à l'autre lors des fêtes de génération."], "II. 1 à 3."),
   (EVAL, 10, "Travail individuel", ["Activité d'application II."], ["Classement des peuples par système politique."], None),
  ]},
  {'titre': "Fonctionnement des structures et chefferie aujourd'hui (III)", 'etapes': [
   (PRES, 5, "Retour à la situation", ["« Que fera le professeur une fois intronisé chef ? »"], ["Il réglera les litiges, organisera les cérémonies."], None),
   ("Développement · III. Fonctionnement et chefferie aujourd'hui", 35, "Questionnement, recherche d'exemples, propositions",
    ["Faire relever les rôles des chefs et des conseils et les valeurs de ces sociétés.", "Présenter la chefferie aujourd'hui ; faire proposer des activités pour la paix."],
    ["Organiser la vie, rendre la justice, gérer la terre, présider les cultes, défendre le groupe ; solidarité, respect des aînés, consensus.",
     "Chambre nationale des rois et chefs traditionnels (Constitution de 2016) ; chef relais de l'administration ; rencontres intercommunautaires."], "III, conclusion."),
   (EVAL, 15, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Systèmes, fonctionnement akan, rôles de la chefferie."], None),
  ]},
 ],
 'eclairage': [
  "Trois modèles : pouvoir centralisé (royaumes akan, Kong), sociétés lignagères sans État (Krou, Mandé du Sud), sociétés à classes d'âge (lagunaires, étudiées par H. Memel-Fotê chez les Adioukrou).",
  "La matrilinéarité est très nette chez les Agni et les Abron ; plus souple chez les Baoulé.",
  "La colonisation a transformé les chefferies (chefs de canton) ; la Constitution de 2016 reconnaît la Chambre nationale des rois et chefs traditionnels.",
  "Une société sans roi n'est pas moins organisée : conseils, consensus, palabre.",
 ],
 'difficultes': [
  ("Confusion entre lignage et clan.", "Ancêtre connu (lignage) / ancêtre lointain, souvent mythique (clan) ; exemple de la famille de l'élève."),
  ("Difficulté à comprendre la matrilinéarité.", "Faire appliquer le schéma 1 à un arbre familial réel ou fictif."),
  ("Organigrammes sans logique.", "Partir du schéma 2 ; flèches de l'autorité vers la population."),
 ],
 'soutien': ["Lexique illustré : lignage, clan, filiation, regalia, classe d'âge.", "Organigrammes à compléter avec des étiquettes."],
 'approfondissement': ["Interroger un chef de village ou un notable sur son rôle et en faire un compte rendu.", "Exposé sur une fête de génération ou une intronisation royale."],
 'evaluation': {
  'activites': [
   ("Définis : société lignagère ; matrilinéarité ; classe d'âge.", 3, "Société lignagère : société sans pouvoir central, dirigée par les chefs de lignage et les anciens ; matrilinéarité : transmission de la parenté et de l'héritage par la mère ; classe d'âge : groupe de personnes nées à la même période, qui exercent ensemble des fonctions. 1 pt par définition."),
   ("Classe ces peuples selon leur système politique : Baoulé, Bété, Ébrié, Dioula de Kong, Dan.", 2.5, "Pouvoir centralisé : Baoulé, Dioula de Kong ; lignager : Bété, Dan ; classes d'âge : Ébrié. 0,5 pt par peuple."),
   ("Complète : type de pouvoir et filiation des Krou et des Agni.", 2, "Krou : société lignagère, patrilinéaire (1 pt) ; Agni : royaume, matrilinéaire (1 pt)."),
   ("Cite un symbole du pouvoir royal akan.", 0.5, "Le siège royal (ou les objets en or, les cannes, les sabres, les tambours parleurs). 0,5 pt."),
  ],
  'situation': "Un camarade affirme qu'avec les préfets et les maires, les chefs traditionnels ne servent plus à rien.",
  'consignes': [
   ("Distingue deux systèmes politiques traditionnels de Côte d'Ivoire avec un exemple chacun.", 3, "Les sociétés lignagères sans État (Krou) (1,5 pt) ; les sociétés à pouvoir centralisé, royaumes (Akan) (1,5 pt) ; on accepte aussi les sociétés à classes d'âge (lagunaires)."),
   ("Explique le fonctionnement du pouvoir chez les Akan.", 4, "Le roi est choisi dans la famille royale par la ligne maternelle (1 pt) ; il gouverne avec la reine mère et un conseil de notables qui limite son pouvoir (1,5 pt) ; il commande des chefs de provinces et de villages (1 pt) ; son pouvoir est symbolisé par le siège royal (0,5 pt)."),
   ("Montre deux rôles de la chefferie dans la Côte d'Ivoire d'aujourd'hui.", 3, "Régler les conflits fonciers et familiaux ; servir d'intermédiaire entre l'administration et les populations ; préserver les traditions (1,5 pt par rôle, 2 attendus)."),
  ],
 },
 'valeurs': ["Respect des autorités traditionnelles et administratives.", "Dialogue, consensus et paix sociale.",
             "Liens avec l'EDHC (institutions) et le français (compte rendu d'entretien)."],
}

# ------------------------------------------------------------------ T1-L3
FICHES['4e-h-t1-l3'] = {
 'materiel': ["schéma des mécanismes de prévention (schéma 1)", "schéma des instances de règlement (schéma 2)", "schéma du déroulement d'une palabre (5e)",
              "fiches de rôles pour le jeu de la palabre"],
 'contexte': "la Côte d'Ivoire sort d'une crise sociopolitique qui a gravement perturbé la population.",
 'circonstance': "des élèves de 4e du Lycée moderne 2 d'Abobo décident d'apporter leur appui au président de la Commission Dialogue, Vérité et Réconciliation (CDVR).",
 'taches': ["définir la notion de mécanisme de prévention", "identifier et expliquer les mécanismes de prévention et les moyens de résolution des conflits",
            "proposer des activités de promotion de la paix"],
 'prerequis': ["Les codes de règlementation des conflits et le DIH (5e).", "L'organisation sociopolitique des peuples (leçon 2)."],
 'seances': [
  {'titre': "Les notions et la prévention des conflits (I et II)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation (CDVR).", "« Comment nos ancêtres évitaient-ils et réglaient-ils les conflits ? »"], ["Par le dialogue, les anciens, les alliances."], "Introduction."),
   ("Développement · I. Les notions", 12, "Construction des définitions à partir d'exemples",
    ["Faire définir conflit, prévention, mécanisme de prévention, résolution."],
    ["Conflit : opposition grave ; prévenir : empêcher le conflit de naître ou de s'aggraver ; résoudre : y mettre fin par le dialogue, la médiation ou une décision acceptée."], "I. 1 à 3."),
   ("Développement · II. La prévention", 25, "Travail de groupes, construction du schéma 1",
    ["Chaque groupe explique un mécanisme : alliances à plaisanterie, mariages, éducation et initiation, terre et tutorat, solidarité."],
    ["Pacte de non-agression et d'entraide (Dida – Abbey) ; liens de parenté ; maîtrise de soi et serments ; règles foncières et accueil des étrangers ; entraide."], "II. 1 à 5."),
   (EVAL, 10, "Travail individuel", ["Activités d'application I et II."], ["Définitions ; rôle de l'alliance à plaisanterie."], None),
  ]},
  {'titre': "La résolution des conflits (III)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Et lorsque le conflit a éclaté ? »"], ["On va voir le chef, les anciens."], None),
   ("Développement · III. La résolution", 40, "Lecture du schéma 2, jeu de rôle d'une palabre",
    ["Faire placer des litiges au bon niveau d'instance.", "Organiser le jeu de rôle d'une palabre ; présenter médiateurs, sanctions, rites, traités."],
    ["Lignage, village et conseil (ou classes d'âge), roi et conseil.", "Exposé des parties, témoins, délibération, décision, réconciliation publique ; amendes, réparation, cola, libations ; traités et pactes."], "III. 1 à 5."),
   (EVAL, 10, "Travail individuel", ["Activité d'application III."], ["Étapes de la palabre."], None),
  ]},
  {'titre': "La promotion de la paix (IV)", 'etapes': [
   (PRES, 5, "Retour à la situation", ["« Que peut faire la CDVR ? Que pouvons-nous faire ? »"], ["Dialoguer, écouter les victimes, réconcilier."], None),
   ("Développement · IV. La promotion de la paix", 35, "Présentation, projet de classe, atelier",
    ["Présenter la CDVR (2011) et la CONARIV ; rôle des chefs et des guides religieux.", "Faire concevoir un club de paix, des slogans et une saynète."],
    ["Institutions de réconciliation inspirées du dialogue traditionnel.", "Clubs de paix, activités intercommunautaires, slogans sur la tolérance et la dignité humaine."], "IV, conclusion."),
   (EVAL, 15, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Mécanismes, palabre, propositions pour la paix."], None),
  ]},
 ],
 'eclairage': [
  "Les mécanismes traditionnels relèvent d'une justice restauratrice : réparer le tort et réconcilier plutôt que punir.",
  "Les listes d'alliances à plaisanterie varient selon les sources : le cours ne cite que l'alliance Dida – Abbey, attestée par le programme de 5e.",
  "CDVR créée en 2011 après la crise postélectorale ; CONARIV chargée de l'indemnisation des victimes.",
  "Médiation (le tiers propose) et arbitrage (le chef décide) sont deux modes distincts.",
 ],
 'difficultes': [
  ("Confusion entre prévention et résolution.", "Classer dix exemples en « avant » et « après » le conflit."),
  ("Confusion entre médiation et arbitrage.", "Jeu de rôle : un médiateur propose, un chef décide."),
  ("Difficulté à placer un litige au bon niveau d'instance.", "Exercice avec le schéma 2 et trois litiges concrets."),
 ],
 'soutien': ["Fiche-lexique : palabre, médiation, alliance, libation, réconciliation.", "Schéma 1 à compléter."],
 'approfondissement': ["Interroger un sage sur les alliances et les rites de réconciliation de la région.", "Exposé sur une commission vérité dans un autre pays africain."],
 'evaluation': {
  'activites': [
   ("Définis : conflit ; mécanisme de prévention des conflits.", 2, "Conflit : opposition grave entre personnes ou groupes (1 pt) ; mécanisme de prévention : règles, pratiques et institutions pour éviter les conflits (1 pt)."),
   ("Cite trois mécanismes de prévention des conflits.", 1.5, "Alliances à plaisanterie, alliances matrimoniales, éducation et initiation, règles de la terre et tutorat, solidarité. 0,5 pt par mécanisme."),
   ("Décris les étapes de la palabre.", 2.5, "Exposé des parties par un porte-parole, audition des témoins, délibération des anciens, décision du chef, réconciliation publique. 0,5 pt par étape."),
   ("Explique la différence entre médiation et arbitrage.", 2, "Dans la médiation, un tiers rapproche les parties et propose des solutions (1 pt) ; dans l'arbitrage, un tiers (le chef, le conseil) décide et sa décision s'impose (1 pt)."),
  ],
  'situation': "Deux familles de ton village se disputent un héritage ; les jeunes des deux camps s'insultent et menacent d'en venir aux mains.",
  'consignes': [
   ("Identifie le type de conflit et l'instance traditionnelle qui doit le régler.", 2, "Un conflit entre familles lié à l'héritage (1 pt) ; il relève du chef de village et du conseil des anciens (1 pt)."),
   ("Explique comment les mécanismes traditionnels permettraient de le régler.", 4.5, "Une médiation par des personnes respectées (anciens, alliés, femmes) (1,5 pt) ; une palabre où chaque famille expose sa version et où les anciens délibèrent (1,5 pt) ; une décision suivie d'un rite de réconciliation : cola, repas, libation (1,5 pt)."),
   ("Propose deux activités pour promouvoir la paix entre les jeunes du village.", 3.5, "Une rencontre sportive ou culturelle commune ; un club de paix ou une causerie avec les sages ; une saynète sur le pardon (1,75 pt par activité, 2 attendues)."),
  ],
 },
 'valeurs': ["Paix, dialogue, pardon et réconciliation.", "Respect des aînés et des institutions.",
             "Liens avec l'EDHC (paix, droits de l'homme) et le français (jeu de rôle, argumentation)."],
}
