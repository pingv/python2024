name = input("What's your name: ")

# Just keep overwriting
'''
file = open("harry-potter.txt", "w")
'''

# Append data
a_file = open("harry-potter.txt", "a")
# a_file.write(name + "\n")
a_file.write(f"{name}\n")
a_file.close()

# Simpler way - no need close etc. its all auto closed
with open("harry-potter.txt", "a") as a_file:
    a_file.write(f"{name}\n")
