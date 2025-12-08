"""Solution for 2025 star 16.

Problem page:
    https://adventofcode.com/2025/day/8

Solutions:
    1. Brute force + sorting
        - O(n^2 * n^3 * log(n)) time, O(n) auxiliary space,
            where n = number of circuit boxes,
                  k = number of connections to try
    2. Union find + heap
        - O(n^2 * log(n) + k + n) time, O(n) auxiliary space,
"""

import heapq

from aoc2025.solutions import star15
from aoclibs.union_find import UnionFind


def run(boxes: list[list[int]]) -> int:
    """Connect all junction boxes to one circuit."""
    n = len(boxes)
    pairs = star15.prepare_pairs_heap(boxes)

    uf, components = UnionFind(n), n
    last_x, last_y = -1, -1

    while components > 1:
        _, x, y = heapq.heappop(pairs)

        if uf.union(x, y):
            components -= 1
            last_x, last_y = x, y

    # Multiply the x coordinate of the last two junction boxes
    return boxes[last_x][0] * boxes[last_y][0]


PARSER = star15.PARSER
PRINTER = str
