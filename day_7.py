#!/usr/bin/env python3


def circuit(part=1):
    lines = open("day_7.txt", "r").read().strip().split("\n")
    signals = {}
    while len(lines) > 0:
        line = lines.pop(0)
        parts = line.split(" ")
        destination = parts[len(parts) - 1]
        ok = True
        for i in range(len(parts) - 1):
            if parts[i].isupper() or parts[i] == "->":
                continue
            try:
                parts[i] = int(parts[i])
            except ValueError:
                try:
                    parts[i] = signals[parts[i]]
                except KeyError:
                    ok = False
                    break

        if not ok:
            lines.append(line)
            continue
        if parts[0] == "NOT":
            signals[destination] = ~parts[1]
        elif parts[1] == "AND":
            signals[destination] = parts[0] & parts[2]
        elif parts[1] == "OR":
            signals[destination] = parts[0] | parts[2]
        elif parts[1] == "LSHIFT":
            signals[destination] = parts[0] << parts[2]
        elif parts[1] == "RSHIFT":
            signals[destination] = parts[0] >> parts[2]
        else:
            if part == 2 and destination == 'b':
                signals[destination] = circuit(part=1)
            else:
                signals[destination] = parts[0]
    return signals['a']

print("Day 7, Part 1 - Lights:", circuit(1))
print("Day 7, Part 2 - Birghtness: ", circuit(2))
