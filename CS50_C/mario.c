#include <cs50.h>
#include <stdio.h>

void repeat(char c, int rep);
void mario(int h);

int main(void)
{
    int h;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);
    mario(h);
}

void mario(int h)
{
    char hash = '#';
    char space = ' ';
    for (int i = h - 1; i >= 0; i--)
    {
        repeat(space, i);
        repeat(hash, h - i);
        printf("  ");
        repeat(hash, h - i);
        printf("\n");
    }
}

void repeat(char c, int rep)
{
    for (int r = 0; r < rep; r++)
    {
        printf("%c", c);
    }
}