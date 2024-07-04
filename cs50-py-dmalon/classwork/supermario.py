def main():
    print_square(3)

def print_square(size):
    for i in range (size):
        for j in range (size):
            print("#", end="")
        print("\n", end="")


    # print_row(3)
    # print_column(3)
    
    

def print_column(height):
    print("#\n" * height, end="")


def print_row(width):
    print("#" * width, end="")    

main()