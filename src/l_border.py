import pygame
import os

from l_board import Board

class Border:
    def __init__(self,base_path:str):
        try:
            self.border= pygame.image.load(os.path.join(base_path, "../images/Border.png")).convert()
        except:
            raise Exception("Unable to load border image.")
        self.position = [0,0]

    def display(self,screen:pygame.Surface,board:Board):
        mousepos = pygame.mouse.get_pos()
        if (mousepos[1] < board.ps[1] and mousepos[1] > 0) and (mousepos[0] < board.ps[0] and mousepos[0] > 0):
            for x in range(len(board.yblocks)):
                for y in range(len(board.yblocks)):
                    if(mousepos[0] > x*board.isps and mousepos[0] < (x+1)*board.isps):
                        self.position[0] = x*board.isps
                    if(mousepos[1] > y*board.isps and mousepos[1] < (y+1)*board.isps):
                        self.position[1] = y*board.isps
                    
        screen.blit(self.border,self.position)