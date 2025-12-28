from typing import Dict, List, Tuple, Any


class Graph:
    def __init__(self) -> None:
        """
        Initialize an empty graph.

        The edges dictionary maps vertices to lists of (neighbor, weight) tuples.
        """
        self.edges: Dict[Any, List[Tuple[Any, float]]] = {}

    def add_edge(self, u: Any, v: Any, weight: float) -> None:
        """
        Add a directed edge from vertex u to vertex v with the given weight.

        Args:
            u: Source vertex
            v: Target vertex
            weight: Edge weight (must be non-negative for Dijkstra's algorithm)
        """
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, weight))
