"""
list_daysofchristmas.py

imports The Twelve Days of Christmas lyrical components and outputs full song
"""

import sys

f ="/Users/206886/Python-INFO1-CE9990/12_days_of_christmas_gifts.txt"

try:
    lyrics = open(f)
except FileNotFoundError:
    print("Sorry, cannot find the file\"", f, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open the file\"", f, "\".", sep = "")
    sys.exit(1)

day = ["first",
       "second",
       "third",
       "fourth",
       "fifth",
       "sixth",
       "seventh",
       "eighth",
       "ninth",
       "tenth",
       "eleventh",
       "twelfth"]

gift = lyrics.read().split("\n") # removes line break

for n in range(len(day)):
    print("On the", day[n], "day of Christmas")
    print("my true love gave to me:")
    reverse = gift[n::-1]
    for i in reverse:
        if i == gift[0] and day[n] != day[0]:
            print("and ", end = "")
        if i == gift[0]:
            print(i, ".", sep = "")
        else:
            print(i, ",", sep = "")
    print()   

lyrics.close()
sys.exit(0)

