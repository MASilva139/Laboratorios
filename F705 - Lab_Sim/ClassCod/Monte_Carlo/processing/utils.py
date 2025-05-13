import yaml
import matplotlib.pyplot as plt
from distributions import Distribution
from dto import DistributionsDTO, ParametersDTO

def data_generator():
    with open("configuration.yaml", "r") as file:
        config = yaml.safe_load(file)

    parameters = ParametersDTO(
        N=config["simulacion"]["N"],
        G=config["parametros"]["G"],
        G_distribution=config["parametros"]["G_distribution"],
        G_second_parameter=config["parametros"]["G_deviation"],
        v0_mean=config["parametros"]["v0"],
        v0_mean_distribution=config["parametros"]["v0_distribution"],
        v0_second_parameter=config["parametros"]["v0_deviation"],
        min_angle=config["parametros"]["min_angle"],
        max_angle=config["parametros"]["max_angle"],
        angle_distribution=config["parametros"]["angle_distribution"],
        d_min=config["rango_objetivo"]["dist_min"],
        d_max=config["rango_objetivo"]["dist_max"],
    )

    distribution = Distribution(parameters.N)
    distributions = DistributionsDTO(
        v0_dist=distribution.set(parameters.v0_mean, parameters.v0_second_parameter, parameters.v0_mean_distribution),
        g_dist=distribution.set(parameters.G, parameters.G_second_parameter, parameters.G_distribution),
        angles_dist=distribution.set(parameters.min_angle, parameters.max_angle, parameters.angle_distribution)
    )

    return parameters, distributions

def histogram(axs, position, data, title, xlabel):
    bins = 100
    color="skyblue"
    ecolor="black"
    ylabel="Frecuencia"
    
    axs[position[0], position[1]].hist(data, bins=bins, color=color, edgecolor=ecolor)
    axs[position[0], position[1]].set_title(title)
    axs[position[0], position[1]].set_xlabel(xlabel)
    axs[position[0], position[1]].set_ylabel(ylabel)
    axs[position[0], position[1]].grid(True)

def graphics(ranges, valid_angles, h_max, parameters, distributions):
    fig, axs = plt.subplots(2, 3, figsize=(18, 8))

    # Histograma de la velocidad inicial v0
    histogram(
        axs=axs, position=[0,0], data=distributions.v0_dist, 
        title="Distribución de la velocidad inicial $v_0$",
        xlabel="Velocidad (m/s)",
    )

    # Histograma de la gravedad g
    histogram(
        axs=axs, position=[0,1], data=distributions.g_dist, 
        title="Distribución de la gravedad $g$",
        xlabel="Gravedad (m/s²)",
    )

    # Histograma del alcance (range)
    histogram(
        axs=axs, position=[0,2], data=ranges, 
        title="Distribución del alcance $R$",
        xlabel="Alcance (m)",
    )

    # Histograma de todos los ángulos generados
    histogram(
        axs=axs, position=[1,0], data=distributions.angles_dist, 
        title="Distribución de todos los ángulos generados",
        xlabel="Ángulo (°)",
    )

    # Histograma de los ángulos válidos
    histogram(
        axs=axs, position=[1,1], data=valid_angles, 
        title="Ángulos que cumplen con el rango objetivo",
        xlabel="Ángulo (°)",
    )

    # Histograma de altura maxima
    histogram(
        axs=axs, position=[1,2], data=h_max, 
        title="Distribución de la altura máxima $h_{max}$",
        xlabel="Altura (m)",
    )

    # Ajuste del diseño y visualización
    plt.tight_layout()
    plt.show()
