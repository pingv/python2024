from calculator import square

def main():
    test_square()

def test_square():
    print("Start Testing...")
    if square(2) != 4:
        print("2 squared must be 4")
    if square(3) != 9:
        print("3 squared must be 9")
    print("Test cases run")

    print("Better call Assert...")

    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared must be 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared must be 9")

    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared must be 9")

    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared must be 0")


if __name__ == "__main__":
    main()