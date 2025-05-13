import math
import pygame
import random
import numpy as np
from abc import ABC, abstractmethod

class PropiedadesFisicas(ABC):
    def __init__(self, masa, posicion, v=(0, 0)):
        self._masa = masa
        self._posicion = list(posicion)
        self._v = list(v)
        self.trayectoria = [tuple(posicion)]
        self.activo = True

    @property
    def masa(self):
        return self._masa

    @property
    def posicion(self):
        return tuple(self._posicion)

    @property
    def velocidad(self):
        return tuple(self._v)

    @staticmethod
    def G():
        return 6.67430e-11  # [(N*m^2)/kg^2]

    def actualizar(self, fuerza, dt):
        """Actualiza la posición y velocidad del cuerpo"""
        ax = fuerza[0]/self._masa
        ay = fuerza[1]/self._masa
        self._v[0] += ax * dt
        self._v[1] += ay * dt
        self._posicion[0] += self._v[0] * dt
        self._posicion[1] += self._v[1] * dt
        self.trayectoria.append((self._posicion[0], self._posicion[1]))
        if len(self.trayectoria) > 1000:
            self.trayectoria = self.trayectoria[1:]

    def coord_polares(self):
        """Convierte las coordenadas cartesianas actuales a polares"""
        x, y = self._posicion
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        return r, theta

    @staticmethod
    def cart_a_polar(x, y):
        """Convierte coordenadas cartesianas a polares"""
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        return r, theta

    @staticmethod
    def polar_a_cart(r, theta):
        """Convierte coordenadas polares a cartesianas"""
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        return x, y

class PropiedadesVisuales:
    def __init__(self):
        self._color = self._generar_color()
        self._forma = random.choice(["circulo", "cuadrado", "triangulo"])
        self._radio = 5

    def _generar_color(self):
        """Genera un color RGB aleatorio"""
        return (random.randint(50, 255),
                random.randint(50, 255),
                random.randint(50, 255))

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nuevo_color):
        if isinstance(nuevo_color, (list, tuple)) and len(nuevo_color) == 3:
            self._color = tuple(nuevo_color)

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        self._radio = max(5, valor)

    def dibujar(self, pantalla):
        """Dibuja el cuerpo celeste y su trayectoria"""
        # Dibujar trayectoria
        if len(self.trayectoria) > 1:
            puntos = [(int(x), int(y)) for x, y in self.trayectoria[-50:]]
            pygame.draw.lines(pantalla, self._color, False, puntos, 2)

        # Dibujar cuerpo
        x, y = int(self._posicion[0]), int(self._posicion[1])
        if self._forma == "circulo":
            pygame.draw.circle(pantalla, self._color, (x, y), self._radio)
        elif self._forma == "cuadrado":
            rect = pygame.Rect(x - self._radio, y - self._radio, 
                             self._radio*2, self._radio*2)
            pygame.draw.rect(pantalla, self._color, rect)
        elif self._forma == "triangulo":
            puntos = [
                (x, y - self._radio),
                (x - self._radio, y + self._radio),
                (x + self._radio, y + self._radio)
            ]
            pygame.draw.polygon(pantalla, self._color, puntos)
