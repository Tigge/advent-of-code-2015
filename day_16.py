#!/usr/bin/env python3


def which_sue(part=1):
    sues = []
    for line in open("day_16.txt").read().strip().split("\n"):
        parts = line.split(" ")
        sues.append({parts[2][:-1]: int(parts[3][:-1]),
                     parts[4][:-1]: int(parts[5][:-1]),
                     parts[6][:-1]: int(parts[7])})

    target_sue = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,
                  "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3,
                  "cars": 2, "perfumes": 1}

    for nr, sue in enumerate(sues, start=1):
        for item, count in target_sue.items():
            if item in sue:
                if part == 2 and item in ["cats", "trees"]:
                    if sue[item] <= count:
                        break
                elif part == 2 and item in ["pomeranians", "goldfish"]:
                    if sue[item] >= count:
                        break
                elif sue[item] != count:
                    break
        else:
            return nr


print("Day 16, Part 1 - Sue:", which_sue(1))
print("Day 16, Part 1 - Sue (fixed):", which_sue(2))
