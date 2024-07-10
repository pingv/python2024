# Import everything from cowsay
# MUST install cowsay library [https://pypi.org/project/cowsay/] before using
# Terminal: $ pip install cowsay
import cowsay

# Print cow ASCII art directly
cowsay.cow('Mooooooooooooooooooo')

# Get the cow ASCII art as a string and print it
output_string = cowsay.get_output_string('cow', 'Hello World')
print(output_string)

# Print another message with cow ASCII art directly
cowsay.cow('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris blandit rhoncus nibh. Mauris mi mauris, molestie vel metus sit amet, aliquam vulputate nibh.')

my_fish = r'''
\
 \  
        /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´
'''

cowsay.draw('Sharks are my best friend', my_fish)
cowsay.trex('Sharks are my favorite food')

cowsay.char_names
['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
'turkey', 'turtle', 'tux']

for char_name in cowsay.char_names:
    # Get the function corresponding to the character name
    cowsay_function = getattr(cowsay, char_name)
    # Print the ASCII art
    print(cowsay_function(f"{char_name} says hello!"))