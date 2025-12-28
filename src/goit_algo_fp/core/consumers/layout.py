from goit_algo_fp.core.traversal.step import TraversalStep


class LevelLayoutConsumer:
    def __init__(self):
        self.pos = {}
        self._x_by_node = {}

    def on_step(self, step: TraversalStep):
        node = step.node
        parent = step.parent

        if parent is None:
            x = 0.0  # root
        else:
            parent_x = self._x_by_node[parent]
            offset = 1 / (2**step.depth)

            if node is parent.left:
                x = parent_x - offset
            elif node is parent.right:
                x = parent_x + offset
            else:
                raise ValueError("Node is not a child of its parent")

        self._x_by_node[node] = x
        self.pos[node.id] = (x, -step.depth)


# class LayoutConsumer:
#     def __init__(self):
#         self.pos = {}

#     def on_step(self, step):
#         shade = min(255, 30 + step.index * 15)
#         self.colors[step.node] = f"#{shade:02X}{shade:02X}FF"
#     def compute(self, root: BaseNode) -> dict:
#         pos = {}
#         q = deque([(root, 0, 0)])

#         while q:
#             node, x, y = q.popleft()
#             pos[node.id] = (x, -y)
#             next_y = y + 1
#             if node.left:
#                 next_x = x - 1 / 2 ** next_y
#                 q.append((node.left, next_x, next_y))
#             if node.right:
#                 next_x = x + 1 / 2 ** next_y
#                 q.append((node.right, next_x, next_y))

#         return pos
