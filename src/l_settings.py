import os

game_name = 'Chess'
game_icon_path = '../images/Logo.png'
screen_is_resizable = False
master_audio_volume = 1
font_antialiasing = True
base_path = os.path.dirname(__file__)
infinite_fps = False
base_fps = 120

#########################
if infinite_fps:
    fps = 1000
else:
    fps = 120