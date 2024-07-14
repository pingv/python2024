# % pytest test_say_hello.py

from say_hello import say_hello

def test_say_hello():
    say_hello("Vishnu") == "Hello, Vishnu"

def test_say_hello_default():
    say_hello() == "Hello, World"
