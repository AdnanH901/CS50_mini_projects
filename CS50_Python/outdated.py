months = {  "January":  1,
           "February":  2,
              "March":  3,
              "April":  4,
                "May":  5,
               "June":  6,
               "July":  7,
             "August":  8,
          "September":  9,
            "October": 10,
           "November": 11,
           "December": 12 }
def main():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                dl1 = [int(i) for i in date.split("/")]
                # Splits numebrs into a list containing elements of type str. Then converts said elements into int.
                if 1 <= dl1[0] <= 12 and 1 <= dl1[1] <= 31 and 0 <= dl1[2] <= 9999:
                    print(f"{dl1[2]:04}-{dl1[0]:02}-{dl1[1]:02}")
                    break
            elif "," in date:
                dl2 = date.replace(',', "").split()
                if dl2[0].isalpha() and 1 <= int(dl2[1]) <= 31 and dl2[1].isnumeric() and 0000 <= int(dl2[2]) <= 9999 and dl2[2].isnumeric():
                    dl2 = [int(dl2[2]),months[dl2[0]],int(dl2[1])]
                    # Changes date from month day, year to a list [year, month, day] of type int.
                    print(f"{dl2[0]:04}-{dl2[1]:02}-{dl2[2]:02}")
                    break
        except ValueError:
            pass
        except EOFError:
            break
main()