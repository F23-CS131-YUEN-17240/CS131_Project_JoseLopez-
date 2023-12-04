import networkx as nx
import matplotlib.pyplot as plt

def create_edge_labels(G, tsp_path):
    edge_labels = {(edge[0], edge[1]): edge[2]['weight'] for edge in G.edges(data=True)}
    tsp_edge_labels = {(tsp_path[i], tsp_path[i + 1]): G[tsp_path[i]][tsp_path[i + 1]]['weight'] for i in range(len(tsp_path) - 1)}
    edge_labels.update(tsp_edge_labels)
    return edge_labels

# Create a weighted graph
G = nx.Graph()
edges = [('A', 'B', 3), ('A', 'C', 2), ('A', 'D', 1), ('B', 'C', 4), ('B', 'D', 2), ('C', 'D', 5)]
G.add_weighted_edges_from(edges)

# Solve the Traveling Salesman Problem
tsp_path = nx.approximation.traveling_salesman_problem(G, cycle=True)

# Define graph layout
pos = nx.spring_layout(G, seed=42)

# Plot the graph with annotations
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', edge_color='black', width=1.5)
nx.draw_networkx_edges(G, pos, edgelist=[(tsp_path[i], tsp_path[i + 1]) for i in range(len(tsp_path) - 1)],
                       edge_color='green', width=2, arrows=True, connectionstyle='arc3,rad=0.1')

edge_labels = create_edge_labels(G, tsp_path)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Display the optimal tour path
print("Optimal Tour Path:", tsp_path)

# Show the graph
plt.title("Traveling Salesman Problem - Weighted Graph")
plt.show()

