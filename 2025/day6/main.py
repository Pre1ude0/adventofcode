import os
from math import prod

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.readlines()


def part1():
    rows = [list(map(int, line.split())) for line in lines[:-1]]
    operations = list(map(list, zip(*rows)))
    operators = [i for i in lines[-1].split()]

    total = 0

    for o in range(len(operations)):
        if operators[o] == "+":
            total += sum(operations[o])

        elif operators[o] == "*":
            total += prod(operations[o])

    return total


def part2():
    operators = [i for i in lines[-1].split()]
    opLines = lines[:-1]
    operations = []

    j = 0
    newOp = []
    longestLine = max(len(line) for line in opLines)
    while True:
        if j >= longestLine:
            break

        number = ""
        for i in range(len(opLines)):
            if j < len(opLines[i]) and opLines[i][j] != " ":
                number += opLines[i][j]

        if number.strip() == "":
            operations.append(newOp)
            newOp = []
        else:
            newOp.append(int(number))

        j += 1

    total = 0
    for o in range(len(operations)):
        if operators[o] == "+":
            total += sum(operations[o])

        elif operators[o] == "*":
            total += prod(operations[o])

    return total


print(f"Part1: {part1()}")
print(f"Part2: {part2()}")
