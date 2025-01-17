N, K = map(int, input().split())
ans = len(
    [1 for a in range(1, N + 1) for b in range(1, N + 1) if 1 <= K - (a + b) <= N]
)
print(ans)
