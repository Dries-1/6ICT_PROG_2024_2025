# Dit testbestand is bedoeld om de ontwikkeling van shapes.py te testen. 
# Het bevat al een paar voorbeelden van dingen om te controleren.
# Begin met het lezen van README.md
from vormen import Rechthoek, Vierkant, Ruit

" Testen van klasse Rechthoek "
# recht = Rechthoek(10, 5)

# # Oppervlakte berekenen & hoogte wijzigen.
# print(recht.get_oppervlakte())                      # 50  
# recht.set_hoogte(3)                                 #
# print(recht.get_oppervlakte())                      # 30  


# # Hoe ziet deze rechthoek er uit?
# print(f"Rechthoek: {recht.breedte}x{recht.hoogte}") # Rechthoek: 10x3
# print(recht.afbeelding())
# """ --> 3 regels (=hoogte), met iedere regel 10 asterisken (=breedte)
# **********
# **********
# **********
# """

# # Hoevaak past een rechthoek van 4x3 in bovenstaande rechthoek?
# andere_recht = Rechthoek(4,3) 
# print(recht.get_hoeveel_binnen(andere_recht))       # 2


" Testen van klasse Vierkant "
# vierk = Vierkant(9)

# # Oppervlakte berekenen & zijde wijzigen.
# print(vierk.get_oppervlakte()) # 81
# vierk.set_zijde(5)             #
# print(vierk.get_oppervlakte()) # 25
# vierk.set_breedte(4)           #
# print(vierk.get_oppervlakte()) # 16

# # Hoe ziet het vierkant er uit?
# print(f"Vierkant: {vierk.breedte}x{vierk.hoogte}") # Vierkant: 4x4
# vierk.afbeelding()
# """ --> 4 regels (=hoogte), met iedere regel 4 asterisken (=breedte)
# ****
# ****
# ****
# ****
# """

# # Hoevaak past een rechthoek van 4x3 in bovenstaand vierkant
# andere_recht = Rechthoek(4,3) 
# print(vierk.get_hoeveel_binnen(andere_recht))       # 1


" Testen van klasse Ruit "
# ruit = Ruit(5,9)

# # Oppervlakte berekenen & get_hoeveel_binnen proberen.
# ruit.get_oppervlakte()    # 22.5
# ruit.get_hoeveel_binnen() # Deze methode is niet beschikbaar voor ruiten.

# # Hoe ziet de ruit er uit?
# ruit.afbeelding()
# """ --> 9 regels (=hoogte), met 5 asterisken in het midden (=breedte)
#   *
#   *
#  ***
#  ***
# *****
#  ***
#  ***
#   *
#   *
# """