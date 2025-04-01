import pygame
from fonctions import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


BG_IMAGE = pygame.transform.scale(pygame.image.load("./ressources/echiquier.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))


echiquier = create_pieces()


is_running = True
white_black = 1

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    screen.blit(BG_IMAGE, (0, 0))
    for y, row in enumerate(echiquier):
        for x, piece in enumerate(row):
            screen.blit(piece.image, piece.position)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()