# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
# Tätä jatketaan, kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
# Edellisessä tapauksessa tulostetaan ”Tervetuloa” ja jälkimmäisessä ”Pääsy evätty”. 
# Valitse itse oikea käyttäjätunnus ja salasana (älä käytä oikeita…)

yritetty = 0

while True:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == "Admin" and salasana == "Admin":
        print("Tervetuloa!")
        break

    else:
        print("Väärin, yritä uudestaan.")
        
    yritetty += 1
    if yritetty == 5:
        print("Pääsy evätty.")
        break