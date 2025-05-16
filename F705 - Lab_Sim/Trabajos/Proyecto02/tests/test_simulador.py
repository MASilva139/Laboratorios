import unittest
from unittest.mock import MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from processing.objeto import Particula, SIMULADOR

class TestSimulador(unittest.TestCase):
    def setUp(self):
        self.simulador = SIMULADOR()

    def test_init(self):
        print("Inicio del test __init__")
        self.assertEqual(len(self.simulador.objetos), self.simulador.objetos.__len__())  # solo para verificar existencia

    def test_inicializar_objetos(self):
        print("Inicio del test inicializar_objetos")
        self.assertEqual(len(self.simulador.objetos), self.simulador.objetos.__len__())
        for p in self.simulador.objetos:
            self.assertIsInstance(p, Particula)

    def test_detectar_colisiones(self):
        print("Inicio del test detectar_colisiones")
        if len(self.simulador.objetos) < 2:
            self.simulador.objetos.append(Particula())
            self.simulador.objetos.append(Particula())
        p1 = self.simulador.objetos[0]
        p2 = self.simulador.objetos[1]
        p1.posicion = [100.0, 100.0]
        p2.posicion = [100.0 + p1.r + p2.r - 0.5, 100.0]
        conteo_inicial = len(self.simulador.objetos)
        self.simulador.detectar_colisiones()
        self.assertLess(len(self.simulador.objetos), conteo_inicial)

    def test_actualizar(self):
        print("Inicio del test actualizar")
        dt = 0.2
        fuerzas_mock = {i: [0.0, 0.0] for i in range(len(self.simulador.objetos))}
        self.simulador.calcular_fuerzas = MagicMock(return_value=fuerzas_mock)
        posiciones_iniciales = [p.posicion.copy() for p in self.simulador.objetos]
        self.simulador.actualizar(dt)
        for i, p in enumerate(self.simulador.objetos):
            self.assertEqual(p.posicion, posiciones_iniciales[i])

if __name__ == '__main__':
    unittest.main()