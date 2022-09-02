def render_text(screen,initialized_font,antialiasing,x,y,text,color):
    rendered_font = initialized_font.render(text,antialiasing,color)#therenderedfont
    screen.blit(rendered_font,(x,y))