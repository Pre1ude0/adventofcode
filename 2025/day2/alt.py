import os

with open(os.path.join(os.path.dirname(__file__), "inputSmall.txt")) as f:
    ranges = [
        [int(id) for id in range.split("-")] for range in f.read().strip().split(",")
    ]


def part1() -> int:
    invIdSum = 0
    for endpoints in ranges:
        for id in range(endpoints[0], endpoints[1]):
            if len(str(id)) % 2 != 0:
                continue

            half = len(str(id)) // 2

            if str(id)[:half] == str(id)[half:]:
                invIdSum += id

    return invIdSum


def part2() -> int:
    invIdSum = 0
    for endpoints in ranges:
        for id in range(endpoints[0], endpoints[1] + 1):
            for i in range(len(str(id)) - 1):
                q, shouldBeZero = divmod(len(str(id)), i + 2)
                if shouldBeZero != 0:
                    continue

                slices = [(str(id)[j : j + q]) for j in range(0, len(str(id)), q)]

                match = True
                for s in slices:
                    if slices[0] != s:
                        match = False
                        break

                if match:
                    invIdSum += id
                    break

    return invIdSum


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
