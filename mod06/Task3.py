"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy
gallonamäärän käyttäjältä ja muuntaa sen litroiksi. Muunnos on tehtävä funktiota
hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää
negatiivisen gallonamäärän.
o Yksi gallona on 3,785 litraa
"""

def bensa(gallona):
    litra = 3.785 * gallona
    return litra

while True:
    gallona = float(input("Anna bensan määrä gallonina (Negatiivinen luku päättää ohjelman): "))

    if gallona >= 0:
        litra = bensa(gallona)
        print(f"Bensan määrä on {litra} litroina.")
    else:
        break