from opdracht_12 import Account, Bank

# # TESTEN NIVEAU 1 (  / 5)
account_1 = Account("Jan", 10, "basis")
account_2 = Account("Piet", 1000, "premium")
print("###############")
account_1.overzicht()               # Jan (basis): 10 euro.
account_2.overzicht()               # Piet (premium): 1000 euro.
print("###############")
account_1.storten(1000)             # Nieuwe balans: 1010 euro.
account_2.storten("TIENDUIZEND")    # Ongeldig bedrag ontvangen.
print("###############")
account_1.afhalen(50)               # Nieuwe balans: 960 euro.
account_2.afhalen(1000000)          # Ontoereikende balans.
print("###############")
account_1.overzicht()               # Jan (basis): 960 euro.
account_2.overzicht()               # Piet (premium): 1000 euro.


# # TESTEN NIVEAU 2 (  / 5)
# bank_1    = Bank("KBC", 5)
# bank_2    = Bank("ING", 3)
# print("###############")
# bank_1.toevoegen( Account("Jan", 10, "basis") )      # Account Jan toegevoegd.
# bank_1.toevoegen( Account("Piet", 1000, "premium") ) # Account Piet toegevoegd.
# bank_1.toevoegen( Account("Joris", 10000, "basis") ) # Account Joris toegevoegd.
# bank_2.toevoegen( Account("Korneel", 0, "premium") ) # Account Korneel toegevoegd.
# bank_2.toevoegen("ACCOUNT")                          # Geen geldig account opgegeven.
# print("###############")
# bank_1.overzicht()          # Bank KBC heeft volgende accounts:
#                             # Jan (basis): 10 euro.
#                             # Piet (premium): 1000 euro.
#                             # Joris (basis): 10000 euro.
# bank_2.overzicht()          # Bank ING heeft volgende accounts:
#                             # Korneel (premium): 0 euro.
# print("###############")
# bank_1.bonus_uitkeren()
# bank_2.bonus_uitkeren()
# print("###############")
# bank_1.overzicht()          # Bank KBC heeft volgende accounts:
#                             # Jan (basis): 15 euro.
#                             # Piet (premium): 1010 euro.
#                             # Joris (basis): 10005 euro.
# bank_2.overzicht()          # Bank ING heeft volgende accounts:
#                             # Korneel (premium): 6 euro.