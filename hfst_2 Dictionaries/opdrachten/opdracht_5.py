# Start de opdracht met onderstaande code (je moet pygame installeren)
# import pygame

# Start pygame
pygame.init()

# Zet scherm klaar
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Achtergrond kleur menu")

# Zet kleuren --> RGB instelling klaar
kleuren = {
    "rood": (255,0,0),
    "groen": (0,255,0),
    "blauw": (0,0,255)
}

# Main loop
running = True
while running:
    # Stop pygame door op kruisje te duwen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #### START HIER: gebruik input() om kleur_rgb te bepalen ####

    #############################################################

    # Verander achtergrond en toon aan gebruiker
    screen.fill(kleur_rgb)
    pygame.display.flip()