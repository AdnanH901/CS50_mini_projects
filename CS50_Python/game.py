import random

while True:
    try:
        n = int(input("Level: "))
        random_number = random.randint(1, n)
        break
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if random_number < guess <= n:
            print("Too large!")
        elif 0 < guess < random_number:
            print("Too small!")
        elif guess == random_number:
            print("Just right!")
            break
        elif guess == 0:
            pass
        else:
            raise EOFError
    except ValueError:
        pass
    except EOFError:
        break