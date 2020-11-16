#! /usr/bin/python3

import sys

i = 0
lst = []
num = 0
for line in sys.stdin:
    if i == 0:
        ab = line.split()
        a = int(ab[0])
        b = int(ab[1])
        c = int(ab[2])
        lst = [["_" for i in range(a)] for i in range(b)]
        num = c
    else:
        if i > num:
            break
        ab = line.split()
        a = int(ab[0])
        b = int(ab[1])
        c = int(ab[2])
        d = int(ab[3])
        for k in range(a):
            for j in range(b):
                lst[d + j][c + k] = chr(97 + i - 1)
    i += 1

for i in lst:
    print(''.join(i))
