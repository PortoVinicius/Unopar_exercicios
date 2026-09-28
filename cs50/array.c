#include <stdio.h>

int print_array(int number[], int size);

int main(void) {
    int number[] = {7, 4, 6, 8};

    print_array(number, 4);
    printf("\n");
    return 0;
}

int print_array(int number[], int size) {
    
    for (int i = 0; i < size; i++) {
        printf("%i", number[i]);
    }
}

