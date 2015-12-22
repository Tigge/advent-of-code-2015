#!/usr/bin/env python3

import itertools


def combinations(containers, maximum):
    for i, container in enumerate(containers):
        if container > maximum:
            continue
        yield [container]
        for combination in combinations(containers[i+1:], maximum - container):
            yield itertools.chain([container], combination)


def eggnog(part=1):
    containers = list(map(int, open("day_17.txt").read().strip().split("\n")))
    containers = list(filter(lambda c: sum(c) == 150, map(list, combinations(containers, 150))))
    if part == 1:
        return len(containers)
    else:
        minumum = min(list(map(len, containers)))
        return len(list(filter(lambda c: len(c) == minumum,  containers)))


print("Day 17, Part 1 - Eggnog:", eggnog(1))
print("Day 17, Part 2 - Eggnog (minimum containers):", eggnog(2))
