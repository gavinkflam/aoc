"""Solution for 2025 star 7.

Problem page:
    https://adventofcode.com/2025/day/4

Solutions:
    1. Brute force
        - O(8mn) time, O(1) auxiliary space,
            where m = number of rows,
                  n = length of each row
"""

from aoclibs import inputs


DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def neighbors_of(grid: list[list[str]], r: int, c: int) -> list[tuple[int, int]]:
    """Return all the paper neighbors in the eight directions."""
    rows, cols = len(grid), len(grid[0])
    neighbors = []

    for dr, dc in DIRECTIONS:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
            neighbors.append((nr, nc))

    return neighbors


def run(grid: list[list[str]]) -> int:
    """Count number of paper rolls that the forklift can access."""
    accessible = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            if len(neighbors_of(grid, r, c)) < 4:
                accessible += 1

    return accessible


PARSER = inputs.parse_char_grid
PRINTER = str
