def main():
    userInput = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

    if userInput.strip().casefold() in ("42".casefold(), "forty-two".casefold(), "forty two".casefold()):
        print("Yes")
    else:
        print("No")

"""
    if userInput.casefold() == "42" or userInput == "forty-two" or userInput == "forty two":
        print("Yes")
    else:
        print("No")
"""

main()
