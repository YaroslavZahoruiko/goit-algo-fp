class TraversalStep:
    def __init__(self, node, index, depth, parent=None):
        self.node = node  # what
        self.index = index  # when (order)
        self.depth = depth  # structural fact
        self.parent = parent  # structural relation
