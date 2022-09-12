import pygame

import l_colors
import l_font
from l_piece import Piece

class PieceContainer:
    def __init__(self,position:list,size:list):
        self.position = position
        self.size = size
        self.header_text = 'Captured Pieces:'
        self.header_x = (self.position[0]+5)
        self.header_y = (self.position[1]+5)
        self.start_offset = [self.position[0],self.position[1]+30] # offset for placing pieces
        self.captured_pieces = []
        self.max_x_storage_limit = 8
        self.individual_captured_piece_img_size = [40,40]

        
    def display(self,screen:pygame.Surface):
        pygame.draw.rect(screen,l_colors.piece_container_color,(self.position[0],self.position[1],self.size[0],self.size[1]))
        l_font.render_text(screen,30,self.header_x,self.header_y,self.header_text,l_colors.piece_container_display_text_color)
        xcount = 0
        ycount = 0
        for cp in range(len(self.captured_pieces)):
            if(xcount % self.max_x_storage_limit == 0) and xcount != 0:
                xcount = 0
                ycount += 1
            img = pygame.transform.smoothscale(self.captured_pieces[cp].piece_img,self.individual_captured_piece_img_size)
            screen.blit(img,(self.start_offset[0]+xcount*self.individual_captured_piece_img_size[0],self.start_offset[1]+ycount*self.individual_captured_piece_img_size[0]))
            xcount += 1
    def add_piece(self,piece:Piece):
        self.captured_pieces.append(piece)