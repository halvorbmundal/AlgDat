#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def mergerer(liste1, liste2):
    sorterte = []
    liste1.append((float('inf'), ""))
    liste2.append((float('inf'), ""))
    index1 = 0
    index2 = 0
    for i in range(0, len(liste1) + len(liste2) - 2):
        if liste1[index1][0] > liste2[index2][0]:
            sorterte.append(liste2[index2])
            index2 += 1
        else:
            sorterte.append(liste1[index1])
            index1 += 1
    return sorterte


def merge(deck):
    sorterte = []
    while (len(deck) > 1):
        for i in range(0, len(deck), 2):
            try:
                sorterte.append(mergerer(deck[i], deck[i + 1]))
            except:
                sorterte.append(deck[i])
        deck = sorterte
        sorterte = []
    return trekk_ut_bokstaver(deck)


def trekk_ut_bokstaver(liste):
    ord=""
    for i in liste[0]:
        ord+=i[1]
    return ord


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


main()