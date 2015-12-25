#!/usr/bin/env python3


def next_grid(grid):
    new_grid = dict()
    for (x, y), value in grid.items():
        neighbours = 0
        for cx in range (-1, 2):
            for cy in range (-1, 2):
                if cx != 0 or cy != 0:
                    neighbours += grid.get((x + cx, y + cy), 0)
        if grid[(x, y)] == 1 and neighbours != 2 and neighbours != 3:
            new_grid[(x, y)] = 0
        elif grid[(x, y)] == 0 and neighbours == 3:
            new_grid[(x, y)] = 1
        else:
            new_grid[(x, y)] = grid[(x, y)]
    return new_grid


def fix_broken(grid):
    grid[(0, 0)] = 1
    grid[(0, 99)] = 1
    grid[(99, 0)] = 1
    grid[(99, 99)] = 1


def lights(part=1):
    grid = dict()
    for y, line in enumerate(open("day_18.txt").read().strip().split("\n")):
        for x, value in enumerate(line):
            grid[(x, y)] = 1 if value == "#" else 0
    if part == 2:
        fix_broken(grid)

    for i in range(100):
        grid = next_grid(grid)
        if part == 2:
            fix_broken(grid)
    return sum(grid.values())

print("Day 18, Part 1 - lights:", lights(1))
print("Day 18, Part 2 - lights (with broken):", lights(2))
