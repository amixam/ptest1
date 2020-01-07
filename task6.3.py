#!/usr/bin/env python3


def main():

    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]
    trunk_template = [
        'switchport trunk encapsulation dot1q',
        'switchport mode trunk',
        'switchport trunk allowed vlan'
    ]

    access = {
        '0/12': '10',
        '0/14': '11',
        '0/16': '17',
        '0/17': '150'
    }
    trunk = {
        '0/1': ['add', '10', '20', '50', '40'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17', '20', '50', '40']
    }

    for intf, vlan in access.items():
        print('interface FastEthernet' + intf)
        for command in access_template:
            if command.endswith('access vlan'):
                print(' {} {}'.format(command, vlan))
            else:
                print(' {}'.format(command))
    print('_' * 20 + '\n')

    for intf, vlan in trunk.items():
        print('interface FastEthernet' + intf)
        vlans = ''
        vlans = ','.join(vlan[1:])
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                if vlan[0] == 'add':
                    print(' {} add {}'.format(command, vlans))
                elif vlan[0] == 'del':
                    print(' {} remove {}'.format(command, vlans))
                elif vlan[0] == 'only':
                    print(' {} {}'.format(command, vlans))
            else:
                print(' {}'.format(command))


if __name__ == '__main__':
    main()
