# Fiches enseignant — Histoire 3e (lot 4 de la généralisation du modèle validé)
# Même format que fiches_h.py : étape = (moment, durée en min, stratégie, [activités du professeur],
# [réponses attendues des élèves], trace écrite)

PRES = "Présentation"
EVAL = "Évaluation"

FICHES = {}

# ------------------------------------------------------------------ T1-L1
FICHES['3e-h-t1-l1'] = {
 'materiel': ["carte de l'Afrique vers 1914 (carte 1)", "frise de la colonisation de la Côte d'Ivoire (frise 1)",
              "extraits du discours de Jules Ferry (1885) et de la réponse de Clemenceau", "photographie du palais du gouverneur à Bingerville",
              "papier millimétré pour l'axe chronologique"],
 'contexte': "des élèves de 3e 2 du lycée moderne d'Abobo regardent à la télévision un documentaire sur le cinquantenaire de l'indépendance de la Côte d'Ivoire.",
 'circonstance': "impressionnés par la cérémonie, ils se demandent comment et pourquoi leur pays est devenu une colonie.",
 'taches': ["définir l'impérialisme colonial et en identifier les causes", "analyser le processus de l'impérialisme en Afrique et les étapes de la colonisation de la Côte d'Ivoire",
            "construire un axe chronologique et apprécier les conséquences de la colonisation"],
 'prerequis': ["Les contacts entre la Côte d'Ivoire et l'Europe (4e).", "La révolution industrielle (4e).", "La construction d'un axe chronologique (6e)."],
 'seances': [
  {'titre': "L'impérialisme colonial et ses causes (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation (cinquantenaire de l'indépendance).", "« De quoi la Côte d'Ivoire s'est-elle libérée en 1960 ? »"], ["De la domination coloniale française."], "Introduction."),
   ("Développement · I. L'impérialisme colonial et ses causes", 35, "Étude de documents en groupes, mise en commun",
    ["Faire définir impérialisme et colonisation.", "Distribuer de courts extraits (Ferry, statistiques industrielles) ; chaque groupe relève une famille de causes."],
    ["L'impérialisme est la volonté de dominer d'autres peuples pour les exploiter ; la colonisation en est la mise en œuvre.",
     "Économiques : matières premières, débouchés, capitaux ; politiques : rivalités, prestige ; démographiques : forte natalité ; idéologiques : « mission civilisatrice », évangélisation."], "I. 1 à 5."),
   (EVAL, 12, "Travail individuel", ["Activité d'application I."], ["Définition et classement des cinq causes."], None),
  ]},
  {'titre': "Le processus de l'impérialisme en Afrique (II)", 'etapes': [
   (PRES, 5, "Rappel et question-problème", ["« Comment les Européens se sont-ils partagé l'Afrique ? »"], ["Par des explorations, une conférence, puis la conquête."], None),
   ("Développement · II. Le processus en Afrique", 38, "Exposé dialogué et lecture de la carte 1",
    ["Présenter les explorations et la conférence de Berlin ; faire expliquer la règle d'occupation effective.", "Faire lire la carte 1 : puissances, États indépendants, place de la France."],
    ["Berlin (1884 – 1885) fixe les règles du partage ; il faut occuper réellement un territoire pour le revendiquer.",
     "Course au clocher : traités puis conquête ; en 1914, seuls le Libéria et l'Éthiopie sont indépendants ; la France domine l'Afrique de l'Ouest."], "II. 1 à 3."),
   (EVAL, 12, "Travail individuel", ["Activité d'application II."], ["Occupation effective et course au clocher."], None),
  ]},
  {'titre': "Les étapes de la colonisation de la Côte d'Ivoire (III)", 'etapes': [
   (PRES, 5, "Question-problème", ["« En quelle année la Côte d'Ivoire devient-elle une colonie ? »"], ["En 1893."], None),
   ("Développement · III. Les étapes en Côte d'Ivoire", 35, "Lecture de la frise 1, construction d'un axe",
    ["Présenter les traités du littoral, les explorations et la création de la colonie ; évoquer les résistances.", "Faire construire l'axe chronologique de 1840 à 1960 à partir de la frise 1."],
    ["Traités de 1842 – 1843 ; Binger et Treich-Laplène (1887 – 1889) ; colonie le 10 mars 1893 ; Samory capturé en 1898 ; « pacification » d'Angoulvant (1908 – 1915).",
     "Capitales : Grand-Bassam, Bingerville (1900), Abidjan (1934) ; AOF organisée en 1904."], "III. 1 à 6."),
   (EVAL, 15, "Travail individuel", ["Activité d'application III (ordre chronologique)."], ["Traités → colonie → Samory → Bingerville → AOF → Abidjan."], None),
  ]},
  {'titre': "L'exploitation et les conséquences de la colonisation (IV, V)", 'etapes': [
   (PRES, 5, "Question-problème", ["« À qui profitaient les routes et le chemin de fer construits pendant la colonisation ? »"], ["D'abord à la colonie, pour exporter les produits."], None),
   ("Développement · IV et V. Exploitation et conséquences", 30, "Explication, tableau à deux colonnes",
    ["Expliquer l'administration, l'impôt de capitation, les cultures obligatoires et le travail forcé.", "Construire avec la classe le tableau des conséquences négatives et des héritages ambivalents."],
    ["Administration directe, code de l'indigénat ; impôt en argent qui oblige à produire pour l'exportation ; travail forcé sur les chantiers.",
     "Perte de souveraineté, morts, économie extravertie ; mais territoire unifié, infrastructures, écoles et élite qui conduira à l'indépendance."], "IV, V, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Causes, étapes et conséquences."], None),
  ]},
 ],
 'eclairage': [
  "La conférence de Berlin n'a pas tracé les frontières de l'Afrique : elle a fixé des règles ; les frontières résultent d'accords bilatéraux ultérieurs (par exemple franco-britannique pour la frontière ivoiro-ghanéenne).",
  "La Côte d'Ivoire fait partie de l'AOF dès sa création (1895) ; le décret de 1904 organise définitivement la fédération autour de Dakar.",
  "Après 1871, la France confie la garde de Grand-Bassam et d'Assinie au négociant Arthur Verdier, qui finance les missions de Treich-Laplène.",
  "Les résistances ont été nombreuses et longues : guerre des Baoulé (1893 – 1902), Samory (jusqu'en 1898), révolte des Abbey (1910).",
 ],
 'difficultes': [
  ("Croire que la conférence de Berlin a découpé l'Afrique.", "Relire la règle d'occupation effective ; montrer que les frontières sont fixées ensuite."),
  ("Confondre les capitales successives.", "Frise 1 : Grand-Bassam, Bingerville (1900), Abidjan (1934)."),
  ("Bilan de la colonisation uniquement positif.", "Question : « à qui profitaient les infrastructures ? » ; rappeler le travail forcé."),
 ],
 'soutien': ["Liste de dates à placer sur un axe déjà gradué.", "Tableau des causes à compléter avec des étiquettes."],
 'approfondissement': ["Exposé sur une résistance ivoirienne (Baoulé, Abbey, Samory).", "Comparer les discours de Ferry et de Clemenceau (1885)."],
 'evaluation': {
  'activites': [
   ("Définis : impérialisme colonial ; occupation effective.", 2, "Impérialisme colonial : politique par laquelle un État domine d'autres territoires et peuples pour les exploiter (1 pt) ; occupation effective : règle de Berlin selon laquelle il faut occuper réellement un territoire pour le revendiquer (1 pt)."),
   ("Cite une cause économique, une cause politique et une cause idéologique de l'impérialisme.", 1.5, "Économique : recherche de matières premières ou de débouchés ; politique : rivalités entre puissances ; idéologique : « mission civilisatrice ». 0,5 pt par cause."),
   ("Range dans l'ordre chronologique : création de la colonie ; traités de Bouët-Willaumez ; Abidjan chef-lieu ; capture de Samory.", 2, "Traités de Bouët-Willaumez (1842 – 1843) → création de la colonie (1893) → capture de Samory (1898) → Abidjan chef-lieu (1934). 0,5 pt par élément bien placé."),
   ("Explique comment l'impôt de capitation et le travail forcé ont servi l'exploitation coloniale.", 2.5, "L'impôt payé en argent oblige les paysans à produire pour l'exportation ou à travailler pour les colons (1,5 pt) ; le travail forcé fournit une main-d'œuvre gratuite pour les routes, le chemin de fer et les plantations (1 pt)."),
  ],
  'situation': "Lors d'un débat au club d'histoire, un camarade affirme que « la colonisation a été une bonne chose, puisqu'elle a construit des routes et des écoles ».",
  'consignes': [
   ("Indique deux étapes de la colonisation de la Côte d'Ivoire avec leurs dates.", 2, "Traités de Bouët-Willaumez (1842 – 1843) ; création de la colonie (10 mars 1893) ; on accepte la « pacification » d'Angoulvant (1908 – 1915). 1 pt par étape datée."),
   ("Explique deux conséquences négatives de la colonisation pour les Ivoiriens.", 4, "La perte de la souveraineté et la destruction des structures traditionnelles (2 pts) ; les souffrances du travail forcé et de la conquête, qui ont fait de nombreux morts (2 pts)."),
   ("Réponds à ton camarade en nuançant son affirmation.", 4, "Les routes et les écoles existent (1 pt), mais elles servaient d'abord à exploiter la colonie et ont été construites par le travail forcé (2 pts) ; la colonisation a aussi apporté la perte de liberté et l'exploitation (1 pt)."),
  ],
 },
 'valeurs': ["Respect de la dignité humaine et rejet du racisme.", "Fierté et mémoire des résistances africaines.",
             "Liens avec l'EDHC (droits de l'homme), le français (argumentation) et la géographie (carte de l'Afrique)."],
}

