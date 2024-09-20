import sys
from tabulate import tabulate
import csv

def main():
    try:
        files = sys.argv
        files_length = len(files)
        if files_length < 2:
            raise IndexError
        elif files_length > 2:
            sys.exit("Too many command-line arguments")
        else:
            print(tableify(files[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")
    except IndexError:
        sys.exit("Too few command-line arguments")

def sys_len_check(length = len(sys.argv)):
    if   length < 2:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")
    else:
        pass


def file_info(file):
    return f"{file}".capitalize().rsplit(".")


def tableify(file):
    table_list = []
    if file.endswith(".csv"):
        with open(f"{file}") as menu:
            file_name, file_type = f"{file}".capitalize().rsplit(".")
            menu_dict = csv.DictReader(menu)
            for row in menu_dict:
                table_list.append({f"{file_name} Pizza": row[f"{file_name} Pizza"], "Small": row["Small"], "Large": row["Large"]})
            return tabulate(table_list, headers = "keys", tablefmt = "grid")
    else:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()

### Test 1 ###
# python pizza.py

### Test 2 ###
# python pizza.py regular.csv sicilian.csv

### Test 3 ###
# python pizza.py invalid_file.csv

### Test 4 ###
# python pizza.py sicilian.txt

### Test 5 ###
# python pizza.py regular.csv