#include "stdio.h"
#include "./complejo.h"

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

    //número complejo, magnitud, angulo
    printf(" a = %f + %f*i\n",a_comp.re,a_comp.im);
    printf("\n");
    printf("* Magnitud: %f\n", magnitud(a_comp) );
    printf("* Angulo: %f\n", angulo(a_comp) );

    //conjugado de un complejo
    complejo b_comp = conjugado(a_comp);
    printf("* Conjugado:  %f + %f*i\n",b_comp.re,b_comp.im);

    complejo e_comp;
    //logaritmo de complejos
    e_comp = logaritmo(a_comp);
    printf("* logaritmo natural ln(a): %f + %f*i\n",e_comp.re,e_comp.im);

    //seno de complejos
    e_comp = seno(a_comp);
    printf("* seno sin(a): %f + %f*i\n",e_comp.re,e_comp.im);

    //coseno de complejos
    e_comp = coseno(a_comp);
    printf("* coseno cos(a): %f + %f*i\n",e_comp.re,e_comp.im);

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

    //suma de complejos
    complejo d_comp = suma(a_comp,c_comp);
    printf("* Suma a+c:  %f + %f*i\n",d_comp.re,d_comp.im);

    //multiplicación de complejos
    d_comp = multiplicacion(a_comp,c_comp);
    printf("* multiplicacion a*c:  %f + %f*i\n",d_comp.re,d_comp.im);

    //división de complejos
    d_comp = division(a_comp,c_comp);
    printf("* division a/c:  %f + %f*i\n",d_comp.re,d_comp.im);

    //potenica de complejos
    d_comp = potencia(a_comp,c_comp);
    printf("* potencia a^c: %f + %f*i\n",d_comp.re,d_comp.im);

    //logaritmo de complejos
    d_comp = logaritmo(c_comp);
    printf("* logaritmo natural ln(c): %f + %f*i\n",d_comp.re,d_comp.im);

    //seno de complejos
    d_comp = seno(c_comp);
    printf("* seno sin(c): %f + %f*i\n",d_comp.re,d_comp.im);

    //coseno de complejos
    d_comp = coseno(c_comp);
    printf("* coseno cos(c): %f + %f*i\n",d_comp.re,d_comp.im);

    return 0;
}