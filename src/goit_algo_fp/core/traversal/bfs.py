# traversal/bfs.py
from collections import deque
from goit_algo_fp.core.traversal.strategy import TraversalStrategy
from goit_algo_fp.core.traversal.step import TraversalStep


class BFSStrategy(TraversalStrategy):
    def traverse(self, root):
        queue = deque([(root, 0, None)])  # node, depth, parent
        index = 0

        while queue:
            node, depth, parent = queue.popleft()

            step = TraversalStep(
                node=node,
                index=index,
                depth=depth,
                parent=parent,
            )
            yield step
            index += 1

            if node.left:
                queue.append((node.left, depth + 1, node))
            if node.right:
                queue.append((node.right, depth + 1, node))