# ------------------------------------------------------------------ T1-L2
FICHES['3e-h-t1-l2'] = {
 'materiel': ["schéma des causes à l'indépendance (schéma 1)", "frise de la marche vers l'indépendance (frise 1)",
              "photographie de la marche des femmes sur Grand-Bassam", "extrait du discours de proclamation de l'indépendance (7 août 1960)",
              "papier millimétré pour l'axe chronologique"],
 'contexte': "le club d'histoire-géographie du collège Jules Ferry projette un film sur la célébration de la fête nationale ivoirienne.",
 'circonstance': "les élèves entendent des anecdotes sur la participation de leurs grands-parents à la lutte anticoloniale et veulent en savoir davantage.",
 'taches': ["expliquer les causes de la lutte pour l'indépendance", "identifier les principaux acteurs de la lutte anticolonialiste",
            "analyser le processus de la décolonisation et construire l'axe chronologique des évènements"],
 'prerequis': ["L'exploitation coloniale de la Côte d'Ivoire (leçon précédente).", "La Seconde Guerre mondiale (repères).", "La construction d'un axe chronologique."],
 'seances': [
  {'titre': "Les causes de la lutte (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation et recueil des représentations",
    ["Lire la situation ; demander ce que les grands-parents racontent de la période coloniale.", "« Pourquoi les Ivoiriens ont-ils lutté contre la colonisation ? »"], ["À cause du travail forcé, des injustices, de l'absence de liberté."], "Introduction."),
   ("Développement · I. Les causes", 35, "Lecture du schéma 1 et classement en tableau",
    ["Faire lire le schéma 1 de haut en bas.", "Faire classer les causes en internes et externes dans un tableau."],
    ["Internes : travail forcé, indigénat, impôt, discriminations contre les planteurs africains, élite instruite.",
     "Externes : Seconde Guerre mondiale, Charte de l'Atlantique (1941), ONU (1945), indépendances de l'Inde (1947) et du Ghana (1957)."], "I. 1 et 2."),
   (EVAL, 12, "Travail individuel", ["Activité d'application I."], ["Deux causes politiques, deux causes économiques ou sociales."], None),
  ]},
  {'titre': "Les acteurs de la lutte (II)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Qui a conduit la lutte pour l'indépendance ? »"], ["Houphouët-Boigny, le PDCI-RDA."], None),
   ("Développement · II. Les acteurs", 38, "Travail de groupes sur des fiches portraits, mise en commun",
    ["Chaque groupe présente un acteur : Houphouët-Boigny, SAA, PDCI-RDA, femmes de Grand-Bassam, autres militants.", "Faire relever le rôle de chacun."],
    ["Houphouët-Boigny : président du SAA, député (1945), auteur de la loi du 11 avril 1946, dirigeant du PDCI-RDA.",
     "SAA (1944) : planteurs africains ; PDCI (9 avril 1946), section du RDA (Bamako, octobre 1946) ; femmes : marche sur Grand-Bassam (décembre 1949)."], "II. 1 à 5."),
   (EVAL, 12, "Travail individuel", ["Activité d'application II."], ["Association acteur – rôle."], None),
  ]},
  {'titre': "Le processus de la décolonisation (III)", 'etapes': [
   (PRES, 5, "Question-problème", ["« L'indépendance a-t-elle été obtenue en une seule fois ? »"], ["Non, par étapes."], None),
   ("Développement · III. Le processus", 35, "Exposé dialogué, lecture de la frise 1",
    ["Présenter les quatre périodes ; faire expliquer le changement de stratégie de 1950.", "Faire dégager les caractères de la décolonisation ivoirienne."],
    ["Réformes (1944 – 1946) ; répression (1949 – 1950) ; collaboration et autonomie (loi-cadre 1956, référendum et République en 1958) ; indépendance (7 août 1960).",
     "Décolonisation surtout pacifique et négociée, rôle central d'Houphouët-Boigny, coopération avec la France."], "III. 1 à 5."),
   (EVAL, 15, "Travail individuel", ["Activité d'application III."], ["Trois étapes datées."], None),
  ]},
  {'titre': "L'axe chronologique et l'évaluation (IV)", 'etapes': [
   (PRES, 5, "Rappel", ["« Quelles dates retenir de 1944 à 1960 ? »"], ["1944, 1946, 1949, 1956, 1958, 1960."], None),
   ("Développement · IV. L'axe chronologique", 25, "Construction individuelle guidée",
    ["Faire construire l'axe (1 cm = 1 an) avec titre et légende.", "Comparer avec la frise 1."],
    ["Axe de 16 cm : SAA et Brazzaville (1944), PDCI, loi et RDA (1946), marche des femmes (1949), loi-cadre (1956), République (1958), indépendance (1960)."], "IV, conclusion."),
   (EVAL, 25, "Travail individuel", ["Activité d'application IV et situation d'évaluation de la leçon."], ["Acteurs, étapes et caractères de la décolonisation."], None),
  ]},
 ],
 'eclairage': [
  "La conférence de Brazzaville (1944) promet des réformes mais écarte « toute idée d'autonomie » : elle n'annonce pas l'indépendance.",
  "La loi du 11 avril 1946 abolit le travail forcé dans tous les territoires d'outre-mer ; Houphouët-Boigny en est le rapporteur.",
  "Le désapparentement d'octobre 1950 marque le passage d'une stratégie d'opposition à une stratégie de collaboration.",
  "En 1960, dix-sept États africains deviennent indépendants ; la Côte d'Ivoire entre à l'ONU le 20 septembre 1960.",
 ],
 'difficultes': [
  ("Confusion entre PDCI et RDA.", "Schéma : le RDA, mouvement interafricain ; le PDCI, sa section ivoirienne."),
  ("Confusion entre République (1958) et indépendance (1960).", "Frise 1 : autonomie dans la Communauté, puis souveraineté complète."),
  ("Idée d'une indépendance sans aucune violence.", "Rappeler la répression de 1949 – 1950 et la disparition de Biaka Boda."),
 ],
 'soutien': ["Fiche d'étiquettes (dates et évènements) à placer sur un axe gradué.", "Tableau acteurs – rôles à compléter."],
 'approfondissement': ["Recueillir le témoignage d'un aîné sur la période 1946 – 1960 et le comparer à la frise.", "Comparer la décolonisation ivoirienne et celle de la Guinée (« non » de 1958)."],
 'evaluation': {
  'activites': [
   ("Définis : décolonisation ; autonomie interne.", 2, "Décolonisation : processus par lequel une colonie obtient son indépendance (1 pt) ; autonomie interne : un gouvernement local gère les affaires intérieures, sans indépendance complète (1 pt)."),
   ("Cite deux causes internes et une cause externe de la lutte pour l'indépendance.", 1.5, "Internes : travail forcé, discriminations contre les planteurs africains (ou indigénat) ; externe : Seconde Guerre mondiale, Charte de l'Atlantique ou ONU. 0,5 pt par cause."),
   ("Associe chaque date à son évènement : 9 avril 1946 ; 11 avril 1946 ; décembre 1949 ; 7 août 1960.", 2, "Fondation du PDCI ; loi abolissant le travail forcé ; marche des femmes sur Grand-Bassam ; proclamation de l'indépendance. 0,5 pt par association."),
   ("Explique pourquoi Houphouët-Boigny choisit la collaboration avec la France à partir de 1950.", 2.5, "Après la répression de 1949 – 1950 (arrestations, morts) (1 pt), il estime que la négociation permettra d'obtenir des réformes et l'émancipation sans nouvelles victimes (1,5 pt)."),
  ],
  'situation': "Pendant la fête de l'indépendance, ton petit frère te demande pourquoi on dit que la Côte d'Ivoire a obtenu son indépendance « sans guerre ».",
  'consignes': [
   ("Cite deux acteurs de la lutte anticolonialiste et leur rôle.", 2, "Houphouët-Boigny : dirigeant de la lutte, auteur de la loi du 11 avril 1946 (1 pt) ; les femmes : marche sur Grand-Bassam en 1949 (1 pt) ; on accepte le SAA ou le PDCI-RDA."),
   ("Explique deux étapes du processus qui a conduit à l'indépendance.", 4, "La loi-cadre de 1956 donne l'autonomie interne (2 pts) ; le référendum de 1958 et la proclamation de la République préparent l'indépendance du 7 août 1960 (2 pts)."),
   ("Montre que cette indépendance a été surtout pacifique, mais pas sans sacrifices.", 4, "Elle a été négociée par étapes légales, sans guerre de libération (2 pts) ; mais la répression de 1949 – 1950 a fait des morts, des disparus et des prisonniers (2 pts)."),
  ],
 },
 'valeurs': ["Patriotisme et mémoire des combattants de la liberté.", "Rôle des femmes dans la vie publique.",
             "Liens avec l'EDHC (citoyenneté, symboles de la nation) et le français (récit, témoignage)."],
}

