from collections import deque

(N, M), *E = [[*map(int, l.split())] for l in open(0)]


def dnf(N, E):
    adj = eval("set()," * (N + 1))
    for u, v in E:
        adj[u].add(v)
        adj[v].add(u)

    dist = [0, 0] + [-1] * (N - 1)

    queue = deque([1])
    visited = {1}
    while queue:
        u = queue.pop()
        for v in adj[u] - visited:
            dist[v] = dist[u] + 1
            queue.appendleft(v)
            visited.add(v)

    return dist


dist = dnf(N, E)
print(*dist[1:], sep="\n")
