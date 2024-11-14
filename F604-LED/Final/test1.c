#include "stdio.h"
#include "complejo.h"

int main()
{
    complejo a_comp;
    a_comp.re = 1.1;
    a_comp.im = 2.2;

    fijar_formato(POLAR);

    printf(" a = %s\n",mostrar(a_comp));
    printf("Magnitud: %f\n", magnitud(a_comp) );
    printf("Angulo: %f\n", angulo(a_comp) );

    complejo b_comp = conjugado(a_comp);

    printf("Conjugado:  %s\n",mostrar(b_comp));

    complejo c_comp;

    c_comp.re = 3.3;
    c_comp.im = 4.4;
    printf(" c = %s\n",mostrar(c_comp));

    complejo d_comp = suma(a_comp,c_comp);

    printf("Suma a+c:  %s\n",mostrar(d_comp));

    d_comp = multiplicacion(a_comp,c_comp);

    printf("multiplicacion a*c:  %s\n",mostrar(d_comp));

    d_comp = divicion(a_comp,c_comp);

    printf("divicion a/c:  %s\n",mostrar(d_comp));

    return 0;
    
}