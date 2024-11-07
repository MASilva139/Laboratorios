# LABORATORIO DE ELECTRÓNICA DIGITAL
Semestre: 6to.
\
Licenciado: Héctor Pérez

## Proyectos/Parciales
1. [**Parcial 2:**](Parcial-02) Contiene el proyecto para el segundo parcial del semestre.

    Funciones añadidas: Seno, Coseno, Logaritmo natural, Potencias de complejos.
2. [**Exámen final**](Final) Contiene el proyecto para el exámen final.

## Instalación de gcc en ArchLinux
1. Abrir terminal
2. `sudo pacman -S gcc`

## Extensiones para C
* **C/C++** (C/C++ IntelliSense, debugging, and code browsing - Microsoft)
* **C/C++ Extension Pack** (Popular extensions for C++ development in Visual Studio Code - Microsoft)
* **Better C++ Syntax** (The bleeding edge of the C++ syntax - Jeff Hykin)
* **C/C++ Runner** (Compile, run and debug single or multiple C/C++ files with ease - franneck94)
* **C/C++ Themes** (UI Themes for C/C++ extension - Microsoft)
* **C/C++ Compile Run** (Compile & Run single C/C++ files easly - danielpinto8zz6)
* **CMake** (CMake langage support for Visual Studio Code - twxs)
* **CMake Tools** (Extended CMake support in Visual Studio Code - Microsoft)
* **CodeLLDB** (A native debugger powered by LLDB. Debug C++, Rust and other compiled languages - Vadim Chugunov)

## Compilación de varios archivos C
```
gcc -o [nombre del ejecutable.*extension] (archivo1.c) (archivo2.c) (...) -lm
./[nombre del ejecutable.*extension]
```
* Ejemplo: `gcc -o test test.c complejo.c -lm`