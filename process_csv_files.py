#!/usr/bin/python

import csv
import math
import operator

colnames1 = ("NAME","LEG_LENGTH","DIET")
colnames2 = ("NAME","STRIDE_LENGTH","STANCE")

dinos = {}

# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# g = 9.8

G_CONST = 9.8

with open('dataset1.txt','r') as csvfile:
    reader = csv.DictReader(csvfile, colnames1)

    for obj in reader:
        temp = {}
        if (obj.keys() != obj.values()): 
            temp['LEG_LENGTH'] = obj.get('LEG_LENGTH')
            temp['DIET'] = obj.get('DIET')
            dinos[obj.get('NAME')] = temp 

new_dinos = {}
biped_dinos = {}

with open('dataset2.txt','r') as csvfile:
    reader = csv.DictReader(csvfile, colnames2)
 
    for obj in reader:
        temp = {}
        if (obj.keys() != obj.values()): 
            name = obj.get('NAME')
            temp = dinos.get(name)
            if temp:
               temp['STRIDE_LENGTH'] = obj.get('STRIDE_LENGTH')
               temp['STANCE'] = obj.get('STANCE')
               speed = (((float(temp.get('STRIDE_LENGTH')) / float(temp.get('LEG_LENGTH'))) - 1) * math.sqrt(float(temp.get('LEG_LENGTH')) * G_CONST))
#              print("name: {}, speed: {}").format(name, speed)
               new_dinos[name] = speed
               dinos[name] = temp 
               if obj.get('STANCE') == 'bipedal':
                   biped_dinos[name] = speed
# print(dinos)

print("All dinos with all attributes")
for obj in dinos:
    print(obj, dinos[obj])
print('\n')

print("All dinos sorted by speed")
sorted_d = sorted(new_dinos.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d)
print('\n')

print("All biped dinos sorted by speed")
sorted_d = sorted(biped_dinos.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d)
print('\n')

for i in sorted_d:
    print(i[0])
