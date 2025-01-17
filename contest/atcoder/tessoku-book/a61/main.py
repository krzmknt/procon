(N, M), *X = [[*map(int, line.split())] for line in open(0)]
adj = [set() for _ in range(N + 1)]
for u, v in X:
    adj[u].add(v)
    adj[v].add(u)

for index, adj_list in enumerate(adj):
    if index == 0:
        continue

    print(f"{index}: {{", end="")
    print(*sorted(adj_list), sep=", ", end="")
    print("}")
