import pygame
from script import *


class Piece:
    def __init__(self, color, type, image):
        self.color = color
        self.type = type
        self.image = image
    
    def positionner(self, target_position):
        screen.blit(self.image, target_position)