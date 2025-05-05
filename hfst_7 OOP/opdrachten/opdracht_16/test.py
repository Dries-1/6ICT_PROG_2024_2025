" Bestand voor het testen van de klassen ontwikkelt in dojo.py. "

from dojo import Lid, Student, Instructeur, Workshop

" Testen van klasse Lid "
# lid_1 = Lid("Jan Paumen")
# lid_2 = Lid("Piet verstraten")

# print(lid_1.voorstellen()) # Hey, mijn naam is Jan.
# print(lid_2.voorstellen()) # Hey, mijn naam is Piet.



" Testen van klasse Student "
# student_1 = Student("Jan Paumen", "Lijkt me leuk.")
# student_2 = Student("Piet verstraten", "Veel verdienen later.")

# print(student_1.interesses)             # []
# student_1.interesse_toevoegen("C#")     # 
# student_1.interesse_toevoegen("C#")     # C# is reeds een interesse van Jan.
# student_1.interesse_toevoegen("HTML")   #
# print(student_1.interesses)             # ['C#', 'HTML']
# student_1.interesse_verwijderen("Java") # Java is geen een interesse van Jan.
# student_1.interesse_verwijderen("HTML") #
# print(student_1.interesses)             # ['C#']

# student_2.beschrijving()                # Veel verdienen later.



" Testen van klasse Instructeur "
# instruct_1 = Instructeur("Joris Doemen", "Ik wil mensen leren programmeren.")
# instruct_2 = Instructeur("Korneel Vern", "Ik programmeer reeds 20 jaar en zou graag mijn ervaring delen.")

# print(instruct_1.skills)                 # []
# instruct_1.skill_toevoegen("HTML")       #
# instruct_1.skill_toevoegen("HTML")       # HTML is reeds een skill van Joris.
# instruct_1.skill_toevoegen("CSS")        #
# instruct_1.skill_toevoegen("Javascript") #
# print(instruct_1.skills)                 # ['HTML', 'CSS', 'Javascript']

# instruct_2.beschrijving()                # Ik programmeer reeds 20 jaar en zou graag mijn ervaring delen.



" Testen van klasse Workshop "
# workshop = Workshop("12/03/2024", "HTML")

# student_1 = Student("Jan Paumen", "Lijkt me leuk.")
# student_1.interesse_toevoegen("HTML")
# student_1.interesse_toevoegen("Python")
# student_2 = Student("Piet verstraten", "Veel verdienen later.")
# student_2.interesse_toevoegen("HTML")

# instruct_1 = Instructeur("Joris Doemen", "Ik wil mensen leren programmeren.")
# instruct_1.skill_toevoegen("HTML")
# instruct_1.skill_toevoegen("Python")
# instruct_2 = Instructeur("Korneel Vern", "Ik programmeer reeds 20 jaar en zou graag mijn ervaring delen.")
# instruct_2.skill_toevoegen("Python")


# workshop.deelnemer_toevoegen(student_1)  #
# workshop.deelnemer_toevoegen(student_2)  #
# workshop.deelnemer_toevoegen(instruct_1) #
# workshop.deelnemer_toevoegen(instruct_2) # Korneel heeft geen skill om deze workshop te geven.

# workshop.info()
# """
# Workshop - 12/03/2024 - HTML

# Totaal aantal deelnemers: 3

# Studenten:
# 1. Jan Paumen - HTML,Python
# 2. Piet verstraten - HTML

# Instructeurs:
# 1. Joris Doemen - HTML,Python
# """

# print("######################")


# student_1.interesse_verwijderen("HTML") 
# workshop.update()
# workshop.info() # MERK OP! Jan is geen student meer na update.
#                 # Dit omdat hij geen interesse meer heeft in HTML.
# """
# Workshop - 12/03/2024 - HTML

# Totaal aantal deelnemers: 2

# Studenten:  
# 1. Piet verstraten - HTML 

# Instructeurs:
# 1. Joris Doemen - HTML,Python
# """
