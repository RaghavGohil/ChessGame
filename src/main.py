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
    
    pass

def move_piece(object,board):

    pass

def display_pieces():
    
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

# initialize variables and run the game loop:

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