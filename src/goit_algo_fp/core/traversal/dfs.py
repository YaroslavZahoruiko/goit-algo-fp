# traversal/dfs_iterative.py
from .strategy import TraversalStrategy
from .step import TraversalStep


class DFSIterativeStrategy(TraversalStrategy):
    def traverse(self, root):
        if root is None:
            return

        stack = [(root, 0, None)]  # (node, depth, parent)
        index = 0

        while stack:
            node, depth, parent = stack.pop()

            # emit traversal step
            yield TraversalStep(node=node, index=index, depth=depth, parent=parent)
            index += 1

            # IMPORTANT:
            # push right first so left is processed first
            if node.right:
                stack.append((node.right, depth + 1, node))
            if node.left:
                stack.append((node.left, depth + 1, node))
