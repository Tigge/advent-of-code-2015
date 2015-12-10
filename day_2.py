#!/usr/bin/env python3


def paper_and_ribbon(part=1):
    paper = 0
    ribbon = 0
    for line in open("day_2.txt").read().split("\n"):
        (l, w, h) = tuple(map(int, line.split("x")))
        (r1, r2, _) = sorted((l, w, h))
        rib = r1 * 2 + r2 * 2 + l * w * h
        ribbon += rib
        (l, w, h) = (l * w, w * h, h * l)
        area = 2 * l + 2 * w + 2 * h + min(l, w, h)
        paper += area

    if part == 1:
        return paper
    else:
        return ribbon

print("Day 2, Part 1 - Square feet of paper:", paper_and_ribbon(1))
print("Day 2, Part 2 - Feet of ribbon: ", paper_and_ribbon(2))
