import pygame
import sys
import yaml
from processing.simulacion import Simulacion
from processing.sistema_base import SISTEMA

def main():
    # Cargar configuración
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)

    # Inicializar Pygame
    pygame.init()
    pygame.font.init()

    # Configuración de la pantalla
    pantalla = pygame.display.set_mode(
        (config['simulacion']['ancho'], 
         config['simulacion']['alto'])
    )
    pygame.display.set_caption("Simulación Gravitacional")

    # Crear simulación
    simulacion = Simulacion(pantalla, config)
    
    # Agregar cuerpos del sistema solar
    for cuerpo in SISTEMA.system:
        simulacion.agregar_cuerpo(cuerpo)

    # Bucle principal
    reloj = pygame.time.Clock()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Actualizar y dibujar
        simulacion.actualizar(config['sistema']['dt'])
        simulacion.dibujar()
        
        # Mostrar información
        fuente = pygame.font.Font(None, 24)
        texto = f"Cuerpos activos: {len(simulacion.cuerpos)}"
        superficie_texto = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(superficie_texto, (10, 10))
        
        pygame.display.flip()
        reloj.tick(config['simulacion']['fps'])

if __name__ == "__main__":
    main()
