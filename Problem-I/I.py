#! /usr/bin/python3

import sys

for line in sys.stdin:
    ab = line.split()
    a = int(ab[0])
    b = int(ab[1])
    c = int(ab[2])
# a = 10
# b = 20
# c = 25

d1 = b - a
d2 = c - b

if d1 == d2:
    print("cruised")
elif (d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0):
    print("turned")
elif abs(d2) > abs(d1):
    print("accelerated")
else:
    print("braked")

# print(abs(d1))
# print(abs(d2))
