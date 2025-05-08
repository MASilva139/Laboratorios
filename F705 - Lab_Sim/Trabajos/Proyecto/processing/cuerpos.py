from .obj_fisico import propiedadesfisicas, propiedadesvisuales
from abc import ABC, abstractmethod
from sistema_base import sistema
import math
import numpy as np
import threading

datos = sistema()

class CuerpoCeleste(propiedadesfisicas, propiedadesvisuales, ABC):
    def __init__(self, nombre, masa, posicion, v):
        propiedadesfisicas.__init__(self, masa, posicion, v)
        propiedadesvisuales.__init__(self)
        self.nombre = nombre
        self._radio = max(5, int(math.log(masa)/22)) if masa > 0 else 5

    @abstractmethod
    def obtener_inf(self):
        pass
    
    def coord_polares(self):
        x, y = self._posicion
        r = math.sqrt(x**2 + y**2)
        theta = np.random.uniform(0, 2*np.pi)
        return r, theta
    
    def _vel_orbital(self):     # Velocidad tangencial F=GMm/r^2 -> F=mv^2/r
        r, _ = self.coord_polares()
        return math.sqrt(CuerpoCeleste.G() * self._masa / r)

class Planeta(CuerpoCeleste):
    def __init__(self, nombre, masa, posicion, v=(0, 0)):
        super().__init__(nombre, masa, posicion, v)
        self.lunas = []

    def obtener_inf(self):
        return (
            f"Planeta: {self.nombre}\n"
            f"Masa: {self._masa:.2e} [kg]/n"
            f"Radio: {self._radio/1000:.2f} [km]\n"
        )
    def agregar_luna(self, luna):
        # Se utiliza isinstance para verificar si luna pertenece a la clase Luna
        self.lunas.append(luna)

class Luna(CuerpoCeleste):
    def __init__(self, nombre, masa, posicion, planeta, v=(0, 0)):
        super().__init__(nombre, masa, posicion, v)
        self.planeta = planeta
