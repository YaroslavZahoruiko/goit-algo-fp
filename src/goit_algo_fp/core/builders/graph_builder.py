from goit_algo_fp.core.builders.edge_policies import EdgePolicy


class GraphBuilder:
    def __init__(self, graph_factory, edge_policy: EdgePolicy):
        self.G = graph_factory()
        self.edge_policy = edge_policy

    def add_node(self, node, **attrs):
        self.G.add_node(node, **attrs)

    def connect(self, u, v, data=None):
        self.edge_policy.add_edge(self.G, u, v, data)

    def build(self):
        return self.G


# def _build_graph(
#     node: BaseNode,
# ) -> nx.DiGraph:
#     graph = nx.DiGraph()
#     graph.add_node(node.id, color="skyblue", label=node.val)
#     if node.left is not None:
#         graph.add_edge(node.id, node.left.id)
#         _build_graph(node.left)
#     if node.right is not None:
#         graph.add_edge(node.id, node.right.id)
#         _build_graph(node.right)
#     return graph
