#include "complejo.h"
//#include "stdio.h"
#include "math.h"

double magnitud( complejo comp )
{
    return sqrt( pow( comp.re ,2 ) + pow( comp.im, 2 ) );
}

double angulo( complejo comp )
{
    return atan2( comp.im , comp.re );
}

complejo conjugado( complejo comp )
{
    complejo aux;
    aux.re = comp.re;
    aux.im = -comp.im;
    return aux;
}

complejo suma( complejo comp_a, complejo comp_b )
{
    complejo aux;
    aux.re = comp_a.re + comp_b.re;
    aux.im = comp_a.im + comp_b.im;
    return aux;
}

complejo resta( complejo comp_a, complejo comp_b )
{
    complejo aux;
    aux.re = comp_a.re - comp_b.re;
    aux.im = comp_a.im - comp_b.im;
    return aux;
}

complejo multiplicacion( complejo comp_a, complejo comp_b )
{
    complejo aux;
    aux.re = ( comp_a.re * comp_b.re ) - ( comp_a.im * comp_b.im );
    aux.im = ( comp_a.re * comp_b.im ) + ( comp_a.im * comp_b.re );
    return aux;
}

complejo division( complejo comp_a, complejo comp_b )
{
    complejo aux1, aux2, aux3;
    aux1 = conjugado( comp_b );
    aux2 = multiplicacion( comp_a , aux1 );
    double mag_b = magnitud( comp_b );
    aux3.re = aux2.re/pow(mag_b,2);
    aux3.im = aux2.im/pow(mag_b,2);
    return aux3;
}

complejo potencia(complejo comp_a, complejo comp_b)
{ 
    // Se considerara un complejo (Z=a+bi) elevado respecto a otro complejo (Z1=x+yi)
    // De la identidad de Euler se tiene que Z^Z1 = [abs(a+bi)*exp(io)]^(x+yi)
    double mbase = magnitud(comp_a); //magnitud del número de base
    double abase = angulo(comp_a);  //ángulo del número de base
    double ereal = comp_b.re;  //parte real del exponente
    double eimag = comp_b.im;  // parte imaginaria del exponente
    double mres = pow(mbase, ereal)*exp(-eimag*abase); //magnitud de la potencia
    double ares = ereal*abase + eimag*log(mbase); //ángulo de la potencia

    complejo aux; //Resultado de la operación
    //Polar -> Rectangular
    aux.re = mres*cos(ares);
    aux.im = mres*sin(ares);
    return aux;
}

complejo logaritmo(complejo comp_a)
{
    //El logaritmo de un complejo es ln(Z)=ln(abs[z])+i*o
    double mag = magnitud(comp_a); // Magnitud del número complejo
    double ang = angulo(comp_a); // Ángulo del número complejo

    complejo aux; // Resultado
    aux.re = log(mag); //Parte real del logaritmo
    aux.im = ang;
    return aux;
}

complejo seno(complejo z)
{
    //Definición sen(z)=sen(a)cos(bi)+sen(bi)cos(a); además, 2i*sen(a)= exp[ia]-exp[-ia]
    //Con ello: sen(ai)=i*senh(a), cos(ai)=cosh(a)
    complejo aux;
    aux.re = sin(z.re)*cosh(z.im);
    aux.im = cos(z.re)*sinh(z.im);
    return aux;
}

complejo coseno(complejo z)
{
    //Definición cos(z)=cos(a)cos(bi)-sen(bi)sen(a); además, 2*cos(a)= exp[ia]+exp[-ia]
    //Con ello: sen(ai)=i*senh(a), cos(ai)=cosh(a)
    complejo aux;
    aux.re = cos(z.re)*cosh(z.im);
    aux.im = -sin(z.re)*sinh(z.im);
    return aux;
}