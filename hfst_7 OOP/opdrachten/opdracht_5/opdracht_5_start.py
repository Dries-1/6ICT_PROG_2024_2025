# TODO: kijk voor te beginnen na dat de paden naar
#       de afbeeldingen op regel 18 & 20 correct zijn!!!

import pygame

# Start pygame & wijzig titel van spel.
pygame.init()
pygame.display.set_caption('Opdracht 5')
running = True

# Maak frame aan met bepaalde grootte.
frame_breedte, frame_hoogte = 800, 400
frame = pygame.display.set_mode((frame_breedte, frame_hoogte))

# Zet alle benodigde afbeeldingen & hun startposities klaar.
# x_kogels & y_kogels zijn lijsten omdat ze de posities van alle geschoten kogels zullen bevatten.
x_vlieg, y_vlieg, snelheid_vlieg = 0, frame_hoogte//2, 5
afb_vlieg = pygame.image.load(r"vliegtuig.png")
x_kogels, y_kogels, snelheid_kogel = [], [], 8
afb_kogel = pygame.image.load(r"kogel.png")

# Maak een pygame klok om de FPS van het spel te bepalen.
klok = pygame.time.Clock()
FPS = 60

while running:
    " ACTIE 1: verwerk inputs van gebruiker. "
    pygame.event.pump() # Zorg ervoor dat pygame toetsen mag ophalen.
    toetsen = pygame.key.get_pressed() # Haal toetsen op.

    # Beweeg vliegtuig op basis van toetsen.
    if toetsen[pygame.K_LEFT]   and   x_vlieg > 0:        
        x_vlieg = x_vlieg - snelheid_vlieg
    if toetsen[pygame.K_RIGHT]  and   x_vlieg+afb_vlieg.get_width() < frame_breedte:        
        x_vlieg = x_vlieg + snelheid_vlieg
    if toetsen[pygame.K_UP]     and   y_vlieg > 0:      
        y_vlieg = y_vlieg - snelheid_vlieg
    if toetsen[pygame.K_DOWN]   and   y_vlieg+afb_vlieg.get_height() < frame_hoogte:     
        y_vlieg = y_vlieg + snelheid_vlieg

    # Zet nieuwe kogel langs vliegtuig door toe te voegen aan lijsten x_kogels & y_kogels.
    if toetsen[pygame.K_SPACE]:
        x_kogels.append(x_vlieg + afb_vlieg.get_width()) 
        y_kogels.append(y_vlieg + afb_vlieg.get_height()//2) 

    # Sluit spel af bij indrukken knop rechts-bovenaan.
    for event in pygame.event.get():  # Haal alle pygame events op.
        if event.type == pygame.QUIT: # Als het 'type' QUIT geregistreerd is.
            running = False           # Dan stel running gelijk aan False.

    " ACTIE 2: spel-staat wijzigen. "
    klok.tick(FPS) # Zorg voor constante framerate.
    for index, x_kogel in enumerate(x_kogels): x_kogels[index] = x_kogel + snelheid_kogel # Beweeg de kogels.

    " Actie 3: teken & toon frame. "
    frame.fill((0,0,0), (0,0,frame_breedte,frame_hoogte)) # Maak frame leeg door het zwart te maken.
    frame.blit(afb_vlieg, (x_vlieg,y_vlieg)) # Teken vliegtuig.
    for index, x_kogel in enumerate(x_kogels): frame.blit(afb_kogel, (x_kogels[index],y_kogels[index])) # Teken kogels.
    pygame.display.flip() # Toon frame.

pygame.quit()