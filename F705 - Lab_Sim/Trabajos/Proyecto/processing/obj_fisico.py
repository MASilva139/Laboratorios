import numpy as np
from math import sqrt, atan2
import pygame
import random

class propiedadesfisicas:
    def __init__(self, masa, posicion, v):
        self._masa = masa
        self._posicion = list(posicion)
        self._v = list(v)
        self.r = math.log(masa) if masa > 0 else 1 # Relación entre masa y radio
        self.trayectoria = [tuple(posicion)]
        self.activo = True

    def Force(self, fuerza, dt):
        ax = fuerza[0]/self._masa
        ay = fuerza[1]/self._masa
        self._v[0] += ax * dt
        self._v[1] += ay * dt
        self._posicion[0] += self._v[0] * dt
        self._posicion[1] += self._v[1] * dt
        self.trayectoria.append((self._posicion[0], self._posicion[1]))
        temp_trayectoria = []
        if len(self.trayectoria) > 1000:
            temp_trayectoria = self.trayectoria[1:]
            self.trayectoria = temp_trayectoria
            # print(self.trayectoria)

class propiedadesvisuales:
    def __init__(self, color, forma):
        self.color = color
        self.forma = forma

    def draw(self, pantalla):
        if len(self.trayectoria) > 1:
            puntos = [(int(x), int(y)) for x, y in self.trayectoria[-50:]]
            pygame.draw.lines(pantalla, self.color, False, puntos, 2)
        x, y = int(self._posicion[0]), int(self._posicion[1])
        if self.forma == "circulo":
            pygame.draw.circle(pantalla, self.color, (x, y), self.r)
        elif self.forma == "cuadrado":
            rect = pygame.Rect(x - self.r, y - self.r, self.r*2, self.r*2)
            pygame.draw.rect(pantalla, self.color, rect)
        elif self.forma == "triangulo":
            puntos = [
                (x, y - self.r),
                (x - self.r, y + self.r),
                (x + self.r, y + self.r)
            ]
            pygame.draw.polygon(pantalla, self.color, puntos)
