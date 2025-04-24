import math
import time
import pygame
import random

#No orientado a objetos
# n = 100
# pygame.init()
# initial_angle = [random.uniform(20,160) for _ in range(n)]
# initial_speed = [random.uniform(50,120) for _ in range(n)]
# mass = [random.uniform(2,10) for _ in range(n)]
# # initial_angle = 80
# # initial_speed = 100
# # mass = 5
# coef_rebote_base = 0.7

# # WIDTH, HEIGHT = 800, 600
# WIDTH, HEIGHT = 1280, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Projectile Launcher Simulator")

# WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# g = 9.81  # Gravity
# dt = 0.005  # Time step

# def convertir_coordenadas(x, y):
#     return int(x), HEIGHT - int(y)
# def coef_rebote_masa(m):
#     """Calcula un coeficiente de restitución dependiente de la masa"""
#     return max(0.4, coef_rebote_base - (m / 50))
# def lanzar_proyectil(velocidad, angulo):
#     angulo_rad = math.radians(angulo)
#     vx = velocidad * math.cos(angulo_rad)
#     vy = velocidad * math.sin(angulo_rad)
    
#     x, y = WIDTH/2, 50
#     trayectoria = [(x, y)]
    
#     while x < WIDTH:
#         x += vx * dt
#         vy -= g * dt
#         y += vy * dt
        
#         if y <= 50:
#             y = 50
#             # coef_rebote = coef_rebote_masa(mass)  # Obtener coef. según masa
#             coef_rebote = 0
#             vy = -vy * coef_rebote
#             print(f"Masa: {mass} kg, Coef. de rebote: {coef_rebote:.2f}, Nueva velocidad: {vy:.2f} m/s")
#             # if abs(vy) < 1:  # Condición de parada si la velocidad es muy baja
#             if abs(vy) < 1:  # Condición de parada si la velocidad es muy baja
#                 break
#         trayectoria.append((x, y))
#     return trayectoria

# def main():
#     running = True
#     # trayectori = lanzar_proyectil(initial_speed, initial_angle)
#     trayectori = [lanzar_proyectil(initial_speed[objeto], initial_angle[objeto]) for objeto in range(n)]
#     print(trayectori)
#     # index = 0
#     index = [0]*n
#     while running:
#         screen.fill(WHITE)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         for objeto in range(n):
#             if index[objeto] < len(trayectori[objeto]):
#                 x, y = trayectori[objeto][index[objeto]]
#                 pygame.draw.circle(screen, RED, convertir_coordenadas(x,y), mass[objeto]*2)
#                 index[objeto] += 1
#                 # time.sleep(dt/10)  # Reducir tiempo de espera para animación más fluida
#         pygame.display.flip()
#     pygame.quit()

# if __name__ == "__main__":
#     main()

WIDTH, HEIGHT = 1280, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
x_ref, y_ref = WIDTH/2, 50
n=10

class Proyectil():
    def __init__(self, width, height, x, y, n):
        self.n = n
        self.mu_speed, self.sigma_speed = 50, 10
        self.mu_mass, self.sigma_mass = 1.5, 0.5
        self.initial_angle = [random.uniform(20,160) for _ in range(n)]
        self.initial_speed = [random.uniform(50,120) for _ in range(n)]
        self.mass = [random.uniform(3,6) for _ in range(n)]
        self.x = x
        self.y = y
        self.WIDTH = width
        self.HEIGHT = height
        # initial_angle = 80
        # initial_speed = 100
        # mass = 5
        self.coef_rebote_base = 0.7
        # WIDTH, HEIGHT = 800, 600
        self.g = 9.81  # Gravity
        self.dt = 0.005  # Time step
        self.trayectori = [self.lanzar_proyectil(self.initial_speed[objeto], self.initial_angle[objeto]) for objeto in range(n)]

    def convertir_coordenadas(self, x, y):
        return int(x), self.HEIGHT - int(y)

    def coef_rebote_masa(self, m):
        """Calcula un coeficiente de restitución dependiente de la masa"""
        return max(0.7, self.coef_rebote_base - (m / 50))

    def lanzar_proyectil(self, velocidad, angulo):
        angulo_rad = math.radians(angulo)
        vx = velocidad * math.cos(angulo_rad)
        vy = velocidad * math.sin(angulo_rad)
        x, y = self.x, self.y
        trayectoria = [(x, y)]
        while x < WIDTH:
            x += vx * self.dt
            vy -= self.g * self.dt
            y += vy * self.dt
            if y <= 50:
                y = 50
                coef_rebote = self.coef_rebote_masa(self.mass[0])  # Obtener coef. según masa
                # coef_rebote = 0
                vy = -vy * coef_rebote
                print(f"Masa: {self.mass} kg, Coef. de rebote: {coef_rebote:.2f}, Nueva velocidad: {vy:.2f} m/s")
                # if abs(vy) < 1:  # Condición de parada si la velocidad es muy baja
                if abs(vy) < 1:  # Condición de parada si la velocidad es muy baja
                    break
            trayectoria.append((x, y))
        return trayectoria

class Circ_Proyectil(Proyectil):
    def draw(self, screen, index):
        if index < len(self.trayectori[index]):
            pygame.draw.circle(screen, RED, self.convertir_coordenadas(*self.trayectori[index])[0], int(self.mass * 3))

class Cuad_Proyectil(Proyectil):
    def draw(self, screen, index):
        if index < len(self.trayectori):
            size = int(self.mass*3)
            pygame.draw.rect(screen, RED, pygame.Rect(self.convertir_coordenadas(*self.trayectori[index])[0] - size, 
                                                              self.convertir_coordenadas(*self.trayectori[index])[1] - size, 
                                                              size, size))

class Tri_Proyectil(Proyectil):
    def draw(self, screen, index):
        if index < len(self.trayectori):
            size = int(self.mass * 3)
            points = [
                (self.convertir_coordenadas(*self.trayectori[index])[0], self.convertir_coordenadas(*self.trayectori[index])[1] - size),
                (self.convertir_coordenadas(*self.trayectori[index])[0] - size, self.convertir_coordenadas(*self.trayectori[index])[1] + size ),
                (self.convertir_coordenadas(*self.trayectori[index])[0] + size, self.convertir_coordenadas(*self.trayectori[index])[1] + size )
            ]
            pygame.draw.polygon(screen, RED, points)
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Projectile Launcher Simulator")
    running = True
    proy = [random.choice([Circ_Proyectil, Cuad_Proyectil, Tri_Proyectil])(WIDTH, HEIGHT, x_ref, y_ref, n) for _ in range(n)]
    # p = Proyectil(WIDTH, HEIGHT, x_ref, y_ref, n)
    # print(p.trayectori)
    # index = 0
    index = 0
    max_length = max(len(p.tra) for p in proy)
    # index = [0]*n
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        project_in = True #Indicador de proyectiles dentro del marco
        for p in proy:
            p.draw(screen, index)
            #     x, y = p.trayectori[objeto][index[objeto]]
            #     pygame.draw.circle(screen, RED, p.convertir_coordenadas(x,y), p.mass[objeto]*2)
            index += 1
            project_in = False
            # time.sleep(dt/10)  # Reducir tiempo de espera para animación más fluida
        pygame.display.flip()
        if project_in:
            running = False
    pygame.quit()

if __name__ == "__main__":
    main()