import os
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

# game settings:
fps = 60
font_size = 30
deltatime = 0
now = 0
font_antialiasing = True
winw = 800
winh = 600
winsize = (winw, winh)
screen = pygame.display.set_mode(winsize)
pygame.display.set_caption('Chess')
font = pygame.font.SysFont('aerial', font_size)
clock = pygame.time.Clock()

# paths:
base_path = os.path.dirname(__file__)

# flags:
GAME_OVER = False

# colors:
bg_color = (79, 79, 79)

# ui:
aesthetic_line_color = (143, 143, 143)
aesthetic_line_size = 6


def quit_game():
    pygame.quit()
    quit()


class Board:
    def __init__(self):
        self.board = pygame.image.load(
            os.path.join(base_path, "../images/Board.png"))
        self.size = (winh, winh)
        self.position = (0, 0)
        self.isps = 75#individual square pixel size

    def display(self):
        self.board = pygame.transform.scale(self.board, self.size)
        screen.blit(self.board, self.position)

class Border:
    def __init__(self):
        self.border= pygame.image.load(os.path.join(base_path, "../images/Border.png"))
        self.position = [0,0]
        self.blocknum = 8

    def display(self,board):
        mousepos = pygame.mouse.get_pos()
        if (mousepos[1] < board.size[1] and mousepos[1] > 0) and (mousepos[0] < board.size[0] and mousepos[0] > 0):
            for x in range(self.blocknum):
                for y in range(self.blocknum):
                    if(mousepos[0] > x*board.isps):
                        self.position[0] = x*board.isps
                    if(mousepos[1] > y*board.isps):
                        self.position[1] = y*board.isps
                    
        screen.blit(self.border,self.position)
                        
                    
                

class Piece:
    def __init__(self,defaultspawnpt,cropval):
        self.position = defaultspawnpt
        self.isHeld = False
        self.cropval = cropval
        self.pieces = pygame.image.load(os.path.join(base_path, "../images/Pieces.png"))
        self.size_factor = 0.7
        self.size = (int(640*self.size_factor), int(213*self.size_factor))
        self.pieces = pygame.transform.scale(self.pieces, self.size)
        self.piece = screen.blit(self.pieces,self.position,cropval)

    def display(self):
        self.piece = screen.blit(self.pieces,self.position,self.cropval) #NOTE : use piece later..

def initialize_pieces(board):
    global w_pawn,w_rook,w_knight,w_bishop,w_king,w_queen,b_pawn,b_rook,b_knight,b_bishop,b_king,b_queen
    w_pawn = [Piece((0,board.isps*6),(0,0,board.isps,board.isps)),Piece((board.isps,board.isps*6),(0,0,board.isps,board.isps)),Piece((board.isps*2,board.isps*6),(0,0,board.isps,board.isps)),Piece((board.isps*3,board.isps*6),(0,0,board.isps,board.isps)),Piece((board.isps*4,board.isps*6),(0,0,board.isps,board.isps)),Piece((board.isps*5,board.isps*6),(0,0,board.isps,board.isps)),Piece((board.isps*6,board.isps*6),(0,0,board.isps,board.isps)),Piece((board.isps*7,board.isps*6),(0,0,board.isps,board.isps))]
    w_rook = [Piece((0,board.isps*7),(board.isps,0,board.isps,board.isps)),Piece((board.isps*7,board.isps*7),(board.isps,0,board.isps,board.isps))]
    w_knight = [Piece((board.isps,board.isps*7),(board.isps*2,0,board.isps,board.isps)),Piece((board.isps*6,board.isps*7),(board.isps*2,0,board.isps,board.isps))]
    w_bishop = [Piece((board.isps*2,board.isps*7),(board.isps*3,0,board.isps,board.isps)),Piece((board.isps*5,board.isps*7),(board.isps*3,0,board.isps,board.isps))]
    w_queen = Piece((board.isps*3,board.isps*7),(board.isps*5,0,board.isps,board.isps))
    w_king = Piece((board.isps*4,board.isps*7),(board.isps*4,0,board.isps,board.isps))
    b_pawn = [Piece((0,board.isps),(0,board.isps,board.isps,board.isps)),Piece((board.isps,board.isps),(0,board.isps,board.isps,board.isps)),Piece((board.isps*2,board.isps),(0,board.isps,board.isps,board.isps)),Piece((board.isps*3,board.isps),(0,board.isps,board.isps,board.isps)),Piece((board.isps*4,board.isps),(0,board.isps,board.isps,board.isps)),Piece((board.isps*5,board.isps),(0,board.isps,board.isps,board.isps)),Piece((board.isps*6,board.isps),(0,board.isps,board.isps,board.isps)),Piece((board.isps*7,board.isps),(0,board.isps,board.isps,board.isps))]
    b_rook = [Piece((0,0),(board.isps,board.isps,board.isps,board.isps)),Piece((board.isps*7,0),(board.isps,board.isps,board.isps,board.isps))]
    b_knight = [Piece((board.isps,0),(board.isps*2,board.isps,board.isps,board.isps)),Piece((board.isps*6,0),(board.isps*2,board.isps,board.isps,board.isps))]
    b_bishop = [Piece((board.isps*2,0),(board.isps*3,board.isps,board.isps,board.isps)),Piece((board.isps*5,0),(board.isps*3,board.isps,board.isps,board.isps))]
    b_queen = Piece((board.isps*3,0),(board.isps*5,board.isps,board.isps,board.isps))
    b_king = Piece((board.isps*4,0),(board.isps*4,board.isps,board.isps,board.isps))

def move_piece(object):
    for e in events:
                    if e.type == MOUSEBUTTONDOWN:
                        object.isHeld = True
                    elif e.type == MOUSEMOTION and object.isHeld:
                        rect = object.pieces.get_rect()
                        print(rect)
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            object.position = pygame.mouse.get_pos()
                        object.isHeld = False

def display_and_move_pieces():
    pieces_array = [w_pawn,w_rook,w_knight,w_bishop,w_king,w_queen,b_pawn,b_rook,b_knight,b_bishop,b_king,b_queen]

    for x in pieces_array:
        if type(x) != list:
            x.display()
            move_piece(x)

        else:
            for y in x:
                y.display()
                move_piece(y)

def draw_aesthetic_line(board):
    pygame.draw.rect(screen,aesthetic_line_color,(board.size[1],0,aesthetic_line_size,board.size[1]))

def init():
    global board,border

    board = Board()
    border = Border()
    initialize_pieces(board)

def main():
    draw_aesthetic_line(board)
    board.display()
    border.display(board)
    display_and_move_pieces()

#MAIN EVENTS ARE SEQUENCED HERE:

init()

while True:

    now = pygame.time.get_ticks()

    events = pygame.event.get()

    for e in events:
        if e.type == pygame.QUIT:
            quit_game()

    screen.fill(bg_color)

    if __name__ == "__main__":
        main()

    pygame.display.update()
    clock.tick(fps)

    # deltatime calculation
    deltatime = pygame.time.get_ticks() - now
    now = 0