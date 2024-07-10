# From commandline, try $ python say.py name-1 name-2 name-3

import sys

from sayings import hello
from sayings import goodbye
import sayings

if len(sys.argv) == 2:
    hello(sys.argv[1])
elif len(sys.argv) == 3:
    goodbye(sys.argv[2])
else:
   sayings.main()