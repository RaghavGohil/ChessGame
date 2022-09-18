import pygame

import l_font
from l_board import Board

class InGameLocator:
    def __init__(self):
        self.ds =  ''

    def render_current_in_game_location(self,screen:pygame.Surface,board:Board,bounding_box_color:tuple,font_color:tuple,winw:int,winh:int):
        pygame.draw.rect(screen,bounding_box_color,((winw-40),(winh-35),40,35))
        mousepos = pygame.mouse.get_pos()
        if (mousepos[1] < board.ps[1] and mousepos[1] > 0) and (mousepos[0] < board.ps[0] and mousepos[0] > 0):
            for x in range(len(board.xblocks)):
                for y in range(len(board.yblocks)):
                    if(mousepos[0] > x*board.isps and mousepos[1] > y*board.isps ):
                        self.ds = ''
                        self.ds += board.xblocks[x]
                        self.ds += str(board.yblocks[len(board.yblocks)-(y+1)])

        l_font.render_text(screen,35,(winw-36),(winh-28),self.ds,font_color)