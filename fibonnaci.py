#!/usr/bin/python

import sys

fib_seq = [0,1]

if (len(sys.argv) > 1):
    fib_count = int(sys.argv[1])
    if fib_count == 0:
        exit()
    elif fib_count == 1:
        print(0)
        exit()
    if (fib_count < 3):
        print fib_seq
        exit()
else:
    print("Not enough arguments")
    exit()

i = 2
while (i < fib_count):
   fib_seq.append(fib_seq[i - 2] + fib_seq[i-1])  
#  print(fib_seq)
   i += 1

print(fib_seq)
