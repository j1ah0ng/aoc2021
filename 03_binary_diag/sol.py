import numpy as np
import sys

def rates(bitstrings: list[str]) -> int:
    n_bits = len(bitstrings[0]) - 1
    ones   = [0 for i in range(n_bits)]
    zeros  = [0 for i in range(n_bits)]
    for bs in bitstrings:
        # assuming \n terminations
        for idx, c in enumerate(bs[:-1]):
            if c == "0":
                zeros[idx] += 1
            elif c == "1":
                ones[idx] += 1
            else:
                print("bad input")
                return -1
    epsilon = ""
    gamma = ""
    for i in range(n_bits):
        # assuming they are never equal
        if ones[i] > zeros[i]:
            epsilon += "1"
            gamma += "0"
        else:
            epsilon += "0"
            gamma += "1"
    epsilon = int(epsilon, 2)
    gamma = int(gamma, 2)
    return gamma * epsilon

def rates2(bitstrings: list[str]) -> int:
    n_bits = len(bitstrings[0]) - 1
    data = np.array(
        [[int(x) for x in line[:-1]] for line in [list(s) for s in bitstrings]],
        dtype=int,
    )
    least = data
    most = np.copy(data)

    lo = 0
    hi = 0

    # find the least common
    for place in range(n_bits):
        ones  = np.sum(least[:, place] == 1)
        zeros = np.sum(least[:, place] == 0)
        if ones < zeros:
            least = least[least[:, place] == 1]
        else:
            least = least[least[:, place] == 0]
        if len(least) == 1:
            lo = int("".join([str(x) for x in least[0].tolist()]), 2)
            break
    # then the most common
    for place in range(n_bits):
        ones  = np.sum(most[:, place] == 1)
        zeros = np.sum(most[:, place] == 0)
        if ones < zeros:
            most = most[most[:, place] == 0]
        else:
            most = most[most[:, place] == 1]
        if len(most) == 1:
            hi = int("".join([str(x) for x in most[0].tolist()]), 2)
            break

    return lo * hi

if __name__ == "__main__":
    bitstrings = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            bitstrings.append(line)
    print(rates(bitstrings))
    print(rates2(bitstrings))
