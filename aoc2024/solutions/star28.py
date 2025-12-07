"""Solution for 2024 star 28.

Problem page:
    https://adventofcode.com/2024/day/14#part2

Solutions:
    1. Simulation + DFS
        - O(kr * mn) time, O(mn) auxiliary space
            where k = number of seconds,
                  r = number of robots,
                  m = height,
                  n = width
"""

from aoc2024.solutions import star27


PRINT_PICTURE = False
WIDTH, HEIGHT = 101, 103
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def is_interesting(grid: list[list[int]], threshold: int) -> bool:
    """Determine is the grid interesting by the number of robots in the largest cluster."""
    visited = [[False] * WIDTH for _ in range(HEIGHT)]

    def fun_factor(row: int, col: int) -> int:
        fun = grid[row][col]

        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc

            if not (0 <= nr < HEIGHT and 0 <= nc < WIDTH and grid[nr][nc] > 0):
                continue
            if visited[nr][nc]:
                continue

            visited[nr][nc] = True
            fun += fun_factor(nr, nc)

        return fun

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if grid[row][col] == 0 or visited[row][col]:
                continue
            if fun_factor(row, col) >= threshold:
                return True

    return False


def run(robots: list[list[int]]) -> int:
    """Find the minimum number of seconds for the robots to arrange into a Christmas tree."""
    grid = [[0] * WIDTH for _ in range(HEIGHT)]
    positions = [[px, py] for px, py, _, _ in robots]

    for px, py in positions:
        grid[py][px] += 1

    for s in range(1, 100000):
        for i, (_, _, vx, vy) in enumerate(robots):
            px, py = positions[i]
            grid[py][px] -= 1

            px, py = (px + vx) % WIDTH, (py + vy) % HEIGHT
            grid[py][px] += 1
            positions[i][0], positions[i][1] = px, py

        if is_interesting(grid, 100):
            if PRINT_PICTURE:
                for line in grid:
                    print("".join(" " if c == 0 else str(c) for c in line))
            return s

    return -1


PARSER = star27.PARSER
PRINTER = str
