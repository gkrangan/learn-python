vlan_file = open('vlan.cfg', 'r')

#print(vlan_file.read())

vlans = []
line = vlan_file.readline()

while line:
   temp = {}
   if 'vlan' in line:
       vlan_id = line.strip('vlan').strip()
#      print(vlan_id)
       temp['id'] = vlan_id
#      print(temp)
       vlans.append(temp)
   elif 'name' in line:
       vlan_name = line.strip().strip('name').strip()
#      print(vlan_name)
       temp['name'] = vlan_name
#      print(temp)
       vlans.append(temp)

   line =  vlan_file.readline()

vlan_file.close()

print(vlans)
