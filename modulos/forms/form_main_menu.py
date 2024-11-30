import pygame as pg
from .form import Form
from ..widgets import (
    Button, TextTitle
)
from ..variables import DIMENSION_PANTALLA

class FormMainMenu(Form):
    
    def __init__(self, name, pantalla, x, y, active, level_num, music_path):
        super().__init__(name, pantalla, x, y, active, level_num, music_path)
        
        self.start_first_level = False
        
        # Actualizar la musica aca
        self.music_update()
        
        self.surface = pg.image.load('assets/img/forms/MENU.jpg').convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        self.menu_ppal_title = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-200, texto='THIS OR THAT', pantalla=pantalla, font_size=75)
        self.menu_ppal_subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2-150, texto='MENU PRINCIPAL', pantalla=pantalla, font_size=50)
        
        
        self.button_start = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2, texto='COMENZAR', pantalla=pantalla, on_click=self.click_start)
        # self.button_level_select = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2, texto='SELECCIONAR NIVEL', pantalla=pantalla, on_click=self.click_level_select, on_click_param='form_level_select')
        self.button_options = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+75, texto='OPCIONES', pantalla=pantalla, on_click=self.click_option, on_click_param='form_options')
        self.button_rankings = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+150, texto='RANKING', pantalla=pantalla, on_click=self.click_ranking, on_click_param='form_rankings')
        self.button_exit = Button(x=DIMENSION_PANTALLA[0]//2, y=DIMENSION_PANTALLA[1]//2+225, texto='EXIT', pantalla=pantalla, on_click=self.click_exit)

        self.widget_list = [
            self.menu_ppal_subtitle, self.menu_ppal_title, self.button_exit, #self.button_level_select,
            self.button_options, self.button_rankings, self.button_start
        ]
    
    def click_start(self, parametro):
        self.start_first_level = True
    
    def click_level_select(self, parametro):
        self.set_active(parametro)
    
    def click_option(self, parametro):
        self.set_active(parametro)
    
    def click_exit(self, parametro):
        self.set_active(parametro)
    
    def click_ranking(self, parametro):
        self.set_active(parametro)
    
    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()
    
    def update(self):
        self.draw()
        for widget in self.widget_list:
            widget.update()