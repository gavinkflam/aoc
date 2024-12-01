"""Solution for 2024 star 2.

Problem page:
    https://adventofcode.com/2024/day/1#part2

Solutions:
    1. Brute force - O(n^2) time, O(1) auxiliary space
    2. Hash map - O(n) time, O(n) auxiliary space
"""

from collections import Counter

from aoc2024.aoclibs import inputs

def run(grid: list[list[int]]) -> int:
    """Sum the product of the values in the left column to its frequency in the right column."""
    cols = len(grid)

    right_freqs = Counter(grid[col][1] for col in range(cols))
    product_sum = sum(grid[col][0] * right_freqs[grid[col][0]] for col in range(cols))

    return product_sum

PARSER = inputs.parse_int_grid
PRINTER = str
