from numb3rs import validate


def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True
    assert validate("0.0.0.0") == True


def test_invalid():
    assert validate("275.3.6.28") == False
    assert validate("4.6.300.23") == False
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False
    

def test_format():
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("") == False