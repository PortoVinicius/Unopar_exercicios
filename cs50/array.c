#include <stdio.h>

int print_array(int number[], int size);
int soma_array(int number[], int size);

int main(void) {
    int number[] = {7, 4, 6, 8};

    print_array(number, 4);
    int soma = soma_array(number, 4);
    printf("soma = %i\n", soma);

    return 0;
}


int print_array(int number[], int size) {
    
    for (int i = 0; i < size; i++) {
        printf("%i", number[i]);
    }
    printf("\n");
}


int soma_array(int number[], int size) {
    int soma = 0;

    for (int i = 0; i < size; i++) {
        soma += number[i];
    }

    return soma;
}
