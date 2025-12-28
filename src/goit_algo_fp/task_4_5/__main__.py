import heapq
import networkx as nx
from typing import Type

from goit_algo_fp.core.adapters.heap_to_tree import heap_to_tree
from goit_algo_fp.core.builders.graph_builder import GraphBuilder
from goit_algo_fp.core.builders.edge_policies import BidirectionalPolicy
from goit_algo_fp.core.consumers import (
    StepColorConsumer,
    LevelLayoutConsumer,
    GraphBuilderConsumer,
)
from goit_algo_fp.core.entities.node import Node
from goit_algo_fp.core.renderers.draw_graph import draw_graph
from goit_algo_fp.core.traversal import (
    BFSStrategy,
    DFSIterativeStrategy,
    TraversalRunner,
    TraversalStrategy,
)


def main() -> None:
    """Main function to demonstrate heap to tree conversion and traversal visualization."""
    heap = [0, 4, 5, 10, 1, 3, 7, 2, 6, 8, 9]
    heapq.heapify(heap)
    tree = heap_to_tree(heap)

    # Visualize BFS traversal
    visualize_traversal(BFSStrategy, tree)
    # Visualize DFS traversal
    visualize_traversal(DFSIterativeStrategy, tree)


def visualize_traversal(strategy_class: Type[TraversalStrategy], tree: Node) -> None:
    """
    Visualize tree traversal using the specified strategy.

    Args:
        strategy_class: The traversal strategy class to use (BFSStrategy or DFSIterativeStrategy)
        tree: The root node of the tree to traverse
    """
    graph_builder = GraphBuilder(nx.DiGraph, BidirectionalPolicy())
    layout_consumer = LevelLayoutConsumer()
    step_color_consumer = StepColorConsumer()
    graph_builder_consumer = GraphBuilderConsumer(graph_builder)
    runner = TraversalRunner(
        strategy_class(),
        [layout_consumer, step_color_consumer, graph_builder_consumer],
    )
    runner.run(tree)

    # Draw graph
    pos = layout_consumer.pos
    colors = step_color_consumer.colors
    graph = graph_builder.build()
    draw_graph(
        graph,
        title=f"{strategy_class.__name__} Traversal",
        data={"pos": pos, "node_color": colors},
    )


if __name__ == "__main__":
    main()
