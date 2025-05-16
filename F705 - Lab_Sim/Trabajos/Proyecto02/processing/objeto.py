import numpy as np
import math
import pygame
import random
import yaml
import os #ruta absoluta para llamar al .yaml
from multiprocessing import Pool

config_path = "config.yaml"
# config_path = os.path.join(os.path.dirname(__file__), "..", "config.yaml")
# config_path = os.path.abspath(config_path)

#<<<<<<<<<<<<<Parametros a usar<<<<<<<<<<<<<<<<<<<<<<
with open(config_path) as f:
    import yaml
    config = yaml.safe_load(f)
N = config["parametros"]["N"]
Lx = config["parametros"]["Lx"]
Ly = config["parametros"]["Ly"]
mu = config["parametros"]["mu"]
G = config["parametros"]["G"]
J = config["parametros"]["J"]
sigma = config["parametros"]["sigma"]
dt1 = config["parametros"]["dt1"]

#<<<<<<<<<<<<<<<<caracteristicas del cuerpo<<<<<<<<<<<
class propiedades_fisica:
    def __init__(self):
        self.masa = random.normalvariate(mu,sigma)
        self.posicion = list([random.uniform(1, Lx - 1), random.uniform(1, Ly - 1)])
        self.v = list([0,0])
        self.r = J*(self.masa)**(1/3) # Relación entre masa y radio
        self.trayectoria = [tuple(self.posicion)]
        self.activo = True

class propiedades_visuales:
    def __init__(self):
        self.color = (random.randint(180,255),random.randint(180,255),random.randint(180,255))
        self.forma = random.randint(1,3)

    def draw(self, pantalla):
        x, y = int(self.posicion[0]), int(self.posicion[1])
        r = int(self.r)

        if self.forma == 1:
            pygame.draw.circle(pantalla, self.color, (x, y), r)
        elif self.forma == 2:
            rect = pygame.Rect(x - r, y - r, r*2, r*2)
            pygame.draw.rect(pantalla, self.color, rect)
        elif self.forma == 3:
            puntos = [
                (x, y - r),
                (x - r, y + r),
                (x + r, y + r)
            ]
            pygame.draw.polygon(pantalla, self.color, puntos)
        else:
            # Valor inesperado, dibuja un punto para no fallar
            #El metodo que usé puede fallar!
            pygame.draw.circle(pantalla, (0,0,0), (x, y), 2)

#<<<<<<<<<<<Herencia para definir la particula<<<<<<<<<<<
class Particula(propiedades_fisica, propiedades_visuales):  #Tiene integrado un metodo de fuerza.
    def __init__(self):
        propiedades_fisica.__init__(self)
        propiedades_visuales.__init__(self)

    def Force(self, fuerza, dt):
        ax = fuerza[0]/self.masa
        ay = fuerza[1]/self.masa
        self.v[0] += ax * dt
        self.v[1] += ay * dt
        self.posicion[0] += self.v[0] * dt
        self.posicion[1] += self.v[1] * dt
        self.trayectoria.append((self.posicion[0], self.posicion[1]))
        temp_trayectoria = []
        if len(self.trayectoria) > 1000:
            temp_trayectoria = self.trayectoria[1:]
            self.trayectoria = temp_trayectoria
            # self.trayectoria.pop(0)

def generar_particula(_):
    return Particula()

class SIMULADOR:
    def __init__(self):
        self.objetos = []
        self.inicializar_objetos()

    def inicializar_objetos(self):
        # for i in range(N):
        #     self.objetos.append(Particula())

        # Forma 02
        with Pool() as pool:
            self.objetos = pool.map(generar_particula, range(N))
    
    
    #<<<<<<<<<<<<<<<<<<<<<<<<< Forma 01 >>>>>>>>>>>>>>>>>>>#
    # No se considera el multiprocessing
    def calcular_fuerzas(self): # Cada i-esimo elemento de esta lista es para cada i-esima particula
        fuerzas = {}
        for i in range(len(self.objetos)): 
            if not self.objetos[i].activo:
                continue
            fuerzas[i] = [0, 0]
            for j in range(len(self.objetos)):
                if i == j or not self.objetos[j].activo:
                    continue
                dx = self.objetos[j].posicion[0] - self.objetos[i].posicion[0]
                dy = self.objetos[j].posicion[1] - self.objetos[i].posicion[1]
                distancia = math.hypot(dx, dy) + 1e-3  # Evitar división por cero
                
                fuerza = G * self.objetos[i].masa * self.objetos[j].masa / (distancia**2)
                angulo = math.atan2(dy, dx)
                
                fuerzas[i][0] += fuerza * math.cos(angulo)
                fuerzas[i][1] += fuerza * math.sin(angulo)
        return fuerzas

    def detectar_colisiones(self):
        nuevos_objetos = []
        procesados = set()
        
        for i in range(len(self.objetos)):
            if i in procesados or not self.objetos[i].activo:
                continue
            
            for j in range(i+1, len(self.objetos)):
                if j in procesados or not self.objetos[j].activo:
                    continue
                
                dx = self.objetos[j].posicion[0] - self.objetos[i].posicion[0]
                dy = self.objetos[j].posicion[1] - self.objetos[i].posicion[1]
                distancia = math.hypot(dx, dy)
                
                if distancia < (self.objetos[i].r + self.objetos[j].r):
                    masa_total = self.objetos[i].masa + self.objetos[j].masa
                    # Conservación del momento lineal
                    vel_x = (self.objetos[i].v[0] * self.objetos[i].masa + 
                            self.objetos[j].v[0] * self.objetos[j].masa) / masa_total
                    vel_y = (self.objetos[i].v[1] * self.objetos[i].masa + 
                            self.objetos[j].v[1] * self.objetos[j].masa) / masa_total
                    # Crea la nueva particula luego del choque
                    nuevo = Particula()
                    nuevo.masa=masa_total
                    nuevo.r= J*(nuevo.masa)**(1/3)
                    nuevo.posicion=[(self.objetos[i].posicion[0] + self.objetos[j].posicion[0])/2,(self.objetos[i].posicion[1] + self.objetos[j].posicion[1])/2]
                    nuevos_objetos.append(nuevo)
                    procesados.add(i)
                    procesados.add(j)
        
        self.objetos = [obj for idx, obj in enumerate(self.objetos) 
                       if idx not in procesados and obj.activo]
        self.objetos.extend(nuevos_objetos)

    def actualizar(self, dt):
        fuerzas = self.calcular_fuerzas()  # Forma sin multiprocessing
        # fuerzas = self.cfuerza()    # Forma con multiprocessing
        for idx, fuerza in fuerzas.items():
            self.objetos[idx].Force(fuerza, dt)
        self.detectar_colisiones()
    
    def dibujar(self, pantalla):
        pantalla.fill((0,0,0))
        for obj in self.objetos:
            if obj.activo:
                obj.draw(pantalla)
        pygame.display.flip()


#<<<<<<<<<<<Simulacion<<<<<<<<<<<
# pygame.init()
# # Configurar pantalla
# WIDTH, HEIGHT = Lx, Ly
# pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Prueba 1")

# # Reloj para controlar FPS
# clock = pygame.time.Clock()

# S=SIMULADOR()
# S.inicializar_objetos()

# # Bucle principal
# running = True
# while running:
#     clock.tick(60)  # 60 FPS

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     S.actualizar()
#     S.dibujar(pantalla)


# pygame.quit()