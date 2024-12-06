def getTiles():
    with open("input.txt", "r") as f:
        return f.readlines()

grid = getTiles()

x = 0
y = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            x = i
            y = j

print(x, y)
grid[x].replace("^", ".")

def part1():

    visited = []
    direction = "up"
    pos = x, y
    visited.append(pos)


    while 1:
        if direction == "up":
            if pos[0] - 1 < 0:
                return visited

            elif grid[pos[0] - 1][pos[1]] == "#":
                direction = "right"

            else:
                pos = pos[0] - 1, pos[1]
                if pos not in visited:
                    visited.append(pos)

        elif direction == "right":
            if pos[1] + 1 >= len(grid[0]):
                return visited

            elif grid[pos[0]][pos[1] + 1] == "#":
                direction = "down"

            else:
                pos = pos[0], pos[1] + 1
                if pos not in visited:
                    visited.append(pos)

        elif direction == "down":
            if pos[0] + 1 >= len(grid):
                return visited

            elif grid[pos[0] + 1][pos[1]] == "#":
                direction = "left"

            else:
                pos = pos[0] + 1, pos[1]
                if pos not in visited:
                    visited.append(pos)

        elif direction == "left":
            if pos[1] - 1 < 0:
                return visited

            elif grid[pos[0]][pos[1] - 1] == "#":
                direction = "up"

            else:
                pos = pos[0], pos[1] - 1
                if pos not in visited:
                    visited.append(pos)

    return []

def isStuck(path):

    direction = "up"
    pos = x, y
    stuck = 0

    hitAWallPoints = []
    startCountingHits = False

    while stuck < 10:
        if direction == "up":
            if pos[0] - 1 < 0:
                return False

            elif path[pos[0] - 1][pos[1]] == "#":
                direction = "right"
                if startCountingHits:
                    if pos not in hitAWallPoints:
                        hitAWallPoints.append(pos)
                    else:
                        stuck += 1

            elif path[pos[0] - 1][pos[1]] == "O":
                direction = "right"
                startCountingHits = True

            else:
                pos = pos[0] - 1, pos[1]

        elif direction == "right":
            if pos[1] + 1 >= len(grid[0]):
                return False

            elif path[pos[0]][pos[1] + 1] == "#":
                direction = "down"
                if startCountingHits:
                    if pos not in hitAWallPoints:
                        hitAWallPoints.append(pos)
                    else:
                        stuck += 1

            elif path[pos[0]][pos[1] + 1] == "O":
                direction = "down"
                startCountingHits = True

            else:
                pos = pos[0], pos[1] + 1

        elif direction == "down":
            if pos[0] + 1 >= len(grid):
                return False

            elif path[pos[0] + 1][pos[1]] == "#":
                direction = "left"
                if startCountingHits:
                    if pos not in hitAWallPoints:
                        hitAWallPoints.append(pos)
                    else:
                        stuck += 1

            elif path[pos[0] + 1][pos[1]] == "O":
                direction = "left"
                startCountingHits = True

            else:
                pos = pos[0] + 1, pos[1]

        elif direction == "left":
            if pos[1] - 1 < 0:
                return False

            elif path[pos[0]][pos[1] - 1] == "#":
                direction = "up"
                if startCountingHits:
                    if pos not in hitAWallPoints:
                        hitAWallPoints.append(pos)
                    else:
                        stuck += 1

            elif path[pos[0]][pos[1] - 1] == "O":
                direction = "up"
                startCountingHits = True

            else:
                pos = pos[0], pos[1] - 1

    return True

def part2():
    path = part1()

    grid = getTiles()

    stuck = 0

    for pos in path:
        copy = grid.copy()

        if pos != path[0]:
            lst = list(copy[pos[0]])
            lst[pos[1]] = "O"
            copy[pos[0]] = "".join(lst)

            print(pos)

            if isStuck(copy):
                stuck += 1

    return stuck





print(len(part1()))
print(part2())
