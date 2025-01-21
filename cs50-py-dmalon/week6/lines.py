

def countLinesofCode(filename):
    loc = 0
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() != "" and not line.strip().startswith("#"):
                loc+= 1
        return loc

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

    if not filename.endswith(".py"):
        print("Not a Python file")
        exit(1)

def checkFileExists(filename):
    # try to check if file exists
    try:
        open(filename)
    except FileNotFoundError:
        print("File does not exist")
        exit(1)

def main():
    import sys
    fileNamePath = checkArgs(sys.argv)
    checkFileType(fileNamePath)
    checkFileExists(fileNamePath)
    loc = countLinesofCode(fileNamePath)
    print(f"{loc} lines in {fileNamePath}")

if __name__ == "__main__":
    main()

