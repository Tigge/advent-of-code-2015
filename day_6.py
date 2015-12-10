#!/usr/bin/env python3


def six1():
    inp = open("day_6.txt").read().strip()
    grid = dict()
    for line in inp.split("\n"):
        parts = line.rsplit(" ", 3)
        fr = tuple(map(int, parts[1].split(",")))
        to = tuple(map(int, parts[3].split(",")))

        for x in range(fr[0], to[0] + 1):
            for y in range(fr[1], to[1] + 1):
                if (x, y) not in grid and (parts[0] == "turn on" or parts[0] == "toggle"):
                    grid[(x, y)] = True
                elif (x, y) in grid and (parts[0] == "turn off" or parts[0] == "toggle"):
                    del grid[(x, y)]
    return len(grid)


def six2():
    inp = open("day_6.txt").read().strip()
    grid = dict()
    for line in inp.split("\n"):
        parts = line.rsplit(" ", 3)
        fr = tuple(map(int, parts[1].split(",")))
        to = tuple(map(int, parts[3].split(",")))

        for x in range(fr[0], to[0] + 1):
            for y in range(fr[1], to[1] + 1):
                if parts[0] == "turn on":
                    grid[(x, y)] = grid.get((x, y), 0) + 1
                if parts[0] == "toggle":
                    grid[(x, y)] = grid.get((x, y), 0) + 2
                elif parts[0] == "turn off":
                    grid[(x, y)] = max(grid.get((x, y), 0) - 1, 0)
    return sum(grid.values())

print("Day 6, Part 1 - Lights:", six1())
print("Day 6, Part 2 - Birghtness: ", six2())
