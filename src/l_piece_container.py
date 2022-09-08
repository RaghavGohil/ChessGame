import pygame
import l_colors

class PieceContainer:
    def __init__(self,position:list,size:list):
        self.position = position
        self.size = size
        
    def display(self,screen:pygame.Surface):
        pygame.draw.rect(screen,l_colors.piece_container_color,(self.position[0],self.position[1],self.size[0],self.size[1]))