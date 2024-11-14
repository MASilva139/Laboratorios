// Test de la multiplicación de matrices
#include "complejo.h"
#include "stdio.h"
#include "stdlib.h"

void dim(int* row, int* col, const char* name){
    printf("Ingresar el número de filas de la matriz %s: ", name);
    scanf("%d", row);
    printf("ingresar el número de columnas de la matriz %s: ", name);
    scanf("%d", col);
} //Número de dimensiones de la matriz nxm

void d_matrix(matrix_complejo* matrix, const char* name){
    for (int i=0; i < matrix->row; i++){
        for (int j=0; j < matrix->col; j++){
            printf("Ingresar parte real de %s[%d][%d]: ", name, i, j);
            scanf("%lf", &matrix->data[i][j].re);
            printf("Ingresar parte imaginaria de %s[%d][%d]: ", name, i, j);
            scanf("%lf", &matrix->data[i][j].im);
        }
    }
} // Valores de la matriz nxm

void m_print(matrix_complejo* matrix){
    for (int i=0; i<matrix->row; i++){
        for (int j=0; j<matrix->col; j++){
            printf("(%f + %fi) ", matrix->data[i][j].re, matrix->data[i][j].im);
        }
        printf("\n");
    }
} //Imprimir matriz

int main(int argc, char *argv[]){
    int row1, col1, row2, col2;
    //row1=2, col1=2, row2=2, col2=2;

    printf("Multiplicación de matrices complejas\n");

    // Dimensiones de las matrices m1 y m2
    dim(&row1, &col1, "m1");
    dim(&row2, &col2, "m2");

    // validación para la multiplicación de matrices m1 y m2
    if (col1 != row2){
        printf("Error: las dimensiones de las matrices no permiten la multiplicación.\n");
        return 1;
    }

    // Inicializar las matrices m1 y m2
    matrix_complejo* m1 = matrix_complejo_inicializar(row1, col1);
    matrix_complejo* m2 = matrix_complejo_inicializar(row2, col2);

    //Valores de la primer matriz m1
    /*
    m1->data[0][0].re = 1; m1->data[0][0].im = 1;
    m1->data[0][1].re = 2; m1->data[0][1].im = 2;
    m1->data[1][0].re = 3; m1->data[1][0].im = 3;
    m1->data[1][1].re = 4; m1->data[1][1].im = 4;
    */
    printf("\n");
    printf("Llenando valores de la matriz m1:\n");
    d_matrix(m1, "m1");
    printf("\n");
    m_print(m1);

    //Valores de la segunda matriz m2
    /*
    m2->data[0][0].re = 5; m2->data[0][0].im = 5;
    m2->data[0][1].re = 6; m2->data[0][1].im = 6;
    m2->data[1][0].re = 7; m2->data[1][0].im = 7;
    m2->data[1][1].re = 8; m2->data[1][1].im = 8;
    */
    printf("\n");
    printf("Llenando valores de la matriz m2:\n");
    d_matrix(m2, "m2");
    printf("\n");
    m_print(m2);

    // Producto de matrices
    matrix_complejo* res = matrix_complejo_producto(m1, m2);

    //Resultado del producto entre matrices
    /*
    printf("Resultado de la multiplicación de matrices:\n");
    for (int i = 0; i < res->row; i++) {
        for (int j = 0; j < res->col; j++) {
            printf("(%f + %fi) ", res->data[i][j].re, res->data[i][j].im);
        }
        printf("\n");
    }
    */
    printf("\n");
    if (res){
        printf("Producto entre las matrices m1 y m2:\n");
        m_print(res);
    }

    // Liberación de memoria
    matrix_complejo_liberar(m1);
    matrix_complejo_liberar(m2);
    matrix_complejo_liberar(res);

    return 0;
}