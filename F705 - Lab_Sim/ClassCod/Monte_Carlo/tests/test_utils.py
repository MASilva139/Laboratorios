import unittest
from processing.utils import normal_generator


class TestNormalGenerator(unittest.TestCase):
    def test_length(self):
        data = normal_generator(10)
        self.assertEqual(len(data), 10)

    #def test_valores_con_media_y_sigma_personalizados(self):
    #    data = normal_generator(1000, mu=5, sigma=2)
    #    media_aproximada = sum(data) / len(data)
        
    #    self.assertAlmostEqual(media_aproximada, 5, delta=0.5)
        
    def test_valores_con_media_y_sigma_personalizados(self):
        casos = [
            (1000, 0, 2),
            (100, 5, 2),
            (500, -3, 0.5),
            (750, 10, 3),
            (200, 100, 10)
        ]

        for data, mu, sigma in casos:
            with self.subTest(data=data, mu=mu, sigma=sigma):
                data = normal_generator(data, mu=mu, sigma=sigma)
                media_aproximada = sum(data) / len(data)
                self.assertAlmostEqual(media_aproximada, mu, delta=sigma * 0.25)



    def test_lista_no_vacia(self):
        self.assertTrue(normal_generator(1))