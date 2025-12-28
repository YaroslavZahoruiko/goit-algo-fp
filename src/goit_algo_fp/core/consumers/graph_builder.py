class GraphBuilderConsumer:
    def __init__(self, builder):
        self.builder = builder

    def on_step(self, step):
        node = step.node
        parent = step.parent

        self.builder.add_node(node.id)

        if parent:
            self.builder.connect(parent.id, node.id)
