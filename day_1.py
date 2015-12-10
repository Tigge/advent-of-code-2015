#!/usr/bin/env python3


def floor(part=1):
    input_string = open("day_1.txt").read()
    current_floor = 0
    for i, val in enumerate(input_string, start=1):
        current_floor += 1 if val == '(' else -1
        if part == 2 and current_floor == -1:
            return i
    return current_floor

print("Day 1, Part 1 - Final floor:", floor(1))
print("Day 1, Part 2 - Instructions to basement: ", floor(2))
