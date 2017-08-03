"""

dictionary_hogwartshouses.py

create dictionary from JSON and prints information for any given Hogwarts house
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
    print(dictionary["Founder"], "is the founder of the", h, "house.")
    print("Its house animal is the ", dictionary["Animal"], ".", sep = "")
    print(dictionary["Head"], "is head of house.")
    print(dictionary["Ghost"], "is the", h, "ghost.")
    print("The ", h, " common room is ", dictionary["Common Room"], ".", sep = "")
    
for dictionary in info:
    if dictionary["House"].lower() == house:
        details(dictionary)
        break
else:
    print("Are you sure", h, "is a Hogwarts house?")
    sys.exit(1)

sys.exit(0)
