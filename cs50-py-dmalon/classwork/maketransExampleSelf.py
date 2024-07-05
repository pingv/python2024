# Single argument (dictionary):
# Replace digits with their word equivalents
d = {ord('0'): 'zero', ord('1'): 'one', ord('2'): 'two'}
text = "I have 2 apples and 1 orange"
print(text.translate(str.maketrans(d)))
# Output: I have two apples and one orange

# Two arguments (string to string mapping):
# Caesar cipher (shift by 1)
from_chars = "abcdefghijklmnopqrstuvwxyz"
to_chars   = "bcdefghijklmnopqrstuvwxyza"
text = "hello world"
print(text.translate(str.maketrans(from_chars, to_chars)))
# Output: ifmmp xpsme

# Three arguments (with characters to delete):
# Replace 'a' with 'x', 'e' with 'y', and remove spaces and commas
text = "hello, how are you?"
print(text.translate(str.maketrans('ae', 'xy', ' ,')))
print(text.translate(str.maketrans('', '', 'aeiouAEIOU')))
# Output: hyllohowxryyou