import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Create a simple graph
G = nx.Graph()
G.add_edges_from([("Person A", "Person B"), ("Person A", "Person C"), ("Person B", "Person D"), ("Person C", "Person D")])

# Assign a unique color to each node based on its identifier
node_colors = [mcolors.to_rgba(f"C{i}", alpha=0.8) for i, _ in enumerate(G.nodes)]

# Initialize plot
fig, ax = plt.subplots(figsize=(8, 8))
pos = nx.spring_layout(G)

# Draw nodes with unique colors
nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, font_size=10)

# Display Handshaking Theorem information
sum_of_degrees = sum(dict(G.degree()).values())
num_edges = G.number_of_edges()

# Annotate the graph with explanations
ax.text(0.5, -0.1, f"Step 1: Sum of Degrees = {sum_of_degrees}", ha="center", transform=ax.transAxes, fontsize=12)
ax.text(0.5, -0.15, f"Step 2: 2 * Number of Edges = {2 * num_edges}", ha="center", transform=ax.transAxes, fontsize=12)

# Annotate nodes with degrees
for node, degree in dict(G.degree()).items():
    ax.text(pos[node][0], pos[node][1] + 0.05, f"{node}\nDegree: {degree}", ha="center", fontsize=8)

plt.show()
