# TODO: kijk voor te beginnen na dat de paden naar
#       de afbeeldingen op regel 12, 18 & 23 correct zijn!!!

import pygame

# Start pygame & wijzig titel van spel.
pygame.init()
pygame.display.set_caption('Opdracht 6')
running = True

# Maak frame aan met bepaalde grootte (gelijk aan grootte van achtergrond).
achtergrond = pygame.image.load(r"veld.png") 
achter_breedte, achter_hoogte = achtergrond.get_width(), achtergrond.get_height()
frame = pygame.display.set_mode((achter_breedte, achter_hoogte))

# Zet speler klaar
x_speler, y_speler, snelheid_speler = achter_breedte//2, achter_hoogte//2, 5
afb_speler = pygame.image.load(r"speler.png")

# Zet een lege lijst klaar waarin obstakels bewaard worden.
# De obstakels worden bewaard als pygame Rects (zie regel 48) om collisie met speler te detecteren.
obstakels = []
afb_obstakel = pygame.image.load(r"obstakel.png")

# Maak een pygame klok om de FPS van het spel te bepalen.
klok = pygame.time.Clock()
FPS = 60

while running:
    
    " ACTIE 1: verwerk inputs van gebruiker. "
    pygame.event.pump() # Zorg ervoor dat pygame toetsen/muis mag ophalen.
    toetsen = pygame.key.get_pressed() # Haal toetsen op.

    # Zet mogelijke beweging klaar op basis van ingedrukte toetsen.
    # Eerste element is beweging op x-as, tweede element is beweging op y-as.
    mag_bewegen, beweging = True, (0,0)
    if toetsen[pygame.K_LEFT]:        
        beweging = (-snelheid_speler, 0)
    elif toetsen[pygame.K_RIGHT]:        
        beweging = (snelheid_speler, 0)
    elif toetsen[pygame.K_UP]:      
        beweging = (0, -snelheid_speler)
    elif toetsen[pygame.K_DOWN]:     
        beweging = (0, snelheid_speler)

    # Als linkermuis is ingeduwd, zet hier een obstakel (door de x- en y-positie toe te voegen in een geneste lijst).
    if pygame.mouse.get_pressed()[0]:
        positie_muis = pygame.mouse.get_pos() # Haal huidige positie muis op.
        x_positie_obstakel, y_positie_obstakel = positie_muis[0]-afb_obstakel.get_width()//2, positie_muis[1]-afb_obstakel.get_height()//2 # Zet obstakel gecentreerd op positie van muis.
        obstakel = {"x":x_positie_obstakel,"y":y_positie_obstakel}  # Maak obstakel aan als dictionary met sleutels "x" en "y".
        obstakels.append(obstakel) # Voeg obstakel toe aan lijst.

    # Sluit spel af bij indrukken knop rechts-bovenaan.
    for event in pygame.event.get():  # Haal alle pygame events op.
        if event.type == pygame.QUIT: # Als het 'type' QUIT geregistreerd is.
            running = False           # Dan stel running gelijk aan False.

    " ACTIE 2: spel-staat wijzigen. "
    klok.tick(FPS) # Zorg voor constante framerate.

    ## We gaan op verschillende manieren controleren of speler wel mag bewegen met de in ACTIE 1 bepaalde beweging.
    nieuwe_x_speler = x_speler + beweging[0]
    nieuwe_y_speler = y_speler + beweging[1]

    # Als nieuwe positie de speler buiten de rand van het frame zet, mag beweging niet plaatsvinden.
    if (nieuwe_x_speler < 0) or (nieuwe_x_speler+afb_speler.get_width() > achter_breedte):
        mag_bewegen = False
    if (nieuwe_y_speler < 0) or (nieuwe_y_speler+afb_speler.get_height() > achter_hoogte):
        mag_bewegen = False

    # Als nieuwe positie de speler in een obstakel zou zetten, mag beweging niet plaatsvinden.
    rect_speler = pygame.Rect(nieuwe_x_speler,nieuwe_y_speler,afb_speler.get_width(),afb_speler.get_height())
    for obstakel in obstakels:
        rect_obstakel = pygame.Rect(obstakel["x"], obstakel["y"], afb_obstakel.get_width(), afb_obstakel.get_height()) # Maak obstakel aan.
        if rect_speler.colliderect(rect_obstakel):
            mag_bewegen = False

    if mag_bewegen == True: # Als speler na checks nog mag bewegen, verplaats hem dan naar de nieuwe positie.
        x_speler = nieuwe_x_speler
        y_speler = nieuwe_y_speler

    " Actie 3: teken & toon frame. "
    frame.blit(achtergrond, (0,0)) # Maak frame leeg door het wit te maken.

    frame.blit(afb_speler, (x_speler,y_speler)) # Teken speler.
    for obstakel in obstakels: frame.blit(afb_obstakel, (obstakel["x"],obstakel["y"])) # Teken obstakels.

    pygame.display.flip() # Toon frame

pygame.quit()