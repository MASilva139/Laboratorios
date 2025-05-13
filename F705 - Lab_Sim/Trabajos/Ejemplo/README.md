# Simulación Gravitacional

Este proyecto implementa una simulación visual de gravitación usando Python y Pygame. La simulación muestra múltiples objetos con masas generadas a partir de una distribución normal y posiciones iniciales asignadas de manera aleatoria usando coordenadas polares.

## Características

- Simulación gravitacional en tiempo real
- Generación aleatoria de cuerpos celestes con:
  - Masas siguiendo una distribución normal
  - Posiciones iniciales en coordenadas polares
  - Formas aleatorias (círculo, cuadrado, triángulo)
  - Colores RGB aleatorios
  - Tamaño relacionado con la masa
- Colisiones entre cuerpos
- Visualización de trayectorias
- Procesamiento paralelo para cálculos de fuerzas

## Estructura del Proyecto

```
.
├── main.py              # Punto de entrada principal
├── processing/          # Módulos de procesamiento
│   ├── __init__.py
│   ├── cuerpos.py      # Definición de cuerpos celestes
│   ├── obj_fisico.py   # Propiedades físicas y visuales
│   └── simulacion.py   # Lógica de simulación
├── tests/              # Tests unitarios
├── config.yaml         # Configuración del sistema
├── requirements.txt    # Dependencias del proyecto
├── makefile           # Automatización de tareas
└── README.md          # Documentación
```

## Requisitos

- Python 3.10+
- Pygame
- NumPy
- Matplotlib
- PyYAML

## Instalación

1. Clonar el repositorio
2. Crear ambiente virtual e instalar dependencias:
   ```bash
   make install
   ```

## Uso

Para ejecutar la simulación:
```bash
make run
```

Para ejecutar los tests:
```bash
make test
```

Para ejecutar chequeos estáticos:
```bash
make lint
```

## Características Técnicas

### Herencia Múltiple
- `CuerpoCeleste` hereda de `PropiedadesFisicas` y `PropiedadesVisuales`

### Polimorfismo
- Método `obtener_inf()` implementado diferentemente en `Planeta` y `Luna`

### Encapsulamiento
- Atributos privados para masa, posición y velocidad
- Métodos getter/setter para acceso controlado

### Agregación
- Planetas pueden tener múltiples lunas orbitando

### Multihilos
- Cálculos de fuerzas realizados en paralelo
- Generación de cuerpos en múltiples hilos

## Configuración

El archivo `config.yaml` permite ajustar:
- Número de cuerpos
- Parámetros de distribuciones estadísticas
- Configuración de visualización
- Número de hilos
- Y más...

## Licencia

MIT
