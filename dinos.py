#!/usr/bin/python

"""
Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs 
from fastest to slowest. Do not print any other information.
"""

import csv
import math
import operator

colnames1 = ("NAME","LEG_LENGTH","DIET")
colnames2 = ("NAME","STRIDE_LENGTH","STANCE")

dinos = {}

with open('dataset1.txt','r') as csvfile:
    reader = csv.DictReader(csvfile, colnames1)

    for obj in reader:
        temp = {}
        if (obj.keys() != obj.values()): 
            temp['LEG_LENGTH'] = obj.get('LEG_LENGTH')
            temp['DIET'] = obj.get('DIET')
            dinos[obj.get('NAME')] = temp 

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
               speed = (((float(temp.get('STRIDE_LENGTH')) / float(temp.get('LEG_LENGTH'))) - 1) * math.sqrt(float(temp.get('LEG_LENGTH')) * 9.8))
               dinos[name] = temp 
               if obj.get('STANCE') == 'bipedal':
                   biped_dinos[name] = speed

print("All biped dinos sorted by speed")
sorted_d = sorted(biped_dinos.items(), key=operator.itemgetter(1), reverse=True)
for i in sorted_d:
    print(i[0])
