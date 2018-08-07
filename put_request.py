#!/usr/bin/python

import requests
import json

mydict = {'title':'post_test','body':'helloworld','userid':'666'}

print('Printing dictionary')
print(type(mydict))
print(mydict)

myreq = json.dumps(mydict)
print(type(myreq))
print(myreq)

rpost = requests.post('https://jsonplaceholder.typicode.com/posts',myreq)
print(type(rpost))
print(type(rpost.text))
print(json.loads(rpost.text))
