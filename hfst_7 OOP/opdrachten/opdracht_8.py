# Maak een klasse Rechthoek & Punt zoals aangegeven in opdracht 8.

    

" Via onderstaande code kan je niveau 1 testen. "
# r1 = Rechthoek(breedte=4, hoogte=5)    # Correct
# r2 = Rechthoek(breedte=-4, hoogte=5)   # Raise exception
# r3 = Rechthoek(breedte=-4, hoogte=-5)  # Raise exception


" Via onderstaande code kan je niveau 2 testen. "
# print(r1.omtrek())      # 18
# print(r1.oppervlakte()) # 20


" Via onderstaande code kan je niveau 3 testen. "
# r1 = Rechthoek(breedte=4, hoogte=5, x=3, y=3)
# r2 = Rechthoek(breedte=4, hoogte=4, x=0, y=0)
# r3 = Rechthoek(breedte=4, hoogte=4, x=100, y=100)
# p1 = Punt(x=5, y=7)

# print( p1.zit_in(r1) ) # True
# print( p1.zit_in(r2) ) # False
# print( p1.zit_in(r3) ) # False


" (EXTRA) Via onderstaande code kan je niveau 4 testen. "
# r1 = Rechthoek(breedte=4, hoogte=5, x=3, y=3)
# r2 = Rechthoek(breedte=4, hoogte=4, x=0, y=0)
# r3 = Rechthoek(breedte=4, hoogte=4, x=100, y=100)
# p1 = Punt(x=5, y=7)

# print(r1.overlapt_met(r2)) # True
# print(r1.overlapt_met(r3)) # False
# print(r1.overlapt_met(p1)) # Argument is geen Rechthoek