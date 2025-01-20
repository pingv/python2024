def readFromFile(fileName):
    names = []
    with open(fileName, "r") as file:
        for line in file:
            names.append(line.strip())

    for name in sorted(names):
        print(f"Hello v1, {name}")
def readFromFile_sortAtFile(fileName):
    names = []
    with open(fileName, "r") as file:
        for line in sorted(file):
            print(f"Hello v2, {line.strip()}")

def readFromFile_sortReverseAtFile(fileName):
    names = []
    with open(fileName, "r") as file:
        for line in sorted(file, reverse=True):
            print(f"Hello v3, {line.strip()}")


def readFromFile_csv(fileName):
    import csv
    with open(fileName, "r") as file:
        for line in file:
            # Too many values to unpack
            # name, house = line.strip().split(",")
            line_parts = line.strip().split(",")
            print(f"Full Row: , {line.strip()}")

            # This only gets the characters in the line
            # print(f"Hello v4, {line[0]}")
            # print(f"Hello v4, {line[1]}")
            # print(f"Hello v4, {line[2]}")

            print(f"name: , {line_parts[0]}")
            print(f"house: , {line_parts[1]}")
            print(f"address: , {line_parts[2]}")
def readFromFile_csv_lib_reader(fileName):
    import csv
    with open(fileName, "r") as file:
        reader = csv.reader(file) #csv.reader is a simple iterator so the headers are not considered
        for row in reader:
            # print(f"Full Row: {', '.join(row)}")
            print(f"Name: {row[0]}")
            print(f"House: {row[1]}")
            print(f"Address: {row[2]}")

def readFromFile_csv_lib_DictReader(fileName):
    import csv
    with open(fileName, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # refer via the header instead of index
            print(f"~~~ ^^^ ~~~")
            print(f"Name: {row['Name']}")
            print(f"House: {row['House']}")
            print(f"Address: {row['Address']}")


def get_name(row):
    return row['Name']


def readFromFile_csv_lib_DictReader_sorted_nolambda(fileName):
    import csv
    with open(fileName, "r") as file:
        reader = csv.DictReader(file)
        # Convert reader to list and sort by Name using the get_name function
        sorted_rows = sorted(reader, key=get_name)

        for row in sorted_rows:
            print(f"~~~ ^^^ ~~~")
            print(f"Name: {row['Name']}")
            print(f"House: {row['House']}")
            print(f"Address: {row['Address']}")

def readFromFile_csv_lib_DictReader_sorted_lambda(fileName):
    import csv
    with open(fileName, "r") as file:
        reader = csv.DictReader(file)
        # Convert reader to list and sort by Name using the get_name function
        sorted_rows = sorted(reader, key=lambda row: row['Name'])

        for row in sorted_rows:
            print(f"~~~ ^^^ ~~~")
            print(f"Name: {row['Name']}")
            print(f"House: {row['House']}")
            print(f"Address: {row['Address']}")

def main():
    # print("~~~ v1 ~~~")
    # readFromFile("user_input.txt")
    # print("~~~ v2 ~~~")
    # readFromFile_sortAtFile("user_input.txt")
    # print("~~~ v3 ~~~")
    # readFromFile_sortReverseAtFile("user_input.txt")
    # print("~~~ v4 No library ~~~")
    # readFromFile_csv("harry_potter_characters.csv")
    # print("~~~ v5 Using CSV Plain Reader library ~~~")
    # readFromFile_csv_lib_reader("harry_potter_characters.csv")
    # print("~~~ v6 Using CSV Dict Reader library ~~~")
    # readFromFile_csv_lib_DictReader("harry_potter_characters.csv")
    # print("~~~ v7 Using CSV Dict Reader library with sorting without lambda ~~~")
    # readFromFile_csv_lib_DictReader_sorted_nolambda("harry_potter_characters.csv")
    print("~~~ v8 Using CSV Dict Reader library with sorting with lambda ~~~")
    readFromFile_csv_lib_DictReader_sorted_lambda("harry_potter_characters.csv")


if __name__ == "__main__":
    main()
