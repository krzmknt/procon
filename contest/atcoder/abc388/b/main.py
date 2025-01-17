from bisect import bisect_left, insort_left
from collections import deque
from copy import deepcopy
from heapq import heapify, heappop, heappush
from itertools import accumulate, combinations, permutations, product, pairwise
from math import ceil, factorial, floor, gcd, lcm, sqrt, dist
import sys


sys.setrecursionlimit(10**7)


def main():
    (N, D), *A = [[*map(int, line.split())] for line in open(0)]

    for k in range(1, D + 1):
        ans = max([t * (l + k) for t, l in A])
        print(ans)


if __name__ == "__main__":
    main()
