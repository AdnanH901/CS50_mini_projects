// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);
bool digit(string s);
bool alpha(string s);
bool lower(string s);
bool upper(string s);
bool punct(string s);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    return digit(password) && alpha(password) && lower(password) && upper(password) && punct(password);
}

bool digit(string s)
{
    for (int li = 0; li < strlen(s); li++)
    {
        if isdigit (s[li])
        {
            return true;
        }
    }
    return false;
}

bool alpha(string s)
{
    for (int li = 0; li < strlen(s); li++)
    {
        if isalpha(s[li])
        {
            return true;
        }
    }
    return false;
}

bool lower(string s)
{
    for (int li = 0; li < strlen(s); li++)
    {
        if islower (s[li])
        {
            return true;
        }
    }
    return false;
}

bool upper(string s)
{
    for (int li = 0; li < strlen(s); li++)
    {
        if isupper (s[li])
        {
            return true;
        }
    }
    return false;
}

bool punct(string s)
{
    for (int li = 0; li < strlen(s); li++)
    {
        if ispunct (s[li])
        {
            return true;
        }
    }
    return false;
}
