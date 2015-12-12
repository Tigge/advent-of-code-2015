#!/usr/bin/env python3

import re
import json


def number_sum():
    return sum(map(int, re.findall("-?[0-9]+", open("day_12.txt").read())))


def number_red_sum():
    inp = json.load(open("day_12.txt"))

    def visit(obj):
        if type(obj) is list:
            return sum(map(visit, obj))
        elif type(obj) is dict:
            if "red" not in obj.values():
                return sum(map(visit, obj.values()))
        elif type(obj) is int:
            return obj
        return 0
    return visit(inp)

print("Day 12, Part 1 - Sum of number:", number_sum())
print("Day 12, Part 2 - Sum of number (without red):", number_red_sum())
