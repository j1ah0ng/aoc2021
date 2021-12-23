import numpy as np
import sys
from functools import reduce
from operator import mul

c_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
i_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
d_open = [
    '(',
    '[',
    '{',
    '<',
]
d_close = [
    ')',
    ']',
    '}',
    '>',
]
def isOpen(c: str) -> bool:
    return c in d_open
def isClose(c: str) -> bool:
    return c in d_close
def isPair(o: str, c: str) -> bool:
    idx_o = d_open.index(o)
    idx_c = d_close.index(c)
    return idx_o == idx_c
def scoreLineCorrupt(line: str) -> int:
    stack = []
    for c in line:
        if isOpen(c):
            stack.append(c)
        elif isClose(c):
            # two cases: either empty or not.
            if not len(stack) == 0:
                # nonempty
                if isPair(stack[-1], c):
                    # ok.
                    stack.pop()
                else:
                    # not ok
                    return c_score[c]
            else:
                # empty
                return c_score[c]
    return 0 # either incomplete or uncorrupted
def scoreLineIncomplete(line: str) -> int:
    stack = []
    for c in line:
        if isOpen(c):
            stack.append(c)
        elif isClose(c):
            # two cases: either empty or not.
            if not len(stack) == 0:
                # nonempty
                if isPair(stack[-1], c):
                    # ok.
                    stack.pop()
                else:
                    # is corrupt
                    return 0
            else:
                # empty; is corrupt
                return 0
    closures = list(map(
        lambda o: d_close[d_open.index(o)],
        reversed(stack)
    ))
    return reduce(
        lambda acc, x: (acc * 5) + i_score[x],
        closures,
        0
    )

def scoreCorrupt(lines: list[str]) -> int:
    return reduce(lambda acc, line: acc + scoreLineCorrupt(line), lines, 0)
def scoreIncomplete(lines: list[str]) -> int:
    scores = sorted(list(filter(lambda c: c != 0,map(scoreLineIncomplete, lines))))
    return scores[int(len(scores)/2)]

if __name__ == "__main__":
    lines = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            lines.append(line)

    print(scoreCorrupt(lines))
    print(scoreIncomplete(lines))
