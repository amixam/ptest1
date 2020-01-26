#!/usr/bin/env python3


import sys


def check_ignore(list):
    ignore = ['duplex', 'alias', 'Current configuration']
    flag = False
    for a in ignore:
        flag = (a in list) or flag
    return flag


def main():
    file_name1 = sys.argv[1]
    file_name2 = sys.argv[2]

    with open(file_name1) as f1, open(file_name2, 'w') as f2:
        current_line = f1.readlines()
        for line in current_line:
            if not line.startswith('!'):
                if not check_ignore(line):
                    f2.write(line)


if __name__ == '__main__':
    main()
