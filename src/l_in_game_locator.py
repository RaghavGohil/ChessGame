import pygame
import l_font

display_string = 'A8'

def render_current_in_game_location(screen,initialized_font,board,bounding_box_color,font_color,winw,winh,font_antialiasing):
    global display_string
    pygame.draw.rect(screen,bounding_box_color,((winw-40),(winh-35),40,35))
    mousepos = pygame.mouse.get_pos()
    if (mousepos[1] < board.size[1] and mousepos[1] > 0) and (mousepos[0] < board.size[0] and mousepos[0] > 0):
        for x in range(len(board.xblocks)):
            for y in range(len(board.yblocks)):
                if((mousepos[0] > x*board.isps and mousepos[0] < (x+1)*board.isps) and (mousepos[1] > y*board.isps and mousepos[1] < (y+1)*board.isps)):
                    display_string = ''
                    display_string += board.xblocks[x]
                    display_string += str(board.yblocks[len(board.yblocks)-(y+1)])
    
    l_font.render_text(screen,initialized_font,font_antialiasing,(winw-37),(winh-30),display_string,font_color)