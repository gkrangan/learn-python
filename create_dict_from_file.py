#!/usr/bin/python

vlan_file = open('vlan.cfg', 'r')

vlans = []

for line in vlan_file:
   temp = {}
   if 'vlan' in line:
       temp['id'] = line.strip('vlan').strip()
       vlans.append(temp)
   elif 'name' in line:
       temp['name'] = line.strip().strip('name').strip()
       vlans.append(temp)

vlan_file.close()

print(vlans)
