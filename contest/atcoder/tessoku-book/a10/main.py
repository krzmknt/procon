[N], A, _, *X = [[*map(int, l.split())] for l in open(0)]

max_l_arr = [A[0]]
max_l = A[0]
for a in A:
    max_l = max(max_l, a)
    max_l_arr.append(max_l)

max_r_arr = [A[-1]]
max_r = A[-1]
for a in A[::-1]:
    max_r = max(max_r, a)
    max_r_arr.append(max_r)

for L, R in X:
    print(max(max_l_arr[L - 1], max_r_arr[N - R]))
