#!/usr/bin/env python3

import itertools
import re

weapons = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0)]

armors = [
    ("None", 0, 0, 0),
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5)]

rings = [
    ("None, Left", 0, 0, 0),
    ("None, Right", 0, 0, 0),
    ("Damage +1", 25, 1, 0),
    ("Damage +2", 50, 2, 0),
    ("Damage +3", 100, 3, 0),
    ("Defense +1", 20, 0, 1),
    ("Defense +2", 40, 0, 2),
    ("Defense +3", 80, 0, 3)]


def rpg(part=1):
    monster_hp, monster_damage, monster_armor = map(int, re.findall("[0-9]+", open("day_21.txt").read()))
    player_hp = 100
    win_costs = list()
    loose_costs = list()
    for weapon in weapons:
        for armor in armors:
            for ring1, ring2 in itertools.combinations(rings, 2):
                player_cost = weapon[1] + armor[1] + ring1[1] + ring2[1]
                player_damage = weapon[2] + ring1[2] + ring2[2]
                player_armor = armor[3] + ring1[3] + ring2[3]

                mhp = monster_hp
                php = player_hp
                while True:
                    mhp -= (player_damage - monster_armor)
                    if mhp <= 0:
                        win_costs.append(player_cost)
                        break
                    php -= (monster_damage - player_armor)
                    if php <= 0:
                        loose_costs.append(player_cost)
                        break
    if part == 1:
        return min(win_costs)
    else:
        return max(loose_costs)

print("Day 21, Part 1 - cost (win, min):", rpg(1))
print("Day 21, Part 2 - cost (loose, max):", rpg(2))
