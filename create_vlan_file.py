#!/usr/bin/python

vlan_types = ["USERS", "VOICE", "WLAN", "APP", "WEB", "DB"]

vlan_id = 10

for vlan_type in vlan_types:
    print("vlan " + str(vlan_id))
    print(" name " + vlan_type) 
    vlan_id = vlan_id + 10
