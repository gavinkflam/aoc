"""Solution for 2025 star 17.

Problem page:
    https://adventofcode.com/2025/day/9

Solutions:
    1. Brute force
        - O(n^2) time, O(1) auxiliary space,
            where n = number of red tiles
"""

from aoclibs.hofs import compose, mapf, str_splitf


def run(tiles: list[list[int]]) -> int:
    """Find the largest rectangle using two red tiles as the opposite corners."""
    n = len(tiles)
    max_area = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            height = abs(tiles[i][0] - tiles[j][0]) + 1
            width = abs(tiles[i][1] - tiles[j][1]) + 1

            if (area := height * width) > max_area:
                max_area = area

    return max_area


PARSER = compose(mapf(str_splitf(",", int)), str.splitlines)
PRINTER = str
