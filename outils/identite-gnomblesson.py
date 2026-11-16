#!/usr/bin/env python3
"""Déclinaisons du logo GNOMBLESSON à partir du visuel de référence fourni par le porteur du projet
(identite/logo-gnomblesson-reference.png, 1254 × 1254 px). Le logo n'est pas redessiné : il est
détouré, recadré et réduit.

Produit dans identite/ :
  logo-gnomblesson.png              logo complet, coins arrondis transparents (1254 px)
  logo-gnomblesson-512.png          logo complet pour l'écran d'accueil et l'écran de démarrage
  embleme-gnomblesson-1024.png      emblème seul (HV, globe, livre, colonne) sur fond bleu nuit, carré
  android/…                         icônes Android aux tailles exactes de l'APK
et remplace icons/*.png (site) ; écrit identite/donnees-uri.json (logos intégrés à index.html).
"""
import base64
import io
import json
import os

from PIL import Image, ImageDraw, ImageFilter

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ID = os.path.join(R, 'identite')
REF = os.path.join(ID, 'logo-gnomblesson-reference.png')
BLEU_CENTRE, BLEU_BORD = (0, 48, 112), (0, 33, 88)      # relevés sur le fond du logo (#003070 → #002158)
EMBLEME = (150, 62, 1112, 740)                         # zone de l'emblème dans le visuel de référence


def coins_arrondis(im, rayon):
    m = Image.new('L', (im.width * 4, im.height * 4), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, m.width - 1, m.height - 1], rayon * 4, fill=255)
    m = m.resize(im.size, Image.LANCZOS)
    out = im.convert('RGBA'); out.putalpha(m)
    return out


def fond_degrade(cote):
    """Fond bleu nuit radial comme celui du logo."""
    petit = Image.new('RGB', (64, 64))
    px = petit.load()
    for y in range(64):
        for x in range(64):
            d = min(1.0, (((x - 31.5) ** 2 + (y - 31.5) ** 2) ** .5) / 45)
            px[x, y] = tuple(round(BLEU_CENTRE[i] + (BLEU_BORD[i] - BLEU_CENTRE[i]) * d) for i in range(3))
    return petit.resize((cote, cote), Image.BICUBIC)


def embleme(cote, largeur):
    """Emblème recadré, bords fondus dans un fond bleu nuit carré de « cote » px ; largeur de l'emblème en px."""
    ref = Image.open(REF).convert('RGB')
    # la bande orange et verte du coin supérieur gauche déborde dans la zone de l'emblème : on la recouvre
    # de bleu nuit (triangle x/330 + y/250 < 1,25, bien à l'écart du « H » qui commence vers x/330 + y/250 = 1,4)
    ImageDraw.Draw(ref).polygon([(0, 0), (412, 0), (0, 312)], fill=BLEU_BORD)
    e = ref.crop(EMBLEME)
    h = round(e.height * largeur / e.width)
    e = e.resize((largeur, h), Image.LANCZOS)
    masque = Image.new('L', e.size, 0)
    marge = max(2, round(largeur * 0.045))
    ImageDraw.Draw(masque).rectangle([marge, marge, e.width - 1 - marge, e.height - 1 - marge], fill=255)
    masque = masque.filter(ImageFilter.GaussianBlur(marge * 0.7))
    toile = fond_degrade(cote)
    toile.paste(e, ((cote - largeur) // 2, (cote - h) // 2), masque)
    return toile


def png(im, chemin, **kw):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    im.save(chemin, 'PNG', optimize=True, **kw)


def uri(im, fmt='WEBP', **kw):
    b = io.BytesIO(); im.save(b, fmt, **kw)
    return f'data:image/{fmt.lower()};base64,' + base64.b64encode(b.getvalue()).decode()


def main():
    ref = Image.open(REF).convert('RGB')
    # 1. Logo complet : coins blancs du visuel rendus transparents (rayon relevé ≈ 15 % du côté : 188 px)
    logo = coins_arrondis(ref, round(ref.width * 0.15))
    png(logo, os.path.join(ID, 'logo-gnomblesson.png'))
    logo512 = logo.resize((512, 512), Image.LANCZOS)
    png(logo512, os.path.join(ID, 'logo-gnomblesson-512.png'))
    # 2. Emblème seul (lisible aux petites tailles)
    maitre = embleme(1024, 900)
    png(maitre, os.path.join(ID, 'embleme-gnomblesson-1024.png'))
    # 3. Android : icônes classiques (carré arrondi, emblème large) et icône adaptative (zone sûre centrale)
    tailles = {'mipmap-mdpi': 48, 'mipmap-hdpi': 72, 'mipmap-xhdpi': 96, 'mipmap-xxhdpi': 144, 'mipmap-xxxhdpi': 192}
    for dossier, t in tailles.items():
        ic = coins_arrondis(embleme(t * 4, round(t * 4 * 0.9)), round(t * 4 * 0.2)).resize((t, t), Image.LANCZOS)
        png(ic, os.path.join(ID, 'android', dossier, 'ic_launcher.png'))
    # avant-plan adaptatif 432 px (108 dp en xxxhdpi) : emblème dans le cercle sûr de 66 dp
    png(embleme(432, 250).convert('RGBA'), os.path.join(ID, 'android', 'drawable-xxxhdpi', 'ic_premier_plan.png'))
    # 4. Site (manifeste et iPhone)
    png(coins_arrondis(embleme(768, 690), 150).resize((192, 192), Image.LANCZOS), os.path.join(R, 'icons', 'icon-192.png'))
    png(coins_arrondis(embleme(1024, 920), 200).resize((512, 512), Image.LANCZOS), os.path.join(R, 'icons', 'icon-512.png'))
    png(embleme(1024, 640).resize((512, 512), Image.LANCZOS), os.path.join(R, 'icons', 'icon-maskable-512.png'))
    png(embleme(720, 600).resize((180, 180), Image.LANCZOS), os.path.join(R, 'icons', 'icon-180.png'))
    # 5. Logos intégrés à la page (en-tête 2× et accueil / démarrage)
    entete = coins_arrondis(embleme(384, 350), 80).resize((96, 96), Image.LANCZOS)
    png(entete, os.path.join(ID, 'entete-96.png'))
    accueil = logo.resize((480, 480), Image.LANCZOS)
    donnees = {'entete': uri(entete, quality=88), 'logo': uri(accueil, quality=86)}
    json.dump(donnees, open(os.path.join(ID, 'donnees-uri.json'), 'w'), indent=0)
    print('déclinaisons produites ; en-tête', len(donnees['entete']) // 1024, 'Ko ; logo', len(donnees['logo']) // 1024, 'Ko (base64)')


if __name__ == '__main__':
    main()
