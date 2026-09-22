#include<stdio.h>

int main(void) {
    int linha;
    do {
        printf("Linhas: ");
        scanf("%d", &linha);
    } while (0 > linha);

    for (int i = 0; i < linha; i++) {

        printf("*");

        for (int j = 0; j < i; j++) {
            printf("*");
           
        }
        printf("\n");
    }
}