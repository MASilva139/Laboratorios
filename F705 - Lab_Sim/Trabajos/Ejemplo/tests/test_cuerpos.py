import pytest
import math
from processing.cuerpos import Planeta, Luna, CuerpoCeleste

def test_coord_polares():
    """Prueba la conversión entre coordenadas cartesianas y polares"""
    planeta = Planeta("Test", 1e24, (100, 100))
    r, theta = planeta.coord_polares()
    
    # Verificar que la distancia es correcta
    assert math.isclose(r, math.sqrt(20000), rel_tol=1e-9)
    # Verificar que el ángulo es correcto (45 grados en radianes)
    assert math.isclose(theta, math.pi/4, rel_tol=1e-9)

def test_colision_cuerpos():
    """Prueba la combinación de cuerpos en colisiones"""
    p1 = Planeta("P1", 1e24, (0, 0), (1, 0))
    p2 = Planeta("P2", 2e24, (0, 0), (-1, 0))
    
    # Combinar planetas
    p3 = p1 + p2
    
    # Verificar conservación de masa
    assert p3.masa == 3e24
    # Verificar conservación del momento lineal
    assert p3.velocidad[0] == -1/3  # (1*1e24 + (-1)*2e24)/(3e24)
    assert p3.velocidad[1] == 0

def test_agregar_luna():
    """Prueba la agregación de lunas a planetas"""
    planeta = Planeta("Tierra", 5.972e24, (0, 0))
    luna = Luna("Luna", 7.34767309e22, (384400e3, 0), planeta)
    
    # Verificar agregación exitosa
    assert planeta.agregar_luna(luna)
    assert len(planeta.lunas) == 1
    assert planeta.lunas[0] == luna
    
    # Verificar que no se puede agregar un planeta como luna
    otro_planeta = Planeta("Marte", 6.39e23, (0, 0))
    assert not planeta.agregar_luna(otro_planeta)
