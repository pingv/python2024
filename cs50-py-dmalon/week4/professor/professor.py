'''
In a file called professor.py, implement a program that:

- Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
- Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer 
with 𝑛 digits. No need to support operations other than addition (+).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), 
the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. 
If the user has still not answered correctly after three tries, the program should output the correct answer.
- The program should ultimately output the user’s score: the number of correct answers out of 10.

'''

from random import randint

def main():
    level = get_level()
    print("Level:", level)

    questions = generate_integer(level)
    score = 0

    for i, (x, y) in enumerate(questions, start=1):
        correct_answer = x + y
        print(f"{x} + {y} = ?")

        attempt = 0
        for attempt in range(3):
            answer = input()

            if answer.isdigit() and int(answer) == correct_answer:
                score += 1
                break
            else:
                print("EEE")
                if attempt == 2:
                    print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        n = input("Enter a number (1, 2, or 3): ")
        if n.isdigit() and int(n) in (1, 2, 3):
            return int(n)
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

def generate_integer(level):
    if level <= 0:
        raise ValueError("Number of digits must be a positive integer.")

    math_add_questions = []
    if level == 1:
        range_start = 0
    else:
        range_start = 10 ** (level - 1)

    range_end = (10 ** level) - 1

    for _ in range(10):
        random_x_value = randint(range_start, range_end)
        random_y_value = randint(range_start, range_end)
        math_add_questions.append((random_x_value, random_y_value))

    return math_add_questions

if __name__ == "__main__":
    main()
