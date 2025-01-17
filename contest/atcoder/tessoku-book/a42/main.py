(_, K), *X = [[*map(int, l.split())] for l in open(0)]

print(
    max(
        sum(i <= a <= i + K and j <= b <= j + K for a, b in X)
        for i in range(100)
        for j in range(100)
    )
)
