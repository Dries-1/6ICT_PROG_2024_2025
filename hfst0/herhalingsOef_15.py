""" Vraag een gebruiker zijn/haar naam.
    
    Print alle klinkers die in de naam voorkomen.
        Tip! gebruik de methode .lower()

    >>> Geef een naam op: Korneel
    In Korneel zit een e
    In Korneel zit een o

    EXTRA: print ook hoevaak iedere klinker voorkomt.
"""

naam = input("Geef een naam op: ")

klinkers = "aeiou"

klinker_frequentie = {}

for letter in naam.lower():
    if letter in klinkers:
        if letter in klinker_frequentie:
            klinker_frequentie[letter] += 1
        else:
            klinker_frequentie[letter] = 1


for klinker, aantal in klinker_frequentie.items():
    print(f"In {naam} zit {aantal} keer een {klinker}")
