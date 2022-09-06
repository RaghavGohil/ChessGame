import pygame
import os


class Board:
    def __init__(self, base_path, ps):
        self.board_img = pygame.image.load(
            os.path.join(base_path, "../images/Board.png")).convert()
        self.ps = ps # (winh, winh) pixel size
        self.position = (0, 0)
        self.xblocks = ['A','B','C','D','E','F','G','H']
        self.yblocks = [1,2,3,4,5,6,7,8]
        self.isps = 75  # individual square pixel size
        self.char_board = [ # use this for drawing to the main screen (operations will be done on charboard which will be converted to bitboards)
            'R','N','B','Q','K','B','N','R', # black is represented by upper case
            'P','P','P','P','P','P','P','P',
            'e','e','e','e','e','e','e','e',
            'e','e','e','e','e','e','e','e',
            'e','e','e','e','e','e','e','e',
            'e','e','e','e','e','e','e','e',
            'p','p','p','p','p','p','p','p',
            'r','n','b','q','k','b','n','r', # white is represented by lower case
        ]
        self.w_pawn = self.generate_charboard('p')
        self.w_rook = self.generate_charboard('r')
        self.w_knight = self.generate_charboard('n')
        self.w_bishop = self.generate_charboard('b')
        self.w_queen = self.generate_charboard('q')
        self.w_king = self.generate_charboard('k')
        self.b_pawn = self.generate_charboard('P')
        self.b_rook = self.generate_charboard('R')
        self.b_knight = self.generate_charboard('N')
        self.b_bishop = self.generate_charboard('B')
        self.b_queen = self.generate_charboard('Q')
        self.b_king = self.generate_charboard('K')
        self.char_piece_boards = [self.w_pawn,self.w_rook,self.w_knight,self.w_bishop,self.w_queen,self.w_king,self.b_pawn,self.b_rook,self.b_knight,self.b_bishop,self.b_queen,self.b_king]
        self.mask = [
            0,0,0,0,0,0,0,1,
            0,0,0,0,0,0,0,1,
            0,0,0,0,0,0,0,1,
            0,0,0,0,0,0,0,1,
            0,0,0,0,0,0,0,1,
            0,0,0,0,0,0,0,1,
            0,0,0,0,0,0,0,1,
            0,0,0,0,0,0,0,1,
        ]

    def generate_charboard(self,piece,cba)->list: # generate character board instead of the normal bit board (cba is char board array)

        arr = []

        for x in cba:
            if (x == piece):
                arr.append(x)
            else:
                arr.append('e')

        return arr
    
    def update_board(cba,cpba): # performance heavy.. should be called once per move (cpba is char piece board array , cpb is char piece board in that array)
        for cpb in cpba:
            temp = 'n'
            for x in range(64): # fill in temp with the charboard type thing
                if(cpb[x] != 'e'):
                    temp = cpb[x]
                    break
            for y in range(64):
                if(cba[y] == temp): # make previous spaces empty
                    cba[y] = 'e'
                if(cpb[y] != 'e'): # is not empty
                    cba[y] = cpb[y]
    


    def display(self,screen):
        self.board = pygame.transform.scale(self.board_img, self.size)
        screen.blit(self.board_img, self.position)
    
    
