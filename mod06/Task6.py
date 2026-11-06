"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä
ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
"""

import math

def pizza(halkaisija, hinta):
    sade = (halkaisija / 2) / 100
    ala = math.pi * (sade ** 2)
    y_hinta = hinta / ala
    return y_hinta

halkaisija_1 = float(input("Anna ensimmäisen pizzan halkaisija sentteinä: "))
hinta_1 = float(input("Anna ensimämisen pizzan hinta euroina: "))

halkaisija_2 = float(input("Anna toisen pizzan halkaisija sentteinä: "))
hinta_2 = float(input("Anna toisen pizzan hinta euroina: "))

pizza_1 = pizza(halkaisija_1, hinta_1)
pizza_2 = pizza(halkaisija_2, hinta_2)

print (f"Ensimämisen pizzan neliöhinta on {pizza_1} euroa per neliö")
print (f"Toisen pizzan neliöhinta on {pizza_2} euroo per neliö")

if pizza_1 < pizza_2:
    print("Ensimmäinen pizza on halvempi per neliö")
else:
    print("Toinen pizza on halvempi per neliö")
