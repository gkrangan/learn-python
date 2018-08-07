#!/usr/bin/python

import sys

year = int(sys.argv[1])

if not(year % 4):
    if not(year % 100):
        if not(year % 400):
            print("This is a Leap Year")
        else:
            print("Sorry. This is not a Leap Year")
    else: 
        print("This is a Leap Year")
else:
    print("Sorry. This is not a Leap Year")
