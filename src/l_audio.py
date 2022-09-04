from pygame import mixer
import os

import l_settings

mixer.init()

mixer.music.set_volume(l_settings.master_audio_volume)

# music (paths)

location_select = os.path.join(l_settings.base_path,'../audio/LocationSelect.wav')
move_piece = os.path.join(l_settings.base_path,'')
eat_piece = os.path.join(l_settings.base_path,'')

audio_playlist = [

    location_select,
    move_piece,
    eat_piece,

]

def play(i,mode): # play at index from the playlist (mode specifies if provided audio is music or sound)
    for x in range(len(audio_playlist)):
        if(i == x):
            if(mode == 0):
                play_sound(audio_playlist[x])
            elif(mode == 1):
                play_music(audio_playlist[x])
            else:
                raise Exception("Invalid audio mode.")
            return
    raise Exception("Audio file cannot be played.")

def play_sound(soundpath):
    mixer.Sound(soundpath).play()

def play_music(musicpath):
    mixer.music.load(musicpath)
    mixer.music.play()

def pquit():
    mixer.quit()