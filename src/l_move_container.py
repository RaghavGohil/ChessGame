import pygame

import l_colors
import l_font

class MoveContainer:
    def __init__(self,position:list,size:list):
        self.position = position
        self.size = size
        self.header_text = 'Moves:'
        self.header_text_size = 30
        self.moves = [] # for current move display
        self.all_moves = [] #keeps track of all moves
        self.individual_move_text_size = 25
        self.header_x = (self.position[0]+5)
        self.header_y = (self.position[1]+5)
        self.start_offset = [self.position[0]+10,self.position[1]+30]
        self.max_x_storage_limit = 6
        self.text_fill_limit = 36
        self.individual_text_block_size = [50,self.individual_move_text_size]

    def display(self,screen:pygame.Surface):
        pygame.draw.rect(screen,l_colors.move_container_color,(self.position[0],self.position[1],self.size[0],self.size[1]))
        l_font.render_text(screen,self.header_text_size,self.header_x,self.header_y,self.header_text,l_colors.move_container_display_text_color)
        xcount = 0
        ycount = 0
        if (len(self.moves)-1) < self.text_fill_limit:
            for move in range(len(self.moves)):
                if(xcount % self.max_x_storage_limit == 0) and xcount != 0:
                    xcount = 0
                    ycount += 1
                if (move+1) != len(self.moves): # make text darker
                    l_font.render_text(screen,self.individual_move_text_size,int(self.start_offset[0]+xcount*self.individual_text_block_size[0]),int(self.start_offset[1]+ycount*self.individual_text_block_size[1]),self.moves[move],l_colors.move_container_display_text_color_dimmed)
                else: # make text lighter
                    l_font.render_text(screen,self.individual_move_text_size,int(self.start_offset[0]+xcount*self.individual_text_block_size[0]),int(self.start_offset[1]+ycount*self.individual_text_block_size[1]),self.moves[move],l_colors.move_container_display_text_color)
                xcount += 1
        else:
            self.moves.pop(0)
            for move in range(len(self.moves)):
                if(xcount % self.max_x_storage_limit == 0) and xcount != 0:
                    xcount = 0
                    ycount += 1
                if (move+1) != len(self.moves): # make text darker
                    l_font.render_text(screen,self.individual_move_text_size,int(self.start_offset[0]+xcount*self.individual_text_block_size[0]),int(self.start_offset[1]+ycount*self.individual_text_block_size[1]),self.moves[move],l_colors.move_container_display_text_color_dimmed)
                else: # make text lighter
                    l_font.render_text(screen,self.individual_move_text_size,int(self.start_offset[0]+xcount*self.individual_text_block_size[0]),int(self.start_offset[1]+ycount*self.individual_text_block_size[1]),self.moves[move],l_colors.move_container_display_text_color)
                xcount += 1

    def add_move(self,text:str):
        self.moves.append(text)
        self.all_moves.append(text)