# ------------------------------------------------------------------ T1-L3 (leçon alternante : Biafra)
FICHES['3e-h-t1-l3'] = {
 'materiel': ["carte du Nigeria et du Biafra (carte 1)", "frise de 1960 à 1971 (frise 1)", "carte de l'Afrique de l'Ouest",
              "extrait de la déclaration de Gowon « ni vainqueur ni vaincu » (janvier 1970)", "photographie du pont aérien d'Uli (choisie avec précaution)"],
 'contexte': "des élèves de 3e 3 du lycée moderne de Koumassi visitent le quartier Biafra, à Treichville, où habite un camarade d'origine biafraise.",
 'circonstance': "touchés par des témoignages parfois difficiles à comprendre, ils veulent connaître les causes et les conséquences de la guerre du Biafra.",
 'taches': ["définir la crise sociopolitique et en identifier les causes en Afrique", "localiser la zone de conflit et analyser la guerre du Biafra",
            "apprécier les conséquences de la guerre et le processus de réconciliation"],
 'prerequis': ["La colonisation et la décolonisation de l'Afrique (leçons précédentes).", "La lecture d'une carte de l'Afrique de l'Ouest.", "La notion de droits humains (EDHC)."],
 'seances': [
  {'titre': "La notion de crise, le cadre et les causes (I, II)", 'etapes': [
   (PRES, 8, "Lecture de la situation et questionnement",
    ["Lire la situation ; « Pourquoi un quartier d'Abidjan porte-t-il le nom d'une région du Nigeria ? »"], ["À cause d'une guerre au Nigeria et de l'accueil de réfugiés."], "Introduction."),
   ("Développement · I et II. Notion, cadre et causes", 35, "Exposé dialogué, lecture de la carte 1",
    ["Faire définir la crise sociopolitique et énumérer ses formes et ses causes en Afrique.", "Faire localiser le Biafra, les trois grands peuples et le pétrole ; expliquer les causes de la guerre."],
    ["Troubles graves qui menacent la stabilité d'un État ; causes : héritage colonial, luttes pour le pouvoir, ethnicité manipulée, pauvreté, ressources, ingérences.",
     "Biafra : ancienne région orientale, à l'est du Niger, peuplée surtout d'Igbo, riche en pétrole ; causes : rivalités, coups d'État de 1966, massacres d'Igbo, pétrole, sécession du 30 mai 1967."], "I et II."),
   (EVAL, 12, "Travail individuel", ["Activités d'application I et II."], ["Définition, trois causes, localisation."], None),
  ]},
  {'titre': "Le déroulement et les atteintes aux droits humains (III, IV)", 'etapes': [
   (PRES, 5, "Rappel et question-problème", ["« Comment le gouvernement fédéral a-t-il réagi à la sécession ? »"], ["Par la guerre."], None),
   ("Développement · III et IV. Déroulement, atteintes aux droits humains", 38, "Lecture de la frise 1, étude de documents",
    ["Faire placer les étapes sur la frise ; présenter les soutiens extérieurs.", "Faire relever les atteintes aux droits humains (famine, massacres, bombardements, enfants soldats)."],
    ["Offensive de juillet 1967, prise des villes, blocus et famine (1968 – 1969), capitulation le 15 janvier 1970 ; Grande-Bretagne et URSS pour Lagos ; Biafra reconnu par cinq États, dont la Côte d'Ivoire.",
     "Famine utilisée comme arme, massacres de civils, bombardements de marchés, enrôlement d'enfants, déplacements forcés."], "III et IV."),
   (EVAL, 12, "Travail individuel", ["Activités d'application III et IV."], ["Trois dates ; deux atteintes aux droits humains."], None),
  ]},
  {'titre': "La résolution et les conséquences (V, VI)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Comment réconcilier un pays après une guerre civile ? »"], ["Par le pardon, la reconstruction, la justice."], None),
   ("Développement · V et VI. Résolution et conséquences", 30, "Explication, tableau des conséquences",
    ["Présenter les médiations de l'OUA et la fin de la guerre ; expliquer « ni vainqueur ni vaincu » et les « 3 R ».", "Construire le tableau des conséquences humaines, politiques, économiques et humanitaires."],
    ["Échec des médiations ; victoire fédérale ; réconciliation, reconstruction, réhabilitation.",
     "Plus d'un million de morts selon les estimations courantes ; unité maintenue ; ruine de l'Est ; naissance de Médecins sans frontières (1971)."], "V, VI, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Causes, déroulement et conséquences."], None),
  ]},
 ],
 'eclairage': [
  "Le découpage du 27 mai 1967 en douze États enlève à la région orientale la côte et l'essentiel du pétrole : il précipite la sécession.",
  "Le Biafra a été reconnu par la Tanzanie, le Gabon, la Côte d'Ivoire, la Zambie (1968) et Haïti (1969) ; la France l'a soutenu sans le reconnaître.",
  "Les estimations du nombre de morts vont de 500 000 à plus de 2 millions ; la plupart sont des civils morts de faim et de maladie.",
  "L'expérience du Biafra a contribué à l'idée d'une action humanitaire indépendante des États (Médecins sans frontières, 1971).",
 ],
 'difficultes': [
  ("Localisation erronée du Biafra.", "Carte 1 : sud-est du Nigeria, à l'est du Niger, jusqu'à la frontière camerounaise."),
  ("Confusion entre les protagonistes.", "Tableau : Gowon (fédéral, Lagos) / Ojukwu (Biafra, Enugu)."),
  ("Explication purement ethnique de la guerre.", "Rappeler le rôle des coups d'État, des choix politiques et du pétrole."),
 ],
 'soutien': ["Carte muette du Nigeria à compléter (Biafra, Lagos, Enugu, Port Harcourt, Niger).", "Frise à compléter avec quatre dates données."],
 'approfondissement': ["Exposé sur la naissance de l'action humanitaire moderne.", "Comparer la guerre du Biafra et le génocide des Tutsi au Rwanda (leçon alternante)."],
 'evaluation': {
  'activites': [
   ("Définis : crise sociopolitique ; sécession.", 2, "Crise sociopolitique : période de troubles graves qui menace la stabilité d'un État (1 pt) ; sécession : séparation d'une région qui veut former un État indépendant (1 pt)."),
   ("Localise le Biafra et cite ses deux principales richesses ou caractéristiques.", 1.5, "Sud-est du Nigeria, à l'est du Niger (0,5 pt) ; peuplé surtout d'Igbo (0,5 pt) ; riche en pétrole (0,5 pt)."),
   ("Range dans l'ordre : capitulation du Biafra ; coups d'État ; proclamation du Biafra ; indépendance du Nigeria.", 2, "Indépendance du Nigeria (1960) → coups d'État (1966) → proclamation du Biafra (30 mai 1967) → capitulation (15 janvier 1970). 0,5 pt par élément bien placé."),
   ("Explique pourquoi la famine a fait plus de victimes que les combats.", 2.5, "Le blocus fédéral empêchait l'arrivée de vivres et de médicaments (1,5 pt) ; la population encerclée, surtout les enfants, est morte de faim et de maladie (1 pt)."),
  ],
  'situation': "Un camarade d'origine nigériane te dit que son grand-père a fui l'Est du Nigeria en 1968 et qu'il a été accueilli en Côte d'Ivoire.",
  'consignes': [
   ("Indique deux causes de la guerre du Biafra.", 2, "Les rivalités entre grands peuples aggravées par les coups d'État et les massacres de 1966 (1 pt) ; l'enjeu du pétrole du delta du Niger (1 pt)."),
   ("Explique pourquoi des habitants de l'Est ont fui en 1968.", 4, "La guerre et la prise des villes par l'armée fédérale (2 pts) ; le blocus et la famine qui menaçaient leur vie (2 pts)."),
   ("Montre que la Côte d'Ivoire a été concernée par cette guerre.", 4, "Elle a reconnu le Biafra en 1968 (1,5 pt) ; elle a accueilli Ojukwu en exil et des réfugiés (1,5 pt) ; le quartier Biafra de Treichville en garde la mémoire (1 pt)."),
  ],
 },
 'valeurs': ["Respect de la vie et de la dignité humaine.", "Tolérance, refus de la haine ethnique, solidarité avec les réfugiés.",
             "Liens avec l'EDHC (droits humains, droit humanitaire) et la géographie (Nigeria, pétrole)."],
}

