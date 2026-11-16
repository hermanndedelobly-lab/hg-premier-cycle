#!/usr/bin/env python3
"""Fabrique l'APK d'une nouvelle version à partir de l'APK précédent (même coquille Android) :

  1. remplace assets/www/index.html par la page unique (outils/fichier-unique.py) et ajoute les
     photographies du dossier img/ (assets/www/img/) ;
  2. met à jour versionCode et versionName dans AndroidManifest.xml (binaire) ;
  3. signe : v1 (jarsigner), alignement sur 4 octets, puis APK Signature Scheme v2.

La clé de signature n'est JAMAIS dans le dépôt (dépôt public). Elle est passée par l'environnement :
  HG_KEYSTORE  : chemin du fichier .p12          HG_KS_PASS : mot de passe
  HG_KS_ALIAS  : alias de la clé (défaut « hg »)

Usage :
  python3 outils/fabriquer-apk.py APK_PRECEDENT PAGE_UNIQUE.html SORTIE.apk
Dépendance : le module Python « cryptography » ; « jarsigner » (JDK) dans le PATH.
Contrôle conseillé ensuite : apksigtool verify SORTIE.apk (signature v2) et jarsigner -verify (v1).
"""
import hashlib
import json
import os
import re
import struct
import subprocess
import sys
import tempfile
import zipfile

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import pkcs12

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def code_version(v):
    a, b, c = (int(x) for x in v.split('.'))
    return a * 10000 + b * 100 + c   # 1.10.0 -> 11000, 1.11.0 -> 11100 (convention de l'APK 1.10.0)


def maj_manifeste(m, ancienne, nouvelle):
    """Remplace versionName (pool de chaînes UTF-16, même longueur) et versionCode (entier)."""
    a, n = ancienne.encode('utf-16le'), nouvelle.encode('utf-16le')
    if len(a) != len(n) or m.count(a) != 1:
        sys.exit(f'versionName {ancienne} -> {nouvelle} : remplacement impossible sans réécrire le manifeste')
    m = m.replace(a, n)
    vc_a, vc_n = struct.pack('<I', code_version(ancienne)), struct.pack('<I', code_version(nouvelle))
    # versionCode : valeur typée (type 0x10 = entier décimal) précédée de taille 8, 0, type
    motif = struct.pack('<HBB', 8, 0, 0x10) + vc_a
    if m.count(motif) != 1:
        sys.exit('versionCode introuvable dans le manifeste')
    return m.replace(motif, struct.pack('<HBB', 8, 0, 0x10) + vc_n)


def ecrire_zip_aligne(entrees, sortie):
    """entrees : liste (nom, données, méthode). Les fichiers non compressés sont alignés sur 4 octets."""
    with zipfile.ZipFile(sortie, 'w') as z:
        for nom, data, methode in entrees:
            zi = zipfile.ZipInfo(nom, date_time=(2026, 1, 1, 0, 0, 0))
            zi.compress_type = methode
            zi.create_system = 0
            if methode == zipfile.ZIP_STORED:
                debut = z.fp.tell() + 30 + len(nom.encode())
                zi.extra = b'\x00' * ((4 - debut % 4) % 4)
            z.writestr(zi, data)


def lire_entrees(apk):
    with zipfile.ZipFile(apk) as z:
        return [(i.filename, z.read(i), i.compress_type) for i in z.infolist()]


# ---------- APK Signature Scheme v2 (https://source.android.com/docs/security/features/apksigning/v2) ----------
def lp(b):
    return struct.pack('<I', len(b)) + b


def digest_v2(sections):
    morceaux = []
    for s in sections:
        for i in range(0, len(s), 1 << 20):
            c = s[i:i + (1 << 20)]
            morceaux.append(hashlib.sha256(b'\xa5' + struct.pack('<I', len(c)) + c).digest())
    return hashlib.sha256(b'\x5a' + struct.pack('<I', len(morceaux)) + b''.join(morceaux)).digest()


