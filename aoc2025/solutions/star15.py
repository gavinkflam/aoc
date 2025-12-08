"""Solution for 2025 star 15.

Problem page:
    https://adventofcode.com/2025/day/8

Solutions:
    1. Brute force + sorting
        - O(k * n^3 * log(n)) time, O(n) auxiliary space,
            where n = number of circuit boxes,
                  k = number of connections to try
    2. Union find + heap
        - O(k * log(n) + k + n) time, O(n) auxiliary space,
"""

from collections import defaultdict
import heapq

from aoclibs.hofs import compose, mapf, str_splitf
from aoclibs.union_find import UnionFind


TARGET_TRIALS = 1000


def dist_sq(x: list[int], y: list[int]) -> int:
    """Calculate the square of Ecuclidean distance of the two 3D points x and y."""
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2


def prepare_pairs_heap(boxes: list[list[int]]) -> list[tuple[int, int, int]]:
    """Prepare a heap of each pair prioritized by the distances."""
    n = len(boxes)
    pairs = [
        (dist_sq(boxes[i], boxes[j]), i, j)
        for i in range(n - 1)
        for j in range(i + 1, n)
    ]

    heapq.heapify(pairs)
    return pairs


def run(boxes: list[list[int]]) -> int:
    """Connect junction boxes, and muitply the sizes of the three largest circuits."""
    # Try to connect the k closest pairs of junction boxes
    n = len(boxes)
    uf = UnionFind(n)
    pairs = prepare_pairs_heap(boxes)

    for _ in range(TARGET_TRIALS):
        _, x, y = heapq.heappop(pairs)
        uf.union(x, y)

    # Find sizes of circuits
    circuits = defaultdict(int)

    for i in range(n):
        circuits[uf.find(i)] += 1

    # Find sizes of the three largest circuits
    sizes = [-v for v in circuits.values()]
    heapq.heapify(sizes)

    return -heapq.heappop(sizes) * -heapq.heappop(sizes) * -heapq.heappop(sizes)


PARSER = compose(mapf(str_splitf(",", int)), str.splitlines)
PRINTER = str
