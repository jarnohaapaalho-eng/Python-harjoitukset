# This .py file is intended as temporary exercises done during the class or otherwise
# Now a calculator?

# Komia laskin
print("         ------------")
print("         -> LASKIN <-")
print("         ------------")

# Aloittaa "loopin"
while True:

    # Toistettavat tekstit. Laskimen "Nolla" piste
    print("Valitse mitä toimintoa haluat käyttää:")
    print("[A] Yhteenlasku, [B] Vähennyslasku, [C] Kertolasku, [D] Jakolasku, [Q] Lopeta ohjelma.")

    # Tallentaa valinnan muuttujan, muuttaa tekstin isoksi kirjaimeksi
    valinta = input("Valintasi: ").upper()

    # Tarkistaa haluaako käyttäjä poistua laskimesta
    if valinta == "Q":
        print(f"Poistutaan...")
        break

    # Tarkistaa onko annettu valinta virheellinen
    elif valinta != "A" and valinta != "B" and valinta != "C" and valinta != "D":
        print("Virheellinen valinta. Yritä uudelleen.")

    # Muuttujat laskentaa varten
    a = float(input("Ensimmäinen luku: "))
    b = float(input("Toinen luku: "))

    if valinta == "A":
        print(f"Lukujen {a} ja {b} summa on {a+b}.")
    elif valinta == "B":
        print(f"Lukujen {a} ja {b} erotus on {a-b}.")
    elif valinta == "C":
        print(f"Lukujen {a} ja {b} tulo on {a*b}.")
    elif valinta == "D":
        print(f"Lukujen {a} ja {b} osamäärä on {a/b}.")

    # Tarkistaa onko valinta virheellinen ja palauttaa loopin alkuunsa
    else:
        print("Virheellinen valinta.")
        continue


# Tehtävä <----
# Keksi parempi kohta ilmoittaa virheelllisestä valinnasta.
# Kommentoi koodia, mitä se tekee. Step by step