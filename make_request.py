#!/usr/bin/python

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


for element in todos:
    print element
    for k,v in element.items():
        print k, v
    print('\n')
