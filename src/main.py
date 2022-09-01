#global imports
import os
import pygame
from pygame.locals import *

#local imports
import l_board
import l_border
import l_piece
import l_settings
import l_colors

pygame.init()
pygame.font.init()

# pygame vars:
deltatime = 0
now = 0
winw = 800
winh = 600
winsize = (winw, winh)
screen = pygame.display.set_mode(winsize)
pygame.display.set_caption(l_settings.game_name)
font = pygame.font.SysFont(l_settings.font_name , l_settings.font_size)
clock = pygame.time.Clock()

# flags:
GAME_OVER = False


def quit_game():
    pygame.quit()
    quit()

def initialize_pieces(board):
    global w_pawn,w_rook,w_knight,w_bishop,w_king,w_queen,b_pawn,b_rook,b_knight,b_bishop,b_king,b_queen
    w_pawn = [l_piece.Piece((0,board.isps*6),(0,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps,board.isps*6),(0,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*2,board.isps*6),(0,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*3,board.isps*6),(0,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*4,board.isps*6),(0,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*5,board.isps*6),(0,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*6,board.isps*6),(0,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*7,board.isps*6),(0,0,board.isps,board.isps),l_settings.base_path,screen)]
    w_rook = [l_piece.Piece((0,board.isps*7),(board.isps,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*7,board.isps*7),(board.isps,0,board.isps,board.isps),l_settings.base_path,screen)]
    w_knight = [l_piece.Piece((board.isps,board.isps*7),(board.isps*2,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*6,board.isps*7),(board.isps*2,0,board.isps,board.isps),l_settings.base_path,screen)]
    w_bishop = [l_piece.Piece((board.isps*2,board.isps*7),(board.isps*3,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*5,board.isps*7),(board.isps*3,0,board.isps,board.isps),l_settings.base_path,screen)]
    w_queen = l_piece.Piece((board.isps*3,board.isps*7),(board.isps*5,0,board.isps,board.isps),l_settings.base_path,screen)
    w_king = l_piece.Piece((board.isps*4,board.isps*7),(board.isps*4,0,board.isps,board.isps),l_settings.base_path,screen)
    b_pawn = [l_piece.Piece((0,board.isps),(0,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps,board.isps),(0,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*2,board.isps),(0,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*3,board.isps),(0,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*4,board.isps),(0,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*5,board.isps),(0,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*6,board.isps),(0,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*7,board.isps),(0,board.isps,board.isps,board.isps),l_settings.base_path,screen)]
    b_rook = [l_piece.Piece((0,0),(board.isps,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*7,0),(board.isps,board.isps,board.isps,board.isps),l_settings.base_path,screen)]
    b_knight = [l_piece.Piece((board.isps,0),(board.isps*2,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*6,0),(board.isps*2,board.isps,board.isps,board.isps),l_settings.base_path,screen)]
    b_bishop = [l_piece.Piece((board.isps*2,0),(board.isps*3,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*5,0),(board.isps*3,board.isps,board.isps,board.isps),l_settings.base_path,screen)]
    b_queen = l_piece.Piece((board.isps*3,0),(board.isps*5,board.isps,board.isps,board.isps),l_settings.base_path,screen)
    b_king = l_piece.Piece((board.isps*4,0),(board.isps*4,board.isps,board.isps,board.isps),l_settings.base_path,screen)

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
            x.display(screen)
            move_piece(x)

        else:
            for y in x:
                y.display(screen)
                move_piece(y)

def init():
    global board,border

    board = l_board.Board(l_settings.base_path,(winsize[1],winsize[1]))
    border = l_border.Border(l_settings.base_path)
    initialize_pieces(board)

def main():
    board.display(screen)
    border.display(screen,board)
    display_and_move_pieces()

#MAIN EVENTS ARE SEQUENCED HERE:

init()

while True:

    now = pygame.time.get_ticks()

    events = pygame.event.get()

    for e in events:
        if e.type == pygame.QUIT:
            quit_game()

    screen.fill(l_colors.bg_color)

    if __name__ == "__main__":
        main()

    pygame.display.update()
    clock.tick(l_settings.fps)

    # deltatime calculation
    deltatime = pygame.time.get_ticks() - now
    now = 0