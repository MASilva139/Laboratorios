#include "stdio.h"
#include "complejo.h"
#include "math.h"

int main()
{
    vector_complejo *vect_comp_a = vector_complejo_inicializar( 3 );
    vector_complejo *vect_comp_b = vector_complejo_inicializar( 3 );
    
    printf("Tamaño asignado al vector: %i\n",vector_complejo_tamanio(vect_comp_a));

    // fijar_formato(CARTESIANO);

    complejo aux;

    for(int i = 0; i<3; i++)
    {   
        aux.re = i;
        aux.im = 3-i;
        vector_complejo_asignar(vect_comp_a, i, aux);
        aux.re = 3-i;
        aux.im = i;
        vector_complejo_asignar(vect_comp_b, i, aux);
    }

    complejo aux2;
    for(int i = 0; i<3; i++)
    {
        aux = vector_complejo_obtener(vect_comp_a, i);
        aux2 = vector_complejo_obtener(vect_comp_b, i);
        printf("a = %s; b = %s \n", mostrar(aux), mostrar(aux2));
    }

    aux = vector_complejo_ppunto( vect_comp_a, vect_comp_b);
    printf("Producto punto (interno) A.B = %s\n", mostrar(aux));

    vector_complejo_liberar( vect_comp_a );
    vector_complejo_liberar( vect_comp_b );
    printf("Tamaño asignado al vector: %i\n",vector_complejo_tamanio(vect_comp_a));

    return 0;
}
