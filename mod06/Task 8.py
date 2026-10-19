# Kirjoita ohjelma, jossa on lista viiden tuotteen valmistuskustannuksista. Ohjelma käy
# kustannukset läpi for-silmukan avulla ja tulostaa jokaisen kustannuksen. Samalla ohjelma
# laskee kaikkien tuotteiden valmistuskustannukset yhteen. Lopuksi ohjelma tulostaa
# kokonaiskustannuksen.
# Esimerkki ohjelman tulostuksesta:

# Tuotteen valmistuskustannus: 12.5 €
# Tuotteen valmistuskustannus: 8.2 €
# Tuotteen valmistuskustannus: 15.0 €
# Tuotteen valmistuskustannus: 6.5 €
# Tuotteen valmistuskustannus: 10.8 €
# Valmistuskustannukset yhteensä: 53.0 €

list1 = []


for n1 in range(5):
    var1 = float(input("Anna viiden eri tuotteen valmistuskustannukset: "))
    list1.append(var1)

var2 = 0
for n2 in list1:
    var2 += n2

print(f"Valmistuskustnanukset ovat {list1} ja kokonaiskustannukset ovat {var2}")
