def main():
    message = input("Input: ")
    # Displays Output: message without a,e,i,o,u,A,E,I,O,U
    print(f"Output: {shorten(message)}")


def shorten(text):
    '''
    Locates any vowels in a given string and removes it from the string.
    '''
    new_text = ""
    for letter in text:
        match letter: # Checks if a given letter is a vowel and removes it.
            case "a" | "A" | "e" | "E" | "i" | "I" | "o" | "O" | "u" | "U":
                letter = ""
        new_text += letter
    return new_text


if __name__ == "__main__":
    main()