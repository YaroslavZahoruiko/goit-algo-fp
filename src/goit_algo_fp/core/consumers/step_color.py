from goit_algo_fp.core.traversal.step import TraversalStep


class StepColorConsumer:
    def __init__(self, base_rgb=(18, 150, 240), step_size=12):
        self.colors = []
        self.base_rgb = base_rgb
        self.step_size = step_size

    def on_step(self, step: TraversalStep):
        r, g, b = self.base_rgb
        s = step.index

        r = min(255, r + s * self.step_size)
        g = min(255, g + s * self.step_size)
        b = min(255, b + s * self.step_size)

        self.colors.append(f"#{r:02X}{g:02X}{b:02X}")
