#!/usr/bin/python

import pandas as pd
from lxml import etree

data = "sample.xml"

tree = etree.parse(data)

lstKey = []
lstValue = []
for p in tree.iter() :
    lstKey.append(tree.getpath(p).replace("/",".")[1:])
    lstValue.append(p.text)

df = pd.DataFrame({'key' : lstKey, 'value' : lstValue})
df.sort_values('key')
