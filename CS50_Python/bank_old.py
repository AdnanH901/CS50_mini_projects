def main():
    greet = str(input("Greeting: ")).strip()

    # Extracts the first 5 characters in greet, ideally hello.
    hello_condition = greet[0: 5]

    if hello_condition == "hello" or hello_condition == "Hello":
      print("$0")
    elif hello_condition[0] == "h" or hello_condition[0] == "H":
        print("$20")
    else:
        print("$100")
main()