# ------------------------------------------------------------------ T1-L3b (leçon alternante : Rwanda)
FICHES['3e-h-t1-l3b'] = {
 'materiel': ["carte du Rwanda et des Grands Lacs en 1994 (carte 1)", "frise de 1959 à 2015 (frise 1)", "article 2 de la Convention de l'ONU sur le génocide (1948)",
              "photographie d'un mémorial (sans corps)", "court témoignage de rescapé adapté à l'âge des élèves"],
 'contexte': "des élèves de 3e 4 du collège moderne Nangui Abrogoua regardent à la télévision un documentaire sur la guerre du Rwanda.",
 'circonstance': "choqués, l'un d'eux s'écrie : « Ces gens étaient de véritables sauvages ! » ; les élèves décident de comprendre ce conflit.",
 'taches': ["définir la crise sociopolitique et identifier ses causes", "localiser les zones de conflit et analyser la guerre et le génocide",
            "apprécier les conséquences et le processus de résolution"],
 'prerequis': ["La colonisation et la décolonisation de l'Afrique.", "La notion de droits humains (EDHC).", "La lecture d'une carte et d'une frise."],
 'seances': [
  {'titre': "Notion, cadre et causes (I, II, III)", 'etapes': [
   (PRES, 8, "Lecture de la situation et débat court",
    ["Lire la situation ; noter au tableau la phrase « de véritables sauvages ».", "« Cette affirmation est-elle juste ? Comment le vérifier ? »"], ["Il faut connaître les causes et l'organisation des massacres."], "Introduction."),
   ("Développement · I, II et III. Notion, cadre et causes", 35, "Exposé dialogué, lecture de la carte 1",
    ["Faire définir la crise sociopolitique ; localiser le Rwanda et ses voisins.", "Expliquer comment la colonisation a figé les catégories ; faire relever les causes de la guerre et du génocide."],
    ["Petit pays enclavé des Grands Lacs, capitale Kigali ; même langue et même culture pour tous les Rwandais.",
     "Carte d'identité ethnique (années 1930), discriminations depuis 1959, refus du retour des réfugiés, guerre de 1990, propagande, attentat du 6 avril 1994."], "I, II, III."),
   (EVAL, 12, "Travail individuel", ["Activités d'application I à III."], ["Définition, localisation, rôle de la colonisation."], None),
  ]},
  {'titre': "Le déroulement et les atteintes aux droits humains (IV, V)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Comment passe-t-on d'une guerre à un génocide ? »"], ["Par la propagande, l'organisation des tueurs, un prétexte."], None),
   ("Développement · IV et V. Déroulement et génocide", 38, "Lecture de la frise 1 et du tableau, étude de la Convention de 1948",
    ["Faire placer les étapes de 1990 à juillet 1994.", "Faire lire l'article 2 de la Convention et justifier l'emploi du mot génocide ; relever les preuves de la planification."],
    ["FPR (1990), Arusha (1993), attentat (6 avril 1994), génocide (7 avril – juillet 1994), Kigali (4 juillet 1994).",
     "Intention de détruire les Tutsi ; listes, barrages, distribution d'armes, milices, radio ; entre 800 000 et plus d'un million de morts."], "IV, V."),
   (EVAL, 12, "Travail individuel", ["Activités d'application IV et V."], ["Déroulement ; deux atteintes ; justification du terme génocide."], None),
  ]},
  {'titre': "La résolution et les conséquences (VI, VII)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Comment juger et réconcilier après un génocide ? »"], ["Par la justice, la mémoire, l'unité nationale."], None),
   ("Développement · VI et VII. Résolution et conséquences", 30, "Explication, tableau des conséquences",
    ["Présenter l'échec de la communauté internationale, la victoire du FPR, le TPIR et les gacaca.", "Construire le tableau des conséquences (humaines, politiques, régionales, juridiques)."],
    ["MINUAR réduite ; FPR vainqueur ; TPIR (Arusha, 1994 – 2015) ; gacaca (2002 – 2012) ; suppression de la mention ethnique ; 7 avril.",
     "Morts, orphelins, traumatismes ; réfugiés et guerres des Grands Lacs ; développement de la justice internationale."], "VI, VII, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Causes, génocide, conséquences."], None),
  ]},
 ],
 'eclairage': [
  "L'ONU parle du « génocide perpétré contre les Tutsi » ; des Hutu opposés au génocide ont aussi été tués, mais comme opposants.",
  "Le général Dallaire avait alerté l'ONU dès janvier 1994 ; le 21 avril, le Conseil de sécurité réduit la MINUAR à environ 270 hommes.",
  "Les estimations vont d'environ 800 000 victimes à plus d'un million (1 074 017 selon le recensement rwandais de 2002).",
  "Le rapport Duclert (2021) conclut à des responsabilités « lourdes et accablantes » de la France, sans complicité de génocide.",
 ],
 'difficultes': [
  ("Idée d'une haine ancestrale entre Hutu et Tutsi.", "Rappeler la même langue, la même culture et le rôle de la colonisation."),
  ("Confusion entre guerre civile et génocide.", "Définitions comparées : combats entre armées / extermination de civils."),
  ("Réactions émotionnelles fortes.", "Choisir des documents adaptés ; laisser un temps de parole encadré."),
 ],
 'soutien': ["Carte muette à compléter (Rwanda, Kigali, Ouganda, Zaïre, Tanzanie, Burundi).", "Frise à compléter avec cinq dates données."],
 'approfondissement': ["Exposé sur la justice gacaca.", "Recherche sur les « Justes » rwandais qui ont sauvé des Tutsi."],
 'evaluation': {
  'activites': [
   ("Définis : génocide ; propagande.", 2, "Génocide : crime commis dans l'intention de détruire, en tout ou en partie, un groupe national, ethnique, racial ou religieux (1 pt) ; propagande : diffusion organisée d'idées pour influencer l'opinion (1 pt)."),
   ("Situe le Rwanda et cite trois pays voisins.", 1.5, "Petit pays enclavé d'Afrique centrale, région des Grands Lacs (0,5 pt) ; trois voisins parmi l'Ouganda, la Tanzanie, le Burundi, la RD Congo (1 pt)."),
   ("Associe chaque date à son évènement : 1er octobre 1990 ; 6 avril 1994 ; 4 juillet 1994 ; novembre 1994.", 2, "Attaque du FPR ; attentat contre l'avion du président ; prise de Kigali par le FPR ; création du TPIR. 0,5 pt par association."),
   ("Explique le rôle de la radio dans le génocide.", 2.5, "La RTLM a diffusé la haine en présentant les Tutsi comme des ennemis (1,5 pt) et a appelé au meurtre pendant les massacres (1 pt)."),
  ],
  'situation': "Après un documentaire sur le Rwanda, un camarade affirme que « ces massacres sont arrivés tout seuls, à cause d'une haine très ancienne ».",
  'consignes': [
   ("Indique deux causes du génocide.", 2, "La division figée par la colonisation (carte d'identité ethnique) (1 pt) ; la propagande de haine et la volonté des extrémistes de garder le pouvoir (1 pt)."),
   ("Montre, par deux arguments, que le génocide a été organisé.", 4, "Les listes de victimes, les barrages et la distribution d'armes (2 pts) ; la participation des autorités, de l'armée, des milices et les appels de la radio (2 pts)."),
   ("Réponds à ton camarade en expliquant pourquoi son affirmation est fausse.", 4, "Les Rwandais partageaient la même langue et la même culture : la division a été construite par la colonisation et la politique (2 pts) ; le génocide a été préparé et organisé par des responsables politiques, il n'est pas « arrivé tout seul » (2 pts)."),
  ],
 },
 'valeurs': ["Respect de la dignité humaine, refus du racisme et des discours de haine.", "Devoir de mémoire et vigilance citoyenne.",
             "Liens avec l'EDHC (droits humains), le français (témoignage) et la géographie (Afrique centrale)."],
}

