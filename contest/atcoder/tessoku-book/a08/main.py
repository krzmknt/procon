from itertools import accumulate

# ===================
# input
# -------------------
H, W = map(int, input().split())
X = []
for _ in range(H):
    X.append([*map(int, input().split())])

Q = int(input())
Y = []
for _ in range(Q):
    Y.append([*map(int, input().split())])


# ===================
# Accumulate
# -------------------
for i in range(H):
    X[i] = list(accumulate(X[i]))

for j in range(W):
    for i in range(1, H):
        X[i][j] += X[i - 1][j]


# ===================
# output
# -------------------
for a, b, c, d in Y:
    a -= 1
    b -= 1
    c -= 1
    d -= 1

    ans = X[c][d]
    if a > 0:
        ans -= X[a - 1][d]
    if b > 0:
        ans -= X[c][b - 1]
    if a > 0 and b > 0:
        ans += X[a - 1][b - 1]
    print(ans)
