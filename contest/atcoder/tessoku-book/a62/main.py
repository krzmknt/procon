(N, M), *EDGES = [[*map(int, line.split())] for line in open(0)]

adj = [[] for _ in range(N + 1)]
for u, v in EDGES:
    adj[u].append(v)
    adj[v].append(u)


def is_connected():
    visited = [True, True] + [False] * (N - 1)
    stack = [1]

    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    return all(visited)


if is_connected():
    print("The graph is connected.")
else:
    print("The graph is not connected.")
