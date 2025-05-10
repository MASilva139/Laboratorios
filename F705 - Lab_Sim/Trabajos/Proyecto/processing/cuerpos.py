from processing.obj_fisico import propiedadesfisicas, propiedadesvisuales
from abc import ABC, abstractmethod
import math
import numpy as np

class CuerpoCeleste(propiedadesfisicas, propiedadesvisuales, ABC):
    def __init__(self, nombre, masa, posicion, v=(0, 0)):
        propiedadesfisicas.__init__(self, masa, posicion, v)
        propiedadesvisuales.__init__(self)
        self.nombre = nombre

    @abstractmethod
    def obtener_inf(self):
        pass

class Planeta(CuerpoCeleste):
    def __init__(self, nombre, masa, posicion, v=(0, 0)):
        super().__init__(nombre, masa, posicion, v)

    def obtener_inf(self):
        return (
            f"Planeta: {self.nombre}\n"
            f"Masa: {self._masa:.2e} [kg]/n"
            f"Radio: {self._radio/1000:.2f} [km]\n"
        )

class Luna(CuerpoCeleste):
    def __init__(self, nombre, masa, posicion, planeta, v=(0, 0)):
        super().__init__(nombre, masa, posicion, v)
        self.planeta = planeta
