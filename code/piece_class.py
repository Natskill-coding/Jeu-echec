import pygame


class Piece:
    def __init__(self, color, type, image, position):
        self.color = color
        self.type = type
        self.image = image
        self.position = position