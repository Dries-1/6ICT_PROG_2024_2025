def letter_checker(woord, letter):
    "return of het woord de letter bevat"
    return letter in woord

print(letter_checker("hallo", "e"))  # False
print(letter_checker("dag", "a"))    # True
