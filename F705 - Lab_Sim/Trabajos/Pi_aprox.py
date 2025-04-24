import random
import plotly.express as px
import math
import pandas as pd
import numpy as np

n=1000
class MonteCarloPi:
    def __init__(self, num_puntos):
        self.num_puntos = num_puntos
        self.dentro_circulo = 0

        self.points_in = []
        self.points_out = []

        self.val_pi = self.calcular_pi() #Nueva instancia del valor de pi
    def generar_punto(self):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        return x, y
    def calcular_pi(self):
        for _ in range(self.num_puntos):
            x, y = self.generar_punto()
            if x**2 + y**2 <= 1:
                self.dentro_circulo += 1
                self.points_in.append((x, y))
            else:
                self.points_out.append((x, y))
        return 4 * (self.dentro_circulo / self.num_puntos)

def pi_prom(lista):
    return sum(lista)/len(lista)
def main(lista):
    sum = 0
    for i in lista:
        sum += i
    return sum/len(lista)
    
if __name__ == "__main__":
    pi_vals = [MonteCarloPi(n).val_pi for _ in range(n)]
    pi_med = pi_prom(pi_vals)
    print(f"El valor de promedio de Pi: {pi_med}")

    pi_media = main(pi_vals)
    print(f"El valor de promedio de Pi, tras {len(pi_vals)} iteraciones, es: {pi_media}")

    df = pd.DataFrame(pi_vals, columns=["Valor de pi"])
    monte_carlo = MonteCarloPi(n)
    points_in = np.array(monte_carlo.points_in)
    points_out = np.array(monte_carlo.points_out)

    fig = px.scatter(title="Simulación de Monte Carlo para calcular π")
    fig.update_layout({'plot_bgcolor':'rgba(255,255,255,0.3)','paper_bgcolor':'rgba(0,0,0,0.7)'})
    fig.add_scatter(
        x=points_in[:, 0], y=points_in[:, 1],
        mode="markers", marker=dict(color="blue", size=3),
        name="Puntos dentro del círculo"
    )
    fig.add_scatter(
        x=points_out[:, 0], y=points_out[:, 1],
        mode="markers", marker=dict(color="red", size=3),
        name="Puntos fuera del círculo"
    )
    fig.add_shape(
        type="rect", x0=-1, y0=-1, x1=1, y1=1,
        line=dict(color="black", width=2),
        fillcolor="rgba(0,0,0,0)"  # Sin relleno
    )
    theta = np.linspace(0, 2 * np.pi, 100)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)
    fig.add_scatter(
        x=x_circle, y=y_circle,
        mode="lines", line=dict(color="green", width=2),
        name="Circunferencia"
    )
    fig.update_layout(
        xaxis=dict(range=[-1.1, 1.1], constrain="domain"),
        yaxis=dict(range=[-1.1, 1.1], scaleanchor="x", scaleratio=1),
        showlegend=True,
        title="Puntos dentro y fuera del círculo"
    )
    fig.write_image("Gráficas/MonteCarloPi01.pdf", format="pdf", width=1200, height=1200, scale=2)