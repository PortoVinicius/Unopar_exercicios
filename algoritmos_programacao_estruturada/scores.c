#include <stdio.h>

int main(void) {
    // Get scores Usando loop
    int scores[3];

    for (int i = 0; i < 3; i++) {
        printf("Score: ");
        scanf("%d", &scores[i]);
    }

    // Print average
    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);

}