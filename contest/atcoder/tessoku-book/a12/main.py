from functools import cache

(_, K), A = [[*map(int, l.split())] for l in open(0)]
A = sorted(A)


@cache
def papers_at(time):
    return sum([time // num for num in A])


L, R = 0, 10**9
while L < R:
    M = (L + R) // 2

    if papers_at(M - 1) < K <= papers_at(M):
        print(M)
        break

    if K <= papers_at(M - 1):
        R = M
    else:
        L = M
