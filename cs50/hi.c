#include <stdio.h>
#include <stdlib.h>

char *get_string(void);

int main(void)
{
    char *name;

    name = get_string();

    printf("Nome: %s\n", name);

    free(name);

    return 0;
}

char *get_string(void)
{
    char *n = malloc(100 * sizeof(char));

    if (n == NULL)
    {
        return NULL;
    }

    printf("Name: ");
    scanf("%99s", n);

    return n;
}
