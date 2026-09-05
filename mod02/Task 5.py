# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. 
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.

leiviska = float(input("Kuinka monta leiviskää? "))
naula = float(input("Montako naulaa? "))
luoti = float(input("Ja luotia? "))

print("Nämä painaa",int(((luoti*13.3)+(naula*32*13.3)+(leiviska*20*32*13.3))/1000),
      "kiloa ja",
      (((luoti*13.3)+(naula*32*13.3)+(leiviska*20*32*13.3))%1000),"grammaa.")