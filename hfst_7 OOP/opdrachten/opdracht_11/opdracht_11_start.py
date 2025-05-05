import pygame
import random

# Enkele constantes voor het scherm.
GROOTTE_CELLEN = 20 # Cellen moeten vierkanten zijn, dus dit is zowel de hoogte als de GROOTTE.
AANTAL_CELLEN  = 20 # Zorg dat GROOTTE altijd deelbaar is door AANTAL_CELLEN.    
GROOTTE        = GROOTTE_CELLEN*AANTAL_CELLEN # De grootte van het scherm is het product van bovenstaanden.

# Enkele andere constanten
WIT   = (255, 255, 255)
GROEN = (0, 255, 0)
ROOD  = (255, 0, 0)
FPS   = 10

# Start pygame & wijzig titel van spel.
pygame.init()
pygame.display.set_caption('Opdracht 11')
frame = pygame.display.set_mode((GROOTTE, GROOTTE))
klok = pygame.time.Clock()
running = True

# Slang is een geneste lijst. Ieder element verwijst naar een x- & y-positie op het scherm.
# Deze positie is waar dat deel van het lichaam zich bevindt (meer specifiek de linkerbovenhoek)
# De bewegingen van de slang is opgesplitst in x & y. Hij beweegt bij de start altijd naar rechts.
slang = [(GROOTTE//2, GROOTTE//2), (GROOTTE//2-GROOTTE_CELLEN, GROOTTE//2), (GROOTTE//2-2*GROOTTE_CELLEN, GROOTTE//2)]
slang_richting = (AANTAL_CELLEN, 0)

# Zet het eerste voedsel op een willekeurige positie op het scherm klaar.
# randrange is zo opgesteld dat enkel veelvouden van AANTAL_CELLEN in aanmerking komen.
food = (random.randrange(0, GROOTTE, AANTAL_CELLEN), random.randrange(0, GROOTTE, AANTAL_CELLEN))

while running:

    " ACTIE 1: verwerk inputs van gebruiker. "
    pygame.event.pump() # Zorg ervoor dat pygame toetsen/muis mag ophalen.
    toetsen = pygame.key.get_pressed() # Haal toetsen op.

    # Verander richting van de slang, afhankelijk van ingedrukte toets.
    # De slang kan niet opeens de tegengestelde richting opgaan.
    if toetsen[pygame.K_LEFT] and slang_richting != (AANTAL_CELLEN, 0):        
        slang_richting = (-AANTAL_CELLEN, 0)
    elif toetsen[pygame.K_RIGHT] and slang_richting != (-AANTAL_CELLEN, 0):        
        slang_richting = (AANTAL_CELLEN, 0)
    elif toetsen[pygame.K_UP]  and slang_richting != (0, AANTAL_CELLEN):      
        slang_richting = (0, -AANTAL_CELLEN)
    elif toetsen[pygame.K_DOWN] and slang_richting != (0, -AANTAL_CELLEN):     
        slang_richting = (0, AANTAL_CELLEN)

    # Sluit spel af bij indrukken knop rechts-bovenaan.
    for event in pygame.event.get():  # Haal alle pygame events op.
        if event.type == pygame.QUIT: # Als het 'type' QUIT geregistreerd is.
            running = False           # Dan stel running gelijk aan False.

    " ACTIE 2: spel-staat wijzigen. "
    klok.tick(FPS) # Zorg voor constante framerate.


    # Beweeg hoofd van slang naar nieuwe positie, 
    # Voeg hoofd toe vooraan de lijst slang en verwijder de staart (effect: lijkt alsof slang bewogen is)
    hoofd = (slang[0][0] + slang_richting[0], slang[0][1] + slang_richting[1])
    slang = [hoofd] + slang[:-1]

    # Controleer of een van de randen geraakt is. Zo ja, spel gegaan
    if  (hoofd[0] < 0 or hoofd[0] >= GROOTTE or hoofd[1] < 0  or hoofd[1] >= GROOTTE):
        running = False
    # Controleer of de slang zichzelf raakt. Zo ja, spel gegaan
    if hoofd in slang[1:]:
        running = False

    # Controleer of hoofd van slang op eten staat. Zo ja, maak slang langer en spawn nieuw eten.
    if hoofd == food:
        slang.append(slang[-1])
        food = (random.randrange(0, GROOTTE, AANTAL_CELLEN), random.randrange(0, GROOTTE, AANTAL_CELLEN))

    " Actie 3: teken & toon frame. "
    frame.fill(WIT) # Maak frame leeg.
    for segment in slang: pygame.draw.rect(frame, GROEN, pygame.Rect(segment[0], segment[1], AANTAL_CELLEN, AANTAL_CELLEN)) # Teken ieder onderdeel van de slang.
    pygame.draw.rect(frame, ROOD, pygame.Rect(food[0], food[1], AANTAL_CELLEN, AANTAL_CELLEN)) # Teken het eten.
    pygame.display.flip() # Toon display.