#include <stdio.h>
#include <stdlib.h>
#include "mylib.h"

char *get_string(void)
{
    char *str = malloc(100);

    if (str == NULL)
    {
        return NULL;
    }

    printf("Nome: ");
    scanf("%99s", str);

    return str;
}

// gcc hello.c mylib.c -o hello --> Compila o arquivo que usa a função e mylib.c 