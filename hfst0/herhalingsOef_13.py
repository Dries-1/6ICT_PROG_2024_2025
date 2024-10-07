""" Vraag een gebruiker naar 3 getallen.
    
    Bepaal het gemiddelde van het kleinste 
    en het grootste van de 3 getallen.
    
    >>> Geef eerste getal op: 7
    >>> Geef tweede getal op: 3
    >>> Geef derde  getal op: 23
    Het gemiddelde van 3 en 23 is 13.0
"""


getal1 = float(input("Geef eerste getal op: "))
getal2 = float(input("Geef tweede getal op: "))
getal3 = float(input("Geef derde getal op: "))

kleinste = min(getal1, getal2, getal3)
grootste = max(getal1, getal2, getal3)

gemiddelde = (kleinste + grootste) / 2

print(f"Het gemiddelde van {kleinste} en {grootste} is {gemiddelde:.1f}")