# ------------------------------------------------------------------ T2-L1
FICHES['3e-h-t2-l1'] = {
 'materiel': ["planisphère des deux camps (carte 1)", "frise de la guerre (frise 1)", "affiche de recrutement de tirailleurs ou photographie de tirailleurs",
              "photographie de l'entrée du camp d'Auschwitz-Birkenau", "tableau des pertes humaines par pays (manuel)"],
 'contexte': "des élèves de 3e 2 du groupe scolaire Lavoisier se souviennent des récits d'un grand-père, ancien combattant de la guerre de 1939 à 1945.",
 'circonstance': "ils veulent comprendre les causes et les conséquences de cette guerre qui a tant marqué leur grand-père.",
 'taches': ["identifier les causes de la Deuxième Guerre mondiale et localiser les belligérants", "analyser les caractères de la guerre et caractériser l'Holocauste",
            "apprécier les conséquences de la guerre, notamment pour l'Afrique"],
 'prerequis': ["La colonisation de la Côte d'Ivoire (thème 1).", "La lecture d'un planisphère.", "La notion de génocide (leçon sur le Rwanda, si elle a été traitée)."],
 'seances': [
  {'titre': "Les causes de la guerre (I)", 'etapes': [
   (PRES, 8, "Lecture de la situation, recueil de souvenirs familiaux",
    ["Lire la situation ; « Que savez-vous des tirailleurs africains ? »"], ["Ils ont combattu pour la France pendant les guerres mondiales."], "Introduction."),
   ("Développement · I. Les causes", 35, "Exposé dialogué, classement des causes",
    ["Présenter les causes lointaines (Versailles, crise de 1929, totalitarismes, SDN) et les agressions des années 1930.", "Faire distinguer causes lointaines et cause immédiate."],
    ["Lointaines : traité de Versailles, crise de 1929, montée du fascisme et du nazisme, faiblesse de la SDN.",
     "Immédiate : invasion de la Pologne le 1er septembre 1939 ; déclarations de guerre du 3 septembre."], "I. 1 à 3."),
   (EVAL, 12, "Travail individuel", ["Activité d'application I."], ["Classement des causes."], None),
  ]},
  {'titre': "Belligérants, régions touchées et caractères (II, III)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Pourquoi parle-t-on de guerre mondiale ? »"], ["Elle touche le monde entier."], None),
   ("Développement · II et III. Belligérants et caractères", 38, "Lecture de la carte 1 et de la frise 1",
    ["Faire identifier les deux camps et les six lieux de la carte.", "Faire dégager les deux phases et les caractères (mondiale, totale, idéologique, d'anéantissement)."],
    ["Axe : Allemagne, Italie, Japon ; Alliés : Royaume-Uni, France libre, URSS, États-Unis, Chine ; l'Afrique fournit soldats et produits.",
     "Victoires de l'Axe jusqu'en 1942 ; tournant de Midway, El-Alamein et Stalingrad ; victoires alliées jusqu'en 1945 ; civils pris pour cibles ; bombes atomiques."], "II et III."),
   (EVAL, 12, "Travail individuel", ["Activités d'application II et III."], ["Deux camps, deux régions ; guerre totale."], None),
  ]},
  {'titre': "L'Holocauste (IV)", 'etapes': [
   (PRES, 5, "Lecture d'un document", ["Montrer la photographie d'Auschwitz-Birkenau ; « Qu'était ce lieu ? »"], ["Un camp d'extermination."], None),
   ("Développement · IV. L'Holocauste", 35, "Exposé dialogué, frise des étapes de la persécution",
    ["Présenter les étapes : exclusion (lois de Nuremberg, 1935), ghettos, fusillades, camps d'extermination.", "Faire définir le génocide et le crime contre l'humanité."],
    ["Environ 6 millions de Juifs d'Europe exterminés par les nazis au nom d'une idéologie raciste.",
     "Tsiganes, handicapés, opposants et prisonniers soviétiques aussi massacrés ; génocide et crime contre l'humanité."], "IV."),
   (EVAL, 15, "Travail individuel", ["Activité d'application IV."], ["Définition et deux étapes."], None),
  ]},
  {'titre': "Les conséquences de la guerre (V)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Le monde de 1945 ressemble-t-il à celui de 1939 ? »"], ["Non : destructions, nouvelles puissances, ONU."], None),
   ("Développement · V. Les conséquences", 30, "Tableau des conséquences",
    ["Construire le tableau : humaines, matérielles, politiques, nouvelle organisation du monde, Afrique."],
    ["50 à 60 millions de morts selon les estimations courantes ; Europe ruinée, plan Marshall ; États-Unis et URSS superpuissances ; ONU, Nuremberg, DUDH ; puissances coloniales affaiblies, réformes et nationalismes en Afrique."], "V, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Causes, caractères et conséquences pour l'Afrique."], None),
  ]},
 ],
 'eclairage': [
  "La guerre commence en Asie dès 1937 (invasion de la Chine par le Japon) ; la date de 1939 correspond au début de la guerre en Europe.",
  "Les estimations du bilan humain vont de 50 à plus de 70 millions de morts selon la prise en compte des victimes chinoises et soviétiques.",
  "L'AEF se rallie à la France libre dès août 1940 (Félix Éboué, au Tchad) ; l'AOF, fidèle à Vichy, rejoint les Alliés en novembre 1942.",
  "Le 1er décembre 1944, à Thiaroye (Sénégal), des tirailleurs rapatriés qui réclamaient leurs soldes sont tués par l'armée française.",
 ],
 'difficultes': [
  ("Confusion entre les deux guerres mondiales.", "Frise comparée des deux conflits."),
  ("Oubli de la participation africaine.", "Carte 1 et documents sur les tirailleurs."),
  ("Confusion entre camps de concentration et d'extermination.", "Tableau comparatif."),
 ],
 'soutien': ["Planisphère muet à colorier (Axe, Alliés).", "Frise à compléter avec six dates données."],
 'approfondissement': ["Exposé sur les tirailleurs africains et le massacre de Thiaroye.", "Recherche sur un « Juste parmi les nations »."],
 'evaluation': {
  'activites': [
   ("Définis : guerre totale ; Shoah.", 2, "Guerre totale : guerre qui mobilise toutes les ressources d'un pays et frappe aussi les civils (1 pt) ; Shoah : extermination d'environ 6 millions de Juifs d'Europe par les nazis (1 pt)."),
   ("Cite deux pays de l'Axe et deux pays alliés.", 1, "Axe : Allemagne, Italie ou Japon (0,5 pt) ; Alliés : Royaume-Uni, URSS, États-Unis, France ou Chine (0,5 pt)."),
   ("Range dans l'ordre : Stalingrad ; invasion de la Pologne ; débarquement de Normandie ; Pearl Harbor ; capitulation du Japon.", 2.5, "Invasion de la Pologne (1939) → Pearl Harbor (1941) → Stalingrad (1943) → Normandie (1944) → capitulation du Japon (1945). 0,5 pt par élément bien placé."),
   ("Explique une cause lointaine et la cause immédiate de la guerre.", 2.5, "Cause lointaine : le traité de Versailles, jugé injuste par les Allemands, ou la crise de 1929 qui favorise les nazis (1,5 pt) ; cause immédiate : l'invasion de la Pologne le 1er septembre 1939 (1 pt)."),
  ],
  'situation': "Ton grand-père, ancien tirailleur, te dit : « Nous, les Africains, nous avons aussi gagné cette guerre, et elle a changé notre pays. »",
  'consignes': [
   ("Montre que l'Afrique a participé à la Deuxième Guerre mondiale.", 2, "Elle a fourni des soldats, les tirailleurs (1 pt), et des produits ainsi que des bases militaires (1 pt)."),
   ("Explique deux caractères de cette guerre.", 4, "Guerre mondiale : elle touche tous les continents et océans (2 pts) ; guerre totale : elle mobilise toutes les ressources et frappe les civils (2 pts)."),
   ("Explique comment cette guerre « a changé » la Côte d'Ivoire.", 4, "Elle a affaibli la France et réveillé les revendications des colonisés (2 pts) ; elle a conduit aux réformes de 1944 – 1946 (Brazzaville, abolition du travail forcé), premières étapes vers l'indépendance (2 pts)."),
  ],
 },
 'valeurs': ["Paix, respect de la vie et de la dignité humaine.", "Mémoire des combattants africains ; refus du racisme et de l'antisémitisme.",
             "Liens avec l'EDHC (droits de l'homme), la géographie (planisphère) et le français (témoignage)."],
}

