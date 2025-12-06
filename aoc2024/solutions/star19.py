"""Solution for 2024 star 19.

Problem page:
    https://adventofcode.com/2024/day/10

Solutions:
    1. Brute force, BFS
        - O(mn * mn) time, O(mn) auxiliary space
"""

from aoclibs import inputs2


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def run(grid: list[list[int]]) -> int:
    """Sum the score of all trailheads."""
    rows, cols = len(grid), len(grid[0])
    trailhead_scores = 0

    def score_of(start_row: int, start_col: int) -> int:
        queue = [(start_row, start_col)]
        visited = [[False] * cols for _ in range(rows)]

        for step in range(9):
            new_queue = []

            for row, col in queue:
                for dr, dc in DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                    if grid[nr][nc] != step + 1 or visited[nr][nc]:
                        continue

                    visited[nr][nc] = True
                    new_queue.append((nr, nc))

            if not new_queue:
                return 0
            queue = new_queue

        return len(queue)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                trailhead_scores += score_of(row, col)

    return trailhead_scores


PARSER = inputs2.compose(
    inputs2.mapf(inputs2.mapf(int)),
    str.splitlines,
)
PRINTER = str
