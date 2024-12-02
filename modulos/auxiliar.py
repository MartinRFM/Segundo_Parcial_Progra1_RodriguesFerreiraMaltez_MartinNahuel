import pygame as pg

from .variables import (
    RUTA_FONDO, PUNTOS, 
    
)

def achicar_imagen(ruta_imagen: str, cantidad: int) -> pg.Surface:
    imagen_raw = pg.image.load(ruta_imagen)
    alto = imagen_raw.get_height() // cantidad
    ancho = imagen_raw.get_width() // cantidad
    imagen_final = pg.transform.scale(imagen_raw, (ancho, alto))
    return imagen_final

def crear_diccionario_item(sup_imagen: pg.Surface, sup_rect: pg.Rect) -> dict:
    objeto = {
        "imagen": sup_imagen,
        "rect": sup_rect,
        "visible": True
    }
    return objeto

def sort_matrix(matrix: list[list]):
    
    for i in range(len(matrix) - 1):
        for j in range(i+1, len(matrix)):
            if int(matrix[i][1]) < int(matrix[j][1]):
                matrix[i], matrix[j] =\
                matrix[j], matrix[i]
                
def grabar_puntaje(jugador):
    with open(PUNTOS, '+a') as rkn:
        rkn.write(jugador.to_csv_format())
        print('PUNTAJE GUARDADO CON ÉXITO!')

def cargar_ranking():
    ranking = []
    with open(PUNTOS, 'r') as rkng:
        lineas = rkng.read()
        for linea in lineas.split('\n'):
            ranking.append(linea.split(','))
    
    sort_matrix(ranking)
    
    return ranking


fondo_raw = pg.image.load(RUTA_FONDO)
fondo = pg.transform.scale(fondo_raw, (800, 600))

fuente_sn = pg.font.Font('./assets/fonts/Impact.ttf', 40)
fuente_cn = pg.font.Font('./assets/fonts/Sufinter.otf', 40)
