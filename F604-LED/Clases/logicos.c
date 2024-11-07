#include "stdio.h"
#include "stdlib.h"



int main()
{
    int A =  0;
    int B = 10;
    int C = 20;

    // operadores relacionales <, >, <=, >=, !=, ==
    if(A<B)
        printf("A es menor que B\n");

    // operador && (AND)
    if( ( A<B ) && ( B<C ) )
        printf("A<B<C\n");

    // operador || (OR)
    if( ( A<B ) || ( B<C ) )
        printf( "A<B o B<C\n");

    // operador ! (NOT)
    if( !A )
        printf("A tiene un valor asignado nulo\n");

    return 0;
}