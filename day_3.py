#!/usr/bin/env python3


def walker(inp):
    house = {(0, 0): True}
    x = 0
    y = 0
    for char in inp:
        if char == ">":
            x += 1
        elif char == "<":
            x -= 1
        elif char == "^":
            y -= 1
        elif char == "v":
            y += 1
        house[(x, y)] = True
    return house


def santa(part=1):
    inp = open("day_3.txt").read()
    if part == 1:
        return len(walker(inp))
    else:
        houses = walker(inp[0::2])
        houses.update(walker(inp[1::2]))
        return len(houses)

print("Day 3, Part 1 - At least one present:", santa(1))
print("Day 3, Part 2 - At least one present (+robot): ", santa(2))
