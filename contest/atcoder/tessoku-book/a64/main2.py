import networkx as nx
from itertools import pairwise

G = nx.Graph()
G.add_weighted_edges_from([map(int, line.split()) for line in open(0)][1:])

shortest_paths = nx.shortest_path(G, source=1, weight="weight")
for u in sorted(G.nodes):
    # sp = nx.dijkstra_path(G, source=1, target=u)
    sp = shortest_paths[u]
    print(sum(G[v][u]["weight"] for v, u in pairwise(sp)))
