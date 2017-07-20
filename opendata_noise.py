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
    print(datum[16], ", NY ", datum[8], sep = "") # Incident City, Incident Zip

b = input("What borough do you live in? ")
s = input("Which street do you live on? ")

print()

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

noise.sort(key = lambda row: datetime.datetime.strptime(row[1], "%m/%d/%Y %H:%M:%S %p"), reverse = True)

data.close()

if len(noise) > 0:
    print("Here are the three most recent noise complaints on ", s, " in ", b, ":", sep = "")
    print()
    for i in range(0, 3):
        complaint(noise[i])
        print()
        
sys.exit(0)
