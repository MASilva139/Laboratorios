import unittest
from unittest.mock import MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from processing.objeto import Particula

class TestParticula(unittest.TestCase):
    def test_init(self):
        particula = Particula()
        self.assertTrue(particula.masa > 0)
        self.assertEqual(len(particula.posicion), 2)
        self.assertEqual(len(particula.v), 2)
        self.assertTrue(particula.r > 0)
        self.assertEqual(len(particula.trayectoria), 1)
        self.assertTrue(particula.activo)

    def test_force(self):
        dt = 0.2
        particula = Particula()
        particula.masa = 2
        particula.posicion = [1, 1]
        particula.v = [1, 1]
        particula.trayectoria = [(1, 1)]
        particula.Force([1, 1], dt)  # con dt = 0.2 por defecto
        self.assertAlmostEqual(particula.v[0], 1.1, places=2)
        self.assertAlmostEqual(particula.posicion[0], 1.22, places=2)
        self.assertEqual(len(particula.trayectoria), 2)

if __name__ == '__main__':
    unittest.main()
