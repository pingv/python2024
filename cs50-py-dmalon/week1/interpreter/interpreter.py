def main():
    user_prompt = "Enter the arithmetic operation in the format as X Y Z ...\n"
    user_prompt += "where x is an integer, y is +, -, *, or /, and z is an integer: "
    user_input = input(user_prompt)
    
    # check x & z are integer, else fail
    # z must not be zero if y is /
    # check if y is +, -, *, or /, else fail
    # o/p as floating point, one decimal place

    try:
        intX, operand, intZ = user_input.split()

        
        intX = int(intX)
        intZ = int(intZ)

        if isinstance(intX, int) and isinstance(intZ, int) and operand in ['+', '-', '*', '/'] and not (operand is '/' and intZ is 0):
                #print("Result: ", eval(f"{intX} {operand} {intZ}"))
                print("Result: {:.1f}".format(eval(f"{intX} {operand} {intZ}")))
        else:
            print("Error: Invalid input or operand 222")
    except ValueError:
        print("Error: Invalid input format. Please enter integers only.")


    #print("Result: {:.1f}".format(10.00012212))

main()