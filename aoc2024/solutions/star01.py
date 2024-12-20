"""Solution for 2024 star 1.

Problem page:
    https://adventofcode.com/2024/day/1

Solutions:
    1. Brute force
        - O(n^2) time, O(1) auxiliary space
    2. Sorting
        - O(nlogn) time, O(n) auxiliary space
"""

from aoclibs import inputs


def run(grid: list[list[int]]) -> int:
    """Calculate the sum of absolute differences of value pairs."""
    cols = len(grid)

    left = [grid[col][0] for col in range(cols)]
    right = [grid[col][1] for col in range(cols)]
    left.sort()
    right.sort()

    diff_sum = sum(abs(left[c] - right[c]) for c in range(cols))
    return diff_sum


PARSER = inputs.parse_int_grid
PRINTER = str
