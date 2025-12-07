import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    lines = f.readlines()


def part1():
    beams = set()

    manifold = lines[0].find("S")
    beams.add(manifold)

    splits = 0
    for line in lines:
        if "^" not in line:
            continue

        for i in range(len(line)):
            if line[i] == "^" and i in beams:
                beams.add(i - 1)
                beams.add(i + 1)
                beams.remove(i)

                splits += 1

    return splits


def part2():
    beams = {}

    manifold = lines[0].find("S")
    beams[manifold] = 1

    splits = 1  # Start on 1 because of the initial timeline of the original beam
    for line in lines:
        if "^" not in line:
            continue

        for i in range(len(line)):
            if line[i] == "^" and i in beams:
                count = beams.get(i, 0)
                beams[i + 1] = count + beams.get(i + 1, 0)
                beams[i - 1] = count + beams.get(i - 1, 0)
                beams[i] = 0

                splits += count

    return splits


print(f"Part1: {part1()}")
print(f"Part2: {part2()}")
