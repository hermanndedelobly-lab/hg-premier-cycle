# Outils de publication — GNOMBLESSON · Histoire & Géographie (ex-« Histoire géographie premier cycle »)

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

## Mise à jour de l'application Android sans nouvel APK (depuis la 1.14.0)

L'application télécharge, depuis le canal de mise à jour (`ADRESSE_MAJ` dans `app.js`, actuellement la branche de
développement sur raw.githubusercontent.com ; une adresse peut aussi être saisie dans Réglages) :
`version.json`, `data/contenu.json` et la page `maj/page.html` (code et styles, sans les données).
Au démarrage, le script placé en tête de la page de l'APK utilise la version téléchargée si elle est plus récente
et complète. Sécurité : une version qui ne confirme pas son démarrage en 12 s est écartée et l'application
revient à la version de l'APK ; « Revenir à la version d'origine » (Réglages) efface les versions téléchargées.

Pour publier une mise à jour sans APK :
1. changer le numéro de version (4 fichiers, voir plus haut) ; `version.json` garde `"code": "maj/page.html"` ;
2. `python3 outils/fichier-unique.py maj/page.html --mode maj` ;
3. envoyer sur la branche du canal. Les téléphones la proposent à la prochaine vérification.
Limites : les nouvelles photos (`img/`) ne sont pas dans l'APK installé : elles s'afficheront depuis le canal
quand le téléphone est connecté, ou après un nouvel APK. Taille enregistrée dans le téléphone ≈ 2,4 Mo.

## Identité visuelle GNOMBLESSON (1.14.0)

`identite/logo-gnomblesson-reference.png` (visuel fourni) → `python3 outils/identite-gnomblesson.py` produit les
déclinaisons (logo détouré, emblème, icônes Android et du site, logos de la page). `identite/android.json` décrit
les changements appliqués à l'APK par `fabriquer-apk.py` (nom affiché, couleur, icônes) ; l'identifiant
`ci.hg.premiercycle`, le code Java et la clé de signature ne changent pas.

## Espace enseignant de la 6e (1.15.0)

`outils/espace-enseignant/` (repris de la branche `espace-enseignant-6e`) : `python3 outils/espace-enseignant/construire.py data/contenu.json`
ajoute à la 6e le guide de l'enseignant et une fiche de préparation par leçon (annexes `6e-ens-…`, `enseignant: true`,
`lecon: <identifiant>`). L'application les montre dans l'onglet « Enseignant » de la classe (`#t-6e`) et par le lien
« Fiche de préparation » de chaque leçon. Une leçon enrichie (trois espaces, ex. `6e-h-t1-l1`) garde sa propre préparation
dans son espace Enseignant (`#a-`) : son ancienne fiche reste dans les données (identifiant permanent) mais n'est plus
listée et son adresse mène à l'espace de la leçon. Ordre : `construire.py` puis `integrer-pedagogie.py` puis `integrer-quiz.py --verifier`.

## Passerelle pour l'APK 1.10.0 (clé perdue), sans désinstallation

`python3 outils/fichier-unique.py maj/page.html --mode maj && python3 outils/fabriquer-pont.py` produit `pont/`.
Sur le téléphone en 1.10.0 : Réglages › Adresse du site des mises à jour =
`https://raw.githubusercontent.com/hermanndedelobly-lab/hg-premier-cycle/<branche du canal>/pont` › Enregistrer ›
Vérifier les mises à jour, puis fermer et rouvrir l'application : GNOMBLESSON démarre avec la progression de la 1.10.0
(détails dans `outils/fabriquer-pont.py`). Limites : le nom et l'icône du lanceur Android restent ceux de la 1.10.0 ;
les photos s'affichent depuis le canal quand le téléphone est connecté. À chaque version : régénérer `maj/page.html` puis `pont/`.

## Stockage v2 des mises à jour sans APK (1.17.0)

Module : `outils/stockage-maj.js` (inclus dans la page de l'APK et dans `maj/page.html` par `fichier-unique.py`,
et dans le lanceur de la passerelle par `fabriquer-pont.py`).
- Le contenu complet téléchargé est compressé (gzip, `CompressionStream`), emballé en texte (15 bits par caractère,
  U+0800 – U+87FF) et rangé sous `hg1c.contenu-gz` avec un en-tête `GZ15:version:longueur:empreinte:` ; l'empreinte
  (FNV-1a) est vérifiée à chaque lecture. Rapport mesuré : 4,32 millions de caractères → 0,50 million (8,7 fois moins).
