"""Solution for 2024 star 36.

Problem page:
    https://adventofcode.com/2024/day/18#part2

Solutions:
    1. Brute force, BFS
        - O(k * mn) time, O(mn) auxiliary space
            where k = number of bytes in the intput
"""

from aoc2024.solutions import star35
from aoclibs import inputs, outputs


def run(positions: list[list[int]]) -> list[int]:
    """Find the minumum number of bytes to cut off all roads to the exit."""
    k = len(positions)

    for limit in range(1024, k + 1):
        grid = star35.prepare_grid(positions, limit)
        steps = star35.steps_to_reach_exit(grid)

        if steps == -1:
            return positions[limit - 1]

    return [-1, -1]


PARSER = inputs.parse_int_grid_regexp
PRINTER = outputs.stringify_integer_list
