# pip install pyfiglet

from pyfiglet import Figlet
import sys, random

figlet = Figlet()

# what_to_print = "God Is Love"
# set_fig_font = "banner"

# You can then get a list of available fonts with code like this:
# fig_fonts = figlet.getFonts()
# for fig_font in fig_fonts:
#     print(fig_font)

args = sys.argv

if len(args) == 3:
    if args[1] not in ("-f", "--font"):
        sys.exit("Incorrect flag. Only pass -f or --font")
    elif args[2] not in figlet.getFonts():
        sys.exit("Pass valid font name")
    else:
        set_fig_font = args[2]
elif len(args) == 1:
    set_fig_font = random.choice(figlet.getFonts())
    # print("Font set as ", set_fig_font)
else:
    sys.exit("Too Many args")

what_to_print = input("Input: ")    
     
# You can set the font with code like this, wherein f is the font’s name as a str:
# set_fig_font = "banner"
figlet.setFont(font=set_fig_font)

# And you can output text in that font with code like this, wherein s is that text as a str:
print(figlet.renderText( what_to_print ))