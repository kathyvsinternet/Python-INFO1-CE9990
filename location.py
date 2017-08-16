"""
location.py

object of class Location to be used in uselocation.py
"""

import sys
import urllib.request
import json


class Location(object):

    def __init__(self, latitude, longitude):
        if not (isinstance(latitude, int) or isinstance(latitude, float)):
            raise TypeError("Latitude must be an integer or a float, not " + str(type(latitude)))
        if not (isinstance(longitude, int) or isinstance(longitude, float)):
            raise TypeError("Longitude must be an integer or a float, not " + str(type(longitude)))
        if abs(latitude) > 90:
            raise ValueError("Latitude must be between -90 to 90 (inclusive).")
        if abs(longitude) > 180:
            raise ValueError("Longitude must be between -90 to 90 (inclusive).")

        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        if self.latitude > 0:
            lat = "N"
        else:
            lat = "S"
        if self.longitude > 0:
            lon = "E"
        else:
            lon = "W"
        return "{}°{} {}°{}".format(abs(self.latitude), lat, abs(self.longitude), lon)

    def getLatitude(self):
        return self.latitude

    def setLatitude(self, latitude):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def setLongitude(self, longitude):
        return self.longitude

    def getZipcode(self):
        url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}".format(self.latitude, self.longitude)

        try:
            file = urllib.request.urlopen(url)
        except urllib.error.URLError as urlError:
            print("urllib.error.URLError", urlError)
            sys.exit(1)

        googlemap = file.read()
        file.close()

        try:
            g = googlemap.decode("utf-8")
        except UnicodeError as unicodeError:
            print(unicodeError)
            sys.exit(1)

        try:
            dictionary = json.loads(g)
        except json.JSONDecodeError as jsonError:
            print(jsonError)
            sys.exit(1)

        results = dictionary["results"]                         #results is a list of dictionaries
        if len(results) == 0:
            return 0

        firstResult = results[0]                                #firstResult is a dictionary
        address_components = firstResult["address_components"]  #address_components is a list of dictionaries

        for component in address_components:                    #component is a dictionary
            if "postal_code" in component["types"]:             #component["types"] is a list of strings
                try:
                    c = component["long_name"]                  #component["long_name"] is a string that looks like a zipcode
                except KeyError:
                    return 0
                try:
                    return int(c)
                except ValueError:
                    return 0            

        return 0

    #The definition of classLocation ends here.

if __name__ == "__main__":
    l = Location(40,756098, -73.990188)

    print("The following location is set to The New York Times Building at 620 8th Avenue.")
    print()
    print("The latitude of {} is {}.".format(l, l.getLatitude()))
    print("The longtitude of {} is {}.".format(l, l.getLongitude()))
    print("The zip code of {} is {}.".format(l, l.getZipcode()))

    l.setLatitude(40.712743)
    l.setLongitude(-74.013379)

    print("The new location is set to One World Trade Center.")
    print()
    print("The latitude of {} is {}.".format(l, l.getLatitude()))
    print("The longtitude of {} is {}.".format(l, l.getLongitude()))
    print("The zip code of {} is {}.".format(l, l.getZipcode()))
        
    sys.exit(0)
