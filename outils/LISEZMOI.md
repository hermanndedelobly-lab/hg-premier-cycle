# Outils de publication — Histoire géographie premier cycle

## Modifier ou ajouter des questions de quiz

Les quiz sont rédigés dans `quiz/6e.txt`, `quiz/5e.txt`, `quiz/4e.txt` et `quiz/3e.txt` :

```
@6e-h-t1-l4                      ← identifiant de la leçon
? Un millénaire correspond à :   ← question
+ 1 000 ans                      ← la bonne réponse (une seule)
- 100 ans                        ← mauvaises réponses
- 10 ans
= Mille ans = dix siècles.       ← explication affichée après la réponse (facultative)
```

Les réponses sont mélangées à l'affichage : l'ordre dans le fichier n'a pas d'importance.
Ensuite : `python3 outils/integrer-quiz.py` (contrôle puis écrit `data/contenu.json`).
`python3 outils/integrer-quiz.py --verifier` contrôle sans rien écrire.

## Leçons enrichies (cahier des charges V1.1)

Voir `pedagogie/LISEZMOI.md`. Après modification : `python3 outils/integrer-pedagogie.py`
(contrôles automatiques des trois espaces, des illustrations et du HTML), puis `python3 outils/integrer-quiz.py --verifier`.

## Publier une nouvelle version

1. Changer le numéro dans `version.json`, `data/contenu.json` (champs `version`, `date`, `notes`),
   `sw.js` (`VERSION`) et `index.html` (`window.HG_VERSION`). Les quatre doivent être identiques.
2. Version web : fusionner dans `main` (GitHub Pages). Les téléphones proposent alors « Mettre à jour ».
3. Page unique de l'APK : `python3 outils/fichier-unique.py /tmp/page.html`
   (le script refuse de travailler si `index.html` et `contenu.json` n'ont pas la même version).
4. APK : `python3 outils/fabriquer-apk.py Histoire-geographie-premier-cycle.apk /tmp/page.html HistoGeo-X.Y.Z.apk`
   avec la clé passée par l'environnement (`HG_KEYSTORE`, `HG_KS_PASS`, `HG_KS_ALIAS`).
   Contrôles : `apksigtool verify` (signature v2) et `jarsigner -verify` (signature v1).
5. Remplacer `Histoire-geographie-premier-cycle.apk` par le nouvel APK et ajouter `HistoGeo-X.Y.Z.apk`.

## Clé de signature de l'APK

- Elle n'est **jamais** dans ce dépôt (il est public) : `.gitignore` refuse `*.p12`, `*.jks`, `*.keystore`.
- Un APK ne peut mettre à jour l'application installée que s'il est signé avec **la même clé**.
- La clé de la version 1.10.0 a été perdue : la version 1.11.0 est signée avec une nouvelle clé
  (empreinte SHA-256 du certificat indiquée dans le journal de la version). Pour passer de 1.10.0 à 1.11.0,
  il faut désinstaller l'ancienne application puis installer la nouvelle. Les versions suivantes
  pourront se mettre à jour normalement si la nouvelle clé est conservée (Google Drive privé, clé USB).
  La version 1.12.0 est signée avec cette même clé : elle s'installe par-dessus la 1.11.0 sans perte de données.
