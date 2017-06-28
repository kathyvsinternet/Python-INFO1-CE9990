"""
graphpaper.py

configure sheet of graph paper

"""

import sys


try:
    r = int(input("How many rows of boxes? ")) 
    c = int(input("How many columns of boxes ")) 
    rb = int(input("How many rows of blanks in each box (e.g., 1)? ")) # height
    cb = int(input("How many columns of blanks in each box (e.g., 3)? ")) # width
except ValueError:
        print("Please input an integer.")

i = 0

while i < c:
    j = 0
    while j < r:
        print("+", cb * "-", sep = "", end = "")
        j += 1
    print()
    k = 0
    while k < rb:
        m = 0
        while m < r:
            print("|", cb * " ", sep = "", end = "")
            m += 1
        print()
        k += 1
    i += 1

sys.exit(0)
