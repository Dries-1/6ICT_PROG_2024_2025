database = {
    "Jan": "FkeHsne569*",
    "Piet": "KsnOmd727^",
    "Joris": "DneSje439&",
    "Korneel": "MdsSnz863*"
}

while True:
    naam = input("Wie wilt inloggen: ")

    if naam not in database:
        print(f"{naam} bestaat niet in de database.")
    else:
        wachtwoord = input(f"Geef wachtwoord op van {naam}: ")
        if database[naam] == wachtwoord:
            print(f"Welkom {naam}!")
            break 
        else:
            print("Wachtwoord incorrect.")