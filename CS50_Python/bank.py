def main():
    sen = input("Input: ")
    num = value(sen)
    print(f"${num}")


def value(greeting):
    hello_condition = greeting.lower().strip()[0:5]
    if hello_condition == "hello":
        return 0
    elif hello_condition[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()