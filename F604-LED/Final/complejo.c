#include "complejo.h"
#include "stdio.h"
#include "math.h"
#include "stdlib.h"

static formato_t formato;

char* mostrar(complejo comp)
{
    /* Esta funcion produce un "memory leak" 
     * ya que la memoria que reserva al no ser liberada por
     * medio de la instruccion free, permanece "bloqueda"
     * hasta que el programa finaliza su ejecucion.
     * En este ejemplo se opta por hacerlo de esta forma
     * por simplesa y por que el programa no va a correr
     * de forma permanente, que es cuando el memory
     * leak se vuelve un problema.
     */

    char* buffer = (char*) malloc(100);

    switch (formato)
    {
    case CARTESIANO:
        sprintf(buffer,"(%f, %f)",comp.re,comp.im);
        break;
    case POLAR:
        double mag = magnitud( comp );
        double ang = angulo( comp );
        sprintf(buffer,"(%f < %f)",mag,ang);
        break;
    
    default:
        break;
    }
    

    return buffer;

}

int fijar_formato(formato_t valor)
{
    formato = valor;
}

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


vector_complejo* vector_complejo_inicializar( unsigned short tamanio )
{
    vector_complejo *v_comp = (vector_complejo*) malloc(sizeof(vector_complejo));

    if(!v_comp)
    {
        printf("vector_complejo_inicializar: Fallo la reserva de memoria\n");
        return 0;
    }

    v_comp->data = (complejo*) malloc( tamanio * sizeof(complejo) );

    if(!(v_comp->data))
    {
        printf("vector_complejo_inicializar: Fallo la reserva de memoria\n");
        v_comp->size = 0;
        return 0;
    }

    v_comp->size = tamanio;
    return v_comp;

}

int vector_complejo_liberar( vector_complejo* v_comp )
{
    free( v_comp->data );
    free( v_comp );
    return 0;
}

short vector_complejo_tamanio( vector_complejo *v_comp )
{
    return v_comp->size;
}

complejo vector_complejo_obtener( vector_complejo *v_comp, unsigned short n )
{
    complejo aux;

    if( n <= v_comp->size)
        aux = (v_comp->data)[n];
    else
    {
        printf("vector_complejo_obtener: Valor fuera de rango\n");
        aux.re = 0;
        aux.im = 0;
    }

    return aux;
}

int vector_complejo_asignar( vector_complejo *v_comp, unsigned short n, complejo valor )
{
    if( n <= v_comp->size )
    {
        (v_comp->data)[n] = valor;
        return 0;
    }

    printf("vector_complejo_asignar: Valor fuera de rango\n");
    return 1;
}

complejo vector_complejo_ppunto( vector_complejo* v_comp_A, vector_complejo* v_comp_B)
{
    complejo aux;
    aux.re = 0;
    aux.im = 0;

    if( v_comp_A->size != v_comp_B->size)
    {
        printf("vector_complejo_ppunto: Los vectores son de diferente tamaño\n");
        return aux;
    }

    for(int i = 0 ; i< v_comp_A->size; i++)
        aux = suma( aux, multiplicacion( (v_comp_A->data)[i],(v_comp_B->data)[i] ) );
    return aux;
}

matrix_complejo* matrix_complejo_inicializar(int row, int col){
    matrix_complejo* matrix = (matrix_complejo*)malloc(sizeof(matrix_complejo));
    if (!matrix){
        printf("Error al asignar memoria para la estructura matriz.\n");
        return NULL;
    }
    matrix->row = row; //filas de la matriz
    matrix->col = col; //columans de la matriz
    matrix->data = (complejo**)malloc(row * sizeof(complejo*));
    if (!matrix->data){
        printf("Error al asignar memoria para las filas de la matriz.\n");
        free(matrix);
        return NULL;
    }
    for (int i = 0; i < row; i++){
        matrix->data[i] = (complejo*)malloc(col * sizeof(complejo));
        if (!matrix->data[i]){
            printf("Error al asignar memoria para las columans de la fila %d.\n", i);
            //Liberar la memoria ya asignada antes de salir
            for (int j=0; j<i; j++){
                free(matrix->data[j]);
            }
            free(matrix->data);
            free(matrix);
            return NULL;
        }
    }
    return matrix;
} //Inicializa la matriz dinámica

void matrix_complejo_liberar(matrix_complejo* matrix){
    for (int i=0; i<matrix->row; i++){
        free(matrix->data[i]); //liberar la memoria de cada fila de la matriz "data"
    }
    free(matrix->data); // Libera el arreglo de punteros "data" que almacena las filas.
    free(matrix); // Libera la estructura la estructura de la matriz
} //Liberar la memoria asignada

matrix_complejo* matrix_complejo_producto(matrix_complejo* m1, matrix_complejo* m2){
    if (m1->col != m2->row){
        printf("Error: \n las dimensiones de las matrices no permiten la multiplicación.\n");
        return NULL;
    } //Dimensiones diferentes -> error de la multiplicación de matrices
    matrix_complejo* res = matrix_complejo_inicializar(m1->row, m2->col); //matriz resultado con m1 filas y m2 columnas
    for (int i =0; i < m1->row; i++){
        for (int j=0; j < m2->col; j++){
            res->data[i][j].re = 0; //Genera una parte real a partir de cada posición i,j
            res->data[i][j].im = 0; //Genera una parte imaginaria a partir de cada posición i,j
            for (int k=0; k<m1->col; k++){
                complejo prod = multiplicacion(m1->data[i][k], m2->data[k][j]); //Producto entre los elementos de m1 y m2
                res->data[i][j] = suma(res->data[i][j], prod); //Suma el resultado en la posición (i,j) de res
            }
        }
    }
    return res;
} //Producto entre matrices de números complejos