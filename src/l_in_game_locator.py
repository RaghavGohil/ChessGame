import pygame
import l_font

def render_current_in_game_location(screen,initialized_font,board,bounding_box_color,font_color,winw,winh,font_antialiasing,):
    pygame.draw.rect(screen,bounding_box_color,((winw-35),(winh-35),35,35))
    
    l_font.render_text(screen,initialized_font,font_antialiasing,(winw-32),(winh-30),"E4",font_color)