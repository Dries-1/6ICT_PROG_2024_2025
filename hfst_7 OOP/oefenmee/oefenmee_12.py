" Ouder Dier heeft 2 methoden & eigenschappen.  "
class Dier():
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def heeft_naam(self):
        print(self.naam)


" Niveau 1 (zet terug in commentaar als je met niveau 2 start)"
# hond = Hond("Fido", 3)
# dier = Dier("George", 10)

# hond.info() # De hond Fido is 3 jaar oud.
# dier.info() # AttributeError: no attribute 'info'.

" Niveau 2 (zet terug in commentaar als je met niveau 3 start)"
# hond = Hond("Fido", 3)

# hond.set_massa(7) # 
# hond.weeg()       # De hond Fido weegt 7 kg.

" Niveau 3 "
# hond = Hond("Fido", 3, 40)
# hond.info() # De hond Fido is 3 jaar oud en 40 cm hoog.

# dier = Dier("George", 10, 100) # TypeError: heb geen hoogte.