import math
import pygame
import random
import sys

# Configuración ajustada
WIDTH, HEIGHT = 1280, 720
BACKGROUND_COLOR = (0, 0, 0)
G = 5e3  # Constante gravitacional aumentada

# class GravitationalObject:
#     def __init__(self, masa, posicion, velocidad=(0, 0)):
#         self.masa = masa
#         self.posicion = list(posicion)
#         self.velocidad = list(velocidad)
#         self.radio = max(10, int(math.sqrt(masa) // 50))  # Nueva escala de radio
#         self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
#         self.forma = random.choice(['circle', 'square', 'triangle'])
#         self.trayectoria = [tuple(posicion)]
#         self.active = True

#     def aplicar_fuerza(self, fuerza, dt):
#         ax = fuerza[0] / self.masa
#         ay = fuerza[1] / self.masa
#         self.velocidad[0] += ax * dt
#         self.velocidad[1] += ay * dt
#         self.posicion[0] += self.velocidad[0] * dt
#         self.posicion[1] += self.velocidad[1] * dt
#         self.trayectoria.append((self.posicion[0], self.posicion[1]))
#         if len(self.trayectoria) > 100:
#             self.trayectoria.pop(0)

#     def dibujar(self, pantalla):
#         if len(self.trayectoria) > 1:
#             puntos = [(int(x), int(y)) for x, y in self.trayectoria[-50:]]
#             pygame.draw.lines(pantalla, self.color, False, puntos, 2)
        
#         x, y = int(self.posicion[0]), int(self.posicion[1])
#         if self.forma == 'circle':
#             pygame.draw.circle(pantalla, self.color, (x, y), self.radio)
#         elif self.forma == 'square':
#             rect = pygame.Rect(x-self.radio, y-self.radio, self.radio*2, self.radio*2)
#             pygame.draw.rect(pantalla, self.color, rect)
#         elif self.forma == 'triangle':
#             puntos = [
#                 (x, y-self.radio),
#                 (x-self.radio, y+self.radio),
#                 (x+self.radio, y+self.radio)
#             ]
#             pygame.draw.polygon(pantalla, self.color, puntos)
class GravitationalObject:
    def __init__(self, masa, posicion, velocidad=(0, 0)):
        self.masa = masa
        self.posicion = list(posicion)
        self.velocidad = list(velocidad)
        self.radio = max(5, int(math.log(masa) * 2))  # Radio basado en masa
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.forma = random.choice(['circle', 'square', 'triangle'])
        self.trayectoria = [tuple(posicion)]
        self.active = True
        print(self.trayectoria)

    def aplicar_fuerza(self, fuerza, dt):
        ax = fuerza[0] / self.masa
        ay = fuerza[1] / self.masa
        self.velocidad[0] += ax * dt
        self.velocidad[1] += ay * dt
        self.posicion[0] += self.velocidad[0] * dt
        self.posicion[1] += self.velocidad[1] * dt
        self.trayectoria.append((self.posicion[0], self.posicion[1]))
        temp = []
        if len(self.trayectoria) > 100:
            temp = self.trayectoria[1:] # [5, 1, 2, 3] => [1, 2, 3]
            self.trayectoria = temp
        # if len(self.trayectoria) > 100:
        #     self.trayectoria.pop(0) # [5, 1, 2, 3] => [1, 2, 3]
            print(self.trayectoria)

    def dibujar(self, pantalla):
        if len(self.trayectoria) > 1:
            puntos = [(int(x), int(y)) for x, y in self.trayectoria[-50:]]
            pygame.draw.lines(pantalla, self.color, False, puntos, 2)
        
        x, y = int(self.posicion[0]), int(self.posicion[1])
        if self.forma == 'circle':
            pygame.draw.circle(pantalla, self.color, (x, y), self.radio)
        elif self.forma == 'square':
            rect = pygame.Rect(x-self.radio, y-self.radio, self.radio*2, self.radio*2)
            pygame.draw.rect(pantalla, self.color, rect)
        elif self.forma == 'triangle':
            puntos = [
                (x, y-self.radio),
                (x-self.radio, y+self.radio),
                (x+self.radio, y+self.radio)
            ]
            pygame.draw.polygon(pantalla, self.color, puntos)

