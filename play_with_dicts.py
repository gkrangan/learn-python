#!/usr/bin/python

import collections

device = {"hostname":"falcon"}
print(device)

device['vendor'] = 'nokia'
print(device)

device['model'] = '7750'
print(device)

device.setdefault('type', 'SR12')
print(device)

print(collections.Counter(device))
print(collections.ItemsView(device))
print(collections.KeysView(device))
print(collections.MappingView(device))


for k,v in device.items():
    print(k,v)

for k,v in sorted(device.items()):
    print(k,v)

for item in collections.ItemsView(device):
    print(item)

device.pop('type')
print(device)

device['type'] = 'SR7'
print(device)
