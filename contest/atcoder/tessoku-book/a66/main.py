class UnionFind:
    def __init__(self, n):
        """
        O(n)
        """
        self.parent = [-1] * (n + 1)
        self.size = [1] * (n + 1)

    def root(self, x) -> int:
        """
        O(n)
        Trace the parent of x until it reaches the root
        """
        while not self.parent[x] == -1:
            x = self.parent[x]
        return x

    def unite(self, u, v) -> None:
        """
        O(n) (Dominated by root())
        """
        root_u = self.root(u)
        root_v = self.root(v)

        # Do nothing if u and v are already in the same group
        if root_u == root_v:
            return

        # Merge smaller group into larger group
        if self.size[root_u] < self.size[root_v]:
            self.parent[root_u] = root_v
            self.size[root_v] = self.size[root_u] + self.size[root_v]
        else:
            self.parent[root_v] = root_u
            self.size[root_u] = self.size[root_u] + self.size[root_v]

    def same(self, u, v) -> bool:
        """
        O(n) (Dominated by root())
        """
        return self.root(u) == self.root(v)


(n, _), *q = [[*map(int, l.split())] for l in open(0)]

uf = UnionFind(n)
for mode, u, v in q:
    # mode.1: Add edge between u and v
    if mode == 1:
        uf.unite(u, v)
    # mode.2: Check if u and v are in the same group
    else:
        print(["No", "Yes"][uf.same(u, v)])
