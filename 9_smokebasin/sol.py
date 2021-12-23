import numpy as np
import sys
from functools import reduce
from operator import mul

def getNeighbours(p: [int, int], r: int, c: int) -> list[[int, int]]:
    neighbours = []
    if p[0] == 0:
        if p[1] == 0:
            # top left
            neighbours = [ (1, 0), (0, 1) ]
        elif p[1] == c-1:
            # top right
            neighbours = [ (1, c-1), (0, c-2) ]
        else:
            # top row
            neighbours = [ (0, p[1]-1), (1, p[1]), (0, p[1]+1) ]
    elif p[0] == r-1:
        if p[1] == 0:
            # bottom left
            neighbours = [ (r-2, 0), (r-1, 1) ]
        elif p[1] == c-1:
            # bottom right
            neighbours = [ (r-2, c-1), (r-1, c-2) ]
        else:
            # bottom row
            neighbours = [ (r-1, p[1]-1), (r-2, p[1]), (r-1, p[1]+1) ]
    else:
        if p[1] == 0:
            # left edge
            neighbours = [ (p[0]-1, 0), (p[0], 1), (p[0]+1, 0) ]
        elif p[1] == c-1:
            # right edge
            neighbours = [ (p[0]-1, c-1), (p[0], c-2), (p[0]+1, c-1) ]
        else:
            # centre
            neighbours = [
                (p[0]-1, p[1]),
                (p[0]+1, p[1]),
                (p[0], p[1]-1),
                (p[0], p[1]+1),
            ]
    return neighbours

def saliency(seafloor: list[list[int]], point: [int, int]) -> int:
    r = len(seafloor)
    c = len(seafloor[0])
    basin = [point]

    def ok(p: [int, int]) -> bool:
        non_max = seafloor[p[0]][p[1]] != 9
        not_basin = not p in basin
        return non_max and not_basin

    buf = list(filter(ok, getNeighbours(point, r, c)))

    while len(buf) != 0:
        basin.extend(buf)       # Buf contains the non-9 pts from last iter
        new_neighbours = []
        for pt in buf:
            new_neighbours.extend(getNeighbours(pt, r, c))
        # Dedup and filter
        buf = list(filter(ok, list(set(new_neighbours))))

    # found basin
    return len(basin)

def getReprPts(seafloor: list[list[int]]) -> list[[int, int]]:
    basin_pts = []
    r = len(seafloor)
    c = len(seafloor[0])
    for i in range(r):
        for j in range(c):
            pt = (i, j)
            if all(seafloor[x[0]][x[1]] > seafloor[i][j] for x in getNeighbours(pt, r, c)):
                basin_pts.append(pt)

    return basin_pts

def sumRisk(seafloor: list[list[int]]) -> int:
    return reduce(
        lambda acc, x: acc + 1 + seafloor[x[0]][x[1]],
        getReprPts(seafloor),
        0
    )

def calcBasins(seafloor: list[list[int]]) -> int:
    return reduce(mul, sorted(list(map(
        lambda pt: saliency(seafloor, pt),
        getReprPts(seafloor)
    )))[-3:])

if __name__ == "__main__":
    lines = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            l = list(map(lambda c: int(c), list(line[:-1])))
            lines.append(l)

    print(sumRisk(lines))
    print(calcBasins(lines))
