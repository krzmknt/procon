(N, M, B), A, C = [[*map(int, l.split())] for l in open(0)]

ans = sum(A) * M + sum(C) * N + B * N * M
print(ans)
