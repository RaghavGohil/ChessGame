import pygame

import l_font
from l_board import Board

display_string = 'A8'

def render_current_in_game_location(screen:pygame.Surface,board:Board,bounding_box_color:tuple,font_color:tuple,winw:int,winh:int):
    global display_string
    pygame.draw.rect(screen,bounding_box_color,((winw-40),(winh-35),40,35))
    mousepos = pygame.mouse.get_pos()
    if (mousepos[1] < board.ps[1] and mousepos[1] > 0) and (mousepos[0] < board.ps[0] and mousepos[0] > 0):
        for x in range(len(board.xblocks)):
            for y in range(len(board.yblocks)):
                if(mousepos[0] > x*board.isps and mousepos[1] > y*board.isps ):
                    display_string = ''
                    display_string += board.xblocks[x]
                    display_string += str(board.yblocks[len(board.yblocks)-(y+1)])
    
    l_font.render_text(screen,35,(winw-36),(winh-28),display_string,font_color)