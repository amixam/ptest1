#!/usr/bin/env python3


import sys


def main():
    vlan_id = input('VLAN: ')
    file_name1 = sys.argv[1]
    mac_table = []
    with open(file_name1) as f1:
        mac_list = f1.readlines()
    for line in mac_list:
        if 'DYNAMIC' in line:
            mac_line = line.split()
            mac_line.remove('DYNAMIC')
            mac_table.append(mac_line)
    mac_table.sort()
    for vlan, mac, intf in mac_table:
        if vlan == vlan_id:
            print(f"{vlan:<8}{mac:<20}{intf:<8}")


if __name__ == '__main__':
    main()
