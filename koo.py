from random import random

from inflect import engine

inflect = engine()


BERRIES = """
Cheri Chesto Pecha Rawst Aspear Leppa Oran Persim Lum Sitrus Figy Wiki Mago
Aguav Iapapa Razz Bluk Nanab Wepear Pinap Pomeg Kelpsy Qualot Hondew Grepa
Tamato Cornn Magost Rabuta Nomel Spelon Pamtre Watmel Babiri Chilan Liechi
Ganlon Salac Petaya Apicot Lansat Starf Enigma Micle Custap Jaboca Rowap Roseli
Kee Maranga
""".split()  # thank u bulbapedia

SPIN = """( ovo) *spins furiously*
(   ov)
(     o)
(       )
(o     )
(vo   )
(ovo )
( ovo)
(   ov)"""

ROLL = """( ' ᵛ ' ) *ᵇᵒʳᵇ ʳᵒˡˡ*
 (    ‹:)
  (   ̩ ‸ ̩)
   (:›    )
    ( ' ᵛ ' )
     (    ‹:)
      (   ̩ ‸ ̩)
       (:›    )
        ( ' ᵛ ' )"""

KOOS = [
    # talk
    ('Koo!', 2),
    ('Koo! Koo!', 1),
    ('Koo?', 1),
    ('Koo koo!', 1),
    ('Koo~', 1),
    ('Koo, koo!', 1),
    ('Koo.', 1),
    ('Pip pip~', 0.5),

    # act
    ("*soft chitters*", 0.5),
    ("*flaps n' flutters* \\(ovo)/", 0.5),
    ('*hophop*', 0.5),
    ('*lil spin*', 0.5),
    ('*peckpeckpeck*', 0.5),
    ('*smol boops*', 0.5),
    ('*hop*', 0.5),
    ('*preens*', 0.5),
    ('*lil jig*', 0.5),

    # emote
    ("*warm wiggle* ~'v'~", 0.5),
    ("*ruffles floof* \\(('v'))/", 0.5),
    ('*sleepy toot* (-v-)~', 0.5),
    ('⁽ᵒᵛᵒ ⁾ *excited hops*', 0.5),
    ("*softly vibrates* ⁽ ' ᵛ '⁾", 0.5),
    ("*wing headpats* ( 'v')~", 0.5),
    ('*looks at u* ( ovo )', 0.5),
    ('Koo? ( ‹: )', 0.5),
    (SPIN, 0.5),
    (ROLL, 0.5),

    # encourage
    ('*encouraging hoot*', 0.5),
    ('*reassuring koos*', 0.5),
    ('*knows u can do it*', 0.5),
    ('*believes in u 100%*', 0.5),
    ('*will protect u*', 0.5),
    ('*brings u a poké puff*', 0.2),
] + [
    ('*brings u {} berry*'.format(inflect.a(b.lower())), 1/len(BERRIES))
    for b in BERRIES
]


def koo():
    target = random() * sum((k[1] for k in KOOS))
    total = 0
    for koo, weight in KOOS:
        total += weight
        if total >= target:
            return koo


if __name__ == '__main__':
    print(koo())
