"""

citybike.py

pull data from Citi Bike NYC JSON
"""

import sys
import tkinter
import json
import urllib.request

url = "https://feeds.citibikenyc.com/stations/stations.json"

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
          
address = input("What is your cross street? ")

stationInfo = info["stationBeanList"]

def details(stationInfo):
    print("The station name is", stationInfo["stationName"])
    print("This station is currently", (stationInfo["statusValue"]).lower())
    print("There are currently", stationInfo["availableBikes"], "bikes available here")

for key in stationInfo:
    if address == key["stAddress1"]:
        print(details(key))

print("Last updated:", info["executionTime"])

sys.exit(0)

