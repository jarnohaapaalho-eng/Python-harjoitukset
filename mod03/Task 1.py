# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. 
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen 
# ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. 
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha_minimi = 37
kuha = float(input("Kuinka pitkän kuhan sait pyydystettyä? "))

if kuha < kuha_minimi:
    puuttuva_pituus = kuha_minimi - kuha
    print(f"Laske kuha takaisin järveen! Se on valitettavasti {puuttuva_pituus}cm liian lyhyt.")
else:
    print("Jopas jotakin! Taitaa olla kalavale!")