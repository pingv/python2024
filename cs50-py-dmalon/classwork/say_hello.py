def main():
    name = input("what's your name: ")
    print( say_hello( name ) )
    print( say_hello() )

def say_hello(to = "world"):
    str = f"Hello, {to}"

    # a function must return a value to make it a testable code
    return str 

if __name__ == "__main__":
    main()