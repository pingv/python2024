def e_convert_mc2(userinput):
    mass = int(userinput)
    #print("Mass in Integer: ", mass)
    energy = mass * pow(300000000, 2);
    print("Energy is : ", energy)

def main():
    #userinput = "Hello :) Goodbye :("
    userinput = input("Enter Mass to calculate Energy : ")
    #print("User Input : ", userinput)
    e_convert_mc2(userinput)

main()