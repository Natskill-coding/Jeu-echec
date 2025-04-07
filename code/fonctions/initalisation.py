import pygame


class Piece:
    def __init__(self, color, type, image, position):
        self.color = color
        self.type = type
        self.image = image
        self.position = position

def create_pieces():
    list_pieces = []

    tour_noir_1 = Piece("noir", "tour", pygame.transform.scale(pygame.image.load("ressources/pieces/tour_noir.png").convert_alpha(), (100, 100)), (0, 0))
    list_pieces.append(tour_noir_1)
    tour_noir_2 = Piece("noir", "tour", pygame.transform.scale(pygame.image.load("ressources/pieces/tour_noir.png").convert_alpha(), (100, 100)), (700, 0))
    list_pieces.append(tour_noir_2)
    cavalier_noir_1 = Piece("noir", "cavalier", pygame.transform.scale(pygame.image.load("ressources/pieces/cavalier_noir.png").convert_alpha(), (100, 100)), (100, 0))
    list_pieces.append(cavalier_noir_1)
    cavalier_noir_2 = Piece("noir", "cavalier", pygame.transform.scale(pygame.image.load("ressources/pieces/cavalier_noir.png").convert_alpha(), (100, 100)), (600, 0))
    list_pieces.append(cavalier_noir_2)
    fou_noir_1 = Piece("noir", "fou", pygame.transform.scale(pygame.image.load("ressources/pieces/fou_noir.png").convert_alpha(), (100, 100)), (200, 0))
    list_pieces.append(fou_noir_1)
    fou_noir_2 = Piece("noir", "fou", pygame.transform.scale(pygame.image.load("ressources/pieces/fou_noir.png").convert_alpha(), (100, 100)), (500, 0))
    list_pieces.append(fou_noir_2)
    dame_noir = Piece("noir", "dame", pygame.transform.scale(pygame.image.load("ressources/pieces/dame_noir.png").convert_alpha(), (100, 100)), (300, 0))
    list_pieces.append(dame_noir)
    roi_noir = Piece("noir", "roi", pygame.transform.scale(pygame.image.load("ressources/pieces/roi_noir.png").convert_alpha(), (100, 100)), (400, 0))
    list_pieces.append(roi_noir)
    for i in range(8):
        pion_noir = Piece("noir", "pion", pygame.transform.scale(pygame.image.load("ressources/pieces/pion_noir.png").convert_alpha(), (100, 100)), (i * 100, 100))
        list_pieces.append(pion_noir)

    tour_blanc_1 = Piece("blanc", "tour", pygame.transform.scale(pygame.image.load("ressources/pieces/tour_blanc.png").convert_alpha(), (100, 100)), (0, 700))
    list_pieces.append(tour_blanc_1)
    tour_blanc_2 = Piece("blanc", "tour", pygame.transform.scale(pygame.image.load("ressources/pieces/tour_blanc.png").convert_alpha(), (100, 100)), (700, 700))
    list_pieces.append(tour_blanc_2)
    cavalier_blanc_1 = Piece("blanc", "cavalier", pygame.transform.scale(pygame.image.load("ressources/pieces/cavalier_blanc.png").convert_alpha(), (100, 100)), (100, 700))
    list_pieces.append(cavalier_blanc_1)
    cavalier_blanc_2 = Piece("blanc", "cavalier", pygame.transform.scale(pygame.image.load("ressources/pieces/cavalier_blanc.png").convert_alpha(), (100, 100)), (600, 700))
    list_pieces.append(cavalier_blanc_2)
    fou_blanc_1 = Piece("blanc", "fou", pygame.transform.scale(pygame.image.load("ressources/pieces/fou_blanc.png").convert_alpha(), (100, 100)), (200, 700))
    list_pieces.append(fou_blanc_1)
    fou_blanc_2 = Piece("blanc", "fou", pygame.transform.scale(pygame.image.load("ressources/pieces/fou_blanc.png").convert_alpha(), (100, 100)), (500, 700))
    list_pieces.append(fou_blanc_2)
    dame_blanc = Piece("blanc", "dame", pygame.transform.scale(pygame.image.load("ressources/pieces/dame_blanc.png").convert_alpha(), (100, 100)), (300, 700))
    list_pieces.append(dame_blanc)
    roi_blanc = Piece("blanc", "roi", pygame.transform.scale(pygame.image.load("ressources/pieces/roi_blanc.png").convert_alpha(), (100, 100)), (400, 700))
    list_pieces.append(roi_blanc)
    for i in range(8):
        pion_blanc = Piece("blanc", "pion", pygame.transform.scale(pygame.image.load("ressources/pieces/pion_blanc.png").convert_alpha(), (100, 100)), (i * 100, 600))
        list_pieces.append(pion_blanc )

    return list_pieces