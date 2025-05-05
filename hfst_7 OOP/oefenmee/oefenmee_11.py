" Ouder Dier heeft 2 methoden & eigenschappen.  "
class Dier():
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def heeft_naam(self):
        # Niveau 3: print(self.naam)
        print(f"Dit dier heeft de naam {self.naam}.") # Niveau 3

" Kind Kat neemt deze methoden & eigenschappen over. "
class Kat(Dier):
    pass