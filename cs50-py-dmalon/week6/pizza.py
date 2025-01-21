# pip install tabulate

from tabulate import tabulate

def checkArgs(args):
    if len(args) < 2:
        print("Too few command-line arguments")
        exit(1)
    elif len(args) > 2:
        print("Too many command-line arguments")
        exit(1)
    return args[1]

def checkFileType(filename):
    # check if file is a python file, gonna leave an empty line below for testing

    if not filename.endswith(".csv"):
        print("Not a CSV file")
        exit(1)

def checkFileExists(filename):
    # try to check if file exists
    try:
        open(filename)
    except FileNotFoundError:
        print("File does not exist")
        exit(1)

def read_csv(file_name):
    import csv
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        # convert reader to list and print
        table = list(reader)
        print(tabulate(table, headers="keys", tablefmt="grid"))

def test_tabulate():
    headers = ["Planet", "Radius (km)", "Mass (kg)"]
    table = [["Sun", 696000, 1989100000], ["Earth", 6371, 5973.6],
             ["Moon", 1737, 73.5], ["Mars", 3390, 641.85]]
    print(tabulate(table, headers, tablefmt="grid"))
def main():
    import sys
    # test_tabulate()
    file_name_path = checkArgs(sys.argv)
    checkFileType(file_name_path)
    checkFileExists(file_name_path)
    read_csv(file_name_path)

if __name__ == "__main__":
    main()