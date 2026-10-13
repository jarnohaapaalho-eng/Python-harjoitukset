# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä
# for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen. Lopuksi
# ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
# kuin ne syötettiin. käytä for-toistorakennetta nimien kysymiseen ja for/in
# toistorakennetta niiden läpikäymiseen.

kaupungit = []

for n in range(5):
    kaupunki = input("Syötä viisi eri kaupungin nimea, tulostan ne aakkosjärjestyksessä: ")
    kaupungit.append(kaupunki)
print("Kaupungit ovat:")
for kaupunki in kaupungit:
    print(kaupunki)