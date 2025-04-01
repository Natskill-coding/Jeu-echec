import pygame
from piece_class import *


def create_pieces():
    tour_noir = Piece("black", "tour", pygame.transform.scale(pygame.image.load("./ressources/pieces/tour_noir_1.png").convert(), (100, 100)), (1 * 50, 1 * 50))

    echiquier = [
        [tour_noir]
    ]
    return echiquier

def detect_click_on_piece(echiquier, mouse_pos):
    for y, row in enumerate(echiquier):
        for x, piece in enumerate(row):
            x_intervalle = (piece.position[0], piece.position[0] + 100)
            y_intervalle = (piece.position[1], piece.position[1] + 100)
            if (x_intervalle[0] <= mouse_pos[0] <= x_intervalle[1]) and (y_intervalle[0] <= mouse_pos[1] <= y_intervalle[1]):
                return piece