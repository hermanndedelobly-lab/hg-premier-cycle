# Contenus pédagogiques enrichis (cahier des charges V1.1)

Un dossier par leçon enrichie, nommé par l'**identifiant permanent** de la leçon (ex. `6e-h-t1-l1`).
Ces identifiants ne changent jamais : la progression des utilisateurs (leçons traitées, scores de
quiz, dernière leçon ouverte) y est rattachée et reste stockée à part, sur le téléphone (`hg1c.*`).

| Fichier | Espace | Contenu |
|---|---|---|
| `eleve.html` | B. Élève | Trace écrite (Introduction, I/II/III avec 1./2., Conclusion, « Je retiens »), illustrations, activités d'application. **Remplace le champ `cours`** de la leçon. |
| `evaluation.html` | B. Élève | Questions de compréhension, activités d'application et situation d'évaluation, corrigés expliqués et barèmes. |
| `enseignant.html` | A. Enseignant | Les 12 rubriques du mode enseignant (titres `<h4>1.` à `<h4>11 et 12.`). |
| `preparation.html` | A. Enseignant | Préparation de séance APC (compétence → remédiation). |
| `culture.html` | C. Culture générale | Les 9 rubriques d'approfondissement, dont les références (avec leur état de vérification). |
| `exercices.html` | B. Élève | Facultatif : version corrigée des « exercices traités » de la leçon (le script refuse toute baisse du nombre d'exercices). |
| `banque.html` | B. Élève | Facultatif : version corrigée de la banque d'exercices de la leçon (même garde-fou). |
| `meta.json` | — | Statut de la leçon (`pilote`, `validee`), date, validateur. |

Les exercices existants (champ `exercices`, banque d'exercices) et les quiz sont conservés ; ils ne sont modifiés que par une version corrigée explicite (`exercices.html`, `banque.html`), jamais en nombre réduit.

Conventions : `<span class="badge prog">Programme</span>` pour l'exigible, `<span class="badge approf">Approfondissement</span>`
pour l'enseignant ; chaque illustration est une `<figure class="graphe illus">` avec un `<svg>` (attribut
`aria-label`) et une `<figcaption>` qui commence par son titre en gras, suivie d'un `<p class="illus-expl">` (explication).

Intégration : `python3 outils/integrer-pedagogie.py` (contrôle puis écrit `data/contenu.json`) ;
`--verifier` contrôle sans écrire.
