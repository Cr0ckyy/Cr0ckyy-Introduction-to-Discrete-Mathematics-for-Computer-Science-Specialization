import networkx as nx
import matplotlib.pyplot as plt

# Number of nodes with respective degrees
nodes_degree_6 = 4
nodes_degree_3 = 5
nodes_degree_7 = 3

# Define the degree sequence based on the given information
degrees = [6] * nodes_degree_6 + [3] * nodes_degree_3 + [7] * nodes_degree_7

# Create a graph with the desired degrees
G = nx.random_degree_sequence_graph(degrees)

# Check if the degree sequence is valid and graphical
if nx.is_graphical(degrees):
    # Draw the graph
    nx.draw(G, with_labels=True)
    plt.show()  # This line will show the graph as an image
else:
    print("The given degree sequence is not graphical.")

# Calculating the total degree using the degree sum formula
total_degree = sum(degrees)

# Number of edges is half of the total degree as each edge contributes to two degrees in an undirected graph
number_of_edges = total_degree // 2

# Print the result
print("The number of edges in the graph is:", number_of_edges)
