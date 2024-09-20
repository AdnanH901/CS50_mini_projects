import sys


def main():
    file = sys.argv
    length = len(file)
    if length == 1:
        sys.exit("Too few command-line arguments")
    elif length >=3:
        sys.exit("Too many command-line arguments")
    else:
        if f"{file[1]}".endswith(".py"):
            print(loc(f"{file[1]}"))
        else:
            sys.exit(1)


def loc(python_file):
    lines_of_code = 0
    with open(python_file) as file:
        code = file.readlines()
        for line in code:
            if not (f"{line}".lstrip().startswith('#') or line == '\n' or len(line.strip()) < 1):
                lines_of_code += 1
        return lines_of_code


if __name__ == "__main__":
    main()


