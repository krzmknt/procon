[N], *A = [[*map(int, line.split())] for line in open(0)]

# dp[L][R] := the max score of the game when the blocks in [L, R] are left
dp = [[0] * N for _ in range(N)]

for L in range(N):
    for R in [*range(L + 1, N)][::-1]:
        current_score = dp[L][R]

        def if_block_is_left(block_pos):
            return L <= block_pos - 1 <= R

        # Remove the left block (move down on the square)
        block_pos, score = A[L]
        dp[L + 1][R] = current_score + score * if_block_is_left(block_pos)

        # Remove the right block (move left on the square)
        block_pos, score = A[R]
        dp[L][R - 1] = max(
            dp[L][R - 1], current_score + score * if_block_is_left(block_pos)
        )


ans = max(dp[i][i] for i in range(N))
print(ans)
