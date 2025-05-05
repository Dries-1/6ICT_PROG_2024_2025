" Je kan de code ook rechtstreeks vanuit dit bestand uitvoeren. "
" Pas hiervoor het pad aan zodat je in de folder met opdracht 10 staat. "
from opdracht_10 import Speler, Spel

" Via onderstaande code kan je niveau 1 testen. "

# " Maak spelers aan. "
# speler_1 = Speler("Jan", 10, 100)
# speler_2 = Speler("Piet", 4, 400)
# speler_3 = Speler("Joris", 9, 50)

# " Verhoog level van spelers. "
# speler_1.level_up() # Jan is level 11 geworden.
# speler_2.level_up() # Piet is level 5 geworden.

# print("\n#############\n")

# " Geef spelers een hogere score. "
# speler_1.verhoog_score(100) # GEEN PRINT: score zou nu 200 moeten zijn.
# speler_2.verhoog_score("1000000") # 'verhoog_score' vereist int, niet <class 'str'>.
# speler_3.verhoog_score(450) # GEEN PRINT: score zou nu 500 moeten zijn.

# print("\n#############\n")

# " Toon info van spelers. "
# speler_1.info() # Jan (lvl 11): score 200.
# speler_2.info() # Piet (lvl 5): score 400.
# speler_3.info() # Joris (lvl 9): score 500.



" Via onderstaande code kan je niveau 2 testen. "

# " Maak spelers & spellen aan. "
# speler_1 = Speler("Jan", 3, 100)
# speler_2 = Speler("Piet", 4, 400)
# speler_3 = Speler("Joris", 9, 50)
# speler_4 = Speler("Korneel", 9, 200)

# spel_1 = Spel("Schaak")
# spel_2 = Spel("Wiezen")

# " Voeg spelers toe aan spellen. "
# spel_1.speler_toevoegen(speler_1) # Jan doet mee aan Schaak.
# spel_1.speler_toevoegen(speler_2) # Piet doet mee aan Schaak.

# spel_2.speler_toevoegen("SPELER_1") # 'speler_toevoegen' vereist Speler, niet <class 'str'>.
# spel_2.speler_toevoegen(speler_2)   # Piet doet mee aan Wiezen.
# spel_2.speler_toevoegen(speler_3)   # Joris doet mee aan Wiezen.
# spel_2.speler_toevoegen(speler_4)   # Korneel doet mee aan Wiezen.

# print("\n#############\n")

# " Speel wat spellen " 
# spel_1.spelen() # Piet is gewonnen. Nieuwe score is 500.      --> Piet wint altijd
# spel_1.spelen() # Piet is gewonnen. Nieuwe score is 600.      --> Piet wint altijd
# spel_2.spelen() # Korneel is gewonnen. Nieuwe score is 300.   --> Joris of Korneel wint at-random
# spel_2.spelen() # Joris is gewonnen. Nieuwe score is 150.     --> Joris of Korneel wint at-random

# print("\n#############\n")

# " Toon scorebord voor ieder spel "
# spel_1.scorebord()  # Huidige scores van spelers in Schaak... --> DIT STAAT VAST
#                     # Jan (lvl 3): 100
#                     # Piet (lvl 4): 600
# spel_2.scorebord()  # Huidige scores van spelers in Wiezen... --> DIT IS RANDOM
#                     # Piet (lvl 4): 600
#                     # Joris (lvl 9): 150   
#                     # Korneel (lvl 9): 300