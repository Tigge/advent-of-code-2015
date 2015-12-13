#!/usr/bin/env python3

import itertools


def table_placement(part=1):
    happy_map = {}
    persons = set()
    for line in open("day_13.txt"):
        parts = line.strip().split(" ")
        happy_map[(parts[0], parts[10][:-1])] = int(parts[3]) if parts[2] == "gain" else -int(parts[3])
        persons.add(parts[0])

    if part == 2:
        for person in persons:
            happy_map[(person, "Me")] = 0
            happy_map[("Me", person)] = 0
        persons.add("Me")

    best = (None, None)
    for p in itertools.permutations(persons):
        if p[0] != list(persons)[0]:
            continue
        happy = 0
        for i, person in enumerate(p):
            happy += happy_map[(person, p[(i - 1) % len(p)])] + happy_map[(person, p[(i + 1) % len(p)])]
        if best[0] is None or happy > best[0]:
            best = (happy, p)
    return best[0]


print("Day 13, Part 1 - Total happiness:", table_placement(1))
print("Day 13, Part 2 - Total happiness (with me):", table_placement(2))
