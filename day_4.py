#!/usr/bin/env python3

import itertools
import hashlib


def hashmine(part=1):
    inp = open("day_4.txt").read()
    for i in itertools.count():
        h = hashlib.md5((inp + str(i)).encode("ascii")).hexdigest()
        if (part == 1 and h.startswith("00000")) or (part == 2 and h.startswith("000000")):
            return i

print("Day 4, Part 1 - Five zeroes:", hashmine(1))
print("Day 4, Part 2 - Six zeroes: ", hashmine(2))
