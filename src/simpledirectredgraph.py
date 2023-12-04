import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
G.add_edges_from(edges)

# Plot the directed graph
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', arrowsize=20)
plt.title("Directed Graph")
plt.show()

# Compute and print in-degrees and out-degrees
in_degrees = dict(G.in_degree())
out_degrees = dict(G.out_degree())

print("\nIn-Degrees:")
for node, in_degree in in_degrees.items():
    print(f"{node}: {in_degree}")

print("\nOut-Degrees:")
for node, out_degree in out_degrees.items():
    print(f"{node}: {out_degree}")
