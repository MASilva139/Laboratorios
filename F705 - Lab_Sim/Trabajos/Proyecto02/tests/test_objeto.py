import unittest
from .processing.objeto import Particula, SIMULADOR
from unittest.mock import MagicMock

class TestParticula(unittest.TestCase):
    def test_init(self):
        particula = Particula()
        self.assertEqual(particula.masa, 1)
        self.assertEqual(particula.posicion, [0, 0])
        self.assertEqual(particula.v, [0, 0])
        self.assertEqual(particula.r, 1)
        self.assertEqual(particula.trayectoria, [(0, 0)])
        self.assertEqual(particula.activo, True)

    def test_force(self):
        particula = Particula()
        particula.masa = 2
        particula.posicion = [1, 1]
        particula.v = [1, 1]
        particula.r = 2
        particula.trayectoria = [(1, 1)]
        particula.activo = True
        particula.Force([1, 1])
        self.assertEqual(particula.masa, 2)
        self.assertEqual(particula.posicion, [2, 2])
        self.assertEqual(particula.v, [1.25, 1.25])
        self.assertEqual(particula.r, 2)
        self.assertEqual(particula.trayectoria, [(1, 1), (2, 2)])
        self.assertEqual(particula.activo, True)

class TestSimulador(unittest.TestCase):
    def test_init(self):
        simulador = Simulador()
        self.assertEqual(simulador.objetos[:7])   # Reducción de pñartículas en la prueba

    def test_inicializar_objetos(self):
        self.assertEqual(len(simulador.objetos), 7)
        for p in self.simulador.objetos:
            self.assertIsInstance(p, Particula)

    def test_detectar_colisiones(self):
        p1 = self.simulador.objetos[0]
        p2 = self.simulador.objetos[1]
        p1.posicion = [100.0, 100.0]
        p2.posicion = [100.0 + p1.r + p2.r - 10, 100.0]
        conteo_inicial = len(self.simulador.objetos)
        self.simulador.detectar_colisiones()
        self.assertEqual(len(self.simulador.objetos), conteo_inicial - 1)
    
    def test_actualizar(self):
        self.simulador.calcular_fuerzas = MagicMock(return_value={i: [0.0, 0.0] for i in range(7)})

        posicion_inicial = [p.posicion.copy() for p in self.simulador.objetos]
        self.simulador.actualizar(0.1)
        for i, p in enumerate(self.simulador.objetos):
            self.assertEqual(p.posicion, posicion_inicial[i])

if __name__ == '__main__':
    unittest.main()
