def convert(userinput):
    print(userinput.strip().replace(":)", "\U0001F642").replace(":(", "\U0001F641"))

def main():
    #userinput = "Hello :) Goodbye :("
    userinput = input("Enter a text : ")
    print("User Input : ", userinput)
    convert(userinput)

main()