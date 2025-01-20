def readFromFile(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()

    for line in lines:
        print(f"Hello, {line.strip()}")


def main():
    readFromFile("user_input.txt")


if __name__ == "__main__":
    main()
