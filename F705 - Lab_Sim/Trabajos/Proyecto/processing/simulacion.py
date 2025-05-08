from multiprocessing import Pool
import pygame

datos = sistema()

class SimulacionG:
    def __init__(self, cuerpos: List[CuerpoCeleste], tamaño_pantalla: tuple):
        self.cuerpos = cuerpos
        self.pantalla_ancho, self.pantalla_alto = tamaño_pantalla

    def _fuerzas(self):
        for i, cuerpo01 in enumerate(self.cuerpos):
            for cuerpo02 in self.cuerpos[i+1:]:
                dx = cuerpo02.posicion[0] - cuerpo01.posicion[0]
                dy = cuerpo02.posicion[1] - cuerpo01.posicion[1]
                r = sqrt(dx**2 + dy**2)

                if r == 0:
                    continue

                fuerza = (self.G() * cuerpo01._masa * cuerpo02._masa)/(r**2)
