"""

tkinter_flags.py

draw two country flags (Bangladesh, Laos) with tkinter in python

"""

import tkinter

b = tkinter.Tk()
b.title("Bangladesh Flag")

c = tkinter.Canvas(b, width=1000, height=600)
c.pack()

c.create_rectangle(0, 0, 1000, 600, fill = "#006A4E") # green rectangle
c.create_oval(225, 100, 625, 500, fill = "#F42A41") # red circle


l = tkinter.Tk()
l.title("Laos Flag")

d = tkinter.Canvas(l, width=900, height=600)
d.pack()

d.create_rectangle(0, 0, 900, 150, fill = "#CE1126") # first red stripe
d.create_rectangle(0, 150, 900, 450, fill = "#002868") # blue stripe
d.create_rectangle(0, 450, 900, 600, fill = "#CE1126") # first red stripe
d.create_oval(325, 175, 575, 425, fill = "white") # white circle

