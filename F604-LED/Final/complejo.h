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

typedef struct matrix_complejo_s{
    int row; //Número de filas
    int col; //Número de columnas
    complejo** data; //Matriz de números complejos
} matrix_complejo; //Encargada de almacenar la matriz de números complejos

typedef enum formato_e
{
    CARTESIANO,
    POLAR //función que realice el producto de dos 
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
complejo potencia( complejo, complejo );
complejo logaritmo( complejo );
complejo seno( complejo );
complejo coseno( complejo );

vector_complejo* vector_complejo_inicializar( unsigned short tamanio );
int vector_complejo_liberar( vector_complejo* );
short vector_complejo_tamanio( vector_complejo* );
complejo vector_complejo_obtener( vector_complejo*, unsigned short n );
int vector_complejo_asignar( vector_complejo*, unsigned short n, complejo valor );
complejo vector_complejo_ppunto( vector_complejo*, vector_complejo* );

matrix_complejo* matrix_complejo_inicializar(int row, int col); //Inicializa la matriz de complejos
void matrix_complejo_liberar(matrix_complejo*); //Libera la memoria de una matriz de complejos
matrix_complejo* matrix_complejo_producto(matrix_complejo* m1, matrix_complejo* m2); //Realiza el producto entre dos matrices de complejos

#endif