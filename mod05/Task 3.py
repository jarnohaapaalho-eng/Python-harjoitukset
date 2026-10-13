# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
# o Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13
#   siten, että jako menee tasan.
# o Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös
#   luvulla 3 tai luvulla 7.

luku = int(input("Anna kokonaisluku, katson onko se alkuluku (prime number): "))
alkuluku = True

if luku <= 1:
    alkuluku = False
else:
    for tarkistus in range(2, luku):
        if luku % tarkistus == 0:
            alkuluku = False
            break
if alkuluku:
    print("Oikein, tämä on alkuluku")
else:
    print("Nope")