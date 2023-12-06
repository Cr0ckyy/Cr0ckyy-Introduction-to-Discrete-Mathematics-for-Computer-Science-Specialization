import networkx as nx

def find_largest_clique(graph):
  cliques = nx.find_cliques(graph)
  largest_clique = max(cliques, key=len)
  return largest_clique

C2 = nx.cycle_graph(4)

largest_clique = find_largest_clique(C2)

print(len(largest_clique))
