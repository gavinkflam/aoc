"""Solution for 2024 star 3.

Problem page:
    https://adventofcode.com/2024/day/2

Solutions:
    1. Simple iteration - O(rows * cols) time, O(1) auxiliary space
"""

from aoclibs import inputs

def run(grid: list[list[int]]) -> int:
    """Check whether each report is safe."""
    rows = len(grid)
    safe_reports = rows

    for row in range(rows):
        cols = len(grid[row])
        direction = 1 if grid[row][1] > grid[row][0] else -1

        for col in range(1, cols):
            curr, prev = grid[row][col], grid[row][col - 1]
            if not 1 <= (curr - prev) * direction <= 3:
                safe_reports -= 1
                break

    return safe_reports

PARSER = inputs.parse_int_grid
PRINTER = str
