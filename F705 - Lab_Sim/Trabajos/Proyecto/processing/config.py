import yaml
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)
# Configuración del pygame
WIDTH, HEIGHT = 1280, 720
BACKGROUND_COLOR = (0, 0, 0)

# Constante de Gravitación Universal
G = 6.67430e-11 # [Nm^2/kg^2]
