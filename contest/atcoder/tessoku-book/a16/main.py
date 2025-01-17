[n], A, B = [[*map(int, line.split())] for line in open(0)]

ans = [0, A[0]]

for i in range(2, n):
    ans.append(min(ans[-1] + A[i - 1], ans[-2] + B[i - 2]))

print(ans[-1])
