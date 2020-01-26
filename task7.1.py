#!/usr/bin/env python3


def main():

    template = '''
    Protocol:              OSPF
    Prefix:                {}
    AD/Metric:             {}
    Next-Hop:              {}
    Last update:           {}
    Outbound Interface:    {}
    '''

    with open('/home/max/pyneng-examples-exercises/exercises/07_files/ospf.txt') as f:
        for line in f:
            current_line = f.readline().strip('\n').split()
            print(template.format(current_line[1], current_line[2], current_line[4], current_line[5], current_line[6]))


if __name__ == '__main__':
    main()
