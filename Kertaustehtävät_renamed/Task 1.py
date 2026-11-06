# Kirjoita ohjelma, joka kysyy tuntipalkan, tehdyt tunnit ja viikonpäivän. Ohjelma tulostaa
# päiväpalkan, joka on tuntipalkka kerrottuna tehdyillä tunneilla, paitsi sunnuntaina, jolloin
# tuntipalkka on kaksinkertainen.

Tuntipalkka = float(input("Lasken kuinka paljon olet ansainnut tänään. Kerro ensin mikä on tuntipalkkasi? "))
Tunnit = float(input("Kerrotko myös montako tuntia olet tehnyt tänään töitä? "))
Vkp = input("Ja vielä viikonpäivän, sillä jos tänään on sunnuntai saat tupla palkan! ").upper()

if Vkp == "SUNNUNTAI":
    print(f"Olet ansainnut tänään {Tuntipalkka*Tunnit*2} euroa.")
else:
    print(f"Olet ansainnut tänään {Tunnit*Tuntipalkka} euroa")