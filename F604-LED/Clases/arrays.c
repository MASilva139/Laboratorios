#include "stdio.h"

int main()
{
    // Formas de declarar

    int a[10]; // arreglo de 10 enteros sin inicializar

    int b[10] = {0,1,2,3,4,5,6,7,8,9}; //arreglo de 10 enteros incializado

    int c[10] = {0}; // arreglo de 10 enteros inicializados a cero

    int d[] = {9,8,7,6,5,4,3,2,1,0}; // arreglo de 10 enteros inicializados. El tamanio del arreglo se determina por la inicializacion.

    for(int i=0 ; i<10 ; i++)
        printf("%i\t%i\t%i\t%i\n", d[i], c[i], b[i], a[i]);

    struct comp_t
    {
        float re;
        float im;
    };
    
    struct comp_t e[10];
    
    for(int i=0 ; i<10 ; i++)
    {
        e[i].re = 1/(i+1.0);
        e[i].im = 2/(i+2.0);
    }

    for(int i=0 ; i<10 ; i++)
        printf("( %f, %f )\n", e[i].re, e[i].im);


    // En el caso de arreglos de caracteres, hay otra forma de inicializacion.
    char f[] = "una cadena de caracteres";

    printf("%s\n", f);
}