"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen
yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 20-tahkoista
roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan
pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä
ohjelman suorituksen alussa.
"""

import random

def noppa(nopan_koko):
    silmaluku = random.randint(1, nopan_koko)
    return silmaluku

nopan_koko = int(input("Anna nopan silmien lukumäärä: "))

while True:
    heitto = noppa(nopan_koko)
    print(f"Heitit {heitto}!")

    if heitto == nopan_koko:
        break