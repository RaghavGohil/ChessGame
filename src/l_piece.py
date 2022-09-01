import pygame
import os

class Piece:
    def __init__(self,defaultspawnpt,cropval,base_path,screen):
        self.position = defaultspawnpt
        self.isHeld = False
        self.cropval = cropval
        self.pieces = pygame.image.load(os.path.join(base_path, "../images/Pieces.png"))
        self.size_factor = 0.7
        self.size = (int(640*self.size_factor), int(213*self.size_factor))
        self.pieces = pygame.transform.scale(self.pieces, self.size)
        self.piece = screen.blit(self.pieces,self.position,cropval)

    def display(self,screen):
        self.piece = screen.blit(self.pieces,self.position,self.cropval) #NOTE : use piece later..