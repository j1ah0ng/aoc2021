import numpy as np
import sys

def nFish(fish: np.ndarray, days=80) -> int:
    for _ in range(days):
        new_fish = fish - 1
        n_new = np.sum(new_fish < 0)
        new_fish[new_fish < 0] = 6
        new_fish = np.hstack((
            new_fish, np.ones(n_new) * 8
        ))
        fish = new_fish
    return len(new_fish)

def nFish2(fish: np.ndarray, days=256) -> int:
    clock = np.zeros(9, dtype=int)
    for f in fish:
        clock[f] += 1

    for i in range(days):
        new_clock = np.roll(clock, -1)
        new_clock[6] += clock[0]
        clock = new_clock

    return sum(clock)


if __name__ == "__main__":
    fish = []
    with open(sys.argv[1], 'r') as file:
        l = file.readline()[:-1]
        fish = np.array([int(x) for x in l.split(',')])

    print(nFish(fish))
    print(nFish2(fish))
