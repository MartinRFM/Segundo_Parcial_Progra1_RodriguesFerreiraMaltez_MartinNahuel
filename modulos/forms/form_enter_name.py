import pygame as pg
from .form import Form
from ..widgets import Button, TextBox, TextTitle
from ..variables import DIMENSION_PANTALLA

class FormEnterName(Form):
    '''
    This class represents the enter name form  
    '''
    def __init__(self,name:str,pantalla:object,x:int,y:int,active:bool,level_num:int,music_name:str,score:int)->None:
        super().__init__(name,pantalla,x,y,active,level_num,music_name)

        self.surface = pg.image.load('./assets/img/forms/form_enter_name.png').convert_alpha()
        self.surface = pg.transform.scale(self.surface, DIMENSION_PANTALLA)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.score = score
        
        self.music_update()
        self.confirm_name = False
        
        self.title = TextTitle(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2-200,text="THIS OR THAT",screen=pantalla,font_size=75)
        self.subtitle = TextTitle(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2-90,text="INGRESE SU NOMBRE:",screen=pantalla,font_size=50)
        self.subtitle_score = TextTitle(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2-20,text=f"PUNTAJE:{score}",screen=pantalla,font_size=30)
        
        self.text_box = TextBox(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2+40,text="_________________",screen=pantalla)
        self.button_confirm_name = Button(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2+100,text="CONFIRMAR NOMBRE",screen=pantalla
        ,on_click=self.click_confirm_name)
        
        self.widget_list = [self.title,self.subtitle,self.subtitle_score,self.button_confirm_name]

        
    def click_confirm_name(self,parametro:str)->None: 
        '''
        Sets confirm name flag as True 
        Arguments: parametro (str)  
        Returns: None
        '''  
        self.confirm_name = True
        print(f'Su nombre: {self.writing_text.text} - {self.score} puntos')
        
    def draw(self)->None:
        '''
        Merges the elements of the form with the one from the main screen
        Arguments: None
        Returns: None
        '''
        super().draw()
        for widget in self.widget_list:    
            widget.draw()
        self.text_box.draw()
        self.writing_text  = TextTitle(x=DIMENSION_PANTALLA[0]//2,y=DIMENSION_PANTALLA[1]//2+30,text=f"{self.text_box._wrting.upper()}",
        screen=self.master_surface,font_size=30)
        self.writing_text.draw()

    def update(self,event_list)->None:
        '''
        Executes the methods that need update 
        Arguments: event list (list)
        Returns: None
        '''
        super().draw()
        self.text_box.update(event_list)
        for widget in self.widget_list:    
            widget.update()  
