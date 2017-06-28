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
# n counts up to number of columns for last horizontal line

i = 0
while i < r:
    j = 0
    while j < c:
        print("+", cb * "-", sep = "", end = "")
        j += 1
    print("+") # last plus sign in row
    k = 0
    while k < rb:
        m = 0
        while m < c:
            print("|", cb * " ", sep = "", end = "")
            m += 1
        print("|") # last pipe in row
        k += 1
    i += 1
n = 0
while n < c:
    print("+", cb * "-", sep = "", end = "")
    n += 1
print("+")



sys.exit(0)
