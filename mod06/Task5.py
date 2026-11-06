"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa
toisen listan, joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä
on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma, jossa luot
listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
"""

def laske(lista_1):
    lista_2 = []

    for luku in lista_1:
        if luku % 2 == 0:
            lista_2.append(luku)
    return lista_2

lista = [1,2,3,4,5,6,7,10]
karsittu = laske(lista)

print(f"Täysi lista: {lista}")
print(f"Karsittu lista: {karsittu} ")