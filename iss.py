#!/usr/bin/env python3
#
# http://api.open-notify.org/
#

import json
import urllib.request

#
# ISS Location
#
print("ISS Location")
url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
obj = json.loads(response.read())
#print(obj)
print(json.dumps(obj, indent=4))
print(" ")

#
# ISS Pass Times
# Columbus, coordinates - 39.9612 N, 82.9988 W
#
print("ISS Pass Times over Columbus, OH")
url = "http://api.open-notify.org/iss-pass.json?lat=39.9612&lon=82.9988"
response = urllib.request.urlopen(url)
obj = json.loads(response.read())
#print(obj)
print(json.dumps(obj, indent=4))
print(" ")

#
# ISS on-board
#
print("ISS Astronauts On-board")
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
obj = json.loads(response.read())
#print(obj)
print(json.dumps(obj, indent=4))
print(" ")

