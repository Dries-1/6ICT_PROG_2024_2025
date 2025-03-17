# Maak een klasse rechthoek zoals aangegeven in opdracht 4.



" Oplossing niveau 1: "
# r1 = Rechthoek(breedte=4, hoogte=5)    # Correct
# r2 = Rechthoek(breedte=-4, hoogte=5)   # Raise exception
# r3 = Rechthoek(breedte=-4, hoogte=-5)  # Raise exception

" Oplossing niveau 2: "
# print(r1.omtrek())      # 18
# print(r1.oppervlakte()) # 20

" Oplossing niveau 3: "
# r1.vergelijk_omtrek(15)         # Getal is kleiner dan omtrek rechthoek.
# r1.vergelijk_oppervlakte(20)    # Getal is groter dan opp rechthoek.