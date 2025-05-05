## Opdracht 15
Vervolledig de klassen `Rechthoek` en `Vierkant` in het bestand `vormen.py`. De klasse `Rechthoek` is hierbij een ouder van `Vierkant`. In het bestand **test.py** zijn testen te vinden om de correcte werking van iedere klasse na te gaan. Indien je opdracht 13 gemaakt hebt, kan je onderdelen van de code hieruit copy-pasten voor deze opdracht.

### Rechthoek klasse
Bij het aanmaken van een object van `Rechthoek`, moet deze als eigenschappen `breedte` en `hoogte` hebben. De klasse bevat de volgende methoden.
* `set_breedte`: wijzig de `breedte` naar de meegegeven waarde.
* `set_hoogte`: wijzig de `hoogte` naar de meegegeven waarde.
* `get_oppervlakte`: return (niet print!) de oppervlakte van de rechthoek.
* `get_omtrek`: return (niet print!) de omtrek van de rechthoek.
* `afbeelding`: print (niet return!) een string met de vorm van de rechthoek gebruik makend van asterisken (*). Het aantal regels van de string is gelijk aan de `hoogte` van de rechthoek. De hoeveelheid asterisken op iedere regel is gelijk aan de `breedte` van de rechthoek (zie ook voorbeeld beneden).
* `get_hoeveel_binnen`: geef een tweede rechthoek mee aan deze methode. De methode returnt (niet print!) hoeveel keer de tweede rechthoek past in de eerste (zonder te roteren). Als voorbeeld, een rechthoek van breedte 4 en hoogte 3 past twee maal in een rechthoek van breedte 8 en hoogte 4 (zie ook voorbeeld beneden). 

### Voorbeeld Rechthoek
```py
recht = Rechthoek(10, 5)

# Oppervlakte berekenen & hoogte wijzigen.
print(recht.get_oppervlakte())                      # 50  
recht.set_hoogte(3)                                 #
print(recht.get_oppervlakte())                      # 30  


# Hoe ziet deze rechthoek er uit?
print(f"Rechthoek: {recht.breedte}x{recht.hoogte}") # Rechthoek: 10x3
print(recht.afbeelding())
""" --> 3 regels (=hoogte), met iedere regel 10 asterisken (=breedte)
**********
**********
**********
"""

# Hoevaak past een rechthoek van 4x3 in bovenstaande rechthoek?
andere_recht = Rechthoek(4,3) 
print(recht.get_hoeveel_binnen(andere_recht))       # 2
```

### Vierkant klasse
De klasse `Vierkant` is een kind van `Rechthoek`. Bij het aanmaken van een object van `Vierkant` mag de gebruiker `breedte` & `hoogte` niet meer apart ingeven. In plaats hiervan krijgen deze eigenschappen hun waarde van een gezamenlijke parameter (bijvoorbeeld zijde). 

Maak ook een extra methode `set_zijde`. De `breedte` & `hoogte` van het vierkant moeten gelijk gesteld worden aan de meegegeven waarde. Bijkomend moet het gebruiken van `set_breedte`/`set_hoogte` zowel de `breedte` als `hoogte` veranderen naar de meegegeven waarde.

### Voorbeeld Vierkant
```py
vierk = Vierkant(9)

# Oppervlakte berekenen & zijde wijzigen.
print(vierk.get_oppervlakte()) # 81
vierk.set_zijde(5)             #
print(vierk.get_oppervlakte()) # 25
vierk.set_breedte(4)           #
print(vierk.get_oppervlakte()) # 16

# Hoe ziet het vierkant er uit?
print(f"Vierkant: {vierk.breedte}x{vierk.hoogte}") # Vierkant: 4x4
vierk.afbeelding()
""" --> 4 regels (=hoogte), met iedere regel 4 asterisken (=breedte)
****
****
****
****
"""

# Hoevaak past een rechthoek van 4x3 in bovenstaand vierkant
andere_recht = Rechthoek(4,3) 
print(vierk.get_hoeveel_binnen(andere_recht))       # 1
```

### Extra: Ruit klasse
Maak een nieuwe klasse `Ruit`. Deze klasse is een kind van `Rechthoek`. Bij het aanmaken van een object, worden nog steeds `breedte` en `hoogte` als eigenschappen aangemaakt. De breedte slaat op de afstand tussen de twee zij-punten. De hoogte op de afstand tussen het bovenste en onderste punt (zie **afbeelding**).

<p align="center">
  <img src="diamond.png" width="200" height="300"/>
</p>

De methode `get_hoeveel_binnen` vervalt. Het oproepen van deze methode met een object van `Ruit` print: "Deze methode is niet beschikbaar voor ruiten." .

De methoden `get_oppervlakte`, `get_omtrek` en `afbeelding` blijven bestaan in `Ruit`. Deze moeten echter wel gewijzigd worden om te werken met de vorm van een ruit. De methode `afbeelding` zal niet voor iedere vorm een perfecte ruit kunnen printen. Het is voldoende als deze op het hoogste en laagste punt een asterisk is, en in het midden een aantal asterisken gelijk aan de breedte. 



#### Voorbeeld Ruit
```py
ruit = Ruit(5,9)

# Oppervlakte berekenen & get_hoeveel_binnen proberen.
ruit.get_oppervlakte()    # 22.5
ruit.get_hoeveel_binnen() # Deze methode is niet beschikbaar voor ruiten.

# Hoe ziet de ruit er uit?
ruit.afbeelding()
""" --> 9 regels (=hoogte), met 5 asterisken in het midden (=breedte)
  *
  *
 ***
 ***
*****
 ***
 ***
  *
  *
"""
```