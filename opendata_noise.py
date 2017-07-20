"""
opendata_noise.py

uses 311 noise complaint data and prints the most recent noise complaint
"""

import sys
import datetime
import csv
import urllib.request

url = "https://data.cityofnewyork.us/api/views/afa6-2qh4/rows.csv" \
      "?accessType=DOWNLOAD"

try:
    data = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

def complaint(datum):
    print(datum[1]) # Created Date
    print(datum[6]) # Descriptor
    print(datum[9]) # Incident Address
    print(datum[17], ", NY ", datum[8], sep = "") # Incident City, Incident Zip

b = input("What borough do you live in? ")
s = input("Which street do you live on? ")

borough = b.lower()
street = s.lower()

noise = [] 
for datum in data:
    try:
        string = datum.decode("utf-8")
    except UnicodeError as unicodeError:
        print(unicodeError)
        sys.exit(1)

    row = csv.reader([string])
    fields = next(row)
    if fields[23].lower() == borough and street in fields[10].lower():
        noise.append(fields)

""" # this doesn't work to sort by date. need to figure out.
noise.sort(key = lambda row: datetime.striptime(row[0], "%d-%b-%y, reverse = True)
"""

data.close()

if len(noise) > 0:
    print("Here are the most recent noise complaints in ", b, ".", sep = "")
    for i in range(len(noise)):
        complaint(noise[i])
        
        
sys.exit(0)
