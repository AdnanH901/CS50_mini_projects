from validator_collection import checkers


def main():
    print(email_check(input("What's your email address? ")))


def email_check(email):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()