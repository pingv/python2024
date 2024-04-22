print("Hello World")

i = 1
while(i<=5):
    print(i)
    i = i+1



def my_function():
  print("Hello from a function")

my_function()

def vishnus_fun():
    print("GIG")
    print("vaule if i is: ", i)
    print("Value of i in string: " + str(i))

vishnus_fun()

fruits = ["apple", "orange", "guava", "papaya", "banana"]
#print(fruits.pop())
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[0:100])

print("For loop...START")
for item in fruits:
    print(item)
print("For loop...DONE")

a_bool = "a".endswith("x")

print(a_bool)

a_string = "some string"

print(a_string, a_bool)
exit(0)

list_of_numbers = [10, 20, 30, 40, 50, 60, 78]
print(list_of_numbers)
list_of_numbers.insert(7, "vis")
print("inserted", list_of_numbers)