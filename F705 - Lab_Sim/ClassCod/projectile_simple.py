import math
import time
import pygame
import random

pygame.init()

initial_angle = 45
initial_speed = 70
mass = 5
coef_rebote_base = 0.7

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Launcher Simulator")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

g = 9.81  # Gravity
dt = 0.005  # Time step

def convertir_coordenadas(x, y):
    return int(x), HEIGHT - int(y)

def coef_rebote_masa(m):
    """Calcula un coeficiente de restitución dependiente de la masa"""
    return max(0.4, coef_rebote_base - (m / 50))

def lanzar_proyectil(velocidad, angulo):
    angulo_rad = math.radians(angulo)
    vx = velocidad * math.cos(angulo_rad)
    vy = velocidad * math.sin(angulo_rad)
    
    x, y = 50, 50
    trayectoria = [(x, y)]
    
    while x < WIDTH:
        x += vx * dt
        vy -= g * dt
        y += vy * dt
        
        if y <= 50:
            y = 50
            coef_rebote = coef_rebote_masa(mass)  # Obtener coef. según masa
            vy = -vy * coef_rebote
            
            print(f"Masa: {mass} kg, Coef. de rebote: {coef_rebote:.2f}, Nueva velocidad: {vy:.2f} m/s")

            if abs(vy) < 1:  # Condición de parada si la velocidad es muy baja
                break
        
        trayectoria.append((x, y))
    
    return trayectoria

def main():
    running = True

    trayectori = lanzar_proyectil(initial_speed, initial_angle)
    print(trayectori)
    
    index = 0
    
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if index < len(trayectori):
            pygame.draw.circle(screen, RED, convertir_coordenadas(*trayectori[index]), mass*2)
            index += 1
            time.sleep(dt/10)  # Reducir tiempo de espera para animación más fluida
        
        pygame.display.flip()
        
    pygame.quit()

if __name__ == "__main__":
    main()
