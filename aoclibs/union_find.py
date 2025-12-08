"""Union-find algorighm, aka disjoint set union."""


class UnionFind:
    """Union-find algorithm with path compression and union by rank."""

    def __init__(self, size):
        self.size = size
        self.leaders = list(range(size))
        self.ranks = [0] * size

    def find(self, x: int) -> int:
        """Find the leader of the node x.
        Perform path compression at the same time to optimize performance."""
        if self.leaders[x] != self.leaders[self.leaders[x]]:
            self.leaders[x] = self.find(self.leaders[x])
        return self.leaders[x]

    def union(self, x: int, y: int) -> bool:
        """Union node x and y by their ranks."""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        if self.ranks[px] == self.ranks[py]:
            self.ranks[px] += 1

        if self.ranks[px] > self.ranks[py]:
            self.leaders[py] = px
        else:
            self.leaders[px] = py
        return True
