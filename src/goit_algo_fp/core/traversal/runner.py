class TraversalRunner:
    def __init__(self, strategy, consumers):
        self.strategy = strategy
        self.consumers = consumers

    def run(self, root):
        for step in self.strategy.traverse(root):
            for consumer in self.consumers:
                consumer.on_step(step)