class SimuladorGravitacional:
    def __init__(self):
        self.objetos = []
        self.inicializar_objetos()
    
    def inicializar_objetos(self):
        # Objetos más cercanos con masas mayores
        self.objetos.append(GravitationalObject(
            masa=1000,
            posicion=(WIDTH/2 - 100, HEIGHT/2),
            velocidad=(0, 0)  # Velocidad inicial agregada
        ))
        self.objetos.append(GravitationalObject(
            masa=5000,
            posicion=(WIDTH/2 + 100, HEIGHT/2),
            velocidad=(0, 0)  # Velocidad inicial agregada
        ))
        self.objetos.append(GravitationalObject(
            masa=10000,
            posicion=(WIDTH/2 -200, HEIGHT/2+300),
            velocidad=(0, 0)  # Velocidad inicial agregada
        ))
        self.objetos.append(GravitationalObject(
            masa=100,
            posicion=(WIDTH/2, HEIGHT/2-200),
            velocidad=(0, 0)  # Velocidad inicial agregada
        ))
        self.objetos.append(GravitationalObject(
            masa=10,
            posicion=(WIDTH/2-200, HEIGHT/2-200),
            velocidad=(0, 5)  # Velocidad inicial agregada
        ))
    
    def calcular_fuerzas(self):
        fuerzas = {}
        for i in range(len(self.objetos)):
            if not self.objetos[i].active:
                continue
            fuerzas[i] = [0, 0]
            for j in range(len(self.objetos)):
                if i == j or not self.objetos[j].active:
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
            if i in procesados or not self.objetos[i].active:
                continue
            
            for j in range(i+1, len(self.objetos)):
                if j in procesados or not self.objetos[j].active:
                    continue
                
                dx = self.objetos[j].posicion[0] - self.objetos[i].posicion[0]
                dy = self.objetos[j].posicion[1] - self.objetos[i].posicion[1]
                distancia = math.hypot(dx, dy)
                
                if distancia < (self.objetos[i].radio + self.objetos[j].radio):
                    masa_total = self.objetos[i].masa + self.objetos[j].masa
                    # Conservación del momento lineal
                    vel_x = (self.objetos[i].velocidad[0] * self.objetos[i].masa + 
                            self.objetos[j].velocidad[0] * self.objetos[j].masa) / masa_total
                    vel_y = (self.objetos[i].velocidad[1] * self.objetos[i].masa + 
                            self.objetos[j].velocidad[1] * self.objetos[j].masa) / masa_total
                    
                    nuevo = GravitationalObject(
                        masa=masa_total,
                        posicion=(
                            (self.objetos[i].posicion[0] + self.objetos[j].posicion[0])/2,
                            (self.objetos[i].posicion[1] + self.objetos[j].posicion[1])/2
                        ),
                        velocidad=(vel_x, vel_y)
                    )
                    nuevos_objetos.append(nuevo)
                    procesados.add(i)
                    procesados.add(j)
        
        self.objetos = [obj for idx, obj in enumerate(self.objetos) 
                       if idx not in procesados and obj.active]
        self.objetos.extend(nuevos_objetos)
    
    def actualizar(self, dt):
        fuerzas = self.calcular_fuerzas()
        for idx, fuerza in fuerzas.items():
            self.objetos[idx].aplicar_fuerza(fuerza, dt)
        self.detectar_colisiones()
    
    def dibujar(self, pantalla):
        pantalla.fill(BACKGROUND_COLOR)
        for obj in self.objetos:
            if obj.active:
                obj.dibujar(pantalla)
        pygame.display.flip()

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulación Gravitacional Mejorada")
    
    simulador = SimuladorGravitacional()
    reloj = pygame.time.Clock()
    
    running = True
    while running:
        dt = reloj.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        simulador.actualizar(dt)
        simulador.dibujar(pantalla)
    
    pygame.quit()

if __name__ == "__main__":
    main()