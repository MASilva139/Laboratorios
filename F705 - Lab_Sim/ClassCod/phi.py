import random

class MonteCarloPi:
    def __init__(self, num_puntos):
        self.num_puntos = num_puntos
        self.dentro_circulo = 0

    def generar_punto(self):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        return x, y

    def calcular_pi(self):
        for _ in range(self.num_puntos):
            x, y = self.generar_punto()
            if x**2 + y**2 <= 1:
                self.dentro_circulo += 1

        return 4 * (self.dentro_circulo / self.num_puntos)
    
if __name__ == "__main__":
    pi_val = MonteCarloPi(10000)
    print(pi_val.calcular_pi())
    