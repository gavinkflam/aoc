"""Solution for 2025 star 14.

Problem page:
    https://adventofcode.com/2025/day/7#part2

Solutions:
    1. Brute force, backtracking
        - O(2^mn * mn) time, O(mn) auxiliary space,
            where m = number of rows,
                  n = number of columns
    2. DP
        - O(mn) time, O(mn) auxiliary space
"""


def run(grid: list[str]) -> int:
    """Count the number of timelines."""
    rows, cols = len(grid), len(grid[0])
    occupied = [
        [1 if grid[r][c] == "S" else 0 for c in range(cols)] for r in range(rows)
    ]

    for r in range(1, rows):
        for c in range(cols):
            # Propagate downward through empty space
            if grid[r][c] == "." and occupied[r - 1][c]:
                occupied[r][c] += occupied[r - 1][c]
            # Split beam to the left and right
            elif grid[r][c] == "^" and occupied[r - 1][c]:
                if c - 1 >= 0 and grid[r][c - 1] == ".":
                    occupied[r][c - 1] += occupied[r - 1][c]
                if c + 1 < cols and grid[r][c + 1] == ".":
                    occupied[r][c + 1] += occupied[r - 1][c]

    return sum(occupied[-1])


PARSER = str.splitlines
PRINTER = str
