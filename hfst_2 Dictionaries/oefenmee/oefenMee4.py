lijst = {
    "TED" : 5, 
    "TED2" : 5, 
    "TED3" : 5, 
}
# Niveau 1
# Gebruik input() om de gebruiker naar een sleutel in jouw dictionary te vragen.
# Print vervolgens de waarde die overeenkomt met deze sleutel.
"""
aanvraag_gebr = input('geef een film: ')

waarde = lijst[aanvraag_gebr]

print(waarde)
"""

#Niveau 2 
# Een gebruiker kan opgeven wat deze wilt. Volgende situatie kan momenteel dus ook optreden.
# 	Welk soort fruit zoek je: friet	input
# foutmelding
# 	KeyError: 'friet'
	
# We willen dit niet. Er moet dus eerst gecontroleerd worden of de input van de gebruiker effectief in de dictionary zit. Voeg volgende functionaliteit toe aan de code.
# 	• Sleutel bestaat: voer code uit Niveau 1 uit.
# 	• Sleutel bestaat niet: print 'Kon *input* niet vinden in de fruitmand.'

# 	Tip! Gebruik if ... In ... om te controleren of de input van de gebruiker in de dictionary bestaat.

aanvraag_gebr = input('geef een film: ')

waarde = lijst[aanvraag_gebr]

if aanvraag_gebr not in lijst:
    print(f'{aanvraag_gebr} staat niet in de lijst ')

else: 
    print(waarde)
