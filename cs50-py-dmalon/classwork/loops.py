print("While Loop")
i = 0
while(i < 3):
    print(i)
    i += 1


print("While Loop - break")
i = 0
while True:
    if i > 3:
        break
    print(i)
    i += 1


print("For loop using ()")
for i in (1, 2, 3):
    print(i)

print("For loop using []]")
for i in [1, 2, 3]:
    print(i, end="###")

print("For loop using Range")
for i in range(1, 3+1):
    print(i)

print("For *")
print("Hello \n" *  3)

print("For *")
print("Hello \n" *  3, end="")
