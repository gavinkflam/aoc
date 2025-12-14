"""Solution for 2024 star 20.

Problem page:
    https://adventofcode.com/2024/day/10#part2

Solutions:
    1. Brute force, BFS
        - O(mn * mn) time, O(mn) auxiliary space
    2. DFS + memo
        - O(mn) time, O(mn) auxiliary space
"""

from aoc2024.solutions import star19
from aoclibs.executions import SolutionModule


def run(grid: list[list[int]]) -> int:
    """Sum the rating of all trailheads."""
    rows, cols = len(grid), len(grid[0])
    trailhead_ratings = 0
    ratings = [[-1] * cols for _ in range(rows)]

    def rating_of(row: int, col: int, step: int) -> int:
        if ratings[row][col] >= 0:
            return ratings[row][col]
        if grid[row][col] == 9:
            return 1

        ratings[row][col] = 0
        for dr, dc in star19.DIRECTIONS:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == step + 1:
                ratings[row][col] += rating_of(nr, nc, step + 1)

        return ratings[row][col]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                trailhead_ratings += rating_of(row, col, 0)

    return trailhead_ratings


solution = SolutionModule(run=run)
solution.parser = star19.solution.parser
