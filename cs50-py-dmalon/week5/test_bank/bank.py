def main():
    userInput = input("Greeting: ")
    greeting = value( userInput)
    str = f"${greeting}"
    print(str)    

def value(greeting):
    if greeting.strip('"\'').strip().casefold().startswith("Hello".casefold()):
        return int(0)
    elif greeting.strip().casefold().startswith("H".casefold()):
        return int(20)
    else:
        return int(100)

if __name__ == "__main__":
    main()