#include "stdio.h"

int variable_global = 10;

int una_funcion()
{
    int variable_local = 2;

    printf("f: Global = %i, Local = %i\n", variable_global, variable_local);

    return 0;
}

int main()
{
    int variable_local = 1;

    
    printf("1: Global = %i, Local = %i\n", variable_global, variable_local);

    {
        int variable_interna = 3;        
        printf("2: Global = %i, Local = %i, Interna %i\n", variable_global, variable_local, variable_interna);
    }

    {
        int variable_interna = 4;       
        printf("3: Global = %i, Local = %i, Interna %i\n", variable_global, variable_local, variable_interna);
    }

    una_funcion();

    return 0;

}