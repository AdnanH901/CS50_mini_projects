import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ipa := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        return 0 <= int(ipa.group(1)) <= 255 and 0<= int(ipa.group(2)) <= 255 and 0<= int(ipa.group(3)) <= 255 and 0<= int(ipa.group(4)) <= 255
    else:
        return False



if __name__ == "__main__":
    main()