#!/usr/bin/env python3


def main():
    mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
    mac_cisco = []
    for macs in mac:
        print(macs)
        mac_cisco.append(macs.replace(':', '.'))
    print(mac_cisco)


if __name__ == '__main__':
    main()
