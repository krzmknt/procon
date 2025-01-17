from graphlib import TopologicalSorter

[N], A = [[*map(int, line.split())] for line in open(0)]

graph = {i: set() for i in range(1, N + 1)}
for u, parent in zip(range(2, N + 1), A):
    graph[parent].add(u)

ans = [0] * (N + 1)
for u in TopologicalSorter(graph).static_order():
    ans[u] = len(graph[u]) + sum(ans[child] for child in graph[u])
print(*ans[1:])
