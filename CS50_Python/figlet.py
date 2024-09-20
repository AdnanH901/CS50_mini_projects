from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


def main():
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    except IndexError:
        # This is the case where no desired font is given.
        figlet.setFont(font=random.choice(figlet.getFonts()))
    figlet_text = figlet.renderText(input("Input: "))
    print(figlet_text)

if __name__ == "__main__":
    main()
