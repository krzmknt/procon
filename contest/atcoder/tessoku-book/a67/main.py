class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * (n + 1)
        self.size = [1] * (n + 1)

    def root(self, x) -> int:
        while not self.parent[x] == -1:
            x = self.parent[x]
        return x

    def unite(self, u, v) -> None:
        root_u, root_v = self.root(u), self.root(v)
        if root_u == root_v:
            return
        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] = self.size[root_u] + self.size[root_v]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] = self.size[root_u] + self.size[root_v]

    def same(self, u, v) -> bool:
        return self.root(u) == self.root(v)


(N, M), *E = [[*map(int, line.split())] for line in open(0)]

E = sorted(E, key=lambda edge: edge[2])


def kruskal(n):
    tree_uf = UnionFind(n)
    tree_weight = 0
    for v, u, w in E:
        if not tree_uf.same(v, u):
            tree_uf.unite(v, u)
            tree_weight += w
    return tree_uf, tree_weight


mst_uf, mst_weight = kruskal(N)
print(mst_weight)
