# Maak een klasse Student & Cursus zoals aangegeven in opdracht 9.
import random


" Via onderstaande code kan je niveau 1 testen. "
# # 1. Maak objecten aan voor studenten en cursussen.
# #    Student heeft als input: naam & studentnummer.
# #    Cursus heeft als input : naam & cursusnummer.
# studenten = []
# for naam in ["Jan", "Piet", "Joris", "Korneel"]:
#     studenten.append(Student(naam, f"S{random.randrange(1,100000)}"))
# cursussen = []
# for naam in ["Wisk", "Prog", "Netw", "Frans"]:
#     cursussen.append(Cursus(naam, f"C{random.randrange(1,100000)}"))

# # 3. Print info van iedere leerling & cursus. (2. volgt in niveau 2)
# for student in studenten: student.info()
# for cursus in cursussen: cursus.info()



" Via onderstaande code kan je niveau 2 testen. (zet testcode niveau 1 terug in commentaar) "
# # 1. Maak objecten aan voor studenten en cursussen.
# #    Student heeft als input: naam & studentnummer.
# #    Cursus heeft als input : naam & cursusnummer.
# studenten = []
# for naam in ["Jan", "Piet", "Joris", "Korneel"]:
#     studenten.append(Student(naam, f"S{random.randrange(1,100000)}"))
# cursussen = []
# for naam in ["Wisk", "Prog", "Netw", "Frans"]:
#     cursussen.append(Cursus(naam, f"C{random.randrange(1,100000)}"))

# # 2. Probeer een persoon 2x voor dezelfde cursus in te schrijven.
# #    Bij de 2de poging, mag de cursus niet toegevoegd worden.
# studenten[0].inschrijven(cursussen[0])
# studenten[0].inschrijven(cursussen[0])
# # 2. Voeg at-random 8 cursussen toe aan de personen.
# for _ in range(8):
#     student = random.choice(studenten)
#     cursus  = random.choice(cursussen)
#     student.inschrijven(cursus)

# # 3. Print info van iedere leerling.
# for student in studenten: student.info()