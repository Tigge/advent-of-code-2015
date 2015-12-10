#!/usr/bin/env python3

import itertools


def look_and_say(part=1):
    inp = open("day_10.txt").read().strip()
    for i in range(0, 40 if part == 1 else 50):
        inp = "".join(map(lambda a: str(len(list(a[1]))) + a[0], itertools.groupby(inp)))
    return len(inp)

print("Day 10, Part 1 - 40 iterations:", look_and_say(1))
print("Day 10, Part 2 - 50 iterations:", look_and_say(2))
