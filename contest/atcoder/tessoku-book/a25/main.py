H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

# dp[i][j]: (i, j)に到達するまでの経路の数
dp = [[0] * W for _ in range(H)]

for i in range(H):
    if C[i][0] == "#":
        break
    dp[i][0] = 1

for j in range(W):
    if C[0][j] == "#":
        break
    dp[0][j] = 1

for i in range(1, H):
    for j in range(1, W):
        if C[i][j] == "#":
            continue
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[H - 1][W - 1])
