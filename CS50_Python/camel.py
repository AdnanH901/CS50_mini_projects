def main():
    camel = input("camelCase: ")
    print(snake_case(camel))

def snake_case(string):
    s= ""
    for char in string:
        if char.isupper():
            char = f"_{char.lower()}"
        s += char
    return s
main()

