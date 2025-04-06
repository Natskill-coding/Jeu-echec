import pygame
from fonctions.initalisation import *
from fonctions.verifications import *
from fonctions.initalisation import *


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


BG_IMAGE = pygame.transform.scale(pygame.image.load("ressources/echiquier.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))


list_pieces = create_pieces()


def detect_click_on_piece(list_pieces, mouse_pos):
    for piece in list_pieces:
        x_intervalle = (piece.position[0], piece.position[0] + 100)
        y_intervalle = (piece.position[1], piece.position[1] + 100)
        if (x_intervalle[0] <= mouse_pos[0] <= x_intervalle[1]) and (y_intervalle[0] <= mouse_pos[1] <= y_intervalle[1]):
            return piece



piece_clicked = None
piece_clicked_pos_initial = None
offset_x = 0
offset_y = 0

white_black = 1

is_running = True
while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            piece_clicked = detect_click_on_piece(list_pieces, event.pos)
            if piece_clicked:
                piece_clicked_pos_initial = piece_clicked.position
                offset_x =  event.pos[0] - piece_clicked.position[0]
                offset_y = event.pos[1] - piece_clicked.position[1]
        
        elif event.type == pygame.MOUSEMOTION:
            if piece_clicked:
                piece_clicked.position = (event.pos[0] - offset_x, event.pos[1] - offset_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            if piece_clicked:
                if event.pos[0] > 800 or event.pos[0] < 0 or event.pos[1] > 800 or event.pos[1] < 0:
                    piece_clicked.position = piece_clicked_pos_initial
                else: 
                    color_to_play = a_qui_de_jouer(white_black)
                    if piece_clicked.color == color_to_play:
                        if piece_clicked.type == "tour":
                            pos_final_correct = tour_is_mouvement_correct(list_pieces, piece_clicked_pos_initial, event.pos)
                        elif piece_clicked.type == "cavalier":
                            pos_final_correct = cavalier_is_mouvement_correct(piece_clicked_pos_initial, event.pos)
                        elif piece_clicked.type == "fou":
                            pos_final_correct = fou_is_mouvement_correct(list_pieces, piece_clicked_pos_initial, event.pos)
                        elif piece_clicked.type == "dame":
                            pos_final_correct = dame_is_mouvement_correct(list_pieces, piece_clicked_pos_initial, event.pos)
                        elif piece_clicked.type == "roi":
                            pos_final_correct = roi_is_mouvement_correct(piece_clicked_pos_initial, event.pos)

                        if pos_final_correct:
                            piece_collision = is_collision(list_pieces, piece_clicked_pos_initial, pos_final_correct)
                            if piece_collision:
                                list_pieces.remove(piece_collision)
                            piece_clicked.position = pos_final_correct
                            white_black += 1
                        else:
                            piece_clicked.position = piece_clicked_pos_initial
                    else:
                        piece_clicked.position = piece_clicked_pos_initial
            piece_clicked = None


    screen.blit(BG_IMAGE, (0, 0))
    for piece in list_pieces:
        screen.blit(piece.image, piece.position)


    pygame.display.flip()
    clock.tick(60)


pygame.quit()