def main():
    tankSize = getInput()

    if tankSize <= 1:
        print("E")
    elif tankSize >= 99:
        print("F")
    else:
        print(f"{tankSize}%")


def getInput():
    while True:
        try:
            fraction = input("Fraction: ").strip().split('/')
            intX = int(fraction[0])
            intY = int(fraction[1])

            decimal_value = eval(f"{intX} / {intY}")
            percentage = round(decimal_value * 100) 

            if intX > intY:
                # print("Percentage cannot be greater than 100.")
                continue
        except ValueError:
            # print("Either X or Y not an integer")
            continue
        except ZeroDivisionError:
            # print("Y must be > than ZERO.")
            continue
        else:
            break
    
    # print("percentage:  ", percentage)
    return percentage


main()
