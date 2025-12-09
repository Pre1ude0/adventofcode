import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    tiles = [[int(x) for x in i.split(",")] for i in f.readlines()]


def part1():
    maxArea = 0

    for i in range(len(tiles)):
        for j in range(len(tiles) - i):
            x1, x2 = tiles[i][0], tiles[i + j][0]
            y1, y2 = tiles[i][1], tiles[i + j][1]

            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > maxArea:
                maxArea = area

    return maxArea


def pointBetweenRed(px, py, poly):
    """
    Returns True if point is inside or ON the boundary of the polygon.

    I'm going to write comments for this function because even I don't really understand how it works
    """
    inside = False
    n = len(poly)

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        # check if point is on the boundary (edge) of the polygon
        dx = x2 - x1
        dy = y2 - y1
        dxp = px - x1
        dyp = py - y1

        if dx * dyp - dy * dxp == 0:
            if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2):
                return True  # on boundary

        # check if edge straddles the horizontal ray at y = py
        if (y1 > py) != (y2 > py):
            # find x coordinate where the edge intersects y = py
            xinters = x1 + (py - y1) * (dx / dy)
            if px < xinters:
                inside = not inside

    return inside


def part2():
    maxArea = 0
    for i in range(len(tiles)):
        for j in range(len(tiles) - i):
            x1, x2 = tiles[i][0], tiles[i + j][0]
            y1, y2 = tiles[i][1], tiles[i + j][1]

            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            if area > maxArea:
                inPolygon = True
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        if grid[y][x] != "X" or grid[y][x] != "#":
                            inPolygon = False
                            break
                    if not inPolygon:
                        break

                if inPolygon:
                    maxArea = area

    return maxArea


# Heres an extra function I wrote while trying to figure this out
def drawTiles():
    global grid
    maxX = max(tile[0] for tile in tiles) + 2
    maxY = max(tile[1] for tile in tiles) + 2

    grid = [["." for _ in range(maxX + 1)] for _ in range(maxY + 1)]

    prevTile = tiles[-1]
    for tile in tiles:
        x, y = tile
        prevX, prevY = prevTile

        # for lineY in range(min(y, prevY), max(y, prevY) + 1):
        #     if not lineY == prevY:
        #         grid[lineY][x] = "X"

        # for lineX in range(min(x, prevX), max(x, prevX) + 1):
        #     if not lineX == prevX:
        #         grid[y][lineX] = "X"

        grid[y][x] = "#"

        prevTile = tile

        for y in range(maxY + 1):
            for x in range(maxX + 1):
                if grid[y][x] != ".":
                    continue
                if pointBetweenRed(x, y, tiles):
                    grid[y][x] = "X"

    for row in grid:
        print("".join(row))


drawTiles()
print(f"Part1: {part1()}")
print(f"Part2: {part2()}")
