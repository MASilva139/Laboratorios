import math
import time
import pygame
import random

WIDTH, HEIGHT = 1280, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
x_ref, y_ref = WIDTH/2, 50
n=20

class Proyectil():
    def __init__(self, width, height, x, y, n):
        self.n = n
        self.initial_angle = [random.uniform(20,160) for _ in range(n)]
        self.initial_speed = [random.uniform(50,120) for _ in range(n)]
        self.mass = [random.uniform(3,8) for _ in range(n)]
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

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Projectile Launcher Simulator")
    running = True
    # trayectori = lanzar_proyectil(initial_speed, initial_angle)
    p = Proyectil(WIDTH, HEIGHT, x_ref, y_ref, n)
    print(p.trayectori)
    # index = 0
    index = [0]*n
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for objeto in range(len(p.trayectori)-1,-1,-1):#Iteración en reversa para evitar problemas al eliminar los proyectiles que estan fuera del marco (costados y abajo)
            if index[objeto] < len(p.trayectori[objeto]):
                x, y = p.trayectori[objeto][index[objeto]]
                if 0<=x < WIDTH and y>=0:
                    pygame.draw.circle(screen, RED, p.convertir_coordenadas(x,y), p.mass[objeto]*2)
                    index[objeto] += 1
                else:
                    del p.trayectori[objeto]
                    del index[objeto]
                    del p.mass[objeto]
                    del p.initial_angle[objeto]
                    del p.initial_speed[objeto]
            else:
                del p.trayectori[objeto]
                del index[objeto]
                del p.mass[objeto]
                del p.initial_angle[objeto]
                del p.initial_speed[objeto]
                    # time.sleep(dt/10)  # Reducir tiempo de espera para animación más fluida
        pygame.display.flip()
        if not p.trayectori:
            running = False
    pygame.quit()

if __name__ == "__main__":
    main()