# ------------------------------------------------------------------ T2-L2
FICHES['3e-h-t2-l2'] = {
 'materiel': ["organigramme de l'ONU (schéma 1)", "graphique du nombre d'États membres (graphique 1)", "extraits de la Charte (préambule, article 1)",
              "articles 1 à 5 de la Déclaration universelle des droits de l'homme", "photographie d'une séance du Conseil de sécurité"],
 'contexte': "des élèves de 3e 7 du lycée moderne d'Angré discutent du rôle de l'ONU.",
 'circonstance': "certains affirment qu'elle n'a jamais servi à rien et reprennent le mot de De Gaulle, qui la traitait de « machin » en 1960 ; d'autres ne sont pas d'accord.",
 'taches': ["définir l'ONU et décrire sa création", "expliquer ses objectifs et principes, décrire ses organes et construire son organigramme",
            "réaliser un tableau des succès et des échecs et apprécier ses actions"],
 'prerequis': ["La Deuxième Guerre mondiale et ses conséquences (leçon précédente).", "La notion de droits de l'homme (EDHC).", "La lecture d'un graphique."],
 'seances': [
  {'titre': "Création, objectifs et principes (I, II)", 'etapes': [
   (PRES, 8, "Lecture de la situation et débat court",
    ["Lire la situation ; « L'ONU est-elle un “machin” inutile ? » ; noter les avis au tableau."], ["Avis partagés : utile pour la paix, inutile face aux guerres."], "Introduction."),
   ("Développement · I et II. Création, objectifs et principes", 35, "Exposé dialogué, lecture du graphique 1 et d'extraits de la Charte",
    ["Présenter les étapes de la création ; faire lire le graphique 1.", "Faire relever les objectifs et les principes dans l'article 1 de la Charte."],
    ["Échec de la SDN ; Charte de l'Atlantique (1941) ; San Francisco (26 juin 1945) ; entrée en vigueur (24 octobre 1945) ; 51 puis 193 membres.",
     "Paix et sécurité, relations amicales, coopération, droits de l'homme ; égalité souveraine, règlement pacifique, non-recours à la force, non-ingérence."], "I et II."),
   (EVAL, 12, "Travail individuel", ["Activités d'application I et II."], ["Définition, dates, siège, membres ; objectifs et principes."], None),
  ]},
  {'titre': "Les organes et l'organigramme (III, IV)", 'etapes': [
   (PRES, 5, "Question-problème", ["« Qui décide à l'ONU ? »"], ["L'Assemblée générale et le Conseil de sécurité."], None),
   ("Développement · III et IV. Organes et organigramme", 38, "Travail de groupes, construction de l'organigramme",
    ["Chaque groupe présente un organe (composition, rôle).", "Construire l'organigramme au tableau à partir du schéma 1 ; rattacher les institutions à leur domaine."],
    ["Assemblée générale (tous les États) ; Conseil de sécurité (15 membres, 5 permanents avec veto) ; Secrétariat ; CIJ (La Haye) ; ECOSOC (54 membres) ; Conseil de tutelle (suspendu).",
     "UNESCO : éducation, science, culture ; OMS : santé ; FAO : alimentation ; UNICEF : enfance ; HCR : réfugiés."], "III et IV."),
   (EVAL, 12, "Travail individuel", ["Activités d'application III et IV."], ["Rôle du Conseil de sécurité ; institutions et domaines."], None),
  ]},
  {'titre': "La DUDH et le bilan de l'ONU (V, VI)", 'etapes': [
   (PRES, 5, "Lecture de l'article 1 de la DUDH", ["« Que signifie “libres et égaux en dignité et en droits” ? »"], ["Tous les êtres humains ont les mêmes droits."], None),
   ("Développement · V et VI. DUDH, succès et échecs", 30, "Lecture de documents, tableau synoptique",
    ["Présenter la DUDH (10 décembre 1948) et faire relever des droits.", "Construire le tableau des succès et des échecs ; revenir au débat de la situation."],
    ["Droit à la vie, à la liberté, égalité devant la loi, interdiction de l'esclavage et de la torture, droit à l'éducation.",
     "Succès : pas de guerre mondiale, décolonisation, ONUCI, santé ; échecs : Rwanda, veto, dépendance financière, pas de siège permanent africain."], "V, VI, conclusion."),
   (EVAL, 20, "Travail individuel", ["Situation d'évaluation de la leçon."], ["Organes, bilan nuancé."], None),
  ]},
 ],
 'eclairage': [
  "La Charte est signée le 26 juin 1945 par 50 États ; la Pologne la signe ensuite et compte parmi les 51 membres fondateurs.",
  "Le Conseil de sécurité est passé de 11 à 15 membres en 1965 ; l'Afrique y dispose de trois sièges non permanents.",
  "Les institutions spécialisées (UNESCO, OMS, FAO) sont autonomes ; les fonds et programmes (UNICEF, PNUD, PAM, HCR) dépendent de l'Assemblée générale.",
  "António Guterres achève son mandat le 31 décembre 2026 ; vérifier le nom de son successeur avant d'en parler en classe.",
 ],
 'difficultes': [
  ("Confusion entre Assemblée générale et Conseil de sécurité.", "Tableau comparatif : composition, vote, pouvoirs."),
  ("Croire que l'ONU possède sa propre armée.", "Les Casques bleus sont prêtés par les États."),
  ("Jugement tout positif ou tout négatif.", "Tableau synoptique avec exemples précis."),
 ],
 'soutien': ["Organigramme à compléter avec des étiquettes.", "Liste de sigles à associer à leur domaine."],
 'approfondissement': ["Exposé sur l'ONUCI en Côte d'Ivoire.", "Débat : faut-il donner un siège permanent à l'Afrique ?"],
 'evaluation': {
  'activites': [
   ("Définis : ONU ; droit de veto.", 2, "ONU : organisation internationale qui regroupe presque tous les États pour maintenir la paix et développer la coopération (1 pt) ; droit de veto : droit d'un membre permanent du Conseil de sécurité de bloquer une décision (1 pt)."),
   ("Donne la date de signature de la Charte, le siège de l'ONU et le nombre de ses membres.", 1.5, "26 juin 1945 à San Francisco ; New York ; 193 États. 0,5 pt par élément."),
   ("Associe chaque organisme à son domaine : OMS ; UNESCO ; FAO ; HCR ; UNICEF.", 2.5, "Santé ; éducation, science et culture ; alimentation et agriculture ; réfugiés ; enfance. 0,5 pt par association."),
   ("Explique pourquoi le nombre d'États membres a beaucoup augmenté entre 1955 et 1975.", 2, "La décolonisation (1 pt) : de nombreux pays d'Afrique et d'Asie devenus indépendants, dont la Côte d'Ivoire en 1960, sont entrés à l'ONU (1 pt)."),
  ],
  'situation': "Ton cousin affirme : « L'ONU ne sert à rien, c'est un “machin”, comme disait De Gaulle. »",
  'consignes': [
   ("Cite deux organes principaux de l'ONU et leur rôle.", 2, "Assemblée générale : réunit tous les États, discute et vote le budget (1 pt) ; Conseil de sécurité : maintient la paix (1 pt) ; on accepte le Secrétariat, la CIJ ou l'ECOSOC."),
   ("Présente deux succès de l'ONU, dont un en Afrique.", 4, "L'ONUCI a contribué au retour de la paix en Côte d'Ivoire (2 pts) ; l'ONU a soutenu la décolonisation ou éradiqué la variole (2 pts)."),
   ("Réponds à ton cousin par une appréciation nuancée.", 4, "L'ONU a des limites : impuissance au Rwanda, blocage par le veto (2 pts) ; mais elle a évité une nouvelle guerre mondiale et agit pour la santé, l'éducation et les réfugiés : elle n'est pas inutile (2 pts)."),
  ],
 },
 'valeurs': ["Paix, coopération entre les peuples, respect des droits de l'homme.", "Esprit critique et argumentation nuancée.",
             "Liens avec l'EDHC (DUDH), la géographie (mondialisation) et le français (débat argumenté)."],
}
