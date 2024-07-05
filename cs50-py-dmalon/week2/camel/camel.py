def main():
    # camelCase = "name"
    # camelCase = "camelCase"
    # camelCase = "firstName"
    # camelCase = "lastNameIs"
    #camelCase = "testVariable123"
    #camelCase = "preferredFirstName"

    camelCase = input("camelCase: ")
    camelCase = camelCase.strip()

    snake_case = ''

    for char in camelCase:
        # print(char)
        if char.isupper():
            snake_case = snake_case + "_" + char.lower()
        else:
            snake_case = snake_case + char

    print("snake_case: ", snake_case, sep='')



main()
