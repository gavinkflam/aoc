"""Solution for 2025 star 8.

Problem page:
    https://adventofcode.com/2025/day/4#part2

Solutions:
    1. Brute force
        - O(mn * mn) time, O(mn) auxiliary space,
            where m = number of rows,
                  n = length of each row
    2. BFS
        - O(mn) time, O(mn) auxiliary space
"""

from aoc2025.solutions import star07


def run(grid: list[list[str]]) -> int:
    """Count the number of paper rolls that the forklift can remove."""
    removed = 0
    rows, cols = len(grid), len(grid[0])

    # Initialize queue
    neighbors = [[0] * cols for _ in range(rows)]
    queue = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue

            neighbors[r][c] = len(star07.neighbors_of(grid, r, c))
            if neighbors[r][c] < 4:
                queue.append((r, c))

    # Simulate paper removal using BFS
    while queue:
        new_queue = []

        for r, c in queue:
            grid[r][c] = "."
            removed += 1

            for nr, nc in star07.neighbors_of(grid, r, c):
                neighbors[nr][nc] -= 1
                if neighbors[nr][nc] == 3:
                    new_queue.append((nr, nc))

        queue = new_queue

    return removed


PARSER = star07.PARSER
PRINTER = str
