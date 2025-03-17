# Maak een klasse Button om het programmeren van een knop op de RPi te vereenvoudigen.
# In niveau 2 combineer je de klasse Button met de klasse Led uit oefen mee 8.


" Via onderstaande code kan je de klasse van niveau 1 testen. "

# # Maak een knop aan op pin 5
# knop_5 = Button(5)

# while True:
#    # Controleer of een wijziging is gebeurt TOV de vorige loop.
#    # Indien ja, print huidige stand van knop.
#    knop_5.detect_wijziging()



" Via onderstaande code kan je de klassen van niveau 2 testen. "

# # Maak een knop op pin 5
# Knop_5 = Button(5)
# # Maak een led op pin 8 en 10
# led_8 = Led(8)
# led_10 = Led(10)

# while True:
#   # Controleer wat de toestand van de knop is:
#   #   True indien knop net is ingeduwd, False indien net losgelaten.
#   #   Indien de toestand niet gewijzigd is, return None.
#   toestand = knop_5.detect_wijziging()

#   # Als de knop net is ingedrukt, schakel led 8 aan en 10 uit.
#   if toestand == True:
#     led_8.aan()
#     led_10.uit()
#   # Anders als de knop net is losgelaten, schakel led 10 aan en 8 uit.
#   elif toestand == False:
#     led_8.uit()
#     led_10.aan()
#   # Anders als de toestand van de knop niet gewijzigd is, doe niets.
#   else:
#     pass
