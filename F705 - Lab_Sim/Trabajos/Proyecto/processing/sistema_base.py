from .cuerpos import Planeta, Luna
import random

def sistema(config):
    system = []
    sol = Planeta(nombre = "Sol", radio = 6.957e8, masa = 1.989e30, posicion = (0, 0))

    mercurio = Planeta(nombre="Mercurio", radio = 2439.7e3, masa = 3.302e23, posicion = (57.909227e9, 0))

    venus = Planeta(nombre="Venus", radio = 6051.8e3, masa = 4.87e24, posicion = (1.08e11, 0))

    tierra = Planeta(nombre="Tierra",radio=6378000, masa=5.97*10**24, posicion = (1.49597870691e11,0))
    luna = Luna(nombre = "Luna", masa = 7.347e22, posicion = (3.844e8, 0))
    tierra.agregar_luna(luna)
    
    marte = Planeta(nombre = "Marte",radio = 3389.5e3, masa = 6.4185e23, posicion = (2.27936640e11,0))
    fobos = Luna(nombre = "Fobos", masa = 1.479e16, posicion = (9.377e6, 0))
    deimos = Luna(nombre = "Deimos", masa = 1.579e15, posicion = (9.3460e7, 0))
    marte.agregar_luna(fobos)
    marte.agregar_luna(deimos)

    jupiter = Planeta(nombre = "Jupiter", radio = 71.492e6, masa = 1.899e27, posicion = (7.78412026e11,0))
    lunas_jupiter = [
        Luna(nombre = "Metis", masa = 3.6e17, posicion = (128e6, 0)),
        Luna(nombre = "Adrastea", masa = 1.8894e16, posicion = (129e6, 0)),
        Luna(nombre = "Amaltea", masa = 2.08e18, posicion = (181,4e6, 0)),
        Luna(nombre = "Tebe", masa = 1.5e21, posicion = (221.9e6, 0)),
        Luna(nombre = "Ío", masa = 8.94e22, posicion = (421.8e6, 0)),
        Luna(nombre = "Europa", masa = 4.80e22, posicion = (671.1e6, 0)),
        Luna(nombre = "Ganímedes", masa = 1.482e23, posicion = (1.0704e9, 0)),
        Luna(nombre = "Calisto", masa = 1.075938e23, posicion = (1.8827e9, 0)),
        Luna(nombre = "Temisto", masa = 6.9e14, posicion = (7.3985e9, 0)),
        Luna(nombre = "Leda", masa = 1.1e16, posicion = (11.1464e9, 0)),
        Luna(nombre = "Ersa", masa = 1.93e15, posicion = (11.401e9, 0))
    ]
    for lun in lunas_jupiter:
        jupiter.agregar_luna(lun)

    return 
