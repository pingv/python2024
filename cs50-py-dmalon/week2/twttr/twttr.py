def main():
    
    name = "Hello, World!"
    name = "  ~!~!  World Wide Web   "
    name = "aeiou!"
    name = "What's your name?"
    name = "CS50"

    name = input("Input: ")
    remove_chars = "aeiouAEIOU"
    translation_table = str.maketrans("", "", remove_chars)
    new_string = name.translate(translation_table)
    print("Output: ", new_string)  # Output: "He, Wrd!"

main()