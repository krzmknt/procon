(N, K), A = [[*map(int, line.split())] for line in open(0)]

ans = 0
R = 0


def f(L, R):
    return A[R] - A[L] <= K


for L in range(N - 1):
    if L == R:
        R += 1

    while R < N and f(L, R):
        R += 1

    ans += R - L - 1

print(ans)
