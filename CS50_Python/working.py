import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if time := re.search(r"^([0-9]{1,2}):([0-9]{2}) (AM|PM) to ([0-9]{1,2}):([0-9]{2}) (AM|PM)$", s):
            t1 = hour_conversion1(time, 3)
            t2 = hour_conversion1(time, 6)
            return f"{t1[0]:02}:{t1[1]:02} to {t2[0]:02}:{t2[1]:02}"
        elif time := re.search(r"^([0-9]{1,2}) (AM|PM) to ([0-9]{1,2}) (AM|PM)$", s):
            t1 = hour_conversion2(time, 2)
            t2 = hour_conversion2(time, 4)
            return f"{t1:02}:00 to {t2:02}:00"
        else:
            raise ValueError
    except ValueError:
        sys.exit("ValueError")


def hour_conversion1(time, x):
    if 0 <= int(time.group(x-1)) <= 59:
        if 0 <= int(time.group(x-2)) <= 11:
            if time.group(x) == "PM":
                return int(time.group(x-2)) + 12, int(time.group(x-1))
            else:
                return int(time.group(x-2)), int(time.group(x-1))
        elif int(time.group(x-2)) == 12:
            if time.group(x) == "AM":
                return 0, 0
            elif time.group(x) == "PM":
                return 12, 0
        else:
            raise ValueError
    else:
        raise ValueError


def hour_conversion2(time, x):
    if 0 <= int(time.group(x-1)) <= 11:
        if time.group(x) == "PM":
            return int(time.group(x-1)) + 12
        else:
            return int(time.group(x-1))
    elif int(time.group(x-1)) == 12:
        if time.group(x) == "AM":
            return 0
        elif time.group(x) == "PM":
            return time.group(x-1)
    else:
        raise ValueError


if __name__ == "__main__":
    main()