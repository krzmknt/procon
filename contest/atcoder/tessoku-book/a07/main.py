from itertools import accumulate

[N], _, *A = [[*map(int, line.split())] for line in open(0)]

nums = [0] * N

for L, R in sorted(A):
    nums[L - 1] += 1
    nums[R] -= 1

print(*accumulate(nums), sep="\n")
