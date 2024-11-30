import pygame as pg
from .form import Form
from ..widgets import (
    Button, TextTitle
)
from ..variables import DIMENSION_PANTALLA

class FormOptions(Form):
    
    def __init__(self, name, pantalla, x, y, active, level_num, music_path):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
        
        self.surface = pg.image.load('assets/img/forms/form_options.png').convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        self.optiones_title = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-200, texto='THIS OR THAT', pantalla=pantalla, font_size=75)
        self.optiones_subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-150, texto='OPCIONES', pantalla=pantalla, font_size=50)
        
        self.button_music_on = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-70, texto='ACTIVAR MUSICA', pantalla=pantalla, on_click=self.click_music_on)
        self.button_music_off = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+70, texto='DESACTIVAR MUSICA', pantalla=pantalla, on_click=self.click_music_off)
        
        self.button_back = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+250, texto='VOLVER AL MENU PRINCIPAL', pantalla=pantalla, on_click=self.click_back, on_click_param='form_main_menu')
        self.widgets_list = [
            self.optiones_subtitle, self.optiones_title,
            self.button_back, self.button_music_off,
            self.button_music_on
        ]
        self.music_update()
        
    def click_music_on(self, parametro):
        pg.mixer.music.unpause()
    
    def click_music_off(self, parametro):
        pg.mixer.music.pause()
    
    def click_back(self, parametro):
        self.set_active(parametro)
    
    def draw(self):
        super().draw()
        for widget in self.widgets_list:
            widget.draw()
        
    def update(self):
        super().draw()
        for widget in self.widgets_list:
            widget.update()