#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string encrypt(char letter, string key);
void encrypt_text(string text, string key);
bool omnialpha(string s);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        if (omnialpha(argv[1]) && strlen(argv[1]) == 26)
        {
            string text = get_string("plaintext: ");
            printf("ciphertext: ");
            encrypt_text(text, argv[1]);
            printf("\n");
            return 0;
        }
        else
        {
            printf("Key must contain 26 characters.");
            return 1;
        }
    }
    else
    {
        printf("Usage: ./substitution key");
        return 1;
    }
}

char encrypt_letter(char letter, string key)
{
    string al = "abcdefghijklmnopqrstuvwxyz";
    string au = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    for (int li = 0; li < 26; li++)
    {
        if (letter == al[li])
        {
            return tolower(key[li]);
        }
        else if (letter == au[li])
        {
            return toupper(key[li]);
        }
    }
    return letter;
}

void encrypt_text(string text, string key)
{
    for (int li = 0; li < strlen(text); li++)
    {
        printf("%c", encrypt_letter(text[li], key));
    }
}

bool omnialpha(string s)
{
    for (int i = 0; i < strlen(s); i++)
    {
        if (!isalpha(s[i]))
        {
            return false;
        }
    }
    return true;
}