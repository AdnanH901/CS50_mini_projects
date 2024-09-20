import csv
import sys


def main():
    try:
        files_length = len(sys.argv)
        if files_length < 3:
            raise IndexError
        elif files_length > 3:
            sys.exit("Too many command-line arguments")
        else:
            before_to_after(csv_to_dict(sys.argv[1]))
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    except IndexError:
        sys.exit("Too few command-line arguments")


def csv_to_dict(file_path):
    names_dict = {}
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            names_dict[row['name']] = row
    return names_dict

def before_to_after(file_name):
    with open(f"{sys.argv[2]}", "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        for full_name, name_dict in file_name.items():
            last_name, first_name = name_dict['name'].rsplit(", ")
            writer.writerow({"first": first_name, "last": last_name, "house": name_dict['house']})


if __name__ == "__main__":
    main()

# python scourgify.py before.csv after.csv