#!/usr/bin/env python3


def badwords_1(inp):
    VOWELS = "aeiou"
    double = False
    vowels = 0
    for x in range(len(inp)):
        tup = inp[x:x + 2]
        if len(tup) == 2:
            if tup in ["ab", "cd", "pq", "xy"]:
                return False
            elif tup[0] == tup[1]:
                double = True
        if tup[0] in VOWELS:
            vowels += 1

    return vowels >= 3 and double


def badwords_2(inp):
    for x in range(len(inp) - 2):
        if inp[x] == inp[x + 2]:
            break
    else:
        return False

    for x in range(0, len(inp) - 3):
        if inp.find(inp[x] + inp[x + 1], x + 2) != -1:
            break
    else:
        return False

    return True


def badwords(part=1):
    inp = open("day_5.txt").read().split("\n")
    if part == 1:
        return sum(map(lambda x: 1 if x else 0, map(badwords_1, inp)))
    else:
        return sum(map(lambda x: 1 if x else 0, map(badwords_2, inp)))

print("Day 5, Part 1 - Nice strings:", badwords(1))
print("Day 5, Part 2 - Nice strings (revised): ", badwords(2))
