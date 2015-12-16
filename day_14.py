#!/usr/bin/env python3

import itertools


def reindeers_parse():
    reindeers = []
    for line in open("day_14.txt").read().split("\n"):
        parts = line.split(" ")
        reindeers.append({"name": parts[0], "km/s": int(parts[3]), "fly": int(parts[6]), "rest": int(parts[13])})
    return reindeers


def reindeer_distance(reindeer, seconds):
        period = (reindeer["fly"] + reindeer["rest"])
        return ((seconds // period) * reindeer["fly"] + min(seconds % period, reindeer["fly"])) * reindeer["km/s"]


def score_system_1(seconds):
    reindeers = reindeers_parse()
    distance = dict()
    for reindeer in reindeers:
        distance[reindeer["name"]] = reindeer_distance(reindeer, seconds)
    return max(distance.values())


def score_system_2(seconds):
    reindeers = reindeers_parse()
    distances = dict()
    for second in range(1, seconds+1):
        lists = list(map(lambda r: (reindeer_distance(r, second), r), reindeers))
        best = max(lists, key=lambda r: r[0])[0]
        for distance, reindeer in lists:
            if distance == best:
                distances[reindeer["name"]] = distances.get(reindeer["name"], 0) + 1
    return max(distances.values())

print("Day 14, Part 1 - Best score:", score_system_1(2503))
print("Day 14, Part 2 - Best score (new system):", score_system_2(2503))
