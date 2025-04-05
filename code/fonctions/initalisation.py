import pygame


class Piece:
    def __init__(self, color, type, image, position):
        self.color = color
        self.type = type
        self.image = image
        self.position = position

def create_pieces():
    list_pieces = []
    tour_noir_1 = Piece("black", "tour", pygame.transform.scale(pygame.image.load("./ressources/pieces/tour_noir_1.png").convert(), (100, 100)), (0, 0))
    list_pieces.append(tour_noir_1)
    cavalier_noir_1 = Piece("black", "cavalier", pygame.transform.scale(pygame.image.load("./ressources/pieces/cavalier_noir_1.png").convert(), (100, 100)), (100, 0))
    list_pieces.append(cavalier_noir_1)
    fou_noir_1 = Piece("black", "fou", pygame.transform.scale(pygame.image.load("./ressources/pieces/fou_noir_1.png").convert(), (100, 100)), (200, 0))
    list_pieces.append(fou_noir_1)
    dame_noir_1 = Piece("black", "dame", pygame.transform.scale(pygame.image.load("./ressources/pieces/dame_noir_1.png").convert(), (100, 100)), (300, 0))
    list_pieces.append(dame_noir_1)
    roi_noir_1 = Piece("black", "roi", pygame.transform.scale(pygame.image.load("./ressources/pieces/roi_noir_1.png").convert(), (100, 100)), (400, 0))
    list_pieces.append(roi_noir_1)

    return list_pieces