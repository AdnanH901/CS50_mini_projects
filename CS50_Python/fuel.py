def main():
    frac = input("Input: ")
    percent = convert(frac)
    print(gauge(percent))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            X, Y = int(x), int(y)
            if X > Y:
                raise ValueError
            return round(X/Y*100)
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()