- `hg1c.contenu-maj` ne contient plus qu'un descripteur (quelques centaines de caractères) : le script de démarrage des APK
  installés (1.14.x) n'exige que son numéro de version. Pour la passerelle 1.10.0, c'est un squelette (≈ 49 ko) porteur du
  lanceur ; le contenu complet est lu à l'adresse `source` (`../data/contenu.json` depuis `pont/`).
- Ordre d'écriture : contenu compressé dans une clé temporaire → relecture et comparaison → page de code → contenu définitif
  → descripteur (en dernier). Ancien format (contenu en clair) : migré automatiquement au premier démarrage de la 1.17.0.
- Contenu illisible au démarrage : la mise à jour enregistrée est retirée (jamais la progression), un incident est noté
  (`hg1c.maj-incident`) et l'application redémarre sur la version de l'APK (ou la 1.10.0 d'origine pour la passerelle).
- Les clés de progression (`faites`, `quiz`, `derniere`, `classe`, `reglages`) ne sont jamais lues ni modifiées par ce module ;
  « Revenir à la version d'origine » retire seulement les clés de mise à jour (et, pour la passerelle, son adresse).
- Limite connue : un téléphone resté sur un code antérieur à 1.17.0 télécharge encore l'ancien format (en clair) ; il doit
  passer par la 1.17.0 avant une version dont le contenu dépasserait environ 5 millions de caractères.

## Contenu allégé : textes de recherche, fiches enseignant, préparations et évaluations reconstitués (1.18.0 à 1.20.0)

`data/contenu.json` doit rester assez léger pour le chemin le plus exigeant : après une version écartée (démarrage non
confirmé), le code de l'APK 1.14.0 reprend la main alors que le contenu compressé (≈ 0,6 million de caractères) et la page
de code (≈ 0,35 million) sont encore rangés ; il enregistre la nouvelle version **en clair**. Avec la limite du stockage
(≈ 5,24 millions de caractères), le contenu doit rester sous ≈ 4,25 millions de caractères (1.19.0 : 4,21 millions ; 1.20.0 : 4,04 millions avec les 53 leçons enrichies ; contrôle :
`test-stockage-apk`, étape « version cassée » puis « nouvelle version saine »). Pour cela :
- Textes de recherche (`texte`, `texteBanque`, `texteEns`, `texteCult` des leçons, `texte` des annexes et des schémas) :
  laissés vides par `integrer-pedagogie.py` et `construire.py` ; reconstitués au chargement par `app.js` (`completerTextes`).
- Fiches de l'onglet Enseignant : `construire.py` range les données compactes de la fiche (champ `fiche`) et une phrase de
  remplacement dans `html` ; `app.js` (`completerFiches`) reconstitue le HTML à l'identique. Après toute modification de
  `construire.py` ou de `completerFiches` : `python3 outils/verifier-fiches.py` (égalité exacte des fiches, 41 sur 41 en 1.19.0).
- Le squelette de la passerelle (`fabriquer-pont.py`) n'emporte pas les données des fiches.
- Préparation de séance et évaluation des leçons enrichies (1.20.0) : quand `preparation.html` et `evaluation.html` sont
  exactement ceux que produit `generer-evaluation-preparation.py`, `construire.py` range une phrase de remplacement dans
  `preparation` / `evaluation` et les questions de compréhension dans `qc` ; `app.js` (`completerEP`) reconstitue le HTML à
  l'identique depuis la fiche compacte. Une préparation ou une évaluation retouchée à la main reste stockée telle quelle.
  `verifier-fiches.py` contrôle aussi ces champs (155 sur 155 en 1.20.0 : 53 fiches, 102 préparations et évaluations).
- Marge restante en 1.20.0 : ≈ 0,2 million de caractères. Toute nouvelle illustration lourde (carte) doit rester légère
  (fond 110m, coordonnées arrondies au pixel).
