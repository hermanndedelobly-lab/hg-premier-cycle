/*
 * Contenu du Portail culturel Wê (MW+).
 * Tout le texte du site est ici : modifiez ce fichier pour enrichir le portail
 * sans toucher au code. Les mentions « À compléter » signalent les rubriques
 * qui attendent les contributions de la communauté.
 */
window.SITE = {
  nom: "MW+",
  slogan: "La Culture Wê, notre fierté",
  // Adresse qui reçoit les messages des formulaires (contact, partenariat, contenu).
  emailContact: "contact@mondewe.ci",

  sections: [
    {
      id: "accueil",
      label: "Accueil",
      pages: []
    },

    {
      id: "histoire",
      label: "Histoire & Civilisation",
      court: "Histoire",
      intro: "D'où vient le peuple wê, comment il s'est organisé et ce qu'il a transmis de génération en génération.",
      pages: [
        {
          id: "origines",
          titre: "Origines du peuple wê",
          chapo: "Les Wê vivent dans l'ouest de la Côte d'Ivoire, entre forêts, collines et rivières, dans les régions du Guémon et du Cavally.",
          texte: [
            "Le peuple wê appartient au grand ensemble des peuples de langues krou, présents dans l'ouest et le sud-ouest de la Côte d'Ivoire ainsi qu'au Liberia voisin. On distingue habituellement deux grandes composantes : les Guéré et les Wobé, qui partagent une même langue, le wê, et un même fonds de croyances et de coutumes.",
            "Le pays wê s'étend autour de villes comme Duékoué, Guiglo, Bangolo, Blolequin, Toulépleu, Facobly et Kouibly. Chaque village se rattache à un lignage et à un ancêtre fondateur dont on raconte l'histoire lors des veillées.",
            "Cette rubrique rassemblera les récits d'origine propres à chaque canton et à chaque village, tels que les transmettent les anciens."
          ],
          aCompleter: true
        },
        {
          id: "patrimoine",
          titre: "Histoire et patrimoine",
          chapo: "Les grandes étapes de l'histoire du pays wê et les biens matériels et immatériels qui en témoignent.",
          texte: [
            "Organisation lignagère, alliances entre villages, rencontres avec les peuples voisins, période coloniale puis Côte d'Ivoire indépendante : l'histoire wê se lit dans les récits, les chants et les objets.",
            "Le patrimoine wê comprend notamment les masques, la statuaire, les cases et sites sacrés, les forêts protégées par la tradition et un très riche patrimoine oral."
          ],
          aCompleter: true
        },
        {
          id: "personnalites",
          titre: "Personnalités historiques",
          chapo: "Chefs, résistants, savants, artistes et bâtisseurs qui ont marqué l'histoire du peuple wê.",
          texte: [
            "Chaque fiche présentera la vie de la personnalité, son village d'origine, son rôle et les sources qui la documentent.",
            "Vous connaissez une figure qui mérite d'y figurer ? Proposez sa biographie depuis la page « Proposer un contenu »."
          ],
          aCompleter: true
        },
        {
          id: "traditions",
          titre: "Traditions ancestrales",
          chapo: "Croyances, rites de passage, règles de vie et savoirs transmis par les anciens.",
          texte: [
            "Chez les Wê, le masque occupe une place centrale : il n'est pas un simple objet mais une puissance qui intervient dans la vie de la communauté, pour divertir, enseigner, juger ou apaiser les conflits.",
            "Rites de naissance, d'initiation, de mariage et de funérailles, respect des aînés, solidarité du lignage : cette rubrique décrira ces traditions avec l'accord et l'aide des gardiens de la coutume."
          ],
          aCompleter: true
        },
        {
          id: "chefferies",
          titre: "Chefferies traditionnelles",
          chapo: "L'organisation du pouvoir traditionnel : chefs de village, chefs de canton, notables et conseils des anciens.",
          texte: [
            "Le village est dirigé par un chef entouré de notables et des représentants des lignages. Les questions importantes sont débattues en assemblée, sous l'arbre à palabres.",
            "Un annuaire des chefferies, canton par canton, viendra compléter cette page."
          ],
          aCompleter: true
        }
      ]
    },

    {
      id: "langue",
      label: "Langue wê",
      court: "Langue",
      intro: "Parler, écrire et transmettre le wê, langue de nos parents et de nos enfants.",
      pages: [
        {
          id: "apprendre",
          titre: "Apprendre le wê",
          chapo: "Des leçons progressives pour découvrir la langue : salutations, nombres, famille, vie quotidienne.",
          texte: [
            "Le wê est une langue krou à tons : la hauteur de la voix change le sens des mots. C'est pourquoi chaque leçon sera accompagnée d'enregistrements audio.",
            "Leçons prévues : 1. Saluer et se présenter — 2. Compter — 3. La famille — 4. Le marché — 5. Le village et la nature."
          ],
          aCompleter: true
        },
        {
          id: "dictionnaire",
          titre: "Dictionnaire français-wê",
          type: "dictionnaire",
          chapo: "Cherchez un mot en français ou en wê.",
          texte: [
            "Le dictionnaire s'enrichit des contributions des locuteurs. Chaque mot est relu avant d'être publié, et la variante (guéré, wobé, canton) est indiquée quand elle compte."
          ]
        },
        {
          id: "proverbes",
          titre: "Proverbes et expressions",
          chapo: "La sagesse des anciens en quelques mots : proverbes, dictons et expressions imagées, avec leur traduction et leur sens.",
          texte: [
            "Chaque proverbe sera présenté en wê, traduit mot à mot, puis expliqué : dans quelle situation on l'emploie et quelle leçon il transmet."
          ],
          aCompleter: true
        },
        {
          id: "contes",
          titre: "Contes et légendes",
          chapo: "Les histoires racontées au clair de lune : animaux rusés, héros, esprits de la forêt.",
          texte: [
            "Les contes seront publiés en version bilingue, avec l'enregistrement du conteur quand c'est possible."
          ],
          aCompleter: true
        },
        {
          id: "audio",
          titre: "Audio et prononciation",
          chapo: "Écouter pour bien prononcer : tons, sons propres au wê et mots du quotidien.",
          texte: [
            "Les enregistrements seront réalisés avec des locuteurs de différents cantons afin de faire entendre la richesse des parlers wê."
          ],
          aCompleter: true
        }
      ]
    },

    {
      id: "culture",
      label: "Culture & Traditions",
      court: "Culture",
      intro: "Danses, musiques, saveurs, tenues et cérémonies qui font vivre la culture wê.",
      pages: [
        {
          id: "danses",
          titre: "Danses traditionnelles",
          chapo: "Danses de réjouissance, danses de masques, danses des femmes et des jeunes.",
          texte: [
            "Chaque danse a son occasion, ses pas, ses tambours et ses chants. Les fiches préciseront l'origine, le sens et les moments où elle est exécutée."
          ],
          aCompleter: true
        },
        {
          id: "musique",
          titre: "Musique traditionnelle",
          chapo: "Chants de travail, chants de veillée, chants funéraires et chants de masques.",
          texte: [
            "La musique accompagne tous les moments de la vie wê. Cette rubrique présentera les grands genres, leurs paroles et leurs interprètes."
          ],
          aCompleter: true
        },
        {
          id: "instruments",
          titre: "Instruments",
          chapo: "Tambours, percussions, instruments à cordes et à vent : comment ils sont fabriqués et joués.",
          texte: [
            "Pour chaque instrument : nom en wê, matériaux, fabrication, technique de jeu et extrait sonore."
          ],
          aCompleter: true
        },
        {
          id: "gastronomie",
          titre: "Gastronomie",
          chapo: "Les saveurs du pays wê : sauces, plats de fête, boissons et produits de la forêt.",
          texte: [
            "Riz, manioc, banane plantain, graine de palme, gombo, gibier et produits de la forêt sont à la base de la cuisine de l'Ouest. Les recettes seront présentées pas à pas, avec les noms des plats en wê."
          ],
          aCompleter: true
        },
        {
          id: "habillement",
          titre: "Habillement traditionnel",
          chapo: "Pagnes, parures, coiffures et tenues de cérémonie.",
          texte: [
            "Les tenues disent l'âge, le rang et l'occasion. Cette rubrique décrira les tenues d'hier et leurs réinterprétations par les créateurs d'aujourd'hui."
          ],
          aCompleter: true
        },
        {
          id: "ceremonies",
          titre: "Cérémonies culturelles",
          chapo: "Fêtes de génération, sorties de masques, intronisations, funérailles et fêtes des récoltes.",
          texte: [
            "Un calendrier des cérémonies, village par village, sera tenu à jour dans la rubrique Événements."
          ],
          aCompleter: true
        }
      ]
    },

    {
      id: "musique",
      label: "Musique & Artistes",
      court: "Musique",
      intro: "Les voix d'hier et d'aujourd'hui : artistes, sorties, clips et entretiens.",
      pages: [
        { id: "artistes", titre: "Artistes wê", chapo: "Portraits des chanteurs, musiciens, groupes et danseurs du pays wê et de la diaspora.", texte: ["Chaque portrait présentera le parcours de l'artiste, sa discographie et ses liens officiels.", "Artiste ou manager ? Envoyez votre biographie et vos photos depuis « Proposer un contenu »."], aCompleter: true },
        { id: "nouveautes", titre: "Nouveautés musicales", chapo: "Les dernières sorties des artistes wê.", texte: ["Les nouveautés seront publiées chaque semaine, avec un extrait et les liens d'écoute."], aCompleter: true },
        { id: "albums", titre: "Albums et singles", chapo: "La discographie des artistes wê, classée par artiste et par année.", texte: ["Titre, année, label, liste des morceaux et liens vers les plateformes d'écoute."], aCompleter: true },
        { id: "clips", titre: "Clips vidéo", chapo: "Les clips des artistes wê, à regarder directement sur le portail.", texte: ["Les clips seront intégrés depuis les chaînes officielles des artistes."], aCompleter: true },
        { id: "interviews", titre: "Interviews", chapo: "Les artistes racontent leur parcours, leurs inspirations et leur attachement à la culture wê.", texte: ["Entretiens écrits, audio et vidéo."], aCompleter: true }
      ]
    },

    {
      id: "tourisme",
      label: "Tourisme & Découverte",
      court: "Tourisme",
      intro: "Partir à la découverte du pays wê : villages, forêts, montagnes et hospitalité.",
      pages: [
        { id: "villages", titre: "Nos villages", chapo: "Chaque village a son histoire, ses lignages, ses fêtes et ses figures.", texte: ["Une fiche par village : localisation, histoire, chefferie, sites remarquables, fêtes et contacts utiles.", "Les fiches seront regroupées par département : Duékoué, Guiglo, Bangolo, Blolequin, Toulépleu, Facobly, Kouibly, Taï…"], aCompleter: true },
        { id: "sites", titre: "Sites touristiques", chapo: "Montagnes, forêts sacrées, rivières et lieux de mémoire.", texte: ["Parmi les sites naturels de la région figurent le parc national du Mont Péko et, plus au sud, le parc national de Taï, inscrit au patrimoine mondial de l'UNESCO.", "Chaque site sera présenté avec les conditions d'accès, la meilleure saison et les règles à respecter."], aCompleter: true },
        { id: "paysages", titre: "Paysages et nature", chapo: "Forêt dense, collines, savanes arborées, faune et flore de l'Ouest ivoirien.", texte: ["Galeries photos et fiches sur les espèces et les paysages remarquables."], aCompleter: true },
        { id: "hebergements", titre: "Hébergements", chapo: "Hôtels, auberges, gîtes et séjours chez l'habitant.", texte: ["Liste des hébergements par ville, avec coordonnées et services. Établissements : inscrivez-vous via « Devenir partenaire »."], aCompleter: true },
        { id: "guides", titre: "Guides touristiques", chapo: "Des guides locaux pour visiter le pays wê en confiance.", texte: ["Chaque guide présentera ses circuits, ses langues parlées et ses coordonnées."], aCompleter: true }
      ]
    },

    {
      id: "mediatheque",
      label: "Médiathèque",
      court: "Médiathèque",
      intro: "Livres, documents, photos, vidéos et archives à consulter et télécharger.",
      pages: [
        { id: "telechargements", titre: "Téléchargements", chapo: "Tous les fichiers mis à disposition par le portail.", texte: ["Leçons de wê, fiches culturelles, affiches d'événements, sonneries et fonds d'écran."], aCompleter: true },
        { id: "livres", titre: "Livres et documents PDF", chapo: "Ouvrages, mémoires, thèses et articles sur le peuple wê.", texte: ["Chaque document sera publié avec l'accord de son auteur ou s'il est libre de droits."], aCompleter: true },
        { id: "photos", titre: "Photos", chapo: "Galeries : villages, cérémonies, portraits, paysages.", texte: ["Envoyez vos photos en précisant le lieu, la date et l'auteur."], aCompleter: true },
        { id: "videos", titre: "Vidéos", chapo: "Documentaires, reportages, cérémonies filmées.", texte: ["Les vidéos seront classées par thème et par village."], aCompleter: true },
        { id: "archives", titre: "Archives historiques", chapo: "Documents anciens, photographies d'époque et enregistrements rares.", texte: ["Vous détenez des archives familiales ? Le portail peut les numériser et les préserver avec votre accord."], aCompleter: true }
      ]
    },

    {
      id: "actualites",
      label: "Actualités",
      court: "Actualités",
      intro: "Ce qui se passe dans le pays wê et dans la diaspora.",
      pages: [
        { id: "culturelles", titre: "Actualités culturelles", type: "actualites", filtre: "Culture", chapo: "Festivals, sorties d'albums, expositions, publications." },
        { id: "communautaires", titre: "Actualités communautaires", type: "actualites", filtre: "Communauté", chapo: "La vie des villages, des associations et de la diaspora." },
        { id: "evenements", titre: "Événements", type: "actualites", filtre: "Événement", chapo: "L'agenda des fêtes, cérémonies, concerts et rencontres." },
        { id: "annonces", titre: "Annonces", type: "actualites", filtre: "Annonce", chapo: "Avis, communiqués, décès, mariages, recherches." }
      ]
    },

    {
      id: "business",
      label: "Wê Business",
      court: "Wê Business",
      intro: "L'économie du pays wê : entreprises, commerces, entrepreneurs et artisans.",
      pages: [
        { id: "annuaire", titre: "Annuaire des entreprises", type: "annuaire", chapo: "Trouvez une entreprise ou un professionnel wê." },
        { id: "commerces", titre: "Commerces et services", type: "annuaire", filtre: "Commerce", chapo: "Boutiques, restaurants, transport, services." },
        { id: "entrepreneurs", titre: "Entrepreneurs", type: "annuaire", filtre: "Entrepreneur", chapo: "Celles et ceux qui créent et développent des activités." },
        { id: "artisans", titre: "Artisans", type: "annuaire", filtre: "Artisan", chapo: "Sculpteurs, tisserands, forgerons, potiers, couturiers." },
        { id: "publicites", titre: "Publicités et partenariats", chapo: "Faites connaître votre activité auprès de la communauté wê.", texte: ["Bannières, articles sponsorisés, partenariats d'événements : le portail propose plusieurs formules pour soutenir son fonctionnement tout en valorisant les entreprises de la communauté.", "Contactez-nous depuis la page « Devenir partenaire »."] }
      ]
    },

    {
      id: "contact",
      label: "Contact",
      court: "Contact",
      intro: "Nous écrire, devenir partenaire ou partager vos connaissances.",
      pages: [
        {
          id: "a-propos",
          titre: "À propos",
          chapo: "MW+ est un portail dédié à la valorisation, à la préservation et à la transmission de la culture wê.",
          texte: [
            "Notre mission : rassembler en un seul lieu l'histoire, la langue, les arts, les lieux et les forces vives du peuple wê, pour les jeunes, pour la diaspora et pour tous ceux qui veulent le découvrir.",
            "Le portail est collaboratif : chacun peut proposer un texte, une photo, un enregistrement ou une correction. Chaque contribution est relue avant publication."
          ]
        },
        { id: "nous-contacter", titre: "Nous contacter", type: "formulaire", formulaire: "contact", chapo: "Une question, une remarque, une correction ? Écrivez-nous." },
        { id: "partenaire", titre: "Devenir partenaire", type: "formulaire", formulaire: "partenaire", chapo: "Entreprises, associations, institutions : soutenons ensemble la culture wê." },
        { id: "proposer", titre: "Proposer un contenu", type: "formulaire", formulaire: "contenu", chapo: "Partagez un récit, un proverbe, une photo, un enregistrement ou un mot pour le dictionnaire." }
      ]
    }
  ],

  /*
   * Dictionnaire : ajoutez des entrées sous la forme
   * { fr: "bonjour", we: "…", categorie: "Salutations", variante: "guéré", exemple: "…" }
   * Ne publiez que des mots vérifiés par des locuteurs.
   */
  dictionnaire: [],

  /*
   * Actualités : { date: "2026-11-07", categorie: "Culture" | "Communauté" | "Événement" | "Annonce",
   *                titre: "…", resume: "…", lieu: "…" }
   */
  actualites: [
    {
      date: "2026-11-07",
      categorie: "Annonce",
      titre: "Lancement du portail MW+",
      resume: "Le portail de la culture wê ouvre ses portes. Histoire, langue, arts, tourisme, médiathèque et annuaire : toutes les rubriques sont ouvertes aux contributions de la communauté.",
      lieu: "En ligne"
    },
    {
      date: "2026-11-07",
      categorie: "Communauté",
      titre: "Appel à contributions : dictionnaire français-wê",
      resume: "Locuteurs guéré et wobé, aidez-nous à constituer le premier dictionnaire en ligne. Proposez vos mots depuis la page « Proposer un contenu ».",
      lieu: "En ligne"
    }
  ],

  /*
   * Annuaire : { nom: "…", categorie: "Commerce" | "Entrepreneur" | "Artisan" | "Service",
   *              activite: "…", ville: "…", telephone: "…", description: "…" }
   */
  annuaire: []
};
