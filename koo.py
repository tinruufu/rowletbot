from random import random


SPIN = """( ovo) *spins furiously*
(   ov)
(     o)
(       )
(o     )
(vo   )
(ovo )
( ovo)
(   ov)"""

KOOS = [
    ('Koo!', 2),
    ('Koo! Koo!', 1),
    ('Koo?', 1),
    ('Koo koo!', 1),
    ('Koo~', 1),
    ('Pip pip~', 0.5),
    ("*soft chitters*", 0.5),
    ("*flaps n' flutters* \\(ovo)/", 0.5),
    ('*encouraging hoot*', 0.5),
    ("*warm wiggle* ~'v'~", 0.5),
    ("*ruffles floof* \\(('v'))/", 0.5),
    ('*sleepy toot* (-v-)~', 0.5),
    ('⁽ᵒᵛᵒ ⁾ *excited hops*', 0.5),
    ("*softly vibrates* ⁽ ' ᵛ '⁾", 0.5),
    ('*smol boops*', 0.5),
    (SPIN, 0.5),
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
