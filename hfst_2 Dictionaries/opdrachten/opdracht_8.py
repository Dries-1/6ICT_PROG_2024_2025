# Los de problemen uit de opdracht op met behulp van onderstaande code.

# Niveau 1
dict_1={1: 10, 2: 20}
dict_2={3: 30, 4: 40}
dict_3={5: 50, 6: 60}
# Resultaat: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

resultaat = {**dict_1, **dict_2, **dict_3}
print(resultaat)

# Niveau 2
dict = {'a': 'Red', 'b': 'Green', 'c': None}
# Resultaat: {'a': 'Red', 'b': 'Green'}


# Niveau 3
dict = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50, "g": 60} 
te_verwijderen = ["d", "g", "b"]
# Resultaat: {'a': 10, 'c': 30, 'e': 50}

# Niveau 4
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}
# Resultaat: {'a': 400, 'b': 400, 'd': 400, 'c': 300})

