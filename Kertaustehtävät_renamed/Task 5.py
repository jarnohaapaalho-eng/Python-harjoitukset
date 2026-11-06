# Kirjoita ohjelma, joka pyytää käyttäjältä sanoja. Jos käyttäjä kirjoittaa sanan "loppu",
# ohjelma tulostaa muodostuneen tarinan ja lopettaa.

# Anna sana lisättäväksi tarinaan: Olipa
# Anna sana lisättäväksi tarinaan: kerran
# Anna sana lisättäväksi tarinaan: kauan
# Anna sana lisättäväksi tarinaan: sitten
# Anna sana lisättäväksi tarinaan: suuri
# Anna sana lisättäväksi tarinaan: vihreä
# Anna sana lisättäväksi tarinaan: lohikäärme
# Anna sana lisättäväksi tarinaan: loppu
# Olipa kerran kauan sitten suuri vihreä lohikäärme

# Bonus: Muuta ohjelmaa niin, että silmukka loppuu myös, jos käyttäjä syöttää saman sanan
# kahdesti peräkkäin.

list1 = []

while True:
    var1 = input("Lisää tarinaan: ")
    if var1 == "loppu":
        break

    list1.append(var1)
print(*list1)

# eipä tullut bonareita :(