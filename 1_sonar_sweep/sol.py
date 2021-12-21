import os
import sys

def sweep(a: list[int]) -> int:
    ct = 0
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            ct += 1

    return ct

def sweep2(a: list[int]) -> int:
    ct = 0
    last = sum(a[0:3])
    for i in range(4, len(a) + 1):
        now = sum(a[i-3:i])
        if sum(a[i-3:i]) > last:
            ct += 1
        last = now

    return ct

if __name__ == "__main__":
    nums = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            nums.append(int(line))
    print(sweep(nums))
    print(sweep2(nums))
