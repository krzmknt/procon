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
    N = int(input())
    A = [*map(int, input().split())]
    D = [0] * (N + 1)

    # -----------------------
    # Solve

    curr_sum = 0

    for i in range(N):
        curr_sum += D[i]
        curr_ai = A[i] + curr_sum
        coins_to_give = min(curr_ai, N - i - 1)

        if 0 < coins_to_give:
            D[i + 1] += 1
            if i + coins_to_give < N:
                D[i + 1 + coins_to_give] -= 1

        A[i] = curr_ai - coins_to_give

    # -----------------------
    # Output
    print(*A)


def solve():
    return True


if __name__ == "__main__":
    main()
