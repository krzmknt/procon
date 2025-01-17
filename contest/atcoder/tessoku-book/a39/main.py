[N], *X = [[*map(int, line.split())] for line in open(0)]

pos = 0
ans = 0

X = sorted(X)
X = sorted(X, key=lambda x: x[1])

for L, R in X:
    if pos <= L:
        pos = R
        ans += 1

print(ans)
