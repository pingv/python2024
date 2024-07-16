print("Try option 1 ---")

name_array = []

with open("harry-potter-class.txt", "r") as a_file:
    for a_line in a_file:
        if a_line.strip(): # ignore if the line has nothing
            row = a_line.rstrip().split(",")
            name_array.append( row ) # adding to the array as each item

for name in sorted(name_array):
    print(f"hello, {name[0]} is in {name[1]}")


print("Try option 2 ---")

students = []

with open("harry-potter-class.txt", "r") as a_file:
    for a_line in a_file:
        if a_line.strip(): # ignore if the line has nothing
            name, school = a_line.rstrip().split(",")
            students.append( f"hello, {name} is in {school}") # adding to the array as each item

for student in sorted(students):
    print(student)    

print("Try option 3 ---")

students_list = []

with open("harry-potter-class.txt", "r") as a_file:
    for a_line in a_file:
        if a_line.strip(): # ignore if the line has nothing
            name, school = a_line.rstrip().split(",")
            student = {"name" : name.strip(), "school" : school.strip()}
            students_list.append( student ) # adding the dictionary

def get_school(student):
    return student["school"]

def get_name(student):
    return student["name"]

for student in sorted(students_list, key=get_name):
    print( f"hello, {student['name']} is in {student['school']}" )       

print("Try option 4 ---")

# here without using the get_school but using lambda anonymous function
for student in sorted(students_list, key=lambda student: student['name']):
    print( f"hello, {student['name']} is in {student['school']}" )            