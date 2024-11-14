#include "stdio.h"
#include "complejo.h"

int main()
{
    complejo a_comp;
    /*
    a_comp.re = 1.1;
    a_comp.im = 2.2;
    */
    printf("Introducir la parte real del primer número complejo: ");
    scanf("%lf", &a_comp.re);
    printf("Introducir la parte imaginaria del primer número complejo: ");
    scanf("%lf", &a_comp.im);
    printf("\n");

    fijar_formato(POLAR);

    printf(" a = %s\n",mostrar(a_comp));
    printf("Magnitud: %f\n", magnitud(a_comp) );
    printf("Angulo: %f\n", angulo(a_comp) );

    complejo b_comp = conjugado(a_comp);

    printf("Conjugado:  %s\n",mostrar(b_comp));

    complejo c_comp;
    /*
    c_comp.re = 3.3;
    c_comp.im = 4.4;
    */
    printf("\n\n");
    printf("Introducir la parte real del segundo número complejo: ");
    scanf("%lf", &c_comp.re);
    printf("Introducir la parte imaginaria del segundo número complejo: ");
    scanf("%lf", &c_comp.im);
    printf("\n");
    printf(" c = %f + %f*i\n",c_comp.re,c_comp.im);
    printf("\n");
    printf(" c = %s\n",mostrar(c_comp));

    complejo d_comp = suma(a_comp,c_comp);
    printf("Suma a+c:  %s\n",mostrar(d_comp));

    d_comp = multiplicacion(a_comp,c_comp);
    printf("Multiplicacion a*c:  %s\n",mostrar(d_comp));

    d_comp = division(a_comp,c_comp);
    printf("Division a/c:  %s\n",mostrar(d_comp));

    //potenica de complejos
    d_comp = potencia(a_comp,c_comp);
    printf("* potencia a^c: %s\n",mostrar(d_comp));

    //logaritmo de complejos
    d_comp = logaritmo(c_comp);
    printf("* logaritmo natural ln(c): %s\n",mostrar(d_comp));

    //seno de complejos
    d_comp = seno(c_comp);
    printf("* seno sin(c): %s\n",mostrar(d_comp));

    //coseno de complejos
    d_comp = coseno(c_comp);
    printf("* coseno cos(c): %s\n",mostrar(d_comp));

    return 0;
    
}