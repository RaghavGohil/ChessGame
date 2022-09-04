from pygame import mixer
import l_settings

mixer.init()

mixer.music.set_volume(l_settings.master_audio_volume)



def play(sound):
    mixer.Sound(sound).play()
    
def pquit():
    mixer.quit()