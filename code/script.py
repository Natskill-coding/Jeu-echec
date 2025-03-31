import pygame
from initialisation import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


bg_image = pygame.transform.scale(pygame.image.load("ressources/echiquier.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))


echiquier = create_positionner_pieces()


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(bg_image, (0, 0))
    pygame.display.flip()
    # clock.tick(60)


pygame.quit()