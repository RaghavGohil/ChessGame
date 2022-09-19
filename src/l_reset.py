from typing import Any
import pygame

import l_font
import l_colors

class Reset: #clickable button
    def __init__(self,position:list,size:list):
        self.position = position
        self.size = size
        self.header_text = 'Reset'
        self.header_font_size = 35
        self.header_font = pygame.font.SysFont(l_font.font_name_path,self.header_font_size)
        self.isresetting = False
        self.click_rect = pygame.Rect(position,size)
    
    def display(self,screen:pygame.Surface):
        pygame.draw.rect(screen,l_colors.reset_bounding_box_color,(self.position,self.size))
        l_font.render_text_load_already(screen,self.header_font,self.position[0]+7,self.position[1]+7,self.header_text,l_colors.reset_text_color)

    def handle_reset(self,events:Any):
        mousepos = pygame.mouse.get_pos()
        if self.click_rect.collidepoint(mousepos):
            for e in events: 
                if e.type == pygame.MOUSEBUTTONDOWN:
                    self.isresetting = True
