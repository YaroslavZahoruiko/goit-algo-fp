from goit_algo_fp.core.builders.graph_builder import GraphBuilder
from goit_algo_fp.core.entities.basel_node import BaseNode


def tree_to_graph(node: BaseNode, builder: GraphBuilder):
    """
    Adapter: Tree → Graph
    """

    def dfs(node):
        builder.add_node(node.id, label=node.val)

        for child in (node.left, node.right):
            if child:
                builder.add_node(child.id, label=child.val)
                builder.connect(node.id, child.id)
                dfs(child)

    dfs(node)
    return builder.build()
