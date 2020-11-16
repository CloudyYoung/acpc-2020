#! /usr/bin/python3

import sys

i = 0
cards = []
cardsAmount = 0  # cards amount
for line in sys.stdin:
    if i != 0:
        cards = line.split()
    else:
        cardsAmount = int(line)
    i += 1

cards = [int(i) for i in cards]
cards.sort()
# print(cards)

index = 0  # current card index
turns = 0  # how many turns


while not len(cards) == 0:
    current = cards[index]
    # print("current", current)
    try:
        nextIndex = cards.index(current + 1)
        cards.pop(index)
        index = nextIndex - 1
    except:
        cards.pop(index)
        turns += 1
        index = 0

    # print("cards", cards)
    # print("turns", turns)

print(turns)
