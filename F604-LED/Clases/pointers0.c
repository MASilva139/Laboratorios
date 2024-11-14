#include "stdio.h"


int main()
{
    int a = 0x41414141;
    int *a_ptr = &a;
    float *float_ptr = (float*)a_ptr;
    char *char_ptr = (char*)a_ptr;

    printf("El valor de a es: %i\n",a);
    printf("La dirección de memoria de a es: %p\n",a_ptr);
    printf("El valor de a obtenido desde a_ptr es: %i\n",*a_ptr);
    printf("El valor de a obtenido desde double_ptr es: %f\n",*float_ptr);
    printf("El valor de a obtenido desde double_ptr es: %s\n",char_ptr);

}