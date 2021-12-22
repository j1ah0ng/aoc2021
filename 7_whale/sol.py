import numpy as np
import sys

def leastFuelOptimMedian(positions: np.ndarray) -> int:
    return int(np.sum(np.abs(
        positions - np.median(positions)
    )))

def leastFuelOptimSquares(positions: np.ndarray) -> int:
    # discreteness sux
    def getFuelWithRoundFn(fn):
        center = fn(np.mean(positions))
        delta  = np.abs(positions - center)
        return int(np.sum((delta + 1) * (delta / 2)))
    c1 = getFuelWithRoundFn(np.ceil)
    c2 = getFuelWithRoundFn(np.floor)
    return min(c1, c2)


if __name__ == "__main__":
    positions = []
    with open(sys.argv[1], 'r') as file:
        l = file.readline()[:-1]
        positions = np.array([int(x) for x in l.split(',')])

    print(leastFuelOptimMedian(positions))
    print(leastFuelOptimSquares(positions))
