"""Solution for 2024 star 35.

Problem page:
    https://adventofcode.com/2024/day/18

Solutions:
    1. Brute force, backtracking
        - O(4^mn) time, O(mn) auxiliary space
    2. BFS
        - O(mn) time, O(mn) auxiliary space
"""

from aoclibs.executions import SolutionModule
from aoclibs.hofs import compose, mapf, str_splitf


SIZE = 71
SPACE, BYTE = 0, 1
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def prepare_grid(positions: list[list[int]], limit: int) -> list[list[int]]:
    """Prepare a grid with the given positions of bytes marked."""
    grid = [[SPACE] * SIZE for _ in range(SIZE)]

    for x, y in positions[:limit]:
        grid[y][x] = BYTE
    return grid


def steps_to_reach_exit(grid: list[list[int]]) -> int:
    """Find the minimum number of steps to reach the exit."""
    steps, queue = 0, [(0, 0)]
    visited = [[False] * SIZE for _ in range(SIZE)]
    visited[0][0] = True

    while queue:
        new_queue = []

        for x, y in queue:
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < SIZE and 0 <= ny < SIZE and grid[ny][nx] == SPACE):
                    continue
                if visited[ny][nx]:
                    continue
                if nx == ny == SIZE - 1:
                    return steps + 1

                visited[ny][nx] = True
                new_queue.append((nx, ny))

        queue = new_queue
        steps += 1

    return -1


def run(positions: list[list[int]]) -> int:
    """Find the minumum number of steps to reach the exit."""
    grid = prepare_grid(positions, limit=1024)
    return steps_to_reach_exit(grid)


solution = SolutionModule(run=run)
solution.parser = compose(mapf(str_splitf(",", int)), str.splitlines)
