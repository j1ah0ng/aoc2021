import os
import sys

def dive(motions: list[tuple[str, int]]) -> int:
    forward = 0
    down = 0
    up = 0
    for motion in motions:
        if motion[0] == "forward":
            forward += motion[1]
        elif motion[0] == "down":
            down += motion[1]
        elif motion[0] == "up":
            up += motion[1]
        else:
            print("received bad input")
            return -1

    depth = down - up
    return depth * forward

def dive2(motions: list[tuple[str, int]]) -> int:
    forward = 0
    aim = 0
    depth = 0
    for motion in motions:
        if motion[0] == "forward":
            forward += motion[1]
            depth += aim * motion[1]
        elif motion[0] == "down":
            aim += motion[1]
        elif motion[0] == "up":
            aim -= motion[1]
        else:
            print("received bad input")
            return -1

    return depth * forward

if __name__ == "__main__":
    vectors = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            spl = line.split(" ")
            direction = spl[0]
            amt = int(spl[1])
            vectors.append( (direction, amt) )
    print(dive(vectors))
    print(dive2(vectors))
