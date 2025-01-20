def getUserInput():
    while mode_correct := True:
        user_string = input("Enter a string: ")
        write_mode = input("Enter write mode (w or a): ")
        if write_mode in ["a", "w"]:
            break
        else:
            print("Invalid write mode. Please use 'w' or 'a'.")
    return user_string, write_mode


def writeToFile(fileName, user_input, write_mode):
        with open("user_input.txt", write_mode) as file:
            # file.write(user_input + "\n")
            file.write(f"{user_input}\n")
            file.close()


def main():
    user_input, write_mode = getUserInput()
    writeToFile("user_input.txt", user_input, write_mode)

if __name__ == "__main__":
    main()