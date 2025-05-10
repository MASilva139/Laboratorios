from processing.obj_fisico import propiedadesfisicas, propiedadesvisuales
import math
import numpy as np

class Cuerpo(propiedadesfisicas, propiedadesvisuales):
    def __init__(self, masa, posicion, v=(0, 0)):
        propiedadesfisicas.__init__(self, masa, posicion, v)
        propiedadesvisuales.__init__(self, color, forma)