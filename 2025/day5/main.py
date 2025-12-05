import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    out = f.readlines()
    ids = set([int(id.strip()) for id in ",".join(out).split(",\n,")[1].split(",")])
    ranges = [
        [int(r.strip()) for r in r.split("-")]
        for r in ",".join(out).split(",\n,")[0].split(",")
    ]


def part1() -> int:
    notSpoiled = set()

    for id in ids:
        for r in ranges:
            if id in range(r[0], r[1]):
                notSpoiled.add(id)
                break

    return len(notSpoiled)


def part2() -> int:
    sortedRanges = sorted((start, end) for start, end in ranges)
    merged = []
    for start, end in sortedRanges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return sum(end - start + 1 for start, end in merged)


print(f"Part1: {part1()}")
print(f"Part2: {part2()}")