def signer_v2(apk, cle, cert_der):
    d = open(apk, 'rb').read()
    eocd = d.rfind(b'PK\x05\x06')
    if eocd < 0 or len(d) - eocd != 22:
        sys.exit('fin de zip inattendue (commentaire présent ?)')
    cd_taille, cd_debut = struct.unpack_from('<II', d, eocd + 12)
    entrees, cd, fin = d[:cd_debut], d[cd_debut:cd_debut + cd_taille], d[eocd:]
    ALGO = 0x0103  # RSASSA-PKCS1-v1_5 avec SHA2-256
    signed_data = lp(lp(struct.pack('<I', ALGO) + lp(digest_v2([entrees, cd, fin])))) + lp(lp(cert_der)) + lp(b'')
    signature = cle.sign(signed_data, padding.PKCS1v15(), hashes.SHA256())
    cle_pub = cle.public_key().public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
    signataire = lp(signed_data) + lp(lp(struct.pack('<I', ALGO) + lp(signature))) + lp(cle_pub)
    valeur = lp(lp(signataire))
    paire = struct.pack('<Q', 4 + len(valeur)) + struct.pack('<I', 0x7109871a) + valeur
    taille = len(paire) + 8 + 16
    bloc = struct.pack('<Q', taille) + paire + struct.pack('<Q', taille) + b'APK Sig Block 42'
    fin = fin[:16] + struct.pack('<I', cd_debut + len(bloc)) + fin[20:]
    with open(apk, 'wb') as f:
        f.write(entrees + bloc + cd + fin)


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    precedent, page, sortie = sys.argv[1:]
    ks, mdp, alias = os.environ.get('HG_KEYSTORE'), os.environ.get('HG_KS_PASS'), os.environ.get('HG_KS_ALIAS', 'hg')
    if not ks or not mdp:
        sys.exit('HG_KEYSTORE et HG_KS_PASS doivent être définis (clé hors du dépôt).')
    version = json.load(open(os.path.join(RACINE, 'version.json')))['version']
    html = open(page, 'rb').read()
    if ('window.HG_VERSION="' + version + '"').encode() not in html or b'window.HG_MODE="apk"' not in html:
        sys.exit(f'la page unique n\'est pas une page « apk » de la version {version}')

    entrees, ancienne = [], None
    for nom, data, methode in lire_entrees(precedent):
        if nom.startswith('META-INF/') or nom.startswith('assets/www/img/'):
            continue   # signature refaite ; photos reprises depuis le dossier img/ du dépôt (ci-dessous)
        if nom == 'AndroidManifest.xml':
            # versionName : seule chaîne « x.y.z » du pool de chaînes (UTF-16)
            ancienne = re.findall(rb'(?:[0-9]\x00)+\.\x00(?:[0-9]\x00)+\.\x00(?:[0-9]\x00)+', data)
            if len(ancienne) != 1:
                sys.exit('versionName introuvable dans le manifeste')
            ancienne = ancienne[0].decode('utf-16le')
            data = maj_manifeste(data, ancienne, version)
        elif nom == 'assets/www/index.html':
            data = html
        entrees.append((nom, data, methode))
    # photographies des leçons (img/) : fichiers à côté de la page, chargés par chemin relatif
    # (la page est ouverte depuis file:///android_asset/www/index.html)
    n_img = 0
    for dossier, _, fichiers in sorted(os.walk(os.path.join(RACINE, 'img'))):
        for f in sorted(fichiers):
            chemin = os.path.join(dossier, f)
            rel = os.path.relpath(chemin, RACINE).replace(os.sep, '/')
            methode = zipfile.ZIP_STORED if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')) else zipfile.ZIP_DEFLATED
            entrees.append(('assets/www/' + rel, open(chemin, 'rb').read(), methode))
            n_img += 1
    print(f'coquille {precedent} : version {ancienne} -> {version} (versionCode {code_version(version)}) ; {n_img} fichier(s) img/ ajouté(s)')

    with tempfile.TemporaryDirectory() as tmp:
        brut = os.path.join(tmp, 'brut.apk')
        ecrire_zip_aligne(entrees, brut)
        subprocess.run(['jarsigner', '-keystore', ks, '-storetype', 'PKCS12', '-storepass:env', 'HG_KS_PASS',
                        '-sigalg', 'SHA256withRSA', '-digestalg', 'SHA-256', '-sigfile', 'HG', brut, alias],
                       check=True, stdout=subprocess.DEVNULL)
        ecrire_zip_aligne(lire_entrees(brut), sortie)   # réaligne après jarsigner
    cle, cert, _ = pkcs12.load_key_and_certificates(open(ks, 'rb').read(), mdp.encode())
    signer_v2(sortie, cle, cert.public_bytes(serialization.Encoding.DER))
    print(f'{sortie} : {os.path.getsize(sortie) / 1e6:.2f} Mo, signé v1 + v2')


if __name__ == '__main__':
    main()
