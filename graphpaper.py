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

# i counts up to number of rows
# j counts up to number of columns for horizontal line
# k counts up to height
# m counts up to number of columns for vertical lines

i = 0
while i < r:
    j = 0
    while j < c:
        print("+", cb * "-", sep = "", end = "")
        j += 1
    print()
    k = 0
    while k < rb:
        m = 0
        while m < c:
            print("|", cb * " ", sep = "", end = "")
            m += 1
        print()
        k += 1
    i += 1

sys.exit(0)
