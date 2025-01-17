(N, _), *A = [[*map(int, line.split())] for line in open(0)]

# A(N-長ビット列のリスト)の要素をいくつか選んで、ORがAll 1になるようにする
# そのような選び方の要素数の最小値を求める

# "0 1 1" => 3
A = [int("".join(map(str, bits)), 2) for bits in A]

# dp[a] = 商品集合aを獲得するのに必要なクーポン枚数
dp = [0] + [INF := N + 1] * (1 << N)

for i in range(len(dp) - 1):
    for a in A:
        dp[i | a] = min(dp[i | a], dp[i] + 1)

print(dp[-2] if dp[-2] < INF else -1)
