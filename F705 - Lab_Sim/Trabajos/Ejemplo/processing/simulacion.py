import pygame
import numpy as np
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple
import yaml
import random
from .cuerpos import Planeta, Luna, CuerpoCeleste

class Simulacion:
    def __init__(self, pantalla, config):
        self.pantalla = pantalla
        self.cuerpos = []
        self.ancho, self.alto = pantalla.get_size()
        self.config = config
        self.num_hilos = config['sistema']['num_hilos']
        self.executor = ThreadPoolExecutor(max_workers=self.num_hilos)
        self.lock = threading.Lock()
        self.escala = config['sistema']['escala_distancia']
        self.centro_x = self.ancho // 2
        self.centro_y = self.alto // 2

    def generar_cuerpos(self):
        """Genera cuerpos celestes en paralelo usando coordenadas polares"""
        futures = []
        conteo = self.config['cuerpos']['conteo_inicial']
        
        for _ in range(conteo):
            future = self.executor.submit(self._generar_cuerpo)
            futures.append(future)
        
        for future in futures:
            cuerpo = future.result()
            with self.lock:
                self.cuerpos.append(cuerpo)

    def _generar_cuerpo(self) -> CuerpoCeleste:
        """Genera un único cuerpo celeste con parámetros aleatorios"""
        # Generar masa usando distribución normal
        masa = np.random.normal(
            self.config['distribucion']['masa']['mu'],
            self.config['distribucion']['masa']['sigma']
        )
        masa = abs(masa)  # Asegurar masa positiva

        # Generar posición usando coordenadas polares
        r = random.uniform(
            self.config['distribucion']['posicion']['r_min'],
            self.config['distribucion']['posicion']['r_max']
        )
        theta = random.uniform(0, 2 * np.pi)
        
        # Convertir a coordenadas cartesianas
        x, y = Planeta.polar_a_cart(r, theta)
        x += self.ancho // 2  # Centrar en la pantalla
        y += self.alto // 2

        # Calcular velocidad orbital
        v_base = np.random.normal(
            self.config['distribucion']['velocidad']['mu'],
            self.config['distribucion']['velocidad']['sigma']
        )
        # Velocidad perpendicular para órbita circular
        vx = -v_base * np.sin(theta)
        vy = v_base * np.cos(theta)

        return Planeta(f"Planeta_{len(self.cuerpos)}", masa, (x, y), (vx, vy))

    def calcular_fuerza(self, cuerpo1: CuerpoCeleste, cuerpo2: CuerpoCeleste) -> Tuple[float, float]:
        """Calcula la fuerza gravitacional entre dos cuerpos"""
        dx = cuerpo2._posicion[0] - cuerpo1._posicion[0]
        dy = cuerpo2._posicion[1] - cuerpo1._posicion[1]
        r = np.sqrt(dx**2 + dy**2)
        
        if r == 0:
            return (0, 0)
        
        F = cuerpo1.G() * cuerpo1.masa * cuerpo2.masa / (r**2)
        Fx = F * dx/r
        Fy = F * dy/r
        return (Fx, Fy)

    def calcular_fuerzas_cuerpo(self, indice: int) -> Tuple[int, List[float]]:
        """Calcula las fuerzas totales sobre un cuerpo"""
        cuerpo = self.cuerpos[indice]
        if not cuerpo.activo:
            return indice, [0, 0]

        fuerza_total = [0, 0]
        for j, otro_cuerpo in enumerate(self.cuerpos):
            if indice != j and otro_cuerpo.activo:
                fx, fy = self.calcular_fuerza(cuerpo, otro_cuerpo)
                fuerza_total[0] += fx
                fuerza_total[1] += fy
        return indice, fuerza_total

    def detectar_colisiones(self):
        """Detecta y maneja colisiones entre cuerpos"""
        colisiones = set()
        for i, cuerpo1 in enumerate(self.cuerpos):
            if i in colisiones or not cuerpo1.activo:
                continue
            for j, cuerpo2 in enumerate(self.cuerpos[i+1:], i+1):
                if j in colisiones or not cuerpo2.activo:
                    continue
                    
                dx = cuerpo2.posicion[0] - cuerpo1.posicion[0]
                dy = cuerpo2.posicion[1] - cuerpo1.posicion[1]
                distancia = math.sqrt(dx**2 + dy**2)
                
                if distancia < (cuerpo1.radio + cuerpo2.radio):
                    nuevo_cuerpo = cuerpo1 + cuerpo2
                    cuerpo1.activo = False
                    cuerpo2.activo = False
                    colisiones.add(i)
                    colisiones.add(j)
                    self.cuerpos.append(nuevo_cuerpo)

    def actualizar(self, dt):
        """Actualiza el estado de todos los cuerpos"""
        # Calcular fuerzas en paralelo
        futures = []
        for i in range(len(self.cuerpos)):
            future = self.executor.submit(self.calcular_fuerzas_cuerpo, i)
            futures.append(future)

        # Recopilar resultados y actualizar cuerpos
        for future in futures:
            indice, fuerza_total = future.result()
            self.cuerpos[indice].actualizar(fuerza_total, dt)

        # Detectar colisiones
        self.detectar_colisiones()

        # Limpiar cuerpos inactivos
        self.cuerpos = [c for c in self.cuerpos if c.activo]

    def dibujar(self):
        """Dibuja todos los cuerpos en la pantalla"""
        self.pantalla.fill(tuple(self.config['simulacion']['color_fondo']))
        for cuerpo in self.cuerpos:
            if cuerpo.activo:
                # Escalar y centrar posición para visualización
                pos_x = self.centro_x + cuerpo._posicion[0] * self.escala
                pos_y = self.centro_y + cuerpo._posicion[1] * self.escala
                pos_escalada = (int(pos_x), int(pos_y))
                
                # Convertir trayectoria
                trayectoria_escalada = []
                for x, y in cuerpo.trayectoria[-50:]:
                    x_esc = self.centro_x + x * self.escala
                    y_esc = self.centro_y + y * self.escala
                    trayectoria_escalada.append((int(x_esc), int(y_esc)))
                
                # Dibujar trayectoria
                if len(trayectoria_escalada) > 1:
                    pygame.draw.lines(self.pantalla, cuerpo.color, False, trayectoria_escalada, 2)
                
                # Dibujar cuerpo
                pygame.draw.circle(self.pantalla, cuerpo.color, pos_escalada, cuerpo.radio)

    def __del__(self):
        """Limpia recursos al destruir la instancia"""
        self.executor.shutdown()
