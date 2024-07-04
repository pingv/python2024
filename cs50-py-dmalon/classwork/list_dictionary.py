students = ["Hermione", "Ron", "Harry", "Draco"]

print("--- using _ instead of a variable ---")
for _ in students:
    print(_)

print("--- for x in xs func ---")
for student in students:
    print(student)

print("--- range func ---")
for i in range (len(students)): #range must be a number so must get a length
    print(students[i])


print("--- range func print # ---")
for i in range (len(students)): #range must be a number so must get a length
    print(i+1, students[i])    

# Now dictionary

students = ["Hermione", "Ron", "Harry", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


print("--- multi list range func print # ---")
for i in range (len(students)): #range must be a number so must get a length
    print(i+1, students[i], houses[i], sep=" -> ")


studentsDictionary = {
    "Hermione" : "Gryffindor", 
    "Ron" : "Gryffindor", 
    "Harry" : "Gryffindor", 
    "Draco" : "Slytherin"
}

print("--- dictionary range func print # ---")
for a_student in studentsDictionary: #range must be a number so must get a length
    print( a_student, " -> ", studentsDictionary[a_student])


#Multi dictionary - An Array or dictionary


array_of_dicts = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "Diana", "age": 28, "city": "Los Angeles"},
    {"name": "Ethan", "age": 32, "city": "Boston"}
]

for person in array_of_dicts:
    print(person)

for person in array_of_dicts:
    print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

studentsMultiDictionary = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "otter"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Jack Russell Terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
]

for students in studentsMultiDictionary:
    print(f"NAME: {students['name']}, HOUSE: {students['house']}, PATRONUS: {students['patronus']}")
