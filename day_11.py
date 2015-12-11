#!/usr/bin/env python3

import itertools


def gen_passwords(p):
    while True:
        for i in range(len(p) - 1, -1, -1):
            if p[i] != 'z':
                p = p[0:i] + chr(ord(p[i]) + 1) + p[i + 1:]
                break
            else:
                p = p[0:i] + 'a' + p[i + 1:]
        else:
            return
        yield p

def valid_password(p):
    for i in range(0, len(p) - 2):
        if ord(p[i]) + 1 == ord(p[i + 1]) and ord(p[i]) + 2 == ord(p[i + 2]):
            break
    else:
        return False

    if p.find('i') != -1 or p.find('o') != -1 or p.find('l') != -1:
        return False

    glen = map(lambda a: (len(list(a[1]))), itertools.groupby(p))
    glef = filter(lambda b: b >= 2, glen)
    return len(list(glef)) >= 2 or len(list(glef)) >= 1


def gen_valid_passwords(p):
    for p in gen_passwords(p):
        if valid_password(p):
            yield p


def password(part=1):
    inp = open("day_11.txt").read().strip()

    generator = gen_valid_passwords(inp)
    new_password = next(generator)
    if part == 2:
        new_password = next(generator)
    return new_password


print("Day 11, Part 1 - Next password:", password(1))
print("Day 11, Part 2 - Next password (again):", password(2))
