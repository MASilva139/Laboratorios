#include "stdio.h"

int funcion_entera(int a, int b)
{
    printf("a=%i, b=%i\n", a, b);
    // los valores de a y b son copias locales de los enviados.
    a=0;
    b=5;

    printf("a=%i, b=%i\n", a, b);

    return a+b;
}

// se pueden declarar funciones sin retorno

void funcion_sr(int a)
{
    printf("a=%i\n",a);

    return;
}

int main()
{
    int A=10;
    int B=20;

    printf("A=%i, B=%i\n", A, B);

    int C=funcion_entera(A,B);

    printf("C=%i\n", C);

    printf("A=%i, B=%i\n", A, B);

    funcion_sr(A);

    return 0;

}