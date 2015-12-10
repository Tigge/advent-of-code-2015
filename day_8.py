#!/usr/bin/env python3


import string


def encode_diff():
    inp = open("day_8.txt").read().strip()
    os = 0
    rs = 0

    for line in inp.split("\n"):
        i = 0
        os += len(line)
        line = line[1:-1]
        while i < len(line):
            if line[i] == "\\" and i < len(line) - 1:
                if line[i + 1] == "\\" or line[i + 1] == "\"":
                    i += 1
                elif line[i + 1] == "x" and i < len(line) - 3 and line[i + 2] in string.hexdigits and line[i + 3] in string.hexdigits:
                    i += 3
            rs += 1
            i += 1
    return os - rs


def decode_diff():
    inp = open("day_8.txt").read().strip()
    os = 0
    rs = 0

    for line in inp.split("\n"):
        os += len(line)
        rs += 2
        for char in line:
            if char == "\\" or char == "\"":
                rs += 1
            rs += 1
    return rs - os

print("Day 8, Part 1 - Encode diff:", encode_diff())
print("Day 8, Part 2 - Decode diff:", decode_diff())
