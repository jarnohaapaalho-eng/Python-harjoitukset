# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. 
# Vuosi on karkausvuosi, jos se on jaollinen neljällä. 
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Anna vuosiluku, tarkastan onko se karkausvuosi: "))

if vuosi % 400 == 0:
    print("Se on karkausvuosi!")
elif vuosi % 100 == 0:
    print("Nope")
elif vuosi % 4 == 0:
    print("Se on karkausvuosi!")
else: 
    print("Nope")