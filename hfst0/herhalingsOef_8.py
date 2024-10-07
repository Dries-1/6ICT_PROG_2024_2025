def seconden_in_leven(leeftijd, geslacht):
    """ return de seconden die een persoon nog leeft
        Tip! een jaar is gemiddeld 365.25 dagen
             gebruik ook de formule uit oefening 7 
    
        Maak hiervoor gebruik van:
        - de huidige leeftijd van de persoon.
        - Het geslacht van de persoon.
    
        Een man wordt gemiddeld 80 jaar,
        een vrouw wordt gemiddeld 84 jaar.
    """
    
    if geslacht == "man":
        levensverwachting = 80
    elif geslacht == "vrouw":
        levensverwachting = 84
    else:
        return "Onbekend geslacht"
    
    resterende_jaren = levensverwachting - leeftijd
    
    seconden_per_jaar = 365.25 * 24 * 60 * 60

    resterende_seconden = resterende_jaren * seconden_per_jaar
    
    return int(resterende_seconden)

print(seconden_in_leven(0, "vrouw"))   # 2524608000
print(seconden_in_leven(74, "man"))    # 189345600
print(seconden_in_leven(56, "vrouw"))  # 757382400
