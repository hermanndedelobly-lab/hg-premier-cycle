"""Modifications ciblées des ressources compilées d'un APK (resources.arsc), sans aapt :
- remplacement d'une chaîne du pool global (ex. le nom affiché sous l'icône, ressource app_name) ;
- remplacement d'une couleur (valeur ARGB d'une ressource color).
Le pool de chaînes est réécrit entièrement (décalages, remplissage, taille des blocs) ; les identifiants de
ressources, les clés et les types ne changent pas.
"""
import struct


def _lire_long(data, pos, utf8):
    if utf8:
        n = data[pos]
        if n & 0x80:
            return ((n & 0x7F) << 8) | data[pos + 1], pos + 2
        return n, pos + 1
    n = struct.unpack_from('<H', data, pos)[0]
    if n & 0x8000:
        return ((n & 0x7FFF) << 16) | struct.unpack_from('<H', data, pos + 2)[0], pos + 4
    return n, pos + 2


def _ecrire_long(n, utf8):
    if utf8:
        if n > 0x7FFF:
            raise ValueError('chaîne trop longue')
        return bytes([n]) if n < 0x80 else bytes([0x80 | (n >> 8), n & 0xFF])
    return struct.pack('<H', n) if n < 0x8000 else struct.pack('<HH', 0x8000 | (n >> 16), n & 0xFFFF)


def lire_pool(arsc):
    """Renvoie (chaînes, informations) du pool de chaînes global de resources.arsc."""
    t, hs, taille, npaq = struct.unpack_from('<HHII', arsc, 0)
    assert t == 0x0002 and hs == 12, 'resources.arsc inattendu'
    p = 12
    t, hs, taille_pool, n, nstyles, flags, debut, debut_styles = struct.unpack_from('<HHIIIIII', arsc, p)
    assert t == 0x0001, 'pool de chaînes global introuvable'
    utf8 = bool(flags & 0x100)
    decal = struct.unpack_from(f'<{n}I', arsc, p + hs)
    chaines = []
    for d in decal:
        q = p + debut + d
        if utf8:
            _, q = _lire_long(arsc, q, True)
            nb, q = _lire_long(arsc, q, True)
            chaines.append(arsc[q:q + nb].decode('utf-8'))
        else:
            nc, q = _lire_long(arsc, q, False)
            chaines.append(arsc[q:q + 2 * nc].decode('utf-16le'))
    info = dict(pos=p, hs=hs, taille=taille_pool, n=n, nstyles=nstyles, flags=flags, debut=debut, debut_styles=debut_styles, utf8=utf8)
    return chaines, info


def remplacer_chaine(arsc, ancienne, nouvelle):
    chaines, i = lire_pool(arsc)
    if chaines.count(ancienne) != 1:
        raise ValueError(f'chaîne « {ancienne} » trouvée {chaines.count(ancienne)} fois dans le pool global')
    chaines[chaines.index(ancienne)] = nouvelle
    p, utf8 = i['pos'], i['utf8']
    # styles conservés tels quels (blocs bruts)
    decal_styles = struct.unpack_from(f'<{i["nstyles"]}I', arsc, p + i['hs'] + 4 * i['n']) if i['nstyles'] else ()
    styles = arsc[p + i['debut_styles']:p + i['taille']] if i['nstyles'] else b''
    donnees, decal = bytearray(), []
    for s in chaines:
        decal.append(len(donnees))
        if utf8:
            b = s.encode('utf-8')
            donnees += _ecrire_long(len(s.encode('utf-16le')) // 2, True) + _ecrire_long(len(b), True) + b + b'\x00'
        else:
            b = s.encode('utf-16le')
            donnees += _ecrire_long(len(b) // 2, False) + b + b'\x00\x00'
    while len(donnees) % 4:
        donnees += b'\x00'
    debut = i['hs'] + 4 * (i['n'] + i['nstyles'])
    debut_styles = debut + len(donnees) if i['nstyles'] else 0
    taille = debut + len(donnees) + len(styles)
    entete = struct.pack('<HHIIIIII', 0x0001, i['hs'], taille, i['n'], i['nstyles'], i['flags'], debut, debut_styles)
    pool = entete + arsc[p + 28:p + i['hs']] + struct.pack(f'<{i["n"]}I', *decal) + struct.pack(f'<{i["nstyles"]}I', *decal_styles) + bytes(donnees) + styles
    neuf = arsc[:p] + pool + arsc[p + i['taille']:]
    t, hs, taille_table, npaq = struct.unpack_from('<HHII', neuf, 0)
    return struct.pack('<HHII', t, hs, taille_table + len(pool) - i['taille'], npaq) + neuf[12:]


def remplacer_couleur(arsc, ancienne_argb, nouvelle_argb):
    """Remplace la valeur d'une ressource couleur (Res_value de type ARGB8 = 0x1c)."""
    motif = struct.pack('<HBBI', 8, 0, 0x1C, ancienne_argb)
    if arsc.count(motif) != 1:
        raise ValueError(f'couleur {ancienne_argb:#010x} trouvée {arsc.count(motif)} fois')
    return arsc.replace(motif, struct.pack('<HBBI', 8, 0, 0x1C, nouvelle_argb))
