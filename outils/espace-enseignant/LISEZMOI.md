# Espace enseignant — sources

Les fiches de préparation et le guide de l'enseignant de 6e sont écrits dans
`fiches_h.py` (histoire), `fiches_g.py` (géographie) et `guide.py`.

Pour régénérer l'Espace enseignant après une correction :

    python3 outils/espace-enseignant/construire.py data/contenu.json

Le script remplace les éléments « enseignant » de la 6e dans `data/contenu.json`
(ils sont stockés comme annexes marquées `enseignant: true`, ce qui les rend
visibles aussi dans les anciennes versions de l'application Android).
Pensez ensuite à augmenter la version (version.json, sw.js, index.html, data/contenu.json).
