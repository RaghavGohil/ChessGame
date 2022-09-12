import pygame
import l_colors
import l_font

class PieceContainer:
    def __init__(self,position:list,size:list):
        self.position = position
        self.size = size
        self.header_text = 'Captured Pieces:'
        self.header_x = (self.position[0]+5)
        self.header_y = (self.position[1]+5)
        self.start_offset = [self.position[0]+5,self.position[1]+10] # offset for placing pieces

        
    def display(self,screen:pygame.Surface):
        pygame.draw.rect(screen,l_colors.piece_container_color,(self.position[0],self.position[1],self.size[0],self.size[1]))
        l_font.render_text(screen,25,self.header_x,self.header_y,self.header_text,l_colors.piece_container_display_text_color)

    def add_piece():
        pass