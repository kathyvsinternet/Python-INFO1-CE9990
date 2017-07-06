"""

forif_characterloop.py

Looping through alphabet with ba, be, bi, etc... zi, zou, zu

"""

import sys

c = "bcdfghjklmnpqrstvwxyz"
v = "aeiou"

for i in range(len(c)):
    for j in range(len(v)):
        print(c[i], v[j], sep = "")

sys.exit(0)
