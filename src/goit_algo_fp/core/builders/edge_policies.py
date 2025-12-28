from abc import ABC, abstractmethod


class EdgePolicy(ABC):
    @abstractmethod
    def add_edge(self, G, u, v, data=None):
        pass


class DefaultPolicy(EdgePolicy):
    def add_edge(self, G, u, v, data=None):
        G.add_edge(u, v, **(data or {}))


class BidirectionalPolicy(EdgePolicy):
    def add_edge(self, G, u, v, data=None):
        G.add_edge(u, v, **(data or {}))
        G.add_edge(v, u, **(data or {}))
