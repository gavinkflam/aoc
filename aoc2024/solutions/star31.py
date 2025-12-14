"""Solution for 2024 star 31.

Problem page:
    https://adventofcode.com/2024/day/16

Solutions:
    1. Brute force, backtracking
        - O(5^mn) time, O(mn) auxiliary space
    2. Dijkstra's algorithm
        - O(mn * logmn + mn) time, O(mn) auxiliary space
"""

import heapq
from typing import Optional

from aoclibs.executions import SolutionModule


EAST, SOUTH, WEST, NORTH = 0, 1, 2, 3
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_cell(maze: list[str], target: str) -> Optional[tuple[int, int]]:
    """Find the target cell in the maze."""
    rows, cols = len(maze), len(maze[0])

    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == target:
                return (row, col)

    return None


def find_best_path(maze: list[list[str]]) -> int:
    """Use Dijkstra's algorithm to find the best path to finish the maze."""
    rows, cols = len(maze), len(maze[0])
    sr, sc = find_cell(maze, target="S")

    # Dijkstra's algorithm
    heap = [(0, sr, sc, EAST)]
    visited = [[False] * cols for _ in range(rows)]
    visited[sr][sc] = True

    while heap:
        score, row, col, direction = heapq.heappop(heap)

        for new_dir, (dr, dc) in enumerate(DIRECTIONS):
            nr, nc = row + dr, col + dc
            if maze[nr][nc] == "#" or visited[nr][nc]:
                continue

            new_score = score + 1 + (1000 if new_dir != direction else 0)
            if maze[nr][nc] == "E":
                return new_score

            visited[nr][nc] = True
            heapq.heappush(heap, (new_score, nr, nc, new_dir))

    return -1


def run(maze: list[list[str]]) -> int:
    """Find the lowest possible score to complete the given maze."""
    return find_best_path(maze)


solution = SolutionModule(run=run)
solution.parser = str.splitlines
