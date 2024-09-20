// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

void replace(string word);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./no-vowels word\n");
        return 1;
    }
    else
    {
        replace(argv[1]);
        printf("\n");
    }
}

void replace(string word)
{
    for (int letter_index = 0, len = strlen(word); letter_index < len; letter_index++)
    {
        char letter = word[letter_index];
        switch (letter)
        {
            case 'a':
                printf("6");
                break;
            case 'e':
                printf("3");
                break;
            case 'i':
                printf("1");
                break;
            case 'o':
                printf("0");
                break;
            default:
                printf("%c", letter);
        }
    }
}

// no-vowels