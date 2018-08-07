#!/usr/bin/python

def get_commands(vlan, name):
   commands = []
   commands.append('vlan ' + vlan)
   commands.append('name ' + name)
   return commands

def push_commands(device, cmds):
   print("Connecting to: " + device)

   for cmd in cmds:
      print("Sending cmd: " + cmd)

"""   
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
"""
