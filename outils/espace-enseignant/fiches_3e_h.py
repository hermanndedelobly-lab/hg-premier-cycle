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
