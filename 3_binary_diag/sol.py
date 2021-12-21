import os
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
    print("epsilon: %s" % epsilon)
    print("gamma: %s" % gamma)
    epsilon = int(epsilon, 2)
    gamma = int(gamma, 2)
    return gamma * epsilon

if __name__ == "__main__":
    bitstrings = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            bitstrings.append(line)
    print(rates(bitstrings))
