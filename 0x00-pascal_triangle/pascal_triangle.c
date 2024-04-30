#include <stdio.h>
#include <stdlib.h>

// Function to generate a single row of Pascal's triangle
int* generate_pascal_row(int row_num, int* prev_row, int prev_row_length) {
    int* new_row = (int*)malloc((row_num + 1) * sizeof(int));
    new_row[0] = 1; // First element of the row is always 1
    new_row[row_num] = 1; // Last element of the row is always 1

    // Calculate the values for the middle elements of the row
    for (int i = 1; i < row_num; i++) {
        new_row[i] = prev_row[i - 1] + prev_row[i];
    }

    return new_row;
}

// Function to generate Pascal's triangle up to n rows
int** generate_pascal_triangle(int n) {
    int** triangle = (int**)malloc(n * sizeof(int*));
    
    // Generate each row of the triangle
    for (int i = 0; i < n; i++) {
        triangle[i] = generate_pascal_row(i, triangle[i - 1], i);
    }

    return triangle;
}

// Function to print Pascal's triangle
void print_pascal_triangle(int** triangle, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            printf("%d ", triangle[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int num_rows = 5;
    // printf("Enter the number of rows for Pascal's triangle: ");
    // scanf("%d", &num_rows);

    int** triangle = generate_pascal_triangle(num_rows);
    print_pascal_triangle(triangle, num_rows);

    return 0;
}
