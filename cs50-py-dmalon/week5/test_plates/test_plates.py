from plates import is_valid

def test_is_valid():
    is_valid("CS50") == True

def test_is_valid_CS05():
    is_valid("CS05") == False

def test_is_valid_PI3():
    is_valid("PI3.14") == False

def test_is_valid_H():
    is_valid("H") == False

def test_is_valid_OUTATIME():
    is_valid("OUTATIME") == False
