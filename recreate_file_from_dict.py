#!/usr/bin/python

vlans = [{'id': '10'}, {'name': 'USERS'}, {'id': '20'}, {'name': 'VOICE'}, {'id': '30'}, {'name': 'WLAN'}, {'id': '40'}, {'name': 'APP'}, {'id': '50'}, {'name': 'WEB'}, {'id': '60'}, {'name': 'DB'}]

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
