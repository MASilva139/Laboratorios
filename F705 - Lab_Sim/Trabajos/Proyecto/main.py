from turtle import width
import pygame
from processing.simulacion import SimulacionG
from processing.utils import load_config

def main():
    config = load_config()
    width = config['pantalla']['width']
    height = config['pantalla']['height']
    
    pygame.init()
    pantalla = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Proyecto - Simulación")
    
