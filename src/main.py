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
import l_move_container
import l_reset

# initializing pygame
pygame.init()

# pygame variables:
deltatime = 0
now = 0
winw = 1000
winh = 600
winsize = [winw, winh]
screen_flags = DOUBLEBUF|RESIZABLE
if not l_settings.screen_is_resizable:
    screen = pygame.display.set_mode(winsize)
else:
    screen = pygame.display.set_mode(winsize,screen_flags)
pygame.display.set_caption(l_settings.game_name)
try:
    pygame.display.set_icon(pygame.image.load(os.path.join(l_settings.base_path,l_settings.game_icon_path)))
except:
    raise Exception("Unable to load game icon.")

clock = pygame.time.Clock()

# game state:
game_is_running = True

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
    global board,border,piece_container,move_container,in_game_locator,reset

    l_audio.play(0,0) #play start sound
    board = l_board.Board(l_settings.base_path,(winsize[1],winsize[1]))
    border = l_border.Border(l_settings.base_path)
    in_game_locator = l_in_game_locator.InGameLocator([winw-40,winh-35],[40,35])
    piece_container = l_piece_container.PieceContainer([board.ps[0] + 20,20],[winsize[0]-(board.ps[0]+20)-60,193])
    move_container = l_move_container.MoveContainer([piece_container.position[0],piece_container.position[1]+piece_container.size[1]+20],piece_container.size)
    reset = l_reset.Reset([in_game_locator.position[0]-90,in_game_locator.position[1]],[80,35])
    l_piece.initialize_pieces(board)

def main():
    board.display(screen)
    piece_container.display(screen)
    move_container.display(screen)
    l_piece.process_piece_events(events,board,border,MOUSEMOTION,screen,piece_container,move_container,in_game_locator)
    border.display(screen,board)
    l_piece.display_pieces(screen)
    in_game_locator.render_current_in_game_location(screen,board,l_colors.current_location_font_bounding_box_color,l_colors.current_location_font_color,winw,winh)

    reset.display(screen)
    reset.handle_reset(events)
    if(reset.isresetting):
        reinit()
        reset.isresetting = False

def reinit():
    global board,border,piece_container,move_container,in_game_locator,reset,game_is_running
    game_is_running = False
    del board
    del border
    del piece_container
    del move_container
    del in_game_locator
    l_piece.reinit_processes()
    init() # reinitialize everything
    game_is_running = True

# initialize variables and run the game loop:

init()

while game_is_running:

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