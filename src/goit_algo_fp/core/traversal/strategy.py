from abc import ABC, abstractmethod


class TraversalStrategy(ABC):
    @abstractmethod
    def traverse(self, G, start):
        """Yield TraversalStep"""
