import math
import pygame
import random

pygame.init()

class Tiro:
    def __init__(self):
        self.angle0 = random.uniform(0,180)
        self.v0 = random.uniform(10, 80)
        self.mass = random.uniform(0, 80)
        self.g = 9.8
        self.dt = 0.1  # Reducido para mayor precisión
        self.cotaMAXWIDTH = 800
        self.x0, self.y0 = 10.0, 10.0  # Posición inicial

    def Lanzamiento(self):
        rad_angle0 = math.radians(self.angle0)
        v_0x = self.v0 * math.cos(rad_angle0)
        v_0y = self.v0 * math.sin(rad_angle0)

        x, y = self.x0, self.y0
        Trayectoria = [(x, y)]

        while abs(x) < self.cotaMAXWIDTH:
            x += v_0x * self.dt
            v_0y -= self.g * self.dt
            y += v_0y * self.dt
            Trayectoria.append((x, y))

        return Trayectoria

# Configuración de pantalla
WIDTH, HEIGHT = 1200, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Launcher Simulator")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

def convertir_coordenadas(x, y):

    return int(WIDTH // 2 + x), int(HEIGHT // 2 - y)

def main():
    running = True
    clock = pygame.time.Clock()
    n = 50 # Número de pelotas
    tiros = [Tiro() for _ in range(n)]  # Crear n proyectiles
    trayectorias = [tiro.Lanzamiento() for tiro in tiros]  # Generar trayectorias
    indices = [0] * n  # Índices para recorrer cada trayectoria


    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i in range(n):
            if indices[i] < len(trayectorias[i]):
                x, y = trayectorias[i][indices[i]]
                pygame.draw.circle(screen, RED, convertir_coordenadas(x, y), 3)
                indices[i] += 1


        pygame.display.flip()
        clock.tick(60)  # Controlar la velocidad de actualización

    pygame.quit()

if __name__ == "__main__":
    main()