# Kirjoita ohjelma, joka simuloi tehtaan tuotantoa. Ohjelma kysyy käyttäjältä, mitä tuotetta
# valmistetaan ja kuinka monta kappaletta sitä valmistetaan. Tallenna tuotteiden nimet ja
# määrät omiin listoihinsa.Tämän jälkeen ohjelma kysyy "Jatketaanko tuotantoa?". Jos
# käyttäjä vastaa "Kyllä", ohjelma kysyy seuraavan tuotteen ja sen määrän. Ohjelma jatkaa
# kysymistä, kunnes käyttäjä syöttää "Ei".
# Kun tuotanto lopetetaan, ohjelma tulostaa kaikki valmistetut tuotteet ja niiden määrät.

# Mitä tuotetta valmistetaan? Pöytä
# Kuinka monta valmistetaan? 20
# Jatketaanko tuotantoa? Kyllä
# Mitä tuotetta valmistetaan? Tuoli
# Kuinka monta valmistetaan? 50
# Jatketaanko tuotantoa? Kyllä
# Mitä tuotetta valmistetaan? Hylly
# Kuinka monta valmistetaan? 15
# Jatketaanko tuotantoa? Ei
# Tuotanto lopetettu!
# Valmistetut tuotteet:
# Pöytä: 20 kpl
# Tuoli: 50 kpl
# Hylly: 15 kpl

list1 = []
list2 = []

print("Jos haluat lopettaa tehtaan käytön vastaa kyselyyn tuotannon jatkosta 'Ei' ")

while True:
    var1 = input("Mitä tuotetta valmistetaan? ")
    var2 = int(input("Kuinka monta valmistetaan? "))

    list1.append(var1)
    list2.append(var2)

    lopetus = input("Jatketaanko tuotantoa? ").upper()
    if lopetus == "EI":
        break

print("Tuotanto lopetettu!")
print("Valmistetut tuotteet:")
for n in range(len(list1)):
    print(f"{list1[n]}: {list2[n]} kpl")