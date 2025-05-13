import numpy as np

def simulation(parameters, distributions):

    # Cálculo del alcance para cada combinación
    ranges = (distributions.v0_dist ** 2) * np.sin(2 * np.radians(distributions.angles_dist)) / distributions.g_dist
    # Filtrado de ángulos que cumplen con el rango de distancia deseado
    valid_angles = distributions.angles_dist[(ranges >= parameters.d_min) & (ranges <= parameters.d_max)]
    # Altura maxima
    h_max = (distributions.v0_dist * np.sin(np.radians(distributions.angles_dist)))**2 / (2 * distributions.g_dist)

    # Impresión de resultados
    if len(valid_angles) == 0:
        print("No se encontró ningún ángulo que cumpla con el rango especificado.")
    else:
        angle_min = np.min(valid_angles)
        angle_max = np.max(valid_angles)
        angle_mean = np.mean(valid_angles)
        print(f"Ángulo mínimo válido: {angle_min:.2f}°")
        print(f"Ángulo máximo válido: {angle_max:.2f}°")
        print(f"Ángulo medio válido: {angle_mean:.2f}°")
        print(f"Número de casos válidos: {len(valid_angles)}")

    return ranges, valid_angles, h_max