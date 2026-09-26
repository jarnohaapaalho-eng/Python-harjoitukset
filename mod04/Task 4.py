# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1–10. 
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, 
# Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

arvattava_luku = random.randint(1, 10)

while True:
    arvattu_luku = float(input("Arvaa luku 1-10 välillä: "))

    if arvattu_luku == arvattava_luku:
        print("Oikein")
        break

    elif arvattu_luku < arvattava_luku:
        print("Liian pieni arvaus")

    else:
        print("Liian suuri arvaus")