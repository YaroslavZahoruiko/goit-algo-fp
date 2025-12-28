import heapq
from math import inf
from typing import Dict, Tuple, Any, Optional, List

from goit_algo_fp.task_3.graph import Graph


def dijkstra(graph: Graph, start: Any) -> Tuple[Dict[Any, float], Dict[Any, Optional[Any]]]:
    """
    Dijkstra's algorithm using binary heap.

    Args:
        graph: Graph object with edges attribute
        start: Starting vertex

    Returns:
        A tuple containing:
        - dist: Dictionary mapping vertex -> shortest distance
        - prev: Dictionary mapping vertex -> previous vertex (for path reconstruction)
    """
    graph_dict = graph.edges

    # Collect all vertices (both sources and destinations)
    all_vertices = set(graph_dict.keys())
    for neighbors in graph_dict.values():
        for v, _ in neighbors:
            all_vertices.add(v)

    dist = {v: inf for v in all_vertices}
    prev = {v: None for v in all_vertices}
    dist[start] = 0.0

    # (distance, vertex)
    heap = [(0.0, start)]

    while heap:
        d, u = heapq.heappop(heap)

        # Lazy deletion: skip if this is an outdated entry
        if d != dist[u]:
            continue

        for v, w in graph_dict.get(u, []):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))

    return dist, prev


def reconstruct_path(
    prev: Dict[Any, Optional[Any]], start: Any, target: Any
) -> Optional[List[Any]]:
    """
    Reconstruct the shortest path from start to target.

    Args:
        prev: Dictionary mapping vertex -> previous vertex (from dijkstra)
        start: Starting vertex
        target: Target vertex

    Returns:
        List of vertices representing the path, or None if target is unreachable
    """
    if target == start:
        return [start]
    
    # Check if target was reached during Dijkstra's algorithm
    if target not in prev or prev[target] is None:
        return None
    
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path
