#ifndef __COMPLEJO_H__
#define __COMPLEJO_H__

typedef struct complejo
{
    double re;
    double im;
} complejo;


double magnitud( complejo );
double angulo(  complejo );
complejo conjugado( complejo );
complejo suma( complejo, complejo );
complejo resta( complejo, complejo );
complejo multiplicacion( complejo, complejo );
complejo divicion( complejo, complejo );
complejo potencia( complejo, complejo );
complejo logaritmo( complejo );
complejo seno( complejo );
complejo coseno( complejo );

#endif