def mag_stemmen(leeftijd, inwoner):
    """ return of de persoon mag stemmen 
    
        Een persoon mag stemmen als deze:
            - 18 of ouder is.
            - EN een inwoner is van het land.
    """
    if leeftijd >= 18 and inwoner: 
        return "mag stemmen"
    else: 
        return "mag niet stemmen"

print( mag_stemmen(17, False) ) # mag niet stemmen
print( mag_stemmen(29, False) ) # mag niet stemmen
print( mag_stemmen(8,  True)  ) # mag niet stemmen
print( mag_stemmen(65, True)  ) # mag stemmen