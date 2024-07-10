# imports everything
import random
import sys

# import specific package
from random import randint
from statistics import mean
from statistics import median
from statistics import mode

toss = random.choice(["heads", "tails"])

print("Toss: ", toss)


print("Rand_Int: ", randint(2,10))

print("Statistics Mean: ", mean([100,200]))
print("Statistics Median: ", median([100,200]))
print("Statistics Mode: ", mode([100,200]))

# slicing start from index 1 to end:
print("My name is ", sys.argv[1:])

for arg in sys.argv:
    print("Hello tags : ", arg)

# slicing start from index 1 and end before 1 before
for arg in sys.argv[1 : -1]:
    print("Hello tags w.o prgm name: ", arg)

if(len(sys.argv) < 2):
    sys.exit("Too few args")
elif(len(sys.argv) > 2):
    sys.exit("Too many args")
else:
    print("My name is ", sys.argv[1])

