import pygame
import os


class Board:
    def __init__(self, base_path, size):
        self.board = pygame.image.load(
            os.path.join(base_path, "../images/Board.png"))
        self.size = size  # (winh, winh)
        self.position = (0, 0)
        self.xblocks = ['A','B','C','D','E','F','G','H']
        self.yblocks = [1,2,3,4,5,6,7,8]
        self.isps = 75  # individual square pixel size

    def display(self,screen):
        self.board = pygame.transform.scale(self.board, self.size)
        screen.blit(self.board, self.position)
