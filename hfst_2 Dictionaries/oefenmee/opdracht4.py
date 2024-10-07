# Dictionaries worden vaak gebruikt om informatie bij te houden.
# Bekijk onderstaande dictionary. Het bevat info die de ICT-dienst bijhoudt van een fictieve leerling.
laptop_korneel = {
    "serial": "R44508ZH1",
    "model": {"id": 8, "name": "L390", "touch": True},
    "assigned_to": {"username": "VAKO190900", "name": "Korneel Valo"},
    "category": {"id": 4, "status": "laptopMETtouch"},
    "manufacturer": {"id": 2, "name": "LENOVO"},
    "supplier": "???",
    "supplier_2": "bol.com"
}

# Niveau 1 
"""
Maak volgende wijzigingen aan de huidige dictionary.
        • Voeg een nieuw element toe. De sleutel is "status", de waarde is "deployed".
        • Wijzig een element. De sleutel "supplier" moet als waarde "signpost" hebben.
        • Verwijder een element. Het element met als sleutel "supplier_2".
"""

laptop_korneel["status"] = "deployed"
laptop_korneel["supplier"] = "signpost"
del laptop_korneel["supplier_2"]


print("Gewijzigde dictionary:")
print(laptop_korneel)



# Niveau 2
"""
Bekijk de sleutels "model", "assigned_to", "category" & "manufacturer". Wat valt je op?
Print de waarde van sleutel "assigned_to". Print vervolgens de waarde van sleutel "username".
        Tip! Je plaatst [] om in de eerste dictionary te springen. Dus hoe spring je erna in de tweede?
We zullen hier meer op ingaan in het deel "Geneste dictionaries".
"""

assigned_to_value = laptop_korneel["assigned_to"]
print("\nWaarde van assigned_to:", assigned_to_value)

username_value = laptop_korneel["assigned_to"]["username"]
print("Waarde van username:", username_value)