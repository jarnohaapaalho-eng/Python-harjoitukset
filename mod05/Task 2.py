# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää
# tyhjän merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi
# suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille
# argumentiksi reverse=True.

luvut = []

while True:
    syote = input("Anna luku, paina Enteriä lopettaaksesi lukujen syöttämisen: ")
    if syote == "":
        break
    luvut.append(float(syote))
luvut.sort(reverse=True)

print("Tässä sinulle suurinta lukua:")
for luku in luvut[0:5]:
    print(luku)