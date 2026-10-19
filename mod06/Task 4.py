# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaislukuja. Jos luku on pienempi kuin nolla,
# ohjelma tulostaa viestin "Virheellinen numero". Jos luku on suurempi kuin nolla, ohjelma
# tulostaa luvun neliöjuuren Pythonin sqrt-funktiolla. Molemmissa tapauksissa ohjelma kysyy
# sen jälkeen uutta lukua. Jos käyttäjä syöttää luvun nolla, ohjelma lopettaa kysymisen ja
# poistuu silmukasta.
# Esimerkki sqrt-funktion käytöstä:
#   from math import sqrt
#   print(sqrt(9)

import math

var1 = int(input("Anna jokin luku, mieluiten pienempi kuin nolla."))

while var1 > 0:
    print(f" {math.sqrt(var1)}")
    var1 = int(input("Anna seuraava numero"))

if var1 <= 0:
    print("Sanoin, että mielummin pienempi kuin nolla... ")
else:
    print("Heipparallaa")