def main():
    
    location = {"x" : 0, "y" : 0}

    while True:
        direction, steps = get_command()
        steps = int(steps)
        direction = direction.lower()

        # 101 x 101 grid
        # start point (0,0)
        # x or y when >50 or <-50 => error fell off cliff

        if direction == "left":
            location["x"] -= steps
        elif direction == "right":
            location["x"] += steps
        elif direction == "up":
            location["y"] += steps
        elif direction == "down":
            location["y"] -= steps

        print(f"Current Location: {location}")

        x = location["x"]
        y = location["y"]

        if x < -50 or x > 50 or y < -50 or y > 50  :
            print("Fell off the cliff")
            break

def get_command():
    x = input("What command? ")
    direction, steps, *extra = x.split()
    print(f"Directions: {direction}, steps: {steps}, extra: {extra}")
    return direction, steps

main()

'''
Pretend you’re writing a game where a robot moves on a 101x101 grid: -50 to +50 on the X-axis; +50 to -50 on the Y-axis. He starts from the center, located at the point (0, 0), and can move up, down, left or right. The robot can accept a command like:


UP 4


and moves that many number of steps in the given direction. All numbers must be positive, and the directions can be given in lowercase, uppercase or mixed case.


Your job is to write a program that repeatedly gives commands to the robot and has it print out where it is. If the robot goes over an edge of the grid, print the message “I fell off the edge!”, and end the program. The robot can also accept the QUIT command, that terminates the program. QUIT can also be given in any casing. Here are two sample runs:


I am at (0, 0)

What is your command, master? left 20

I am now at (-20, 0)

What is your command, master? up 40

I am now at (-20, 40)

What is your command, master? RIGHT 4

I am now at (-16, 40)

What is your command, master? DoWn 8

I am now at (-16, 32)

What is your command, master? Left 50

Whoops! I fell off the edge!


I am at (0, 0)

What is your command, master? left 20

I am now at (-20, 0)

What is your command, master? up 40

I am now at (-20, 40)

What is your command, master? RIGHT 4

I am now at (-16, 40)

What is your command, master? DoWn 8

I am now at (-16, 32)

What is your command, master? QUIT

Phew! I’m tired!


This is a bigger program that you’ve written before — when that happens, you should think of breaking it up into smaller pieces — smaller programs — FUNCTIONS! For this program, write 5 functions:


The move_robot(starting_pos, direction, steps) function takes the starting position of the robot, a direction, and the number of steps, and calls one of the following four functions to do its job:


move_robot_up(starting_pos, steps)

move_robot_down(starting_pos, steps)

move_robot_left(starting_pos, steps)

move_robot_right(starting_pos, steps)


The variable starting_pos is a list of two elements, [x, y], the position of the robot. Each function returns the ending position of the robot, or the special Python value None if it fell off.'''