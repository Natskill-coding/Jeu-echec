import math
from .plus_proches import *
from .is_collision import *


def tour_is_mouvement_correct(list_pieces, pos_initial, pos_final):
    pos_initial_tab = ((pos_initial[0] / 100), (pos_initial[1] / 100))
    pos_final_tab_rounded = (math.floor(pos_final[0] / 100), math.floor(pos_final[1] / 100))

    if pos_initial_tab[0] == pos_final_tab_rounded[0]:
        list_piece_same_x = list(filter(lambda piece: piece.position[0] / 100 == pos_initial_tab[0] and piece.position[1] / 100 != pos_initial_tab[1], list_pieces))
        if list_piece_same_x:
            pieces_same_y_plus_proches = tour_pieces_plus_proches(list_piece_same_x, key=lambda piece: abs(piece.position[1] / 100 - pos_initial_tab[1]))
            if len(pieces_same_y_plus_proches) == 1:
                if pieces_same_y_plus_proches[0].position[1] / 100 > pos_initial_tab[1]:
                    if pos_final_tab_rounded[1] < pieces_same_y_plus_proches[0].position[1] / 100:
                        return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
                elif pieces_same_y_plus_proches[0].position[1] / 100 < pos_initial_tab[1]:
                    if pos_final_tab_rounded[1] > pieces_same_y_plus_proches[0].position[1] / 100:
                        return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
        else: 
            return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
        
    if pos_initial_tab[1] == pos_final_tab_rounded[1]:
        list_piece_same_y = list(filter(lambda piece: piece.position[1] / 100 == pos_initial_tab[1] and piece.position[0] / 100 != pos_initial_tab[0], list_pieces))
        if list_piece_same_y:
            pieces_same_x_plus_proches = tour_pieces_plus_proches(list_piece_same_y, key=lambda piece: abs(piece.position[0] / 100 - pos_initial_tab[0]))
            if len(pieces_same_x_plus_proches) == 1:
                if pieces_same_x_plus_proches[0].position[0] / 100 > pos_initial_tab[0]:
                    if pos_final_tab_rounded[0] < pieces_same_x_plus_proches[0].position[0] / 100:
                        return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
                elif pieces_same_x_plus_proches[0].position[0] / 100 < pos_initial_tab[0]:
                    if pos_final_tab_rounded[0] > pieces_same_x_plus_proches[0].position[0] / 100:
                        return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
        else: 
            return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
        

def cavalier_is_mouvement_correct(pos_initial, pos_final):
    pos_initial_tab = ((pos_initial[0] / 100), (pos_initial[1] / 100))
    pos_final_tab_rounded = (math.floor(pos_final[0] / 100), math.floor(pos_final[1] / 100))

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
            

def fou_is_mouvement_correct(list_pieces, pos_initial, pos_final):
    pos_initial_tab = ((pos_initial[0] / 100), (pos_initial[1] / 100))
    pos_final_tab_rounded = (math.floor(pos_final[0] / 100), math.floor(pos_final[1] / 100))

    if abs(pos_final_tab_rounded[0] - pos_initial_tab[0]) == abs(pos_final_tab_rounded[1] - pos_initial_tab[1]):
        # print(f"Initial: {pos_initial_tab}, Final: {pos_final_tab_rounded}")
        pieces_same_diagonale = list(filter(lambda piece: abs(pos_initial_tab[0] - piece.position[0] / 100) == abs(pos_initial_tab[1] - piece.position[1] / 100), list_pieces))
        if pieces_same_diagonale:
            for piece in pieces_same_diagonale:
                print(f"Même diagonale : {piece.type}")
            pieces_same_diagonale_plus_proches = fou_pieces_plus_proches(pieces_same_diagonale, lambda piece: abs(piece.position[0] / 100 - pos_initial_tab[0]))
            for piece in pieces_same_diagonale_plus_proches:
                print(f"Plus proches : {piece.type}")
            if len(pieces_same_diagonale_plus_proches) == 1:
                if pos_initial_tab[0] > pieces_same_diagonale_plus_proches[0].position[0] / 100:
                    if pos_final_tab_rounded[0] > pieces_same_diagonale_plus_proches[0].position[0] / 100:
                        return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
                if pos_initial_tab[0] < pieces_same_diagonale_plus_proches[0].position[0] / 100:
                    if pos_final_tab_rounded[0] < pieces_same_diagonale_plus_proches[0].position[0] / 100:
                        return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)
        else: 
            return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)


def dame_is_mouvement_correct(pos_initial, pos_final):
    pos_initial_tab = ((pos_initial[0] / 100), (pos_initial[1] / 100))
    pos_final_tab_rounded = (math.floor(pos_final[0] / 100), math.floor(pos_final[1] / 100))
    
    dx = abs(pos_final_tab_rounded[0] - pos_initial_tab[0])
    dy = abs(pos_final_tab_rounded[1] - pos_initial_tab[1])
    if dx == 0 or dy == 0 or dx == dy:
        return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)


def roi_is_mouvement_correct(pos_initial, pos_final):
    pos_initial_tab = ((pos_initial[0] / 100), (pos_initial[1] / 100))
    pos_final_tab_rounded = (math.floor(pos_final[0] / 100), math.floor(pos_final[1] / 100))

    dx = abs(pos_final_tab_rounded[0] - pos_initial_tab[0])
    dy = abs(pos_final_tab_rounded[1] - pos_initial_tab[1])
    if dx <= 1 and dy <= 1:
        return (pos_final_tab_rounded[0] * 100, pos_final_tab_rounded[1] * 100)