[n], A = [[*map(int, line.split())] for line in open(0)]

A_with_index = sorted(zip(range(n), A), key=lambda x: x[1])

compressed = [0]
prev = -1
for i in range(n):
    if A_with_index[i][1] == prev:
        compressed.append(compressed[-1])
    else:
        compressed.append(compressed[-1] + 1)
    prev = A_with_index[i][1]

C = sorted(zip(A_with_index, compressed[1:]))

print(*[c[1] for c in C])
