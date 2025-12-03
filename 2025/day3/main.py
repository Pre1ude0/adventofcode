import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    banks = [list(i.strip()) for i in f.readlines()]


def part1() -> int:
    maxJoltage = 0
    for bank in banks:
        maxJ = max(bank[:-1])
        maxJoltage += int(str(maxJ) + str(max(bank[bank.index(maxJ) + 1 :])))

    return maxJoltage


def part2() -> int:
    maxJoltage = 0
    for bank in banks:
        fullJoltage = ""
        for i in range(12):
            maxJ = max(bank[: -(11 - i)] if 11 - i > 0 else bank)
            fullJoltage += str(maxJ)
            bank = bank[bank.index(maxJ) + 1 :]
        maxJoltage += int(fullJoltage)

    return maxJoltage


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
