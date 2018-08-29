#!/usr/bin/python

numbers = range(1,10)

print numbers

for num in numbers:
    if (num == 1):
        print('1st')
    elif (num == 2):
        print('2nd')
    elif (num == 3):
        print('3rd')
    else:
        print('{}th').format(str(num))
