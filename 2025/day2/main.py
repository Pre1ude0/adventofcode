import os
import re

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    ranges = [
        [int(id) for id in range.split("-")] for range in f.read().strip().split(",")
    ]


def part1() -> int:
    invIdSum = 0
    pattern = re.compile(r"^(\d+)\1$")
    for endpoints in ranges:
        for id in range(endpoints[0], endpoints[1]):
            if len(str(id)) % 2 != 0:
                continue

            if pattern.match(str(id)):
                invIdSum += id

    return invIdSum


def part2() -> int:
    invIdSum = 0
    pattern = re.compile(r"^(\d+)\1+$")
    for endpoints in ranges:
        for id in range(endpoints[0], endpoints[1]):
            if pattern.match(str(id)):
                invIdSum += id

    return invIdSum


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
