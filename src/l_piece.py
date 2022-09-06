# import pygame
# import os

# class Piece:
#     def __init__(self,defaultspawnpt,base_path,piece):
#         self.position = defaultspawnpt
#         self.cropval = cropval
#         self.pieces = pygame.image.load(os.path.join(base_path, "../images/Pieces.png"))
#         self.size_factor = 0.7
#         self.size = (int(640*self.size_factor), int(213*self.size_factor))
#         self.pieces = pygame.transform.scale(self.pieces, self.size)
#         self.piece = screen.blit(self.pieces,self.position,self.cropval)

#     def display(self,screen):
#         self.piece = screen.blit(self.pieces,self.position,self.cropval)