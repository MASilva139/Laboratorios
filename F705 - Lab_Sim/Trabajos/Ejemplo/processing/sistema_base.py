from .cuerpos import Planeta, Luna
import random
import math

class Sistema:
    def __init__(self):
        self.system = []
        
        # Crear el Sol en el centro
        self.sol = Planeta("Sol", 1.989e30, (0, 0))
        self.sol.color = (255, 255, 0)  # Color amarillo para el Sol
        self.system.append(self.sol)

        # Mercurio
        mercurio = Planeta("Mercurio", 3.302e23, (57.909227e9, 0))
        self.system.append(mercurio)

        # Venus
        venus = Planeta("Venus", 4.87e24, (1.08e11, 0))
        self.system.append(venus)

        # Tierra y Luna
        tierra = Planeta("Tierra", 5.97e24, (1.49597870691e11, 0))
        luna = Luna("Luna", 7.347e22, (1.49597870691e11 + 3.844e8, 0), tierra)
        tierra.agregar_luna(luna)
        self.system.append(tierra)
        self.system.append(luna)
        
        # Marte y sus lunas
        marte = Planeta("Marte", 6.4185e23, (2.27936640e11, 0))
        fobos = Luna("Fobos", 1.479e16, (2.27936640e11 + 9.377e6, 0), marte)
        deimos = Luna("Deimos", 1.579e15, (2.27936640e11 + 9.3460e7, 0), marte)
        marte.agregar_luna(fobos)
        marte.agregar_luna(deimos)
        self.system.append(marte)
        self.system.append(fobos)
        self.system.append(deimos)

        # Calcular velocidades orbitales iniciales
        for cuerpo in self.system[1:]:  # Excluir el Sol
            r, theta = cuerpo.coord_polares()
            v_orbital = math.sqrt(self.sol.G() * self.sol.masa / r) * 0.000001  # Factor de escala
            vx = -v_orbital * math.sin(theta)
            vy = v_orbital * math.cos(theta)
            cuerpo._v = [vx, vy]

# Instancia global del sistema
SISTEMA = Sistema()
