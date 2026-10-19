# Kirjoita ohjelma, joka laskee, kuinka monessa sanassa listassa on enemmän kuin 5
# kirjainta.
# Luo lista itse ja käytä len()-funktiota sanojen pituuden tarkistamiseen.

list1 = ["puu", "omena", "talo", "banaani", "meri", "mansikka", "auto", "kissa", "porkkana", "tie", 
        "kurkku", "koira", "lumi", "tomaatti", "kuu", "tuoli", "herne", "mustikka", "sade", "kirja", 
        "kala", "ananas", "valo", "sipuli", "maa", "peruna", "tuuli", "kaali", "myrsky", "pöytä"]

var1 = 0

for var2 in list1:
    if len(var2) > 5:
        var1 += 1

print(f"Listassa on {var1}kpl sanoja, joissa on enemmän kuin 5 kirjainta.")