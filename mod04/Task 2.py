# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan 
# kunnes käyttäjä antaa negatiivisen tuumamäärän. 
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

while True:
    tuuma = float(input("Anna minulle mitta tuumina ja muunnan sen senttimetreiksi."))
    cm = tuuma * 2.54
    if tuuma >= 0:
        print(cm)
        print("Anna minulle seuraava luku")
    else:
        print("Nope")
        break