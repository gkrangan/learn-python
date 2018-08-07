#!/usr/bin/python

import sys
import yaml

filename = sys.argv[1]
print(filename)
 
myfile = open(filename,'r')

result = yaml.safe_load(myfile)

print(result)
print('-' * 20)
for obj in result:
   if isinstance(obj,dict):
     for k1, v1 in obj.items():
        print(str(k1))
        if isinstance(v1,dict):
           for k2, v2 in v1.items():
              print('   ' + str(k2) + ' ' + str(v2))
        else:
           print('  ' + str(k1) + ' ' + str(v1))
   else:
     print('  ' + str(k1)) 

myfile.close()
