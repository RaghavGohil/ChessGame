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
import l_piece_container

# initializing pygame
pygame.init()

# pygame variables:
deltatime = 0
now = 0
winw = 1000
winh = 600
winsize = [winw, winh]
if not l_settings.screen_is_resizable:
    screen = pygame.display.set_mode(winsize)
else:
    screen = pygame.display.set_mode(winsize,pygame.RESIZABLE)
pygame.display.set_caption(l_settings.game_name)
try:
    pygame.display.set_icon(pygame.image.load(os.path.join(l_settings.base_path,l_settings.game_icon_path)))
except:
    raise Exception("Unable to load game icon.")

clock = pygame.time.Clock()

def quit_game():
    pygame.quit()
    l_font.pquit()
    l_audio.pquit()
    quit()

def update_window_width_and_height():
    if l_settings.screen_is_resizable:
        winsize[0] = screen.get_width()
        winsize[1] = screen.get_height()

def init():
    global board,border,piece_container

    l_audio.play(0,0) #play start sound
    board = l_board.Board(l_settings.base_path,(winsize[1],winsize[1]))
    border = l_border.Border(l_settings.base_path)
    piece_container = l_piece_container.PieceContainer([board.ps[0] + 20,20],[winsize[0]-(board.ps[0]+20)-20,100])
    l_piece.initialize_pieces(board)

def main():
    board.display(screen)
    piece_container.display(screen)
    l_piece.move_piece(events,board,border,MOUSEMOTION,screen)
    border.display(screen,board)
    l_piece.display_pieces(screen)
    l_in_game_locator.render_current_in_game_location(screen,board,l_colors.current_location_font_bounding_box_color,l_colors.current_location_font_color,winw,winh)

# initialize variables and run the game loop:

init()

while True:

    update_window_width_and_height()

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