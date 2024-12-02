import sys
import pygame as pg
from .form import Form
from ..widgets import (
    Button, TextTitle
)
from ..variables import DIMENSION_PANTALLA

class FormGame(Form):
    
    def __init__(self, name, pantalla, x, y, active, level_num, music_path):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
    
        self.music_update()
        
        self.start_first_level = True
        
        self.surface = pg.image.load('assets/img/forms/certamen.png').convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        
        self.optiones_title = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-250, texto='THIS OR THAT', pantalla=pantalla, font_size=90)

        self.button_exit = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+225, texto='EXIT', pantalla=pantalla, on_click=self.click_exit)
        self.button_pause = Button( x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+175, texto='PAUSE', pantalla=pantalla, on_click=self.click_pause, on_click_param='form_pause')
        
        self.widgets_list = [
            self.button_exit, self.button_pause
        ]
    
    
    def click_pause(self): 
        self.set_active('form_pause')  

    def click_exit(_): 
        sys.exit()
    
    def draw(self):
        super().draw()
        for widget in self.widgets_list:
            widget.draw()
        
    def update(self):
        super().draw()
        for widget in self.widgets_list:
            widget.update()