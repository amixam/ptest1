#!/usr/bin/env python3


def main():
    ip = ''
    while not ip:
        ip = input('Введите IP: ')
        ip_num = []
        for octets in ip.split('.'):
            try:
                ip_num.append(int(octets))
            except ValueError:
                print('Wrong IP')
                ip = ''
    print(ip)
    if ip == '0.0.0.0':
        print('unassigned')
    elif ip == '255.255.255.255':
            print('local broadcast')
    elif len(ip_num) == 4 and (ip_num[0] in range(1, 256) and
                               ip_num[1] in range(1, 256) and
                               ip_num[2] in range(1, 256) and
                               ip_num[3] in range(1, 256)):
        if ip_num[0] in range(1, 224):
            print('unicast')
        elif ip_num[0] in range(224, 240):
            print('multicast')
        else:
            print('unused')
    else:
        print('Wrong IP')


if __name__ == '__main__':
    main()
