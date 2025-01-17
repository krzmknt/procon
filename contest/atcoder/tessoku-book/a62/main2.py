import sys

sys.setrecursionlimit(10**7)

(N, M), *E = [[*map(int, l.split())] for l in open(0)]
adj = eval("set()," * (N + 1))
for u, v in E:
    adj[u].add(v)
    adj[v].add(u)


def is_connected(adj, s):
    """
    adj: adjucency list for the graph. (adj[0] is not used.)
    s : start point where dfs starts
    """
    ans = False
    visited = set()

    def dfs(u):
        visited.add(u)
        if len(visited) == len(adj) - 1:
            nonlocal ans
            ans = True
        for v in adj[u] - visited:
            dfs(v)

    dfs(s)
    return ans


ans = "" if is_connected(adj, s=1) else "not "
print(f"The graph is {ans}connected.")
