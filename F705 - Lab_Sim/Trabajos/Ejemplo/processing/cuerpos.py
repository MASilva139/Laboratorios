from .obj_fisico import PropiedadesFisicas, PropiedadesVisuales
import math
import numpy as np

class CuerpoCeleste(PropiedadesFisicas, PropiedadesVisuales):
    def __init__(self, nombre, masa, posicion, v=(0, 0)):
        PropiedadesFisicas.__init__(self, masa, posicion, v)
        PropiedadesVisuales.__init__(self)
        self.nombre = nombre
        self.radio = max(5, int(math.log(masa)/22)) if masa > 0 else 5

    def obtener_inf(self):
        """Método abstracto para obtener información del cuerpo"""
        pass

    def __str__(self):
        """Sobrecarga del método str"""
        return f"{self.nombre} (masa={self.masa:.2e} kg)"

    def __add__(self, otro):
        """Sobrecarga del operador + para combinar cuerpos en colisiones"""
        if isinstance(otro, CuerpoCeleste):
            nueva_masa = self.masa + otro.masa
            # Conservación del momento lineal
            vx = (self.masa * self._v[0] + otro.masa * otro._v[0]) / nueva_masa
            vy = (self.masa * self._v[1] + otro.masa * otro._v[1]) / nueva_masa
            # Posición del centro de masa
            x = (self.masa * self._posicion[0] + otro.masa * otro._posicion[0]) / nueva_masa
            y = (self.masa * self._posicion[1] + otro.masa * otro._posicion[1]) / nueva_masa
            
            return Planeta(f"{self.nombre}+{otro.nombre}", nueva_masa, (x, y), (vx, vy))
        return NotImplemented

class Planeta(CuerpoCeleste):
    def __init__(self, nombre, masa, posicion, v=(0, 0)):
        super().__init__(nombre, masa, posicion, v)
        self.lunas = []  # Agregación de lunas

    def obtener_inf(self):
        """Implementación del método abstracto"""
        return (
            f"Planeta: {self.nombre}\n"
            f"Masa: {self.masa:.2e} [kg]\n"
            f"Radio: {self.radio/1000:.2f} [km]\n"
            f"Lunas: {len(self.lunas)}"
        )

    def agregar_luna(self, luna):
        """Agrega una luna al planeta"""
        if isinstance(luna, Luna):
            self.lunas.append(luna)
            return True
        return False

class Luna(CuerpoCeleste):
    def __init__(self, nombre, masa, posicion, planeta, v=(0, 0)):
        super().__init__(nombre, masa, posicion, v)
        self.planeta = planeta
        self.radio = max(3, int(math.log(masa)/25))  # Lunas más pequeñas

    def obtener_inf(self):
        """Implementación del método abstracto"""
        return (
            f"Luna: {self.nombre}\n"
            f"Planeta: {self.planeta.nombre}\n"
            f"Masa: {self.masa:.2e} [kg]\n"
            f"Radio: {self.radio/1000:.2f} [km]"
        )
