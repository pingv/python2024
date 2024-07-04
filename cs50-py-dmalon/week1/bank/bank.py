def main():
    userInput = input("Greeting: ")

    if userInput.strip('"\'').strip().casefold().startswith("Hello".casefold()):
        print("$0")
    elif userInput.strip().casefold().startswith("H".casefold()):
        print("$20")
    else:
        print("$100")

main()