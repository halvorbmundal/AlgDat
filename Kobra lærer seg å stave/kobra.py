#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    # SKRIV DIN KODE HER
    toppnode = Node()
    nodepeker = toppnode
    for i in ordliste:
        for j in i[0]:
            if j in nodepeker.barn:
                nodepeker=nodepeker.barn[j]
            else:
                nodepeker.barn[j]=Node()
                nodepeker = nodepeker.barn[j]
        nodepeker.posi.append(i[1])
        nodepeker=toppnode
    return toppnode


def posisjoner(ord, indeks, node):
    # SKRIV DIN KODE HER
    steder = []
    if len(ord) == 0:
        return node.posi
    elif "?" == ord[0]:
        for noder in node.barn:
            for i in (posisjoner(ord[1:], indeks, node.barn[noder])):
                steder.append(i)
    else:
        # indeks+=1
        for noder in node.barn:
            if noder == ord[0]:
                for i in (posisjoner(ord[1:], indeks, node.barn[noder])):
                    steder.append(i)
                break
    return steder

def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("%s:" % sokeord, end='')
            posi = posisjoner(sokeord, 0, toppnode)
            posi.sort()
            for p in posi:
                print(" %s" % p, end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()
