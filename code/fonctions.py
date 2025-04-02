import pygame
import math
from piece_class import *


def create_pieces():
    tour_noir_1 = Piece("black", "tour", pygame.transform.scale(pygame.image.load("./ressources/pieces/tour_noir_1.png").convert(), (100, 100)), (0, 0))
    cavalier_noir_1 = Piece("black", "cavalier", pygame.transform.scale(pygame.image.load("./ressources/pieces/cavalier_noir_1.png").convert(), (100, 100)), (100, 0))
    fou_noir_1 = Piece("black", "fou", pygame.transform.scale(pygame.image.load("./ressources/pieces/fou_noir_1.png").convert(), (100, 100)), (200, 0))
    dame_noir_1 = Piece("black", "dame", pygame.transform.scale(pygame.image.load("./ressources/pieces/dame_noir_1.png").convert(), (100, 100)), (300, 0))
    roi_noir_1 = Piece("black", "roi", pygame.transform.scale(pygame.image.load("./ressources/pieces/roi_noir_1.png").convert(), (100, 100)), (400, 0))

    echiquier = [
        [tour_noir_1, cavalier_noir_1, fou_noir_1, dame_noir_1, roi_noir_1]
    ]
    return echiquier


def detect_click_on_piece(echiquier, mouse_pos):
    for y, row in enumerate(echiquier):
        for x, piece in enumerate(row):
            x_intervalle = (piece.position[0], piece.position[0] + 100)
            y_intervalle = (piece.position[1], piece.position[1] + 100)
            if (x_intervalle[0] <= mouse_pos[0] <= x_intervalle[1]) and (y_intervalle[0] <= mouse_pos[1] <= y_intervalle[1]):
                return piece


def is_mouvement_correct(pos_initial, pos_final, piece_type):
    pos_initial_tab = ((pos_initial[0] / 100), (pos_initial[1] / 100))
    pos_final_tab_rounded = (math.floor(pos_final[0] / 100), math.floor(pos_final[1] / 100))

    if piece_type == "tour":
        if pos_initial_tab[0] == pos_final_tab_rounded[0] or pos_initial_tab[1] == pos_final_tab_rounded[1]:
            return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
        
    if piece_type == "cavalier":
        if pos_final_tab_rounded[0] - pos_initial_tab[0] == 2:
            if pos_final_tab_rounded[1] - pos_initial_tab[1] == 1:
                return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
            if pos_final_tab_rounded[1] - pos_initial_tab[1] == -1:
                return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
            
        if pos_final_tab_rounded[0] - pos_initial_tab[0] == -2:
            if pos_final_tab_rounded[1] - pos_initial_tab[1] == 1:
                return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
            if pos_final_tab_rounded[1] - pos_initial_tab[1] == -1:
                return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
            
        if pos_final_tab_rounded[1] - pos_initial_tab[1] == 2:
            if pos_final_tab_rounded[0] - pos_initial_tab[0] == 1:
                return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
            if pos_final_tab_rounded[0] - pos_initial_tab[0] == -1:
                return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
            
        if pos_final_tab_rounded[1] - pos_initial_tab[1] == -2:
            if pos_final_tab_rounded[0] - pos_initial_tab[0] == 1:
                return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
            if pos_final_tab_rounded[0] - pos_initial_tab[0] == -1:
                return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
            
    if piece_type == "fou":
        if abs(pos_final_tab_rounded[0] - pos_initial_tab[0]) == abs(pos_final_tab_rounded[1] - pos_initial_tab[1]):
            return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
        
    if piece_type == "dame":
        dx = abs(pos_final_tab_rounded[0] - pos_initial_tab[0])
        dy = abs(pos_final_tab_rounded[1] - pos_initial_tab[1])
        if dx == 0 or dy == 0 or dx == dy:
            return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
        
    if piece_type == "roi":
        dx = abs(pos_final_tab_rounded[0] - pos_initial_tab[0])
        dy = abs(pos_final_tab_rounded[1] - pos_initial_tab[1])
        if dx <= 1 and dy <= 1:
            return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)