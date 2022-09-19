import pygame

import l_font
from l_board import Board

class InGameLocator:
    def __init__(self,position:list,size:list):
        self.header_text =  'A8'
        self.position = position
        self.header_font_size = 35
        self.header_font = pygame.font.SysFont(l_font.font_name_path,self.header_font_size)
        self.size = size

    def render_current_in_game_location(self,screen:pygame.Surface,board:Board,bounding_box_color:tuple,font_color:tuple,winw:int,winh:int):
        pygame.draw.rect(screen,bounding_box_color,(self.position[0],self.position[1],self.size[0],self.size[1])) # ((winw-40),(winh-35),40,35)
        mousepos = pygame.mouse.get_pos()
        if (mousepos[1] < board.ps[1] and mousepos[1] > 0) and (mousepos[0] < board.ps[0] and mousepos[0] > 0):
            for x in range(len(board.xblocks)):
                for y in range(len(board.yblocks)):
                    if(mousepos[0] > x*board.isps and mousepos[1] > y*board.isps ):
                        self.header_text = ''
                        self.header_text += board.xblocks[x]
                        self.header_text += str(board.yblocks[len(board.yblocks)-(y+1)])

        l_font.render_text_load_already(screen,self.header_font,(winw-36),(winh-28),self.header_text,font_color)