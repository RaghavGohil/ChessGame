import os
import pygame
from pygame.locals import *

import l_board
import l_border
import l_piece
import l_settings
import l_colors
import l_in_game_locator
import l_font
import l_bitboards
import l_audio

# initializing pygame
pygame.init()

# pygame variables:
deltatime = 0
now = 0
winw = 800
winh = 600
winsize = (winw, winh)
screen = pygame.display.set_mode(winsize)
pygame.display.set_caption(l_settings.game_name)
pygame.display.set_icon(pygame.image.load(os.path.join(l_settings.base_path,l_settings.game_icon_path)))
initialized_font = pygame.font.SysFont(l_font.font_name_path , l_font.font_size)
clock = pygame.time.Clock()

def quit_game():
    pygame.quit()
    l_font.pquit()
    l_audio.pquit()
    quit()

def initialize_pieces(board):
    # global w_pawn,w_rook,w_knight,w_bishop,w_king,w_queen,b_pawn,b_rook,b_knight,b_bishop,b_king,b_queen
    # w_pawn = []
    # b_pawn = []
    # for x in range(num_pawn):
    #     w_pawn.append(l_piece.Piece(((x)*board.isps,board.isps*6),(0,0,board.isps,board.isps),l_settings.base_path,screen))
    # w_rook = [l_piece.Piece((0,board.isps*7),(board.isps,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*7,board.isps*7),(board.isps,0,board.isps,board.isps),l_settings.base_path,screen)]
    # w_knight = [l_piece.Piece((board.isps,board.isps*7),(board.isps*2,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*6,board.isps*7),(board.isps*2,0,board.isps,board.isps),l_settings.base_path,screen)]
    # w_bishop = [l_piece.Piece((board.isps*2,board.isps*7),(board.isps*3,0,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*5,board.isps*7),(board.isps*3,0,board.isps,board.isps),l_settings.base_path,screen)]
    # w_queen = l_piece.Piece((board.isps*3,board.isps*7),(board.isps*5,0,board.isps,board.isps),l_settings.base_path,screen)
    # w_king = l_piece.Piece((board.isps*4,board.isps*7),(board.isps*4,0,board.isps,board.isps),l_settings.base_path,screen)
    # for x in range(num_pawn):
    #     b_pawn.append(l_piece.Piece(((x)*board.isps,board.isps),(0,board.isps,board.isps,board.isps),l_settings.base_path,screen))
    # b_rook = [l_piece.Piece((0,0),(board.isps,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*7,0),(board.isps,board.isps,board.isps,board.isps),l_settings.base_path,screen)]
    # b_knight = [l_piece.Piece((board.isps,0),(board.isps*2,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*6,0),(board.isps*2,board.isps,board.isps,board.isps),l_settings.base_path,screen)]
    # b_bishop = [l_piece.Piece((board.isps*2,0),(board.isps*3,board.isps,board.isps,board.isps),l_settings.base_path,screen),l_piece.Piece((board.isps*5,0),(board.isps*3,board.isps,board.isps,board.isps),l_settings.base_path,screen)]
    # b_queen = l_piece.Piece((board.isps*3,0),(board.isps*5,board.isps,board.isps,board.isps),l_settings.base_path,screen)
    # b_king = l_piece.Piece((board.isps*4,0),(board.isps*4,board.isps,board.isps,board.isps),l_settings.base_path,screen)
    pass

def move_piece(object,board):

    # held = False #To ensure that only one piece is picked at a time.
    # object_rect = pygame.Rect(object.position[0],object.position[1],board.isps,board.isps)

    # for e in events:
    #     if e.type == MOUSEBUTTONDOWN and object_rect.collidepoint(pygame.mouse.get_pos()):
    #         held = True
    #     elif e.type == MOUSEMOTION and held:
    #         object.position = (pygame.mouse.get_pos()[0]-object.position[0],pygame.mouse.get_pos()[1]-object.position[1])
    #     if e.type == MOUSEBUTTONUP:
    #         held = False
    pass

def display_pieces():
    # pieces_array = [w_pawn,w_rook,w_knight,w_bishop,w_king,w_queen,b_pawn,b_rook,b_knight,b_bishop,b_king,b_queen]

    # for x in pieces_array:
    #     if type(x) != list:
    #         move_piece(x,board)
    #         x.display(screen)

    #     else:
    #         for y in x:
    #             move_piece(y,board)
    #             y.display(screen)
    pass

def init():
    global board,border

    board = l_board.Board(l_settings.base_path,(winsize[1],winsize[1]))
    border = l_border.Border(l_settings.base_path)
    initialize_pieces(board)

def main():
    board.display(screen)
    border.display(screen,board)
    display_pieces()
    l_in_game_locator.render_current_in_game_location(screen,initialized_font,board,l_colors.current_location_font_bounding_box_color,l_colors.current_location_font_color,winw,winh,l_font.font_antialiasing)

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