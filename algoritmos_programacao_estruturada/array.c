#include <stdio.h>

void print_column(int height);

int main(void) {
    int n;
    printf("Higth: ");
    scanf("%d", &n);

    print_column(n);
    return 0;
}

void print_column(int height) {

    for (int i = 0; i < height; i++) {
        printf("%d\n", i);
    }
}
    
