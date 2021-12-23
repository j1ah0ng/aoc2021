import numpy as np
import sys

segs = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

nsegs = {
    0: [0, 1, 2, 4, 5, 6],
    1: [2, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 5, 6],
    4: [1, 2, 3, 5],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    7: [0, 2, 5],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6],
}

def is1478(s: str) -> int:
    n = len(s)
    if (n == segs[1]):
        return 1
    elif (n == segs[4]):
        return 4
    elif (n == segs[7]):
        return 7
    elif (n == segs[8]):
        return 8
    else:
        return -1

def count1478(entries: list[[list[str], list[str]]]) -> int:
    count = 0
    for entry in entries:
        out = entry[1]
        for o in out:
            if is1478(o) != -1:
                count += 1

    return count

def isMatch(s1: str, s2: str) -> bool:
    if not len(s1) == len(s2):
        return False
    else:
        for c in s1:
            if not c in s2:
                return False
        return True

def getSegmentMapping(uniq: list[str]) -> dict[int, str]:
    #  0000
    # 1    2
    # 1    2
    #  3333
    # 4    5
    # 4    5
    #  6666
    im = {}
    # use frequency analysis to find 1, 4, 5
    uniq_np = np.array(list("".join(uniq)))
    freqs   = np.unique(uniq_np, return_counts=True)
    im[1] = freqs[0][np.where(freqs[1] == 6)[0][0]]
    im[4] = freqs[0][np.where(freqs[1] == 4)[0][0]]
    im[5] = freqs[0][np.where(freqs[1] == 9)[0][0]]
    # find the unique-length numbers
    nums = {}
    for u in uniq:
        n = is1478(u)
        if n != -1:
            nums[n] = u
    # elicit the 2
    im[2] = list(filter(lambda c: c != im[5], list(nums[1])))[0]
    # elicit the 3
    im[3] = list(
        filter(
            lambda c: (c != im[1] and c != im[2] and c != im[5]),
            list(nums[4])
        )
    )[0]
    # elicit the 0
    im[0] = list(
        filter(
            lambda c: (c != im[2] and c != im[5]),
            list(nums[7])
        )
    )[0]
    # finally elicit the 6
    im[6] = list(
        filter(
            lambda c: c not in im.values(),
            list(nums[8])
        )
    )[0]
    return im

def getNumberMapping(lut: dict[int, str]) -> dict[str, int]:
    mapping = {}
    for (i, vs) in nsegs.items():
        mapping[i] = list(map(lambda idx: lut[idx], vs))
    return mapping

def getNumber(lut: dict[int, str], s: str) -> int:
    for k, v in lut.items():
        if isMatch(v, s):
            return k
    return -1

def getTotal(lut: dict[int, str], ss: list[str]) -> int:
    acc = getNumber(lut, ss[0])
    for s in ss[1:]:
        acc *= 10
        acc += getNumber(lut, s)
    return acc

def countTotal(entries: list[[list[str], list[str]]]) -> int:
    acc = 0
    for entry in entries:
        sm = getSegmentMapping(entry[0])
        nm = getNumberMapping(sm)
        acc += getTotal(nm, entry[1])
    return acc

if __name__ == "__main__":
    entries = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            s = line.split('|')
            left = s[0].split()
            right = s[1].split()
            entries.append( (left, right) )

    print(count1478(entries))
    print(countTotal(entries))

