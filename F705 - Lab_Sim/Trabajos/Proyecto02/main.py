from processing import objeto
import pygame
import yaml
import os #ruta absoluta para llamar al .yaml

config_path = os.path.join(os.path.dirname(__file__), "..", "config.yaml")
config_path = os.path.abspath(config_path)

with open(config_path) as f:
    import yaml
    config = yaml.safe_load(f)
Lx= config["parametros"]["Lx"]
Ly= config["parametros"]["Ly"]
def main():
    # Inicializar cualquier cosa necesaria
    pygame.init()
    
    # Configurar pantalla, reloj, objetos, etc.


    width, height = Lx, Ly


    pantalla = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simulación")

    clock = pygame.time.Clock()
    simulador = objeto.SIMULADOR()

    # Bucle principal
    running = True
    while running:
        clock.tick(60)  # 60 FPS
        dt=clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        simulador.actualizar(dt)
        simulador.dibujar(pantalla)
        

    pygame.quit()


# Punto de entrada del programa
if __name__ == "__main__":
    main()

