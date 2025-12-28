from typing import List, Any, Optional
from goit_algo_fp.core.entities.node import Node


def heap_to_tree(heap: List[Any]) -> Optional[Node]:
    """
    Convert a heap (list representation) to a TreeNode structure.

    In heapq, a heap is stored as a list where:
    - Index 0 is the root
    - For node at index i: left child is 2*i+1, right child is 2*i+2

    Args:
        heap: List representation of a heap (as used by heapq module)

    Returns:
        Root TreeNode of the heap tree, or None if heap is empty
    """
    if not heap:
        return None

    # Create all nodes first
    nodes = []
    for i, value in enumerate(heap):
        nodes.append(Node(value))

    # Build tree structure by linking nodes
    for i in range(len(nodes)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < len(nodes):
            nodes[i].left = nodes[left_idx]
        if right_idx < len(nodes):
            nodes[i].right = nodes[right_idx]

    return nodes[0]
