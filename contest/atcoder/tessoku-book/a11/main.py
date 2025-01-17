import bisect

(n, x), *a = [[*map(int, open.split())] for open in open(0)]
A = a[0]

print(bisect.bisect_left(A, x) + 1)
