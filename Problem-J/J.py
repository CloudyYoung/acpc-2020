#! /usr/bin/python3

import sys

i = 0
lst = []
for line in sys.stdin:
    if i != 0:
        ab = line.split()
        a = str(ab[0])
        if a == 'Yraglac':
            lst.append('y')
        elif a == 'Notnomde':
            lst.append('n')
    i += 1

# print(lst)

ylead = 0
nlead = 0
ynum = 0
nnum = 0

ycon = 0
maxycon = 0
ncon = 0
maxncon = 0

last = None  # last wins

nwin = None  # who wins under N's system
ywin = None  # who wins under Y's system
for i in lst:
    if i == 'y':
        # lead
        # if last == i:  # last the same with i
        ynum += 1
        # nnum -= 1
        # last = i

        # con
        ycon += 1
        ncon = 0
        maxycon = max(ycon, maxycon)
    elif i == 'n':
        # lead
        # if last == i:
        nnum += 1
        # ynum -= 1
        # last = i

        # con
        ncon += 1
        ycon = 0
        maxncon = max(ncon, maxncon)

    if nnum > ynum:
        nlead = max(nnum - ynum, nlead)
    elif nnum < ynum:
        ylead = max(ynum - nnum, ylead)


# print(ylead, nlead)

# Lead
if ylead > nlead:
    ywin = 'y'
elif nlead > ylead:
    ywin = 'n'
else:
    ywin = None  # tie

# print(maxycon, maxncon)

# Con
if maxycon > maxncon:
    nwin = 'y'
elif maxncon > maxycon:
    nwin = 'n'
else:
    nwin = None  # tie

# print(ywin, nwin)


if nwin == ywin:
    print('Agree')
else:
    print('Disagree')
