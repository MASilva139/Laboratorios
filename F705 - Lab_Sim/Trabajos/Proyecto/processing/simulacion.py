from multiprocessing import Pool
import math
import pygame
from sistema_base import sistema
from config import WIDTH, HEIGHT, BACKGROUND_COLOR
from cuerpos import Planeta

datos = sistema()

class SimulacionG:
    def __init__(self):
        self.cuerpos = []
        self.inicializar_objetos()

    def inicializar_objetos(self):
        self.objetos.append

    def F():
        fuerzas = {}
        for i, objeto_i in enumerate(self.objetos):
            if not objeto_i.activo:
                continue
            F_Total = [0, 0]
            for j, objeto_j in enumerate(self.objetos):
                if i == j or not objeto_j.activo:
                    continue
                dx = objeto_j.posicion[0] - objeto_i.posicion[0]
                dy = objeto_j.posicion[1] - objeto_i.posicion[1]
                rij = matl.sqrt(dx**2 + dy**2) + 1e-5
                fuerza = G*objeto_i.masa*objeto_j.masa / (rij**2)
                theta = math.atan2(dy, dx)
                F_Total[0] += fuerza*math.cos(theta)
                F_Total[1] += fuerza*math.sin(theta)
            fuerzas[i] = F_Total
        return fuerzas

    def colisiones(self):
        cuerpos_new = []
        procesados =  set()

        for i, cuerpo_i in enumerate(self.cuerpos):
            if i in procesados or not cuerpo_i.activo:
                continue
            for j, cuerpo_j in enumerate(self.cuerpos):
                cuerpo_j = self.cuerpos[j]
                if j in procesados or not cuerpo_j.activo:
                    continue
                dx = cuerpo_j.posicion[0] - cuerpo_i.posicion[0]
                dy = cuerpo_j.posicion[1] - cuerpo_i.posicion[1]
                rij = math.sqrt((dx**2)+(dy**2))

                if rij < (cuerpo_i.r + cuerpo_j.r):
                    masa_total = cuerpo_i.masa + objeto_j.masa
                    v_x = (cuerpo_i.v[0] * cuerpo_i.masa + cuerpo_j.v[0]*cuerpo_j.masa)/(masa_total)
                    v_y = (cuerpo_i.v[1] * cuerpo_i.masa + cuerpo_j.v[1]*cuerpo_j.masa)/(masa_total)
                    posicion_n = (
                        (cuerpo_i.posicion[0] + cuerpo_j.posicion[0])/2,
                        (cuerpo_i.posicion[1] + cuerpo_j.posicion[1])/2 
                    )
                    cuerpo_new = 
                    cuerpos_new.append(cuerpo_n)
                    procesados.add(i)
                    procesados.add(j)
        self.cuerpos = [cuerpo for idx, cuerpo in enumerate(self.cuerpos) if idx not in procesados and cuerpo.activo]
        self.cuerpos.extend(cuerpos_new)
    
    def actualizar(self, dt):
        fuerzas = self.F()
        for idx, fuerza in fuerzas.items():
            self.cuerpos[idx].Force(fuerza, dt)
        self.colisiones()
    
    def dibujar(self, pantalla):
        pantalla.fill(BACKGROUND_COLOR)
        for cuerpo in self.cuerpos:
            if cuerpo.cativo:
                cuerpo.dibujar(pantalla)
        pygame.display.flip()
