# Vul de TODO's aan op basis van de uitleg in de README.

import pygame
from particle import BoringParticle

# Constantes.
BREEDTE, HOOGTE = 600,600
FPS = 120
AANTAL_PARTICLES = 20

# Start pygame.
pygame.init()
pygame.display.set_caption("Fire Storm Simulation")
scherm = pygame.display.set_mode((BREEDTE,HOOGTE))
klok = pygame.time.Clock()

# TODO 1: Vul lijst *particles* aan met objecten van de klasse *BoringParticle*.
#         Het aantal aangemaakte objecten is gelijk aan de variabele *aantal_particles*.
particles = []  
""" Vul lijst aan... """
    
running = True
while running:
    # Maak scherm schoon.
    scherm.fill((0,0,0))

    # Zorg voor constante FPS. interval is de tijd tussen iedere frame (in ms)
    interval = klok.tick(FPS)
    
    # Controleer of quit-knop is ingeduwd.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO 2: Overloop iedere particle in lijst met particles:
    #   1. Beweeg positie van ieder particle
    #   2. Reset particle wanneer ze uit het scherm zijn.
    #   3. Teken particle op scherm (deels gemaakt).
    for particle in particles:
        """ 1. Beweeg particle """
        """ 2. Reset particle """
        pygame.draw.circle(scherm, (255,255,255), ("3. Vul aan met x-/y-positie van particle"), 10)

    # Toon scherm aan gebruiker.
    pygame.display.update()

pygame.quit()