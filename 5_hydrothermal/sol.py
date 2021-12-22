import numpy as np
import sys

def getOverlaps(vents: list[tuple[tuple[int, int], tuple[int, int]]], width: int) -> int:
    seafloor = np.zeros((width, width), dtype=int)
    for vent in vents:
        begin = vent[0]
        end   = vent[1]
        if begin[0] == end[0]:
            # Constant row
            if end[1] < begin[1]:
                tmp = end
                end = begin
                begin = tmp
            seafloor[begin[0], begin[1]:end[1]+1] = seafloor[begin[0], begin[1]:end[1]+1] + 1
        elif begin[1] == end[1]:
            # Constant col
            if end[0] < begin[0]:
                tmp = end
                end = begin
                begin = tmp
            seafloor[begin[0]:end[0]+1, begin[1]] = seafloor[begin[0]:end[0]+1, begin[1]] + 1
    print(seafloor.T)
    return np.sum(seafloor > 1)

def getOverlaps2(vents: list[tuple[tuple[int, int], tuple[int, int]]], width: int) -> int:
    seafloor = np.zeros((width, width), dtype=int)
    for vent in vents:
        begin = vent[0]
        end   = vent[1]
        if begin[0] == end[0]:
            # Constant row
            if end[1] < begin[1]:
                tmp = end
                end = begin
                begin = tmp
            seafloor[begin[0], begin[1]:end[1]+1] = seafloor[begin[0], begin[1]:end[1]+1] + 1
        elif begin[1] == end[1]:
            # Constant col
            if end[0] < begin[0]:
                tmp = end
                end = begin
                begin = tmp
            seafloor[begin[0]:end[0]+1, begin[1]] = seafloor[begin[0]:end[0]+1, begin[1]] + 1
        else:
            # 45 deg
            pts = np.linspace(begin, end, num=np.abs(begin[0]-end[0])+1, dtype=int)
            for pt in pts:
                seafloor[pt[0], pt[1]] = seafloor[pt[0], pt[1]] + 1

    print(seafloor.T)
    return np.sum(seafloor > 1)

if __name__ == "__main__":
    vents = []
    width = 0
    with open(sys.argv[1], 'r') as file:
        for line in file:
            chunks = line.split()
            fst = chunks[0]
            snd = chunks[2]
            begin = tuple(int(x) for x in fst.split(','))
            end   = tuple(int(x) for x in snd.split(','))
            vents.append( (begin, end) )
            width = max((
                width, begin[0], begin[1], end[0], end[1]
            )) + 1

    print(getOverlaps(vents, width))
    print(getOverlaps2(vents, width))
