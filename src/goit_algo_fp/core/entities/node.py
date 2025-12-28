from goit_algo_fp.core.entities.basel_node import BaseNode
from typing import Any


class Node(BaseNode):
    """Node of a binary tree with visualization support."""

    def __init__(self, val: Any, color: str = "skyblue"):
        """
        Initialize a tree node.

        Args:
            val: Value stored in the node
            color: Color for visualization (default: "skyblue")
        """
        super().__init__()
        self.val = val
        self.color = color
