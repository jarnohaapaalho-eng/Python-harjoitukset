# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. Ohjelma heittää
# kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä fortoistorakennetta.

import random

maara = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for laskuri in range(maara):
    noppa = random.randint(1, 6)
    summa += noppa
print(f"Sait {summa}!")