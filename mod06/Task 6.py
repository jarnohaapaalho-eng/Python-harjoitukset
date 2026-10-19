# Kirjoita ohjelma, joka pyytää käyttäjää syöttämään arvoja ja lisää ne listaan. Jokaisen
# lisäyksen jälkeen lista tulostetaan kahdella tavalla: lisäysjärjestyksessä ja pienimmästä
# suurimpaan järjestettynä. Ohjelma lopettaa, kun käyttäjä syöttää 0.

list1 = []

var1 = int(input("Kirjoita jokin kokonaisluku, tulostan ne siinä järjestyksessä missä olet lisännyt ne sekä pienimmästä suurimpaan. Lopeta ohjelma kirjoittalmalla luku '0'"))

while True:
    if var1 == 0:
        break
    else:
        list1.append(var1)
        print(*list1)
        print(*sorted(list1))
        var1 = int(input("Anna seuraava luku: "))