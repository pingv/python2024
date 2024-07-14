from calculator import square
# pip install pytest
# pytest test_calculator_pytest.py
import pytest

def main():
    test_square_positive()
    test_square_negative()
    test_square_zero()
    test_str()

def test_square_positive():
    print("Start test_square_positive...")
    assert square(2) == 4
    assert square(3) == 9

def test_square_negative():
    print("Start test_square_negative...")
    assert square(-2) == 4
    assert square(-3) == 9

def test_square_zero():
    print("Start test_square_zero...")
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()