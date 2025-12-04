import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    rows = [list(tile) for tile in f.readlines()]


def part1() -> int:
    def countAdjacent(y, x) -> int:
        count = 0
        for i in range(y - 1, y + 2):
            if not (0 <= i < len(rows)):
                continue

            for j in range(x - 1, x + 2):
                if not (0 <= j < len(rows[i])):
                    continue
                if j == x and i == y:
                    continue

                if rows[i][j] == "@":
                    count += 1

        return count

    validRolls = 0
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if rows[y][x] == "@" and countAdjacent(y, x) < 4:
                validRolls += 1

    return validRolls


def part2() -> int:
    flagged = []
    validRolls = 0

    def countAdjacent(y, x) -> int:
        count = 0
        for i in range(y - 1, y + 2):
            if not (0 <= i < len(rows)):
                continue

            for j in range(x - 1, x + 2):
                if not (0 <= j < len(rows[i])):
                    continue
                if j == x and i == y:
                    continue

                if rows[i][j] == "@":
                    count += 1

        return count

    while True:
        flagged.clear()

        for y in range(len(rows)):
            for x in range(len(rows[y])):
                if rows[y][x] == "@" and countAdjacent(y, x) < 4:
                    validRolls += 1
                    flagged.append([y, x])

        for tile in flagged:
            rows[tile[0]][tile[1]] = "x"

        if len(flagged) == 0:
            break

    return validRolls


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
