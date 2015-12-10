#!/usr/bin/env python3

import itertools


def plan_route(func=min):
    locations = set()
    distances = dict()
    results = dict()
    for line in open("day_9.txt").read().strip().splitlines():
        (fr, _, to, _, dist) = line.strip().split(" ")
        locations |= {fr, to}
        distances.update({(fr, to): int(dist), (to, fr): int(dist)})

    for p in itertools.permutations(locations):
        pdist = sum(map(lambda k: distances[k], zip(p[:-1], p[1:])))
        results[(p[0], p[len(p) - 1])] = func(pdist, results.get((p[0], p[len(p) - 1]), pdist))
    return results[func(results, key=results.get)]

print("Day 9, Part 1 - Minimal route:", plan_route(min))
print("Day 9, Part 2 - Maximal route:", plan_route(max))
