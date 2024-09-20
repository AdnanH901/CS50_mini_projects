import random


def main():
    qn = 1 # The question number.
    score = 0 # The current score that the user has achieved.
    level = get_level()
    chance = 1 # Chances they have till the correct answer is displayed.
    while True:
        try:
            if qn < 11: # Ensures a total of only 10 questions are given.
                if chance == 1:
                    X = generate_integer(level)
                    Y = generate_integer(level)
                    answer = int(input(f"{X} + {Y} = "))
                    if answer == X + Y:
                        score += 1
                        qn += 1 # Generates next question.
                    else:
                        raise ValueError
                elif chance <= 3:
                    answer = int(input(f"{X} + {Y} = "))
                    if answer == X + Y:
                        score += 1
                        qn += 1 # Generates next question.
                    else:
                        raise ValueError
                else:
                    print(f"{X} + {Y} = {X + Y}")
                    qn += 1 # Generates next question.
                    chance = 1 # Resets chances as a new question will now be given.
                    pass
            else:
                print("Score: ", score)
                break
        except ValueError:
            chance += 1
            print("EEE")
            pass
        except EOFError:
            break


def get_level():
    """
    Returns level 1, 2 or 3. Asks for the level
    again if the level <= 0 or 4 <= level.
    """
    while True:
        lvl = input("Level: ")
        if lvl in ["1", "2", "3"]:
            return int(lvl)
        else:
            pass


def generate_integer(level):
    return random.randint( 40*level**2 - 110*level + 70, 10**level - 1)
    # Generates a random number between 0 - 9 if level is 1.
    # Generates a random number between 10 - 99 if level is 2.
    # Generates a random number between 100 - 999 if level is 3.

if __name__ == "__main__":
    main()
