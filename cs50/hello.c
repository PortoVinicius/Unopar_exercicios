#include <stdio.h>
#include <stdlib.h>
#include "mylib.h"

int main(void)
{
    char *name = get_string();

    if (name == NULL)
    {
        return 1;
    }

    printf("Olá, %s!\n", name);

    free(name);
}
