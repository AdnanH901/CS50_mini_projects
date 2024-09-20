#include <cs50.h>
#include <stdio.h>

int llamas_growth(int strts, int ends);

int main(void)
{
    int strts, ends;
    do
    {
        strts = get_int("Start size: ");
    }
    while (strts < 9);
    do
    {
        ends = get_int("End size: ");
    }
    while (ends < strts);
    printf("Years: %i\n", llamas_growth(strts, ends));
}

int llamas_growth(int s, int e)
{
    int yrs = 0;
    while (s < e)
    {
        s += (s / 3) - (s / 4);
        // TRUNCUATION HAPPENS HERE [Don't sneakily do s += s/12 or s = (13*s)/12
        // as (13*9)/12 = 117/12 = 9.75 which when appliead by int stuff makes it 9. Similar for s += s/12]
        printf("%i\n", s);
        yrs++;
    }
    return (yrs);
}

// population