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