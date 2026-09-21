#include<stdio.h>

int main(void) {
    int linha;
    do {
        printf("Linhas: ");
        scanf("%d", &linha);
    } while (0 > linha);

    for (int i = 0; i < linha; i++) {
        printf("%d\n", i);
    }

    printf("Linhas: "); 
    printf("%d\n", linha);
}