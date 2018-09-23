#!/usr/bin/python

#
# Basic string manipulation 
#

hostname = "ROUTER_1"

print(hostname)

name = "john"

print(name.capitalize())
#print(dir(hostname))

interface = "     Ethernet 1/1/1           "

print(interface.strip())

ipaddr = "1.2.3.4"

print(ipaddr.split('.'))

#
# How to use the 'format()' function.. similar to printf in C
#
ping = "ping {} router {} source {}".format("192.168.1.20", "management", "192.168.1.1")

print(ping)

ping = "ping {} router {} source {}"
print(ping.format("192.168.1.20", "management", "192.168.1.1"))

#
# Playing with lists
#
cmd = ["show", "router", "route-table" ]

tmp = " "

print(tmp.join(cmd))

new_list = ["John" , "is", 45, "years","old"]

print new_list

for value in new_list:
  if value == 45:
    print(value)

#
# Playing with dictionaries
#
device = {"hostname":"falcon","vendor":"nokia","model":"7750","type":"SR12"}
# print(device.items())
# print(device.keys())
# print(device.values())

print(tmp.join(device))
names = device.keys()

tmp = ""
print(tmp.join(names))

#
# Playing with sets
#
myset = set(["John", "is", "45", "years","old"])

for value in myset:
  print(value)

myset = set(["John" , "is", "45", "years", "old"])
myset1 = set(["Jane" , "is", "45", "years", "old"])

print(myset1.union(myset))
print(myset1.intersection(myset))
print(myset1.symmetric_difference(myset))

ipaddr = ("192.168.1.10",24)
print(ipaddr)
print(type(ipaddr))
print(ipaddr[0])
print(ipaddr[1])

#
# Playing with conditional statements
#
mylist = ["This", "is", "a", "Nokia", "router"]

if ("Nokia" == mylist[2]):
    print("Yes")
elif (("This" == mylist[0]) and ("router" == mylist[4])):
    print("Yes-1")
else:
    print("No")

for value in mylist:
   print(value)

#
# While loops
#
i = 0
while i < len(mylist):
   print(mylist[i])
   i += 1


port_options = {
    "port_number": "port {}", 
    "description": "description {}", 
    "speed": "speed {}",
    "mode": "mode {}" 
}

print(port_options)
port_params = {
    "port_number": "1/1/1",
    "description": "This a test port", 
    "speed": "1000",
    "mode": "access" 
}
print(port_params)

#
# For loops
#
port_list = []

for attribute, value in port_params.items():
     port = port_options.get(attribute)
     print(port)
     port = port_options.get(attribute).format(value)
     print(port)
     port_list.append(port)

print(port_list)

#
# How to define functions and use them
#
vendors = ["cisco", "juniper", "nokia", "arista"]
print(vendors)

def print_vendor(vendor_name):
   print("This is a " + vendor_name + " router")

for vendor in vendors:
   print_vendor(vendor)

def get_commands(vlan, name):
   commands = []
   commands.append('vlan ' + vlan)
   commands.append('name ' + name)
   return commands

def push_commands(device, cmds):
   print("Connecting to: " + device)

   for cmd in cmds:
      print("Sending cmd: " + cmd)
  
vlans = [{'id':'10', 'name':'USERS'}, {'id':'20', 'name':'VOICE'}, {'id':'30', 'name':'wlan'}]

vlans[0].get('id')

for vlan in vlans:
   print(get_commands(vlan.get('id'), vlan.get('name')))

devices = ["switch1", "switch2", "switch3"]

for vlan in vlans:
#   print(get_commands(vlan.get('id'), vlan.get('name')))
    id = vlan.get('id')
    name = vlan.get('name')
    
    print("Configuring VLAN: " + id)
    for device in devices:
       push_commands(device, get_commands(id, name))
    print("\n")

#
# File operations - read from and write to a file
#
vlan_file = open('vlan.cfg', 'r')

#print(vlan_file.read())

vlans = []
line = vlan_file.readline()

while line != "":
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

#print("I'm here..")

#
# More efficent way to write the previous piece of code
#
vlan_file = open('vlan.cfg', 'r')

vlans = []

for line in vlan_file:
   temp = {}
   if 'vlan' in line:
       vlan_id = line.strip('vlan').strip()
       temp['id'] = vlan_id   
       vlans.append(temp)
   elif 'name' in line:
       vlan_name = line.strip().strip('name').strip()
       temp['name'] = vlan_name   
       vlans.append(temp)

vlan_file.close()

print(vlans) 

#vlans = [{'id': '10'}, {'name': 'USERS'}, {'id': '20'}, {'name': 'VOICE'}, {'id': '30'}, {'name': 'WLAN'}, {'id': '40'}, {'name': 'APP'}, {'id': '50'}, {'name': 'WEB'}, {'id': '60'}, {'name': 'DB'}]

write_to_file = open('new_vlan.cfg', 'w')

for entry in vlans:
#   print(entry)
#   print(entry.keys())
#   print(entry.values())

   if 'id' in entry.keys():
#      print('vlan ' + entry.get('id'))
      write_to_file.write('vlan ' + entry.get('id') + '\n')
   elif 'name' in entry.keys():
#      print(' name ' + entry.get('name'))
      write_to_file.write(' name ' + entry.get('name') + '\n')

write_to_file.close()
