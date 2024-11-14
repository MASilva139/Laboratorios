# EXAMEN FINAL
## Instrucciones:
A partir del código que se encuentra en la carpeta complejo2 de codes, extender el archivo complejo.h y complejo.c para incluir lo siguiente:
* Una estructura (struct) que aloje los datos de una matriz de $`n\times m`$.  
* Una función que realice el producto de dos matrices.
Ademas se debe crear un archivo .c donde se incluyan los archivos modificados y se muestre el funcionamiento de la estructura y funcion añadida.

Se debe subir un archivo comprimido con los archivos de código fuente.

## Resolución
* Código de `complejo.c`
```
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
}

void matrix_complejo_liberar(matrix_complejo* matrix){
    for (int i=0; i<matrix->row; i++){
        free(matrix->data[i]); //liberar la memoria de cada fila de la matriz "data"
    }
    free(matrix->data); // Libera el arreglo de punteros "data" que almacena las filas.
    free(matrix); // Libera la estructura la estructura de la matriz
}

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
}
```
* código de `complejo.h`
```
typedef struct matrix_complejo_s{
    int row;
    int col;
    complejo** data;
} matrix_complejo;

matrix_complejo* matrix_complejo_inicializar(int row, int col);
void matrix_complejo_liberar(matrix_complejo*);
matrix_complejo* matrix_complejo_producto(matrix_complejo* m1, matrix_complejo* m2);
```
* Código de `test.c` (documento *main*)
```
#include "complejo.h"
#include "stdio.h"
#include "stdlib.h"

void dim(int* row, int* col, const char* name){
    printf("Ingresar el número de filas de la matriz %s: ", name);
    scanf("%d", row);
    printf("ingresar el número de columnas de la matriz %s: ", name);
    scanf("%d", col);
}
void d_matrix(matrix_complejo* matrix, const char* name){
    for (int i=0; i < matrix->row; i++){
        for (int j=0; j < matrix->col; j++){
            printf("Ingresar parte real de %s[%d][%d]: ", name, i, j);
            scanf("%lf", &matrix->data[i][j].re);
            printf("Ingresar parte imaginaria de %s[%d][%d]: ", name, i, j);
            scanf("%lf", &matrix->data[i][j].im);
        }
    }
}
void m_print(matrix_complejo* matrix){
    for (int i=0; i<matrix->row; i++){
        for (int j=0; j<matrix->col; j++){
            printf("(%f + %fi) ", matrix->data[i][j].re, matrix->data[i][j].im);
        }
        printf("\n");
    }
}
int main(int argc, char *argv[]){
    int row1, col1, row2, col2;
    printf("Multiplicación de matrices complejas\n");

    dim(&row1, &col1, "m1");
    dim(&row2, &col2, "m2");
    if (col1 != row2){
        printf("Error: las dimensiones de las matrices no permiten la multiplicación.\n");
        return 1;
    }
    matrix_complejo* m1 = matrix_complejo_inicializar(row1, col1);
    matrix_complejo* m2 = matrix_complejo_inicializar(row2, col2);

    printf("\n");
    printf("Llenando valores de la matriz m1:\n");
    d_matrix(m1, "m1");
    printf("\n");
    m_print(m1);

    printf("\n");
    printf("Llenando valores de la matriz m2:\n");
    d_matrix(m2, "m2");
    printf("\n");
    m_print(m2);

    matrix_complejo* res = matrix_complejo_producto(m1, m2);

    printf("\n");
    if (res){
        printf("Producto entre las matrices m1 y m2:\n");
        m_print(res);
    }

    matrix_complejo_liberar(m1);
    matrix_complejo_liberar(m2);
    matrix_complejo_liberar(res);

    return 0;
}
```