import pygame
from fonctions import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


BG_IMAGE = pygame.transform.scale(pygame.image.load("./ressources/echiquier.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))


echiquier = create_pieces()


is_running = True
# white_black = 1
piece_clicked = None
piece_clicked_pos_initial = None
offset_x = 0
offset_y = 0

while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            piece_clicked = detect_click_on_piece(echiquier, event.pos)
            if piece_clicked:
                piece_clicked_pos_initial = piece_clicked.position
                offset_x =  event.pos[0] - piece_clicked.position[0]
                offset_y = event.pos[1] - piece_clicked.position[1]
        
        elif event.type == pygame.MOUSEMOTION:
            if piece_clicked:
                piece_clicked.position = (event.pos[0] - offset_x, event.pos[1] - offset_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            if piece_clicked:
                pos_final_correct = is_mouvement_correct(piece_clicked_pos_initial, event.pos, piece_clicked.type, echiquier)
                if pos_final_correct:
                    piece_clicked.position = pos_final_correct
                else:
                    piece_clicked.position = piece_clicked_pos_initial
            piece_clicked = None


    screen.blit(BG_IMAGE, (0, 0))
    for y, row in enumerate(echiquier):
        for x, piece in enumerate(row):
            screen.blit(piece.image, piece.position)


    pygame.display.flip()
    clock.tick(60)


pygame.quit()