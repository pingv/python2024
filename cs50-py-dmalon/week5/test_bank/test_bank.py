# pytest -v test_bank.py
# pytest test_bank.py

from bank import value

def test_value_hello():
    assert value("Hello") == 0

def test_value_startswith_H():
    assert value("Howdy!") == 20

def test_value_totally_different():
    assert value("Hell Ya!") == 20
    assert value("Kaise Ho Ji!") == 100
    assert value("What’s up") == 100
    

