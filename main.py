import pygame

# Inicializace pygame
pygame.init()

# Vyvoření obrazovky
width = 600
height = 300
Screen = pygame.display.set_mode((width, height))

# Hlavní herní cyklus
lets_continue = True

while lets_continue:
    for event in pygame.event.get():
        print(event)
        lets_continue = False

# Ukončení pygame
pygame.quit()