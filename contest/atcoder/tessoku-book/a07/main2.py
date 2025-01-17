[days], _, *A = [[*map(int, line.split())] for line in open(0)]

nums = [0] + [0] * days

for L, R in sorted(A):
    nums[L - 1] += 1
    nums[R] -= 1

for i in range(days):
    nums[i + 1] += nums[i]

for num in nums[:-1]:
    print(num)
