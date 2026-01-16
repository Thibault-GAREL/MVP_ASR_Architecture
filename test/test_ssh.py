import pygame
import sys

pygame.init()

# Fenêtre
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test Pygame")

clock = pygame.time.Clock()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # fond gris foncé
    pygame.display.flip()
    clock.tick(60)
    print("AAA")

pygame.quit()
sys.exit()
