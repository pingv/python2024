import re, string

def main():
    plate = input("Plate: ")
    # plate = "CS50"
    # plate = "ECTO88"
    # plate = "NRVOUS"
    # plate = "CS05"
    # plate = "CS50P2"
    # plate = "PI3.14"
    # plate = "H"
    # plate = "OUTATIME"

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (check_size_limit(s) and 
        check_first_two_ascii(s) and 
        check_first_number_zero(s) and 
        check_periods_punctuation(s) and 
        last_char_not_number_if_number(s)):
        return True
    return False

def check_size_limit(s):
    retVal = (2 <= len(s) <= 7)
    # print("check_size_limit : ", retVal)
    return retVal

def check_first_two_ascii(s):
    retVal = bool(re.match(r'^[A-Za-z]{2}', s))
    # print("check_first_two_ascii : ", retVal)
    return retVal

def check_first_number_zero(s):
    match = re.search(r'\d', s)
    retVal = not (match and match.group() == '0')
    # print("check_first_number_zero : ", retVal)
    return retVal

def check_periods_punctuation(s):
    # Define the set of punctuation characters
    punctuation = set(string.punctuation)

    # Check if any character in the text is a punctuation
    retVal = all(char not in punctuation for char in s)
    # print("check_periods_punctuation : ", retVal)
    return retVal


def last_char_not_number(s):
    if not s:  # Check if the string is empty
        return False
    retVal =  s[-1].isdigit()
    # print("last_char_not_number : ", retVal)
    return retVal

def last_char_not_number_if_number(s):
    if not s:
        return False

    # Check if the string is alphanumeric
    if not s.isalnum():
        return False

    # Find the position of the first digit
    first_digit_pos = next((i for i, char in enumerate(s) if char.isdigit()), None)

    # If there are no digits, it's valid
    if first_digit_pos is None:
        return True

    # Check if all characters after the first digit are also digits
    if not all(char.isdigit() for char in s[first_digit_pos:]):
        return False

    # Check if the first number is not '0'
    if s[first_digit_pos] == '0':
        return False

    # Check if there are only digits at the end
    return all(char.isdigit() for char in s[first_digit_pos:])


main()