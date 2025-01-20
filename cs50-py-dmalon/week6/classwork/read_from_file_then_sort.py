def readFromFile(fileName):
    names = []
    with open(fileName, "r") as file:
        for line in file:
            names.append(line.strip())

    for name in sorted(names):
        print(f"Hello, {name}")

def main():
    readFromFile("user_input.txt")


if __name__ == "__main__":
    main()
