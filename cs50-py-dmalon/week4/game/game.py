'''
In a file called game.py, implement a program that:

Prompts the user for a level, 
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
Hints
Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.
'''

import random, sys

def main():

    n = 1
    while True:
        n = input("Level: ")
        if n.isdigit() and int(n) > 0:
            n = int(n)
            break

    random_value = random.randint(1, n)
    # generate the random number between 1 & n    
    # print(random_value)
    
    while True:
        guess = input("Guess: ")
        if guess.isdigit():
            guess = int(guess)

            if guess < random_value:
                print("Too small!")
                continue
            elif guess > random_value:
                print("Too large!")
                continue
            else:
                print("Just right!")
                sys.exit(0)
        else:
            continue


if __name__ == "__main__":
    main()