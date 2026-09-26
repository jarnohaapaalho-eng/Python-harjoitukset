# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman. 
# Huomioi, että sinun tulee ”pitää kirjaa” siitä, mikä on pienin ja suurin luku.

numero = input("Anna jokin numero: ")

if numero != "":
    pienin = float(numero)
    suurin = float(numero)

    while True:
        numero = input("Anna seuraava numero: ")
        if numero == "":
            break
        
        luku = float(numero)
        elif luku < pienin:
            pienin = luku
        elif luku > suurin:
            suurin = luku

    print(f"Pienin luku oli: {pienin}")
    print(f"Suurin luku oli: {suurin}")
    