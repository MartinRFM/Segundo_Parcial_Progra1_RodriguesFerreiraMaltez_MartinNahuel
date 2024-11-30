import pygame.mixer as mixer
class Sonido:
    
    def __init__(self):
        mixer.init()

    def play_sonido(self, ruta_snd: str):
        sonido = mixer.Sound(ruta_snd)
        sonido.set_volume(0.8)
        sonido.play()
    
    def play_musica(self, ruta_musica: str):
        mixer.music.load(ruta_musica)
        mixer.music.set_volume(0.6)
        mixer.music.play()
    
    def stop_musica(self):
        mixer.music.fadeout(500)
        # mixer.music.stop()
        