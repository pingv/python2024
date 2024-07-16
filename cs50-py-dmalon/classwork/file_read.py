# 
# Lets read the files now
#     
print("Approach --- 1")
with open("harry-potter.txt", "r") as a_file:
    a_lines = a_file.readlines()

for a_line in a_lines:
    print("hello, ", a_line.rstrip())


print("Approach --- 2")
# 
# Let's do the iterating simpler
#     

with open("harry-potter.txt", "r") as a_file:
    for a_line in a_file:
        print("hello, ", a_line.rstrip())


print("Approach --- 3 --- sorted")
#
# Let's read and sort
#

name_array = []

with open("harry-potter.txt", "r") as a_file:
    for a_line in a_file:
        if a_line.strip(): # ignore if the line has nothing
            name_array.append( a_line.rstrip() ) # adding to the array as each item

for name in sorted(name_array):
    print(f"hello, {name}")