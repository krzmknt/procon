from bisect import bisect_left, insort_left
from collections import deque
from copy import deepcopy
from heapq import heapify, heappop, heappush
from itertools import accumulate, combinations, permutations, product, pairwise
from math import ceil, factorial, floor, gcd, lcm, sqrt, dist
import sys


def main():
    # -----------------------
    # Input
    N = int(input())
    A = [*map(int, input().split())]

    # -----------------------
    # Solve
    ans = solve(N, A)

    # -----------------------
    # Output
    print(ans)


def solve(N, A):
    ans = 0
    for n in A:
        idx = bisect_left(A, n * 2)
        ans += N - idx
    return ans


if __name__ == "__main__":
    main()
