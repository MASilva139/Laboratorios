import math
import pygame
import random
import sys
sys.setrecursionlimit(5000)

WHITE = (255, 255, 255)
WIDTH, HEIGHT = 3200, 800
x_reference = WIDTH / 2
y_reference = 50

class Projectile():
    def __init__(self, width, height, x_reference, y_reference):
        mu_speed = 50
        sigma_speed = 10

        mu_mass = 1.5
        sigma_mass = 0.2

        self.width = width
        self.height = height
        self.dt = 0.1
        self.gravity = 9.81
        self.mass = random.gauss(mu_mass, sigma_mass)
        self.initial_angle = random.uniform(-90, 90)
        self.initial_speed = random.gauss(mu_speed, sigma_speed)
        self.friction = random.gauss(0.8, 0.1)
        self.colour = (0, 0, 0)

        self.trajectory = self.__recursive_projectile_launch(x_reference, y_reference)

    def __recursive_projectile_launch(self, x, y, vx=None, vy=None, trajectory=None):
        if trajectory is None:
            trajectory = [(x, y)]
            rad_angle = math.radians(abs(self.initial_angle))
            vx = self.initial_speed * math.cos(rad_angle)
            vy = self.initial_speed * math.sin(rad_angle)

            if self.initial_angle < 0:
                vx = -vx  

        if not (0 < x < self.width):
            return trajectory

        x += vx * self.dt
        vy -= self.gravity * self.dt
        y += vy * self.dt

        if y <= 50:
            y = 50
            friction_effect = 1 - (self.friction * (self.mass / 10))
            vy = -vy * max(0, friction_effect)

            if abs(vy) < 1:
                return trajectory

        trajectory.append((x, y))
        return self.__recursive_projectile_launch(x, y, vx, vy, trajectory)

    def draw(self, screen, index):
        # Este método será sobrescrito en las subclases
        pass


class CircleProjectile(Projectile):
    def draw(self, screen, index):
        if index < len(self.trajectory):
            pygame.draw.circle(screen, self.colour, convert_coords(*self.trajectory[index]), int(self.mass * 3))


class SquareProjectile(Projectile):
    def draw(self, screen, index):
        if index < len(self.trajectory):
            size = int(self.mass * 3)
            pygame.draw.rect(screen, self.colour, pygame.Rect(convert_coords(*self.trajectory[index])[0] - size, 
                                                              convert_coords(*self.trajectory[index])[1] - size, 
                                                              size, size))


class TriangleProjectile(Projectile):
    def draw(self, screen, index):
        if index < len(self.trajectory):
            size = int(self.mass * 3)
            points = [
                (convert_coords(*self.trajectory[index])[0], convert_coords(*self.trajectory[index])[1] - size),
                (convert_coords(*self.trajectory[index])[0] - size, convert_coords(*self.trajectory[index])[1] + size ),
                (convert_coords(*self.trajectory[index])[0] + size, convert_coords(*self.trajectory[index])[1] + size )
            ]
            pygame.draw.polygon(screen, self.colour, points)


def convert_coords(x, y):
    return int(x), HEIGHT - int(y)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Projectile Launcher Simulator")

    running = True
    projectiles = [random.choice([CircleProjectile, SquareProjectile, TriangleProjectile])(WIDTH, HEIGHT, x_reference, y_reference) for _ in range(1000)]

    index = 0
    max_length = max(len(p.trajectory) for p in projectiles)

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for p in projectiles:
            p.draw(screen, index)

        index += 1
        if index >= max_length:
            break

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
