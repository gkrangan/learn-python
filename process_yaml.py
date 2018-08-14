#!/usr/bin/python

import yaml
import json

with open('sample.yml','r') as f:
   result = yaml.load(f)
   print result
   
#  for obj in result:
#     print obj

#  back_to_yaml = yaml.dump(result)
#  print back_to_yaml
   
   back_to_yaml = yaml.dump(result,default_flow_style=False)
   print back_to_yaml

#  convert_to_json = json.dumps(result)
   convert_to_json = json.dumps(result, indent=4)
   print convert_to_json

