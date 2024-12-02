import pygame as pg


class Jugador:
    
    __instanciado = None
    
    def __init__(self, _):
        
        if Jugador.__instanciado is None:
            Jugador.__instanciado = self
        
        self.puntaje = 0
        self.puntaje_total = 0
    
    @staticmethod
    def get_jugador():
        if Jugador.__instanciado is None:
            Jugador()
        return Jugador.__instanciado
    
    @staticmethod
    def esta_instanciado():
        return Jugador.__instanciado != None
    
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre
    
    def get_puntaje_actual(self):
        return self.puntaje
    
    def get_puntaje_total(self):
        return self.puntaje_total
    
    def set_puntaje(self, puntaje: int):
        self.puntaje = puntaje
    
    def add_puntaje(self, puntaje: int):
        self.puntaje += puntaje
    
    def actualizar_puntaje_total(self):
        self.puntaje_total += self.puntaje
    
    def to_csv_format(self):
        return f'\n{self.nombre},{self.puntaje_total}'
    
    def events(self, lista_eventos: list):
        
        for evento in lista_eventos:
            if evento.type == pg.KEYDOWN:
                if lista_eventos[pg.K_LEFT]:
                    self.rect.x -= 2
                if lista_eventos[pg.K_RIGHT]:
                    self.rect.x += 2
                if lista_eventos[pg.K_UP]:
                    self.rect.y -= 2
                if lista_eventos[pg.K_DOWN]:
                    self.rect.y += 2
    
    def draw(self, screen):
        screen.blit(self.imagen, self.rect)
    
    def update(self, lista_eventos):
        self.events(lista_eventos)
        
        