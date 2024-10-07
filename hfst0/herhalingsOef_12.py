""" Vraag een gebruiker naar de temperatuur in °F.
    Print de temp in °C (op 2 cijfers na de komma). 
    
    Celsius = (5/9)*(Fahrenheit-32)

    >>> Geef een temperatuur op in °F: 100
    100°F komt overeen met 37.78°C
"""

temp_F = int(input('geef de temperatuur in °F: '))

temp_C = (5/9)*(temp_F-32)

temp_C = round(temp_C, 2)

print(f'{temp_F}°F komt overeen met {temp_C}°C')
