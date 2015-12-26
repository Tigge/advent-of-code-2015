#!/usr/bin/env python3

import itertools
import math


def elfhouse(part=1):
    present_target = int(open("day_20.txt").read().strip()) / (10 if part == 1 else 11)

    for i in itertools.count(start=1):
        presents = 0
        end = int(math.ceil(math.sqrt(i)))
        for a in range(1, end):
            if i % a == 0:
                if part == 2 and a * 50 > i:
                    presents += a
                if part == 2 and (i // a) * 50 > i:
                    presents += i // a
        if i % end == 0:
            if part == 2 and end * 50 > i:
                presents += end
        if presents >= present_target:
            return i


print("Day 20, Part 1 - infinite:", elfhouse(1))
print("Day 20, Part 2 - max 50:", elfhouse(2))
