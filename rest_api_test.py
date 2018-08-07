#!/usr/bin/python

""" 
https://jsonplaceholder.typicode.com/

"""

import requests

print('\n')

print('Testing GET request')
print("""rget = requests.get('https://jsonplaceholder.typicode.com/posts/1')""")
rget = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(rget)
print(rget.headers)
print(rget.text)
print('\n')

print('Testing POST request')
print("""rpost = requests.post('https://jsonplaceholder.typicode.com/posts', {'title':'post_test','body':'helloworld','userid':'666'})""")
rpost = requests.post('https://jsonplaceholder.typicode.com/posts', {'title':'post_test','body':'helloworld','userid':'666'})
print(rpost)
print(rpost.headers)
print(rpost.text)
print('\n')

print('Testing PUT request')
print("""rput = requests.put('https://jsonplaceholder.typicode.com/posts/90', {'title':'put_test','body':'helloworld','userid':'999'})""")
rput = requests.put('https://jsonplaceholder.typicode.com/posts/90', {'title':'put_test','body':'helloworld','userid':'999'})
print(rput)
print(rput.headers)
print(rput.text)
print('\n')

print('Testing PATCH request')
print("""rpatch = requests.patch('https://jsonplaceholder.typicode.com/posts/80', {'title':'patch_test','body':'helloworld','userid':'888'})""")
rpatch = requests.patch('https://jsonplaceholder.typicode.com/posts/80', {'title':'patch_test','body':'helloworld','userid':'888'})
print(rpatch)
print(rpatch.headers)
print(rpatch.text)
print('\n')

print('Testing DELETE request')
print("""rdel = requests.delete('https://jsonplaceholder.typicode.com/posts/70')""")
rdel = requests.delete('https://jsonplaceholder.typicode.com/posts/70')
print(rdel)
print(rdel.headers)
print(rdel.text)
