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
