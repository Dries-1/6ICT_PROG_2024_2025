fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}

# Niveau 1
# Een waarde oproepen gebeurt via de sleutel. Tot nu toe hebben we deze sleutel altijd meteen opgeschreven. Het is echter ook mogelijk om de sleutel eerst in een variabele te plaatsen.

# Onderstaande code toont hoe dit gebeurt.
# Print de dictionary-waarde gekoppeld aan onderstaande variabele
"""
fruit = "banaan"
print( fruitmand[fruit] )
"""

# Niveau 2
# Gebruik onderstaande variabelen om een nieuw element toe te voegen aan de dictionary.
"""
nieuw_fruit  = "mango"
nieuw_aantal = 1

fruitmand["mango"] = 1 
print(fruitmand)
"""

# Niveau 4
# Gebruik onderstaande variabelen om de waarde van een element in de dictionary te verlagen.
"""
fruit = "kers"
nieuw_aantal = 43

fruitmand["kers"] = 43
print(fruitmand)
"""

# Niveau 5
# Gebruik onderstaande variabele om een element te verwijderen uit de dictionary.

terugleggen_fruit = "kers"
fruitmand.pop('kers')
print(fruitmand)

