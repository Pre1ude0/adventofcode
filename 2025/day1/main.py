import os


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    numbers = [line.strip() for line in f.readlines()]


def part1() -> int:
    curPos = 50
    hits = 0
    for number in numbers:
        dir, steps = number[0], int(number[1:])
        steps = steps % 100

        if dir == "L":
            curPos -= steps
        elif dir == "R":
            curPos += steps

        if curPos < 0:
            curPos = 100 + curPos
        elif curPos > 99:
            curPos = curPos - 100

        if curPos == 0:
            hits += 1

    return hits


def part2() -> int:
    curPos = 50
    hits = 0
    prevZero = False
    for number in numbers:
        dir, steps = number[0], int(number[1:])
        extraHits, steps = divmod(steps, 100)
        hits += abs(extraHits)

        if dir == "L":
            curPos -= steps
        elif dir == "R":
            curPos += steps

        if curPos < 0 or curPos > 99:
            if curPos < 0:
                curPos += 100
            elif curPos > 99:
                curPos -= 100
            if curPos != 0:
                hits += 1 if not prevZero else 0

        if curPos == 0:
            hits += 1
        prevZero = curPos == 0

    return hits


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
