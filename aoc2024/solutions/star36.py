"""Solution for 2024 star 36.

Problem page:
    https://adventofcode.com/2024/day/18#part2

Solutions:
    1. Brute force, BFS
        - O(k * mn) time, O(mn) auxiliary space
            where k = number of bytes in the intput
    2. Union find
        - O(mn + k) time, O(mn) auxiliary space
"""

from aoc2024.solutions import star35
from aoc2024.solutions.star35 import BYTE, SIZE, SPACE
from aoclibs.hofs import str_join
from aoclibs.union_find import UnionFind


DIRECTIONS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def run(positions: list[list[int]]) -> list[int]:
    """Find the first byte to cut off all roads to the exit."""
    grid = [[SPACE] * SIZE for _ in range(SIZE)]
    uf = UnionFind(SIZE * SIZE + 2)
    south_west, north_east = SIZE * SIZE, SIZE * SIZE + 1

    def node_id(x: int, y: int) -> int:
        return y * SIZE + x

    # Use union find to check whether adding each byte would block all the roads
    for bx, by in positions:
        grid[by][bx] = BYTE

        # Connect neighboring bytes
        for dx, dy in DIRECTIONS:
            nx, ny = bx + dx, by + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE and grid[ny][nx] == BYTE:
                uf.union(node_id(bx, by), node_id(nx, ny))

        # If current byte is on a border, connect it to the corresponding virtual cell
        if bx == 0 or by == SIZE - 1:
            uf.union(south_west, node_id(bx, by))
        if bx == SIZE - 1 or by == 0:
            uf.union(north_east, node_id(bx, by))

        # Check have all the roads to the exit blocked
        if uf.find(south_west) == uf.find(north_east):
            return (bx, by)

    return [-1, -1]


PARSER = star35.PARSER
PRINTER = str_join(",")
