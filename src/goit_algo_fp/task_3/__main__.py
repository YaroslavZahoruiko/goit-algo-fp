from math import inf

from goit_algo_fp.task_3.graph import Graph
from goit_algo_fp.task_3.dijkstra import dijkstra, reconstruct_path


def main() -> None:
    """Demonstrate Dijkstra's algorithm on a sample graph."""
    graph = Graph()
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 1)
    graph.add_edge("C", "B", 2)
    graph.add_edge("C", "D", 5)
    graph.add_edge("B", "D", 1)

    start = "A"
    distances, previous = dijkstra(graph, start)

    print(f"Shortest distances from vertex {start}")
    for vertex in sorted(distances.keys()):
        dist = distances[vertex]
        if dist == inf:
            print(f"  Vertex {vertex}: unreachable")
        else:
            path = reconstruct_path(previous, start, vertex)
            print(f"  Vertex {vertex}: distance = {dist}, path = {path}")


if __name__ == "__main__":
    main()
