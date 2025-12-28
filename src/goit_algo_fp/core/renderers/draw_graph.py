import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(
    G: nx.DiGraph, figsize: tuple = (8, 5), title: str = "", data: dict = {}
):
    plt.figure(figsize=figsize)
    plt.title(title)
    labels = data.pop("labels", nx.get_node_attributes(G, "label")) or {}
    pos = data.pop("pos", nx.get_node_attributes(G, "pos")) or {}
    node_size = data.pop("node_size", 2500)
    nx.draw(G, labels=labels, pos=pos, node_size=node_size, **data)
    plt.show()
