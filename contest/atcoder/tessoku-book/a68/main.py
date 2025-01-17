(n, m), *edges = [[*map(int, line.split())] for line in open(0)]

adj = [set() for _ in range(n+1)]
for u, v, w in edges:
    adj[u].add(v)
    adj[v].add(u)

cap = [[0] * (n + 1) for _ in range(n+1)]
for u, v, w in edges:
		cap[u][v] = w

# Ford-Fulkerson
def get_flow_dfs(v, t, F) -> int:
    if v == t: return F
    visited[v] = True

    for u in [u for u in adj[v] if not visited[u] and cap[v][u]]:
        if (flow := get_flow_dfs(u, t, min(F, cap[v][u]))) > 0 :
            # Hit: Valid path found
            cap[v][u] -= flow
            cap[u][v] += flow
            return flow

    # Miss: No valid path
    return 0

(ans, flow) = (0, -1)
while flow:
    visited = [False] * (n+1)
    ans += (flow := get_flow_dfs(1, n, float('inf')))

print(ans)
