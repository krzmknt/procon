[N], A, B = [[*map(int, line.split())] for line in open(0)]
A = [a - 1 for a in A]
B = [b - 1 for b in B]

dp = [-(10**6)] * N
dp[0] = 0

for i in range(N - 1):
    dp[A[i]] = max(dp[A[i]], dp[i] + 100)
    dp[B[i]] = max(dp[B[i]], dp[i] + 150)

print(dp[N - 1])
