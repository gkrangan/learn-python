#!/usr/bin/python

users = ['Admin', 'John', 'JANE', 'matt', 'Ben', 'brad']
print users

if users:
    for user in users:
        if user == 'admin':
            print("Hello Admin! Would you like to see a special report?")
        else:
            print("Hello {}! Thank you for logging in again.").format(user)
else:
    print "We need to find some users"

newusers = ['BEN', 'mike', 'leo', 'sam', 'jane']

#
# Checking containment in a case sensitive manner for elements in a list 
#
for nuser in newusers:
    if nuser in (u.lower() for u in users):
        print("User name {} already exists. Pick a different user name.").format(nuser)
    elif nuser in (u.upper() for u in users):
        print("User name {} already exists. Pick a different user name.").format(nuser)
    else:
        print("User name {} is available").format(nuser)
