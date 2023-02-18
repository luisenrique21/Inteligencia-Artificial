import networkx as nx
import matplotlib.pyplot as plt


# https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.add_edge.html?highlight=add_edge#networkx.DiGraph.add_edge
# Note: The nodes u and v will be automatically added if they are not already in the graph.
def agregar_arista(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)

    # Si el grafo no es dirigido
    if not di:
        # Agrego otra arista en sentido contrario
        G.add_edge(v, u, weight=w)


if __name__ == '__main__':
    # Instantiate the DiGraph
    G = nx.DiGraph()

    # Add node/edge pairs
    agregar_arista(G, "A", "B", 1, False)
    agregar_arista(G, "A", "C", 2, False)
    agregar_arista(G, "A", "D", 3, False)
    agregar_arista(G, "B", "C", 4, False)
    agregar_arista(G, "C", "D", 5, False)

    # Draw the networks
    pos = nx.layout.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo con NetworkX")
    plt.show()
