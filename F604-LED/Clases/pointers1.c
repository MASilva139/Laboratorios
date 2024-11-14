#include "stdio.h"
#include "stdlib.h"

int* reserva_entero( unsigned short n )
{
    return (int*) malloc( n * sizeof(int) );
}

int modifica( int *bloque, unsigned short n, int valor)
{
    bloque[n] = valor;
    return 0;
}

int main()
{
    int *a_ptr;
    unsigned short tamanio = 3;

    a_ptr = reserva_entero(tamanio);

    for(int i=0; i<=tamanio; i++)
        printf("%i\n",a_ptr[i]);

    
    for(int i=0; i<=tamanio; i++)
        modifica(a_ptr, i, i+1 );

    
    for(int i=0; i<=tamanio; i++)
        printf("%i\n",a_ptr[i]);

}
