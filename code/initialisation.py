import pygame
from piece_class import *


def createPieces():
    tour_noir = Piece("black", "tour", pygame.image.load("./ressources/pieces/tour_noir_1.png").convert())

    echiquier = [
        [tour_noir]
    ]
    return echiquier

def create_positionner_pieces():
    echiquier = createPieces()
    for tab_line in echiquier:
        for piece in echiquier[tab_line]:
            piece.positionner(((echiquier.index(piece) + 1) * 50, (tab_line + 1) * 50))
    return echiquier