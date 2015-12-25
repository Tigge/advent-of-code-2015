#!/usr/bin/env python3

import random


def permutations(molecule, replacements):
    molecules = set()
    for key in replacements:
        index = 0
        while True:
            index = molecule.find(key, index)
            if index == -1:
                break
            for r in replacements[key]:
                molecules.add(molecule[0:index] + r + molecule[index + len(key):])
            index += len(key)
    return molecules


def find(molecule, replacements):
    replacements = list(replacements.items())
    random.shuffle(replacements)
    counts = 0
    work_molecule = molecule
    while True:
        for k, v in replacements:
            if k in work_molecule:
                work_molecule = work_molecule.replace(k, v, 1)
                counts += 1
                break
        else:
            if work_molecule == "e":
                return counts
            else:
                counts = 0
                work_molecule = molecule
                random.shuffle(replacements)


def rudchem(part=1):
    lines = open("day_19.txt").read().strip().split("\n")
    start_molecule = lines[-1]
    replacements = dict()
    replacements_inverted = dict()
    for line in lines[:-2]:
        parts = line.split(" ")
        replacements[parts[0]] = replacements.get(parts[0], []) + [parts[2]]
        replacements_inverted[parts[2]] = parts[0]

    if part == 1:
        return len(permutations(start_molecule, replacements))
    else:
        return find(start_molecule, replacements_inverted)


print("Day 19, Part 1 - permutations:", rudchem(1))
print("Day 19, Part 2 - length:", rudchem(2))
