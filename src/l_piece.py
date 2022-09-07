import pygame
import os

import l_settings

class Piece:
    def __init__(self,defaultspawnpt,base_path,piece):
        self.position = defaultspawnpt
        self.piece = piece
        if(piece == 'P'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_pawn.png')).convert_alpha()
        elif(piece == 'R'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_rook.png')).convert_alpha()
        elif(piece == 'N'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_knight.png')).convert_alpha()
        elif(piece == 'B'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_bishop.png')).convert_alpha()
        elif(piece == 'Q'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_queen.png')).convert_alpha()
        elif(piece == 'K'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/b_king.png')).convert_alpha()
        elif(piece == 'p'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_pawn.png')).convert_alpha()
        elif(piece == 'r'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_rook.png')).convert_alpha()
        elif(piece == 'n'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_knight.png')).convert_alpha()
        elif(piece == 'b'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_bishop.png')).convert_alpha()
        elif(piece == 'q'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_queen.png')).convert_alpha()
        elif(piece == 'k'):
            self.piece_img = pygame.image.load(os.path.join(l_settings.base_path,'../images/w_king.png')).convert_alpha()

    def display(self,screen):
        self.piece = screen.blit(self.piece_img,self.position)