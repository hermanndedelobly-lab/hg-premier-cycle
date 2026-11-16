# Guide de l\'enseignant de 6e (page d\'accueil de l\'Espace enseignant)

def _ul(items):
    return '<ul>\n' + ''.join('<li>' + i + '</li>\n' for i in items) + '</ul>\n'

def _tab(ent, lignes):
    h = '<div class="tbl"><table>\n<thead><tr>' + ''.join('<th>' + e + '</th>' for e in ent) + '</tr></thead>\n<tbody>'
    for l in lignes:
        h += '<tr>' + ''.join('<td>' + str(c) + '</td>' for c in l) + '</tr>\n'
    return h + '</tbody></table></div>\n'

def guide_html(c):
    h = '<p><em>Cet espace est destiné au professeur. Il complète les cours de l\'élève par une fiche de préparation détaillée pour chacune des 17 leçons de 6e, une progression annuelle, des conseils de conduite de classe et des évaluations avec barème.</em></p>\n'

    h += '<h3>1. Comment utiliser l\'Espace enseignant</h3>\n'
    h += _ul([
        '<strong>Avant la leçon :</strong> lire la fiche (analyse de la situation, prérequis, éclairage scientifique) et préparer le matériel indiqué.',
        '<strong>Pendant la leçon :</strong> suivre le déroulement séance par séance ; les réponses attendues aident à conduire le questionnement ; la trace écrite à faire copier est celle du cours de l\'élève.',
        '<strong>Après la leçon :</strong> utiliser l\'évaluation sur 20 (activités d\'application et situation d\'évaluation, avec corrigé et barème), puis remplir le bilan de la séance.',
        '<strong>Partout :</strong> chaque fiche peut être téléchargée, partagée ou imprimée en PDF avec le bouton prévu en haut de page.',
    ])

    h += '<h3>2. Rappels sur l\'approche par les compétences (APC)</h3>\n'
    h += '<p>Le programme éducatif de 6e est organisé en <strong>compétences</strong>, chacune déclinée en <strong>thèmes</strong> puis en <strong>leçons</strong>. Chaque leçon part d\'une <strong>situation d\'apprentissage</strong> qui donne du sens aux savoirs et place l\'élève au centre de l\'activité.</p>\n'
    h += _ul([
        '<strong>La situation d\'apprentissage</strong> comprend un <em>contexte</em> (le cadre de vie de l\'élève), une <em>circonstance</em> (le fait déclencheur) et des <em>tâches</em> (ce que les élèves vont faire, formulées à partir des habiletés).',
        '<strong>Les habiletés</strong> sont des verbes d\'action (définir, identifier, localiser, expliquer, construire…) associés à des contenus : ce sont les objectifs observables de la leçon.',
        '<strong>Les trois moments didactiques :</strong> la <em>présentation</em> (rappel des prérequis, découverte de la situation, émergence des représentations), le <em>développement</em> (construction des savoirs par des activités, partie par partie) et l\'<em>évaluation</em> (activités d\'application et, en fin de leçon, situation d\'évaluation).',
        '<strong>Le professeur</strong> guide, questionne, organise le travail et fait la synthèse ; <strong>l\'élève</strong> observe, recherche, échange, propose et construit la trace écrite.',
    ])

    h += '<h3>3. Progression annuelle indicative de 6e</h3>\n'
    h += '<p>Volume horaire calculé à partir du programme : à répartir selon le calendrier scolaire officiel et l\'emploi du temps de l\'établissement. Il est conseillé d\'alterner une leçon d\'histoire et une leçon de géographie, et de garder une à deux semaines par trimestre pour les évaluations et la remédiation.</p>\n'
    for d in c['disciplines']:
        lignes, cumul = [], 0
        for t in d['themes']:
            for l in t['lecons']:
                cumul += l['duree']
                lignes.append(['T' + str(t['n']) + '-L' + str(l['n']) + ' · <a href="#l-6e-ens-' + l['id'][3:] + '">' + l['titre'] + '</a>', str(l['duree']) + ' h', str(cumul) + ' h'])
        h += '<h4>' + d['nom'] + ' (' + str(cumul) + ' h)</h4>\n' + _tab(['Leçon (T = thème, L = leçon)', 'Durée', 'Cumul'], lignes)
    tot = sum(l['duree'] for d in c['disciplines'] for t in d['themes'] for l in t['lecons'])
    h += '<p><strong>Total : ' + str(tot) + ' heures de cours</strong>, hors évaluations, corrections et remédiation.</p>\n'

    h += '<h3>4. Les stratégies pédagogiques utilisées dans les fiches</h3>\n'
    h += _tab(['Stratégie', 'Quand l\'utiliser', 'Conseils pratiques'], [
        ['Questionnement (questions-réponses)', 'Rappels, découverte d\'une notion', 'Poser des questions courtes et ouvertes ; interroger aussi les élèves qui ne lèvent pas la main ; valoriser les réponses partielles.'],
        ['Brainstorming', 'Faire émerger les représentations', 'Tout noter au tableau sans juger, puis trier avec la classe.'],
        ['Travail de groupes', 'Classements, études de documents, tableaux', 'Groupes de 4 à 6, rôles fixés (secrétaire, rapporteur, gardien du temps), consigne écrite au tableau, temps limité.'],
        ['Travail en binômes', 'Calculs, cartes, exercices', 'Le voisin de table ; idéal dans les classes nombreuses.'],
        ['Étude de documents', 'Sources, cartes, photos, textes', 'Toujours : nature, auteur, date, lieu, sujet ; puis les questions.'],
        ['Débat dirigé', 'Opinions, appréciation', 'Règles : lever la main, respecter l\'autre, argumenter ; le professeur fait la synthèse.'],
        ['Enquête et sortie de terrain', 'Démarche du géographe ou de l\'historien', 'Préparer un questionnaire, obtenir les autorisations, assurer la sécurité, exploiter les résultats en classe.'],
        ['Manipulation et expérience', 'Instruments météo, globe et lampe, maquette', 'Le professeur réalise lui-même les manipulations délicates (eau chaude, flamme).'],
    ])

    h += '<h3>5. Conduire une classe nombreuse</h3>\n'
    h += _ul([
        'Écrire la consigne au tableau avant de former les groupes ; donner un temps précis et l\'annoncer.',
        'Former des groupes « table de devant / table de derrière » pour éviter les déplacements.',
        'Utiliser l\'ardoise ou le cahier de brouillon levé pour vérifier rapidement les réponses de toute la classe.',
        'Faire circuler une seule copie de document par groupe quand la photocopie est impossible, ou recopier le document au tableau.',
        'Désigner des élèves-tuteurs pour aider leurs camarades pendant les exercices.',
        'Prévoir des tâches supplémentaires pour les groupes qui finissent tôt (rubrique « élèves avancés » des fiches).',
    ])

    h += '<h3>6. Évaluer en 6e</h3>\n'
    h += _ul([
        '<strong>Évaluation diagnostique</strong> en début de leçon (rappels, prérequis) : elle oriente la séance.',
        '<strong>Évaluation formative</strong> pendant la leçon : les activités d\'application du cours, corrigées immédiatement.',
        '<strong>Évaluation sommative</strong> en fin de leçon ou de thème : le sujet type sur 20 de chaque fiche (8 points d\'activités d\'application, 12 points de situation d\'évaluation).',
    ])
    h += '<p>La situation d\'évaluation comporte trois consignes progressives : connaissance (identifier, définir), compréhension ou analyse (expliquer, montrer), prise de position ou action (proposer, apprécier). La grille de correction est la même pour toutes les fiches :</p>\n'
    h += _tab(['Critère', 'Ce qu\'on vérifie', 'Points'], [
        ['CM1 – Pertinence', 'La réponse correspond à la consigne', 'dans les points des consignes'],
        ['CM2 – Utilisation correcte des outils de la discipline', 'Notions, dates, localisations, calculs exacts', 'dans les points des consignes'],
        ['CM3 – Cohérence', 'Idées logiques et ordonnées', '1'],
        ['CP – Perfectionnement', 'Présentation, orthographe, originalité', '1'],
    ])
    h += '<p><strong>Règle de la majorité des deux tiers :</strong> on considère qu\'un critère minimal est maîtrisé lorsque l\'élève réussit au moins deux occasions de vérification sur trois. Cette règle aide à décider qui a besoin d\'une remédiation.</p>\n'
    h += '<p><strong>Exemples d\'appréciations :</strong> 0 à 7 : insuffisant, revoir la leçon avec le cahier ; 8 à 9 : passable, des efforts à poursuivre ; 10 à 11 : assez bien ; 12 à 13 : bien ; 14 à 16 : très bien ; 17 à 20 : excellent travail.</p>\n'

    h += '<h3>7. Modèle de fiche de leçon vierge</h3>\n'
    h += _tab(['Rubrique', 'À compléter'], [
        ['Classe / Discipline', ''], ['Thème / Leçon / Séance', ''], ['Durée', '55 min'], ['Supports et matériel', ''], ['Bibliographie', ''],
        ['Compétence', ''], ['Habiletés et contenus de la séance', ''], ['Situation d\'apprentissage (contexte, circonstance, tâches)', ''],
    ])
    h += _tab(['Moments didactiques et durée', 'Stratégies', 'Activités du professeur', 'Activités des élèves', 'Trace écrite'], [
        ['Présentation (10 min)', '', '', '', ''],
        ['Développement (35 min)', '', '', '', ''],
        ['Évaluation (10 min)', '', '', '', ''],
    ])

    h += '<h3>8. Tenir le cahier de textes</h3>\n'
    h += _ul([
        'Date, horaire, classe et discipline.',
        'Titre du thème et de la leçon, numéro de la séance.',
        'Parties traitées (par exemple « I. 1 et 2 ») et activités réalisées.',
        'Exercices donnés à la maison, avec la date de remise.',
        'Évaluations effectuées et date de remise des copies.',
    ])

    h += '<h3>9. Les fiches de préparation de 6e</h3>\n'
    for d in c['disciplines']:
        h += '<p><strong>' + d['nom'] + '</strong></p>\n<ol>\n'
        for t in d['themes']:
            for l in t['lecons']:
                h += '<li><a href="#l-6e-ens-' + l['id'][3:] + '">' + l['titre'] + '</a> (' + str(l['duree']) + ' h)</li>\n'
        h += '</ol>\n'
    return h
