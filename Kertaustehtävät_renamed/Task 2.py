# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun. Jos luku on jaollinen kolmella,
# ohjelma tulostaa ”kolmella jaollinen”. Jos luku on jaollinen viidellä, ohjelma tulostaa "viidellä
# jaollinen". Jos luku on jaollinen sekä kolmella että viidellä, ohjelma tulostaa ”jaollinen
# molemmilla luvuilla!".

var1 = int(input("Anna minulle jokin luku, tarkastan onko se jaollinen kolmella tai viidellä: "))

if var1 % 3 == 0:
    if var1 % 5 == 0:
        print("Luku on jaollinen viidellä ja kolmella.")
    else:
        print("Luku on jaollinen kolmella.")
elif var1 % 5 == 0:
    print("Luku on jaollinen viidellä.")
else:
    print("Se ei ole jaollinen kummallakaan O.o ")