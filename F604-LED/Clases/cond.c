#include "stdio.h"

int main()
{
    // if

    char var_1 = 0;
    int var_2 = 10;
    double var_3 = 3.14;

    if(var_2) 
        printf("if : La variable es diferente de cero\n");
    else
        printf("if : La variable es cero\n");

    // ternario

    printf( ( var_1 ? "? : La variable es diferente de cero\n" : "? : La variable es cero\n" ) );

    // switch - case

    var_1 = 'e';

    switch (var_1)
    {
    case 'a':
        printf("switch : El caracter es a\n");
        break;
    case 'b':
        printf("switch : El caracter es b\n");
        break;
    case 'c':
        printf("switch : El caracter es c\n");
        break;
    default:
        printf("switch : El caracter no es a, b o c\n");
        break;
    }

    return 0;
}