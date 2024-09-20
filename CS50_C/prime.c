#include <cs50.h>
#include <stdio.h>

bool is_prime2(int min,int  max, int n);

int main(void)
{
    int min = get_int("Minimum: ");
    int max = get_int("Maximum: ");
    for (int num = min; num < max; num++)
    {
        if (is_prime2(min, max, num) && num != 1)
        {
            printf("%i\n", num);
        }
    }
}

bool is_prime2(int min, int  max, int n)
{
    if (n == 2 || n == 3)
    {
        return true;
    }
    else
    {
        if ((n % 2 != 0) && (n != 1))
        // Removes any even numbers and 1
        {
            for (int k = 3; k < n; k += 2)
            {
                if (n % k == 0)
                {
                    return false;
                }
            return true;
            }
        }
        return false;
    }
}

bool is_prime1(int min, int  max, int n)
{
    // Loop through every number {k: k ∈ [min, n], k ∈ ℕ} and see if n % k == 0.
    for (int k = 2; k < n; k++)
    {
    if (n % k == 0)
        {
            return false;
        }
    }
    return true;
}

