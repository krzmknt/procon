from heapq import heappop, heappush

# Input
(n, _), *edges = [map(int, line.split()) for line in open(0)]
adj = [set() for _ in range(n + 1)]
for u, v, w in edges:
    adj[u].add((v, w))
    adj[v].add((u, w))

# Initialize
dmin_queue = [(0, 1)]
dist = [float("inf")] * (n + 1)
dist[1] = 0
done = set()

# Dijsktra
while dmin_queue:
    _, v = heappop(dmin_queue)
    if v in done:
        continue
    done.add(v)

    for u, w in adj[v]:
        if dist[v] + w < dist[u]:
            dist[u] = dist[v] + w
            heappush(dmin_queue, (dist[u], u))

# Output
for dist in dist[1:]:
    print(dist if dist < float("inf") else -1)
