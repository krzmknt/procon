"""
utility.py
"""
import math


class Matrix:
    """
    Matrix
    """

    @classmethod
    def print(cls, matrix, description=""):
        """
        print the matrix
        """
        num_of_lows, num_of_cols = len(matrix), len(matrix[0])
        max_digit = max([len(str((e))) for e in sum(matrix, [])])
        cell_width = max_digit

        print("====================================")
        print(f"{description}({num_of_lows},{num_of_cols}):")
        print("------------------------------------")
        print(
            *[f'{"":>{cell_width}s}|']
            + [f"{col_num:>{cell_width}d}" for col_num in range(num_of_cols)]
        )
        print("-" * (cell_width + 1) * (num_of_cols + 1))
        for i, row in enumerate(matrix):
            print(*[f"{i:>{cell_width}d}|"] + [f"{v:>{cell_width}d}" for v in row])
        print("------------------------------------")

    @classmethod
    def transpose(cls, matrix):
        """
        transpose
        """
        num_of_rows = len(matrix[0])
        return [[row[j] for row in matrix] for j in range(num_of_rows)]

    @classmethod
    def remove_duplicate_rows(cls, matrix):
        """
        remove_duplicate_rows
        """
        return list(map(list, set(map(tuple, matrix))))


class Binary:
    """
    Binary
    """

    @classmethod
    def bitarr_to_int(cls, v):
        return int("".join(map(str, v)), 2)

    @classmethod
    def is_cover(cls, V, W):
        """
        Check if V covers W:
        v w |
        0 0 | True
        0 1 | False
        1 0 | True
        1 1 | True
        """
        if not len(V) == len(W):
            raise Exception("length not matched")
        for v, w in zip(V, W):
            if v == 0 and w == 1:
                return False
        return True


class Math:
    """
    Binary
    """

    @classmethod
    def is_prime(cls, num):
        if num < 2:
            return False
        elif num == 2:
            return True
        elif num % 2 == 0:
            return False

        sqrt_num = math.floor(math.sqrt(num))
        for i in range(3, sqrt_num + 1, 2):
            if num % i == 0:
                return False

        return True


class Adj:
    """
    Graph
    """

    def __init__(self, N):
        """
        N : Number of nodes
        """
        self.adj = eval("set()," * (N + 1))

    def add_edges_from(self, edges):
        for v, u in edges:
            self.adj[v].add(u)
            self.adj[u].add(v)

    def is_connected(self, adj, source, vervose=False):
        """
        adj    : adjucency list (adj[0] is filler)
        source : source node where dfs starts
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

    def shortest_path(source, target):
        pass
