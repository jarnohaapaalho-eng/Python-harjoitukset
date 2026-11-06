"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa
listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma, jossa luot
listan, kutsut funktiota ja tulostat sen palauttaman summan.
"""

def laske(lista):
    yhteensa = 0

    for luku in lista:
        yhteensa = yhteensa + luku
    return yhteensa

lista = [1,2,3,4,5,6,10]

yhteensa = laske(lista)

print(f"Listan summa on: {yhteensa}")