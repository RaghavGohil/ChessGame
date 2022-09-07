import pygame

pygame.font.init()

font_size = 35
font_name_path = '../fonts/TheleahFat.ttf'
font_antialiasing = True

def render_text(screen:pygame.Surface,initialized_font:pygame.sysfont,antialiasing:bool,x:int,y:int,text:str,color:tuple): # render text on desired location on the screen
    rendered_font = initialized_font.render(text,antialiasing,color) # therenderedfont
    screen.blit(rendered_font,(x,y))

def pquit(): #pquit stands for pygame quit
    pygame.font.quit()