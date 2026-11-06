"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
silmäluvun väliltä 1-6. Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes
tulee kutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
"""

import random

def noppa():
    silmaluku = random.randint(1,6)
    return silmaluku
while True:
    heitto = noppa()
    print(f"Heitit {heitto}!")

    if heitto == 6:
        break