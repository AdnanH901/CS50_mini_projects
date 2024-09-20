import sys
from PIL import Image, ImageOps


def main():
    try:
        args = sys.argv
        if checks(args):
            shirt_replacemnet(args)
    except FileNotFoundError:
        print("Input does not exist")

def int_endswith(arg1, arg2, phrase):
    return arg1.endswith(phrase) and arg2.endswith(phrase)

def un_endswith(arg1, arg2, phrase):
    return arg1.endswith(phrase) and arg2.endswith(phrase)

def same_ext(args):
     return int_endswith(args[1], args[2], ".jpg") or int_endswith(args[1], args[2], ".jpeg") or int_endswith(args[1], args[2], ".png")

def diff_ext(arg):
    return arg.endswith(".png") or arg.endswith(".jpg") or arg.endswith(".jpeg")

def checks(args):
    # Checks if there are too many or too few inputs.
    if len(args) > 3:
        sys.exit("Too many command-line arguments")
    elif len(args) < 3:
        sys.exit("Too few command-line arguments")
    elif same_ext(args):
        return True
    elif diff_ext(args[1]) and diff_ext(args[2]):
        sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid output")

def shirt_replacemnet(args):
    shirt = Image.open("shirt.png")
    person = Image.open(args[1])
    cropped_photo = ImageOps.fit(person, size = shirt.size)
    cropped_photo.paste(shirt, shirt)
    cropped_photo.save(args[2])

if __name__ == "__main__":
    main()