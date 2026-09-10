# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

annettu_arvo = int(input("Ilmoitatko minulle hemoglobiiniarvosi? "))
sukupuoli = input("Oletko mies [M] vai nainen [N]? ").upper()

if sukupuoli == "M":
    if annettu_arvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif annettu_arvo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")

elif sukupuoli == "N":
    if annettu_arvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif annettu_arvo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")