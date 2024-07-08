def main():
    x = getInput()
    print(f"1. x is {x}")

    simpleIn = getInput()
    print(f"2. x is {simpleIn}")


def getInput():
    while True:
        try:
            x = int(input("What's the input : "))
        except ValueError:
            print("x not an integer")
        else:
            break
            # return x
    return x

def getInputSimple():
    while True:
        try:
            return int(input("What's the input : "))
        except ValueError:
            print("x not an integer")

main()
