from bisect import bisect_left, insort_left
from collections import deque
from copy import deepcopy
from heapq import heapify, heappop, heappush
from itertools import accumulate, combinations, permutations, product, pairwise
from math import ceil, factorial, floor, gcd, lcm, sqrt, dist
import sys


sys.setrecursionlimit(10**7)


def main():
    # -----------------------
    # Input

    # 1 2
    # abcd
    # bcde
    # cdef
    H, W, *S = open(0).read().split()
    H = int(H)
    W = int(W)

    # -----------------------
    # Solve
    print(*S, sep="\n")

    # -----------------------
    # Output
    ans = True
    print(["No", "Yes"][ans])


if __name__ == "__main__":
    main()
