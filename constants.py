import os


def _constants_from(fn):
    with open(os.path.join(os.path.dirname(__file__), fn)) as f:
        return [ln.strip() for ln in f.readlines() if ln.strip()]


BERRIES = """
Cheri Chesto Pecha Rawst Aspear Leppa Oran Persim Lum Sitrus Figy Wiki Mago
Aguav Iapapa Razz Bluk Nanab Wepear Pinap Pomeg Kelpsy Qualot Hondew Grepa
Tamato Cornn Magost Rabuta Nomel Spelon Pamtre Watmel Babiri Chilan Liechi
Ganlon Salac Petaya Apicot Lansat Starf Enigma Micle Custap Jaboca Rowap Roseli
Kee Maranga
""".split()


MONS = _constants_from('mons.txt')
MOVES = _constants_from('moves.txt')
