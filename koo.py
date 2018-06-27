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
(   ov)
(     o)
(       )
(o     )
(vo   )
(ovo )
( ovo)
(   ov)
(     o)
(       )
(o     )
(vo   )
(ovo )
( ovo)
"""

ROLL = """( ' ᵛ ' ) *ᵇᵒʳᵇ ʳᵒˡˡ*
 (    ‹:)
  (   ̩ ‸ ̩)
   (:›    )
    ( ' ᵛ ' )
     (    ‹:)
      (   ̩ ‸ ̩)
       (:›    )
        ( ' ᵛ ' )
         (    ‹:)
          (   ̩ ‸ ̩)
           (:›    )
           \( ' ᵛ ' )/"""

KOOS = [
    # talk
    ('Koo koo!', 1),
    ('Koo koooo!! Kooooo~~', 1),
    ('Koo! Koo!', 1),
    ('Koo!', 2),
    ('Koo, koo!', 1),
    ('Koo-koo!', 1),
    ('Koo.', 1),
    ('Koo?', 1),
    ('Kooo!', 1),
    ('Kooo; koo? Kooo!', 1),
    ('Koo~', 1),
    ('Pip pip~', 0.5),

    # act
    ("*flaps n' flutters* \\(ovo)/", 0.5),
    ("*soft chitters*", 0.5),
    ("*swoops n' flaps*", 0.5),
    ("*twirls n' whistles*", 0.5),
    ('*a feathery flap*', 0.5),
    ('*chases a leaf*', 0.5),
    ('*does owl things*', 0.5),
    ('*does toots at u*', 0.5),
    ('*falls from the window ledge above yours*', 0.1),
    ('*flapflap*', 0.5),
    ('*flaps onto ur head*\n\nKoo!', 0.5),
    ('*gently nibbles ur finger*', 0.5),
    ('*hop*', 0.5),
    ('*hophop*', 0.5),
    ('*hugs ur leg*', 0.5),
    ('*is ready for adventure*', 0.5),
    ('*lil jig*', 0.5),
    ('*lil spin*', 0.5),
    ('*looks for backpacks*', 0.5),
    ('*peckpeckpeck*', 0.5),
    ('*preens*', 0.5),
    ('*sleeps*', 0.5),
    ('*smol boops*', 0.5),
    ('*soars gracefully*', 0.5),
    ('*stretches wings*', 0.5),
    ('*thinks about popplio*\n\n*smiles*', 0.5),
    ('*waddles about a bit*', 0.5),
    ('>-<', 0.5),

    # refresh
    ("*does a lil flap in time with your shout*", 0.5),
    ("*hugs u so u won't worry*", 0.5),
    ("*toughs it out so u won't feel sad*", 0.5),
    ('*is bursting with enthusiasm*', 0.5),
    ('*is in a bit of a pinch*\n\n*might cry*', 0.1),
    ('*is thinking about poké beans*', 0.5),
    ('*is thrilled to bits*', 0.5),
    ('*looks at u with intense and determined eyes*', 0.5),
    ('*looks at u with trusting eyes*', 0.5),
    ('*seems curious about your fashion*', 0.5),
    ('*sees u*\n\n*feels more secure*', 0.5),
    ('*turns towards u*\n\n*nods in understanding*', 0.5),
    ('*wants to be petted*', 0.5),

    # emote
    ("*ruffles floof* \\(('v'))/", 0.5),
    ("*softly vibrates* ⁽ ' ᵛ '⁾", 0.5),
    ("*tiny toot*", 0.5),
    ("*warm wiggle* ~'v'~", 0.5),
    ("*wing headpats* ( 'v')~", 0.5),
    ('*looks at u* ( ovo )', 0.5),
    ('*sleepy toot* (-v-)~', 0.5),
    ('Koo? ( ‹: )', 0.5),
    ('⁽ᵒᵛᵒ ⁾ *excited hops*', 0.5),
    (SPIN, 0.5),
    (ROLL, 0.5),

    # encourage
    ('*believes in u 100%*', 0.5),
    ('*encouraging hoot*', 0.5),
    ('*is here for u*', 0.5),
    ('*knows u can do it*', 0.5),
    ('*reassuring koos*', 0.5),
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
