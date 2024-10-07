# Niveau 1
# Maak een lege dictionary relaties aan.
"""
Geef vervolgens 2 inputs aan de gebruiker.
        • (Sleutel) Geef relatie tot persoon op.
        • (Waarde) Geef naam van persoon op.

Voeg een nieuw element toe aan de dictionary op basis van deze 2 inputs.
Print tenslotte de gewijzigde dictionary.

        Voorbeeld in de terminal.
        Geef relatie tot persoon op: Broer
        Geef naam van persoon op: Korneel
        {'Broer': 'Korneel'}
        input
input
print
"""
relaties = {

}
relatie = input("Geef relatie tot persoon op: ") #sleutel
naam = input("geef de naam van de persoon op: ") # waarde

relaties[relatie] = naam
print (relaties)

# Niveau 2
# Momenteel komt er slechts 1 element in de dictionary te staan. Dit is natuurlijk nutteloos.
# Pas de code aan. Zet de 2 inputs en het toevoegen van het nieuwe element in een while True.
# Het programma zal dus oneindig lang nieuwe relaties kunnen toevoegen. Het programma stopt hiermee wanneer je STOP antwoord op een van de 2 vragen.
# Hierna print het de volledige dictionary relaties.

while True:
    relatie = input("Geef relatie tot persoon op: ")
    if relatie == "STOP":  
        break
    naam = input("Geef naam van persoon op: ")
    relaties[relatie] = naam
print(relaties)


# Niveau 3
# Momenteel kan je 2 keer dezelfde relatie ingeven. Dit overschrijft de originele waarde van het element (probeer dit uit!). Pas dit aan, controleer of een relatie (sleutel) reeds in de dictionary staat.
# Als dit het geval is, print "Kan relatie niet toevoegen, deze bestaat reeds".


while True:
    relatie = input("Geef relatie tot persoon op: ")
    if relatie == "STOP":  
        break
    naam = input("Geef naam van persoon op: ")
    if relatie in relaties:
        print("Kan relatie niet toevoegen, deze bestaat reeds")
    else:
        relaties[relatie] = naam 
print(relaties) 

          
# Niveau 4 (extra)
# De oplossing uit niveau 3 is natuurlijk niet ideaal. Een persoon kan meerdere broers hebben. Denk zelf na over een manier om dit probleem op te lossen.
        

while True:
    # Input van de gebruiker voor relatie en naam
    relatie = input("Geef relatie tot persoon op: ")
    if relatie == "STOP":  # Stoppen wanneer de gebruiker 'STOP' invoert
        break
    naam = input("Geef naam van persoon op: ")

    # Controleer of de relatie al bestaat
    if relatie in relaties:
        # Voeg de nieuwe naam toe aan de bestaande lijst
        relaties[relatie].append(naam)
    else:
        # Maak een nieuwe lijst met de naam
        relaties[relatie] = [naam]
    
    # Vraag of er meerdere personen onder dezelfde relatie moeten worden toegevoegd
    while True:
        extra_persoon = input(f"Wil je nog iemand toevoegen als {relatie}? (ja/nee): ").lower()
        if extra_persoon == "nee":
            break
        elif extra_persoon == "ja":
            extra_naam = input(f"Geef de naam van een andere {relatie}: ")
            relaties[relatie].append(extra_naam)
        else:
            print("Ongeldig antwoord, kies ja of nee.")
    
# Print het volledige woordenboek na de invoer
print(relaties)
