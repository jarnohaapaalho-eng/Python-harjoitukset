# Harjoituksia

lista = ["maito", "leipä", "pasta", "juusto", "makkara"]

while lista:

    tuote = input("Mitä ostit? ").lower()

    if tuote in lista:
        lista.remove(tuote)
        print("Jäljellä:", lista)
    else:
        print("Ei löydy listalta!")

print("Shoppailu done")