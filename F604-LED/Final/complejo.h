#ifndef __COMPLEJO_H__
#define __COMPLEJO_H__

typedef struct complejo_s
{
    double re;
    double im;
} complejo;


typedef struct vector_complejo_s
{
    short size;
    complejo* data;
} vector_complejo;

typedef enum formato_e
{
    CARTESIANO,
    POLAR
} formato_t;

char* mostrar( complejo );
int fijar_formato(formato_t);

double magnitud( complejo );
double angulo(  complejo );
complejo conjugado( complejo );
complejo suma( complejo, complejo );
complejo resta( complejo, complejo );
complejo multiplicacion( complejo, complejo );
complejo division( complejo, complejo );

vector_complejo* vector_complejo_inicializar( unsigned short tamanio );
int vector_complejo_liberar( vector_complejo* );
short vector_complejo_tamanio( vector_complejo* );
complejo vector_complejo_obtener( vector_complejo*, unsigned short n );
int vector_complejo_asignar( vector_complejo*, unsigned short n, complejo valor );
complejo vector_complejo_ppunto( vector_complejo*, vector_complejo* );

#endif