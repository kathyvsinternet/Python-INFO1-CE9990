"""

dictionary_hogwartshouses.py

supposed to create dictionary from JSON and prints information for any given Hogwarts house

wasn't actually able to create dictionary, also seeing error in executing script where "list indices must be integers or slices, not str"
"""

import sys
import json
import urllib.request

url = "https://raw.githubusercontent.com/kathyvsinternet/Python-INFO1-CE9990/master/hogwarts_houses.json"

try:
    data = urllib.request.urlopen(url)
except urllib.error.URLError as urlError:
    print("urllib.error.URLError", urlError)
    sys.exit(1)

file = data.read()

data.close()

try:
    f = file.decode("utf-8")
except UnicodeError as unicodeError:
    print(unicodeError)
    sys.exit(1)

try:
    info = json.loads(f)
except json.JSONDecodeError as jsonDecodeError:
    print(jsonDecodeError)
    sys.exit(1)

h = input("Which Hogwarts House were you sorted in? ")

print()

house = h.lower()

def details(house):
    print(info["Founder"], "is the founder of the", h, "house.")
    print("Its house animal is the ", info["Animal"], ".", sep = "")
    print(info["Head"], "is head of house.")
    print(info["Ghost"], "is the", h, "ghost.")
    print("The ", h, " common room is ", info["Common Room"], ".", sep = "")
    
if house in info["House"].lower():
    details(house)
else:
    print("Are you sure", h, "is a Hogwarts house?")
    sys.exit(1)

sys.exit(0)
