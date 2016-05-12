from random import random


KOOS = [
    ('Koo!', 4),
    ('Koo! Koo!', 2),
    ('Koo?', 1),
    ('Koo koo!', 1),
    ('*soft hoot*', 0.5),
    ('⁽ᵒᵛᵒ ⁾ *ᵉˣᶜᶦᵗᵉᵈ ʰᵒᵖˢ*', 0.5),
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
