S, T = input(), input()

# dp[i][j] := the length of the longest common subsequence of S[:i] and T[:j]
dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

for i in range(len(S)):
    for j in range(len(T)):
        if S[i] == T[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[len(S)][len(T)])
