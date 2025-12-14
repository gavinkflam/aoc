"""Solution for 2025 star 13.

Problem page:
    https://adventofcode.com/2025/day/7

Solutions:
    1. Simple iteration
        - O(mn) time, O(mn) auxiliary space,
            where m = number of rows,
                  n = number of columns
"""

from aoclibs.executions import SolutionModule


def run(grid: list[str]) -> int:
    """Count the number of times the tachyon beam splits."""
    splits = 0
    rows, cols = len(grid), len(grid[0])
    occupied = [[grid[r][c] == "S" for c in range(cols)] for r in range(rows)]

    for r in range(1, rows):
        for c in range(cols):
            # Propagate downward through empty space
            if grid[r][c] == "." and occupied[r - 1][c]:
                occupied[r][c] = True
            # Split beam to the left and right
            elif grid[r][c] == "^" and occupied[r - 1][c]:
                if c - 1 >= 0 and grid[r][c - 1] == ".":
                    occupied[r][c - 1] = True
                if c + 1 < cols and grid[r][c + 1] == ".":
                    occupied[r][c + 1] = True

                splits += 1

    return splits


solution = SolutionModule(run=run)
solution.parser = str.splitlines
