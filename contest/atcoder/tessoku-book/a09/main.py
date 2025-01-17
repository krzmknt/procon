(H, W, N), *X = [[*map(int, l.split())] for l in open(0)]

Z = [[0] * W for _ in range(H)]

for A, B, C, D in X:
    Z[A - 1][B - 1] += 1

    if C < H:
        Z[C][B - 1] -= 1
    if D < W:
        Z[A - 1][D] -= 1
    if C < H and D < W:
        Z[C][D] += 1

for i in range(H):
    for j in range(1, W):
        Z[i][j] += Z[i][j - 1]

for j in range(W):
    for i in range(1, H):
        Z[i][j] += Z[i - 1][j]

for z in Z:
    print(*z)
