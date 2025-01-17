(D, N), *A = [[*map(int, l.split())] for l in open(0)]
dp = [24] * D

for L, R, H in A:
    for i in range(L - 1, R):
        dp[i] = min(dp[i], H)

print(sum(dp))
