#!/usr/bin/env python

import yaml

with open("example.yml", "r") as f:
#    print(f.read())
     result = yaml.load(f)
     print(result)
