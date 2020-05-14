from itertools import chain
from random import random

from inflect import engine

from constants import BERRIES, MONS, MOVES

inflect = engine()


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
           \\( ' ᵛ ' )/"""


def possessify(noun):
    return ("{}'" if noun[-1] == 's' else "{}'s").format(noun)


def monify(fmt, probability, possessive=False):
    return [(
        fmt.format(
            possessify(mon.lower())
            if possessive else mon.lower()
        ),
        probability/len(MONS)
    ) for mon in MONS]


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
    ('*flaps onto ur shoulder*', 0.5),
    ('*gently nibbles ur finger*', 0.5),
    ('*hop*', 0.5),
    ('*hophop*', 0.5),
    ('*hugs ur leg*', 0.5),
    ('*is cheering for you!*', 0.5),
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
    ('*does many happy flaps*', 0.5),
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

    # let's go
    ('*battles sleep*', 0.5),
    ('*blushes happily for some reason*', 0.5),
    ('*brims with hopping spirit*', 0.5),
    ('*calls out to u*', 0.5),
    ('*checks out the buildings*', 0.5),
    ('*curiously surveys the room*', 0.5),
    ('*enjoys the fresh breeze blowing past*', 0.5),
    ('*enjoys the warmth of the sun*', 0.5),
    ('*feels calm and relaxed*', 0.5),
    ('*feels totally carefree*', 0.5),
    ('*feels very calm*', 0.5),
    ('*fidgets around*', 0.5),
    ('*found something in the plants!*', 0.1),
    ('*gazes up aimlessly at the sky*', 0.5),
    ('*gives a strong, reassuring nod*', 0.5),
    ('*gives u a knowing nod*', 0.5),
    ('*greets u energetically*', 0.5),
    ('*happily plays with u*', 0.5),
    ('*has a curiously triumphant expression*', 0.5),
    ('*has a lot of energy*', 0.5),
    ('*has a vacant look*', 0.5),
    ('*has energy to spare*', 0.5),
    ('*hoots some kind of tune*', 0.5),
    ('*hops up and down, overjoyed*', 0.5),
    ('*hurriedly looks all around*', 0.5),
    ('*is a little proud of something*', 0.5),
    ('*is alert, looks all around*', 0.5),
    ('*is bursting with energy*', 0.5),
    ('*is energetically following you*', 0.5),
    ('*is happy to toot at u*', 0.5),
    ('*is having a lot of fun!*', 0.5),
    ('*is having fun following u from behind*', 0.5),
    ('*is hopping around with a cool look on borbface*', 0.5),
    ('*is interested in that new game console*', 0.5),
    ('*is interested in the smell of the dirt*', 0.5),
    ('*is itchy and can\'t stay quiet*', 0.5),
    ('*is really pleased*', 0.5),
    ('*is surprised at how bright the sun is*', 0.5),
    ('*listens intently*', 0.5),
    ('*looks around restlessly*', 0.5),
    ('*looks curiously at a rowlet reflection in ur eyes*', 0.5),
    ('*looks happy*', 0.5),
    ('*looks ur way, startled*', 0.5),
    ('*may have had a good idea!*', 0.5),
    ('*mimics ur rival*', 0.5),
    ('*nimbly hops in the air*', 0.5),
    ('*overflows with energy*', 0.5),
    ('*plots something*', 0.5),
    ('*pokes and plays with the ground*', 0.5),
    ('*pokes at ur legs*', 0.5),
    ('*pokes u*', 0.5),
    ('*prepares for the next adventure!*', 0.5),
    ('*relaxes comfortably*', 0.5),
    ('*responds energetically*', 0.5),
    ('*restlessly darts between ur shoulder and the ground*', 0.5),
    ('*rolls a stone around*', 0.5),
    ('*seems a little embarrassed about something*', 0.5),
    ('*seems to be having fun*', 0.5),
    ('*sleepily nods off*', 0.5),
    ('*sleeps and becomes healthy*', 0.5),
    ('*sleeps peacefully*', 0.5),
    ('*smiles even more sweetly than usual*', 0.5),
    ('*sneezes*', 0.5),
    ('*sniffs around the room*', 0.5),
    ('*sniffs at the air*', 0.5),
    ('*sniffs at the ground*', 0.5),
    ('*stares at u*', 0.5),
    ('*stares at ur outfit*', 0.5),
    ('*stares happily at the swaying flowers*', 0.5),
    ('*still has an ample amount of energy*', 0.5),
    ('*stretches out and relaxes*', 0.5),
    ('*suddenly acts playfully with u*', 0.5),
    ('*surveys the vicinity*', 0.5),
    ('*takes it easy*', 0.5),
    ('*tries to be quiet*', 0.5),
    ('*turns ur way and grins happily*', 0.5),
    ('*vigorously embraces u*', 0.5),
    ('*wants to be praised, perhaps*', 0.5),
    ('*wants to play*', 0.5),
    ('*wants to venture farther ahead as soon as possible*', 0.5),

    # swsh
    ('*dozes off due to is sleepy*', 0.5),
    ('*enjoys camping*', 0.5),
    ('*enjoys the calm air*', 0.5),
    ('*expects u to come up with a great strategy!*', 0.5),
    ('*hides on drakloak\'s head*', 0.1),
    ('*is a bit worried about being able to do well*', 0.5),
    ('*is full and satisfied!*', 0.5),
    ('*is happy to be with u*', 0.5),
    ('*is having fun*', 0.5),
    ('*is in a good mood*', 0.5),
    ('*is reassured by your familiar scent*', 0.5),
    ('*is refreshed by the rain!*', 0.5),
    ('*is still full of energy!*', 0.5),
    ('*is strong AND cute*', 0.5),
    ('*is tired and hungry*', 0.5),
    ('*is training to become huge*', 0.5),
    ('*likes u a lot*', 0.5),
    ('*likes u*', 0.5),
    ('*likes waiting in lines*', 0.5),
    ('*looks very hungry*', 0.5),
    ('*really wants some time to play with u*', 0.5),
    ('*remembers first meeting u*', 0.5),
    ('*seems a bit bored*', 0.5),
    ('*seems a bit nervous*', 0.5),
    ('*seems curious about you*', 0.5),
    ('*seems worried about surroundings*', 0.5),
    ('*thinks about camping*', 0.5),
    ('*wants more attention*', 0.5),
    ('*wants to be here for u forever*', 0.5),
    ('*wants to eat yummy food*', 0.5),
    ('*wants to go somewhere far away*', 0.5),
    ('*wants to play a lot with u*', 0.5),
    ('*wants to play more*', 0.5),
    ('*wants to play with a poké toy*', 0.5),
    ('*wants to play with other pokémon*', 0.5),
    ('*wants to visit lots of different places*', 0.5),

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
] + [
    ('*wants to learn {}*'.format(move.lower()), 1/len(MOVES))
    for move in MOVES
] + list(chain(*(monify(fmt, chance, poss) for fmt, chance, poss in [
    ("*doesn't understand {}*", 0.5, False),
    ("*doesn't understand {} very well*", 0.5, False),
    ("*is a little scared of {}*", 0.5, False),
    ("*is interested in {} scent*", 0.5, True),
    ("*seems afraid of {}*", 0.5, False),
    ("*wants to play with {}*", 1, False),
])))


def _find_dupe_koos():
    seen_koos = set()

    for k, p in KOOS:
        if k in seen_koos:
            raise ValueError('{} is in KOOS more than once'.format(k))
        seen_koos.add(k)


def koo():
    target = random() * sum((k[1] for k in KOOS))
    total = 0
    for koo, weight in KOOS:
        total += weight
        if total >= target:
            return koo


_find_dupe_koos()


if __name__ == '__main__':
    print(koo())
