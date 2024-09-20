#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int CL(int letter, int words, int sentences);

int main(void)
{
    string text = get_string("Text: ");
    int grade = CL(count_letters(text), count_words(text), count_sentences(text));
    if (grade <= 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int count_letters(string text)
{
    int letters_counter = 0;
    for (int ti = 0; ti < strlen(text); ti++)
    {
        if (isalpha(text[ti]))
        {
            letters_counter++;
        }
    }
    return letters_counter;
}

int count_words(string text)
{
    int words_counter = 0;
    for (int ti = 0; ti < strlen(text); ti++)
    {
        if (text[ti] == ' ' || (ti == (strlen(text) - 1) && (text[ti] == '.' || text[ti] == '?' || text[ti] == '!')))
        {
            words_counter++;
        }
    }
    return words_counter;
}

int count_sentences(string text)
{
    int sentence_counter = 0;
    for (int ti = 0; ti < strlen(text); ti++)
    {
        if (text[ti] == '.' || text[ti] == '?' || text[ti] == '!')
        {
            sentence_counter++;
        }
    }
    return sentence_counter;
}

int CL(int letter, int words, int sentences)
{
    float L = 100 * letter / (float) words;
    float S = 100 * sentences / (float) words;
    return round(0.0588 * L - 0.296 * S - 15.8);
}