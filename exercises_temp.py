# This .py file is intended as temporary exercises done during the class or otherwise



nimi = input("Mikä nimesi on? ")

if nimi == "Matti":
    print("Seuraava, kiitos!")
else:
    maara = int(input("Montako saisi olla? "))
    hinta = maara * 5.90
    print(f"Se tekee {hinta:.2f} €, kiitos!")