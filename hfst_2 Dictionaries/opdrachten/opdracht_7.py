# Maak het programma beschreven in de opdracht.


artikelen = {
    "brood": 2.50,
    "melk": 1.30,
    "kaas": 4.20,
    "appels": 3.00,
    "eieren": 2.00,
    "boter" : 7.00,
    "pudding" : 5.97,
}

totaalprijs = 0
aantal_artikelen = 0

while True:
    keuze = input("Welk artikel wilt u kopen? (Typ 'STOP' om af te rekenen): ").lower()

  
    if keuze == "stop":
        break

   
    if keuze in artikelen:
        prijs = artikelen[keuze]
        print(f"{keuze} toegevoegd.")
        totaalprijs += prijs
        aantal_artikelen += 1
    else:
        print(f"{keuze} bestaat niet.")


print(f"\nU heeft {aantal_artikelen} artikelen gekocht.")
print(f"De totaalprijs is: €{totaalprijs:.2f}")
