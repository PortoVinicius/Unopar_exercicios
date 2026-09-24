// get_string and printf with incorrect placeholder

#include <stdio.h>

int main(void) {
    printf("What's your name? ");

    char answer[20];
    scanf("%19s", answer);
    
    printf("hello, %s!\n", answer);

    return 0;
}