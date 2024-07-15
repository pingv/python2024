def main():
    
    name = "Hello, World!"
    name = "  ~!~!  World Wide Web   "
    name = "aeiou!"
    name = "What's your name?"
    name = "CS50"
    name = input("Input: ")
    stripped_str = shorten( name )
    print("Output: ", stripped_str)  # Output: "He, Wrd!"

def shorten( word ):
    remove_chars = "aeiouAEIOU"

    # Overwriting to fail test cases
    # remove_chars = "aeiou"
    translation_table = str.maketrans("", "", remove_chars)
    new_string = word.translate(translation_table)
    return new_string

if __name__ == "__main__":
    main()