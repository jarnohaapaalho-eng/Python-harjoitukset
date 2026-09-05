# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. 
# Ohjelma tulostaa suorakulmion piirin ja pinta-alan. 
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = float(input("Suorakulmion kanta: "))
korkeus = float(input("Suorakulmion korkeus: "))

print("Suorakulmion piiri: ",2*(kanta+korkeus))
print("Suorakulmion pinta-ala: ",kanta*korkeus)