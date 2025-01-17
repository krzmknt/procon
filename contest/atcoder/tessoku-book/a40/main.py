[N], A = [[*map(int, line.split())] for line in open(0)]

count = {}

for a in A:
    count[a] = count.get(a, 0) + 1

print(sum(n * (n - 1) * (n - 2) // 6 for n in count.values()))
