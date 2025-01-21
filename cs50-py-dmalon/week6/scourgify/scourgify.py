def main():
    import sys
    import csv

    # check command line arguments
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    # read csv file
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            students = list(reader)
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

    # create new csv file
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for student in students:
            last, first = student["name"].split(", ")  # Note the reversal here
            writer.writerow({
                "first": first,
                "last": last,
                "house": student["house"]
            })


if __name__ == "__main__":
    main()