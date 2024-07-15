import pytest
from fuel import convert, gauge

def test_convert():
    # Test valid inputs
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99

    # Test edge cases
    assert convert("0/1") == 0
    assert convert("1/1") == 100

    # Test invalid inputs
    with pytest.raises(ValueError):
        convert("abc/def")
    with pytest.raises(ValueError):
        convert("1.5/2.5")
    with pytest.raises(ValueError):
        convert("2/1")  # X greater than Y
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Division by zero

def test_gauge():
    # Test fuel gauge readings
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

if __name__ == "__main__":
    pytest.main()
