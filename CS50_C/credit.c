#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string credit_type(long num);
bool luhn(long num);

int main(void)
{

    long credit_number = get_long("Number: ");
    if (luhn(credit_number))
    {
        printf("%s\n", credit_type(credit_number));
    }
    else
    {
        printf("INVALID\n");
    }
}

bool luhn(long num)
{
    int sum = 0;
    long dup_num = num;
    long num13 = num / 1000000000000;
    long num15 = num / 100000000000000;
    long num16 = num / 1000000000000000;
    num /= 10;
    while (num > 0)
    {
        int digit = 2 * (num % 10);
        num /= 100;
        sum += digit % 10 + digit / 10;
    }
    while (dup_num > 0)
    {
        int digit = dup_num % 10;
        dup_num /= 100;
        sum += digit;
    }
    return sum % 10 == 0;
}

string credit_type(long num)
{
    long num13_1 = num / 1000000000000;
    long num13_2 = num / 100000000000 % 10;
    long num15_1 = num / 100000000000000;
    long num15_2 = num / 10000000000000 % 10;
    long num16_1 = num / 1000000000000000;
    long num16_2 = num / 100000000000000 % 10;
    if (num15_1 == 3 && (num15_2 == 4 || num15_2 == 7))
    {
        return "AMEX";
    }
    else if (num16_1 == 5 && (num16_2 == 1 || num16_2 == 2 || num16_2 == 3 || num16_2 == 4 || num16_2 == 5))
    {
        return "MASTERCARD";
    }
    else if (num16_1 == 4 || num13_1 == 4)
    {
        return "VISA";
    }
    else
    {
        return "INVALID";
    }
}