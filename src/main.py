from typing import Any
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
winw = 1000
winh = 600
winsize = (winw, winh)
screen = pygame.display.set_mode(winsize)
pygame.display.set_caption(l_settings.game_name)
try:
    pygame.display.set_icon(pygame.image.load(os.path.join(l_settings.base_path,l_settings.game_icon_path)))
except:
    raise Exception("Unable to load game icon.")
try:
    initialized_font = pygame.font.SysFont(l_font.font_name_path , l_font.font_size)
except:
    raise Exception("Unable to load font.")

clock = pygame.time.Clock()

def quit_game():
    pygame.quit()
    l_font.pquit()
    l_audio.pquit()
    quit()

# game variables
piece_is_held = False
offsetx,offsety = 0,0
attached_pieces = []

def move_piece():
    global piece_is_held,offsetx,offsety,attached_pieces
    mousepos = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    for e in events:
        for p in pieces:
            if((mousepos[0] > p.position[0] and mousepos[0] < (p.position[0]+board.isps)) and (mousepos[1] > p.position[1] and mousepos[1] < (p.position[1]+board.isps))):
                if pressed[0] and not piece_is_held:
                    piece_is_held = True
                    if len(attached_pieces) < 1:
                        attached_pieces.append(p)
                    offsetx = (mousepos[0]-attached_pieces[0].position[0])
                    offsety = (mousepos[1]-attached_pieces[0].position[1])
                    # piece_prev_pos[0] = p.position[0]
                    # piece_prev_pos[1] = p.position[1]
                if not pressed[0] and piece_is_held:      
                        piece_is_held = False
                        attached_pieces[0].position[0] = border.position[0]
                        attached_pieces[0].position[1] = border.position[1] # wierd but works lmao
                        attached_pieces.pop(0)
                        offsetx,offsety = 0,0
                        l_audio.play(4,0)
        if e.type == MOUSEMOTION and piece_is_held:
                    attached_pieces[0].position[0] = mousepos[0]-offsetx
                    attached_pieces[0].position[1] = mousepos[1]-offsety

def initialize_pieces(): # very performance heavy!
    global pieces

    pieces = []

    for x in range(len(board.xblocks)):
        for y in range(len(board.yblocks)):
            if(board.char_board[y+(x*8)] == 'e'):
                continue
            elif(board.char_board[y+(x*8)] == 'P'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'P'))
            elif(board.char_board[y+(x*8)] == 'R'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'R'))
            elif(board.char_board[y+(x*8)] == 'N'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'N'))
            elif(board.char_board[y+(x*8)] == 'B'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'B'))
            elif(board.char_board[y+(x*8)] == 'Q'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'Q'))
            elif(board.char_board[y+(x*8)] == 'K'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'K'))
            elif(board.char_board[y+(x*8)] == 'p'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'p'))
            elif(board.char_board[y+(x*8)] == 'r'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'r'))
            elif(board.char_board[y+(x*8)] == 'n'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'n'))
            elif(board.char_board[y+(x*8)] == 'b'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'b'))
            elif(board.char_board[y+(x*8)] == 'q'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'q'))
            elif(board.char_board[y+(x*8)] == 'k'):
                pieces.append(l_piece.Piece([y*board.isps,x*board.isps],l_settings.base_path,'k'))

def display_pieces(): # i haven't looped all this nonsense because of readablility issues
    for x in pieces:
        x.display(screen)

def init():
    global board,border

    l_audio.play(0,0) #play start sound
    board = l_board.Board(l_settings.base_path,(winsize[1],winsize[1]))
    border = l_border.Border(l_settings.base_path)
    initialize_pieces()

def main():
    board.display(screen)
    border.display(screen,board)
    move_piece()
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