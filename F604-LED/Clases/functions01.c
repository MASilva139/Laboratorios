#include "stdio.h"

// Encabezados (headers) de funciones
int suma_entera(int, int);
float suma_flotante(float, float);

// funcion principal
int main()
{
    printf("%i\n", suma_entera(1, 2));
    printf("%f\n", suma_flotante(1.2, 3.4));
}

// implementacion de funciones
int suma_entera(int a, int b)
{
    return a+b;
}

float suma_flotante(float a, float b)
{
    return a+b;
}