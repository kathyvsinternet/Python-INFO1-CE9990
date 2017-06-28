"""
control.py

calculate whether one was born in a leap year
"""

import sys

print("Find out if you were born in a leap year.") 

try:
    y = int(input("What year were you born? "))
except ValueError:
    print("Please input an integer.")

if y % 4 == 0:
    print("Yes,", y, "was a leap year.")
elif y % 4 == 2:
    print("No,", y, "was not a leap year. However, it was a Winter Olympics and Midterm Election year.")
else:
    print("No,", y, "was an odd-numbered year and therefore not a leap year.")

sys.exit(0)
