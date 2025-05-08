import numpy as np
from math import sqrt, atan2
import pygame
import random
from abc import ABC, abstractmethod
from sistema_base import sistema

class propiedadesfisicas:
    def __init__(self, masa, posicion, v):
        self.masa = masa
        self.posicion = list(posicion)
        self.v = list(v)
        self.r = math.log(masa) if masa > 0 else 1 # Relación entre masa y radio
        self.trayectoria = [tuple(posicion)]
        self.activo = true

    @staticmethod
    def G():
        return 6.67430e-11 # Unidades en [(N*m^2)/kg^2]

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
    def _init__(self, color, forma):
        self.color = (random.radint(0, 255), random.radint(0, 255), random.radint(0, 255)) # Asignando a cada planeta/estrella un color aleatorio RGB
        self.forma = random.choice(['circulo', 'cuadrado', 'triangulo'])

    def draw(self, pantalla):
        if len(self.trayectoria) > 1:
            puntos = [(int(x), int(y)) for x, y in self.trayectoria[-50:]]
            pygame.draw.lines(pantalla, self.color, False, puntos, 2)
        x, y = int(self._posicion[0]), int(self._posicion[1])
        if self.forma == "circulo":
            pygame.draw.circle(pantalla, self.color, (x, y), self.radio)
        elif self.forma == "cuadrado":
            rect = pygame.Rect(x-self.radio, y-self.radio, self.radio*2, self.radio*2)
            pygame.draw.rect(pantalla, self.color, rect)
        elif self.forma == "triangulo":
            puntos = [
                (x, y-self.radio),
                (x-self.radio, y+self.radio),
                (x+self.radio, y+self.radio)
            ]
            pygame.draw.polygon(pantalla, self.color, puntos)
