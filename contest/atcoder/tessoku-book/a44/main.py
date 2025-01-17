(N, Q), *X = [[*map(int, l.split())] for l in open(0)]

A = [*range(1, N + 1)]

reversed = False
for x in X:
    if len(x) == 1:
        reversed = not reversed
    elif len(x) == 2:
        if reversed:
            print(A[N - x[1]])
        else:
            print(A[x[1] - 1])
    else:
        if reversed:
            A[N - x[1]] = x[2]
        else:
            A[x[1] - 1] = x[2]
