# Kirjoita ohjelma, joka simuloi tuotantolinjan toimintaa. Ohjelma tulostaa viestin "Tuote
# valmistettu!" ja kysyy sen jälkeen "Jatketaanko tuotantoa?" niin kauan, kunnes käyttäjä
# syöttää "Ei". Tämän jälkeen ohjelma tulostaa "Tuotanto lopetettu!" ja päättyy.

var1 = input("Aloita tuotanto kertomalla mitä haluat valmistaa.")

while var1 != "Ei":
    print("Tuote on valmistetu.")
    var1 = input("Jatketaanko tuotantoa?")
    
print("Tuotanto lopetettu")