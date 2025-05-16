# Simulación de Gravitación para N-Cuerpos

## Descripción
Este proyecto está diseñado para simular la interacción gravitacional entre múltiples partículas en un sistema bidimensional, utilizando Pygame para visualización y conceptos de física clásica. Las partículas se representan como formas geométricas con tamaños proporcionales a su masa y colores aleatorios.

## Objetivos
- Aplicar programación orientada a objetos (POO) en python.
- Generar datos aleatorios con distribuciones estadísticas (normal y uniforme).
- Utilizar `pygame` para visualización en tiempo real.
- Simular colisiones con conservación del momento lineal.
- Implementar herencia múltiple, encapsulamiento, polimorfismo y agregación.
- Usar `multiprocessing` para inicializar partículas en paralelo.
- Aplicar pruebas unitarias y organización modular.

## Características
- Simulación de partículas con masa y posición aleatorias.
- Gravitación entre partículas, donde la fuerza es proporcional a la masa de las partículas y inversamente proporcional al cuadrado de la distancia entre ellas.
- Colisiones entre partículas, donde la masa total se conserva y la velocidad se calcula como la media de las velocidades de las partículas colisionantes.
- Configuración de parámetros en un archivo YAML.

## Estructura del proyecto

```
Proyecto/
├── config.yaml
├── main.py
├── processing/
│   ├── objeto.py
│   └── __init__.py
├── requirements.txt
├── tests/
│   ├── test_objeto.py
│   └── test_simulador.py
├── README.md
└── makefile
```

## Clases Principales
### Particula (archivo objeto.py)
Hereda de atributos de 'propiedades_fisica' y 'propiedades_visuales'. Contienen
* Masa, posición, velocidad, trayectoria y radio.
* Forma y color aleatorios.
* Metodo 'Force()' que actualiza el estado físico.
* Metodo 'draw()' que dibuja la partícula en la pantalla.

### SIMULADOR (archivo objeto.py)
Clase que representa la simulación en general. Contiene una lista de particulas y se encarga de ejecutar:
* Calculo de fuerzas gravitacionales con el metodo 'calcular_fuerzas()'.
* Detección de colisiones con el metodo 'detectar_colisiones()'.
* Actualización de las partículas con el metodo 'actualizar()'.
* Visualización de la simulación con el metodo 'dibujar()'.

## Pruebas Unitarias
Ubicadas en la carpeta 'tests/', se encargan de cubrir:
* Inicialización de partículas.
* Aplicación de fuerza.
* Inicialización y actualización del simulador.
* Detección de colisiones.

# Implementación de POO en el código
Los elementos que contiene de POO presentes en el programa son:

* Encapsulamiento:
Encargado de ocultar los detalles internos de un objeto, manteniendo el estado pribado o protegido, accediendo a él solo mediante métodos.

Se encuentran dentro de los atributos y lógica interna en las clases 'Particula' y 'Simulación':
    - Los atributos de 'self.masa', 'self.v', 'self.posicion', 'self.trayectoria' están agrupados dentro de la clase 'propiedades_fisica', encapsulando su estado.
    - El método 'Force(self, fuerza, dt)' contróla cómo se actualiza internamente una partícula, sin exponer directamente su lógica al exterior.

* Herencia múltiple:
Permite que una clase herede atributos y métodos de múltiples superclases, lo que facilita la organización y reutilización del código.
    - Se encuentra en la clase 'Particula', que hereda de las clases 'propiedades_fisica' y 'propiedades_visuales'.

* Polimorfismo:
Permite que diferentes clases respondan de manera diferente a los mismos mensajes, lo que permite una mayor flexibilidad y adaptabilidad del código.
    - Se encuentra en el método 'draw(self, pantalla)', que puede ser implementado de manera diferente para diferentes tipos de partículas, esto se debe a que depende de 'self.forma'.

* Agregación:
Permite que una clase contenga referencias a otros objetos, lo que facilita la organización y reutilización del código.
    - Se encuentra en la clase 'SIMULADOR', que contiene una lista de partículas 'self.objetos = []' y utiliza sus métodos para actualizar su estado.

* Abstracción:
Permite simplificar la representación de un objeto, ocultando detalles complejos y mostrando solo lo esencial.
    - Se encuentra en la clase 'Particula', que tiene un método 'Force(self, fuerza, dt)' que calcula la aceleración de una partícula en función de la fuerza aplicada. Dichas clases abtraen un cuerpo físico con masa, velocidad, trayectoria y propiedades visuales.
    - 'SIMULADOR' abstrae la lógica del sistema completo: inicialización, cálculo de fuerzas, colisiones y visualización.

* Multiprocessing:
Permite la ejecución paralela de procesos, lo que puede mejorar el rendimiento del programa.
    - Se encuentra en la función 'generar_particula(_)', que se encarga de generar partículas en paralelo.

# Autores
Proyecto desarrollado por:
* Saúl Estuardo Najera Allara, 202107506
* Mario Armando Urbina Silva, 201906054

Universidad de San Carlos de Guatemala
Escuela de Ciencias Físicas y Matemáticas
Curso: F705 - Laboratorio de Simulación