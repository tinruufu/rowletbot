from random import random


KOOS = [
    ('Koo!', 2),
    ('Koo! Koo!', 1),
    ('Koo?', 1),
    ('Koo koo!', 1),
    ('Koo~', 1),
    ("*soft chitters*", 0.5),
    ("*flaps and flutters* \(ovo)/", 0.5),
    ('*encouraging hoot*', 0.5),
    ('*sleepy toot* (-v-)~', 0.5),
    ('⁽ᵒᵛᵒ ⁾ *excited hops*', 0.5),
    ("*softly vibrates* ⁽ ' ᵛ '⁾", 0.5),
    ('*smol boops*', 0.5),
    ("""( ovo) *spins furiously*
(   ov)
(     o)
(       )
(o     )
(vo   )
(ovo )
( ovo)
(   ov)""", 0.5)]


def koo():
    target = random() * sum((k[1] for k in KOOS))
    total = 0
    for koo, weight in KOOS:
        total += weight
        if total >= target:
            return koo


if __name__ == '__main__':
    print(koo())
