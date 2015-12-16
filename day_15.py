#!/usr/bin/env python3


def iterator(number, parts):
    if parts == 1:
        yield (number,)
    else:
        for a in range(1, number):
            for b in iterator(number - a, parts - 1):
                yield (a,) + b


def cookie_score(part=1):
    cookies = dict()
    for line in open("day_15.txt").read().strip().split("\n"):
        parts = line.split(" ")
        cookies[parts[0][:-1]] = {"capacity": int(parts[2][:-1]), "durability": int(parts[4][:-1]),
                                  "flavor": int(parts[6][:-1]), "texture": int(parts[8][:-1]),
                                  "calories": int(parts[10])}
    cookies_key = list(cookies.keys())

    best_score = 0
    for amounts in iterator(100, len(cookies)):
        results = {"capacity": 0, "durability": 0, "flavor": 0, "texture": 0, "calories": 0}
        for item, amount in enumerate(amounts):
            cookie = cookies[cookies_key[item]]
            results["capacity"] += cookie["capacity"] * amount
            results["durability"] += cookie["durability"] * amount
            results["flavor"] += cookie["flavor"] * amount
            results["texture"] += cookie["texture"] * amount
            results["calories"] += cookie["calories"] * amount

        score = (max(0, results["capacity"]) * max(0, results["durability"]) *
                 max(0, results["flavor"]) * max(0, results["texture"]))
        if part == 1 or results["calories"] == 500:
            best_score = max(best_score, score)
    return best_score


print("Day 15, Part 1 - Best score:", cookie_score(1))
print("Day 15, Part 1 - Best score (500 kcal):", cookie_score(2))
