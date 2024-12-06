"""Solution for 2024 star 12.

Problem page:
    https://adventofcode.com/2024/day/6#part2

Solutions:
    1. DFS + backtracking - O(mn * mn) time, O(mn) auxiliary space
"""

from aoclibs import inputs
from aoc2024.solutions import star11


TRIED = 1 << 4


def will_be_stuck(
    grid: list[list[str]], visited: list[list[int]], row: int, col: int, facing: int
) -> bool:
    """Run DFS and find out will the guard be stuck."""
    rows, cols = len(grid), len(grid[0])
    visited = [r.copy() for r in visited]

    while 0 <= row < rows and 0 <= col < cols:
        # Detected a loop
        if visited[row][col] & (1 << facing) != 0:
            return True
        visited[row][col] |= 1 << facing

        # Check the next cell for obstacles
        nr, nc = row + star11.FACINGS[facing][0], col + star11.FACINGS[facing][1]
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "#":
            facing = (facing + 1) % 4
        else:
            row, col = nr, nc

    return False


def run(grid: list[list[str]]) -> int:
    """Find out how many new obstacle positions can cause the guard to get stuck."""
    rows, cols = len(grid), len(grid[0])

    # Run DFS to try each valid locations to place an obstacle
    row, col = star11.find_guard_location(grid)
    facing, good_positions = 0, 0
    grid[row][col] = "*"
    visited = [[0] * cols for _ in range(rows)]

    while True:
        visited[row][col] |= 1 << facing

        # Check the next cell
        nr, nc = row + star11.FACINGS[facing][0], col + star11.FACINGS[facing][1]

        # Escaped
        if not (0 <= nr < rows and 0 <= nc < cols):
            return good_positions
        # Obstacle
        if grid[nr][nc] == "#":
            facing = (facing + 1) % 4
        # Valid location to place obstacle
        elif visited[nr][nc] & TRIED == 0 and grid[nr][nc] == ".":
            visited[nr][nc] |= TRIED
            grid[nr][nc] = "#"

            if will_be_stuck(grid, visited, row, col, (facing + 1) % 4):
                good_positions += 1
            grid[nr][nc] = "."
        else:
            row, col = nr, nc


PARSER = inputs.parse_char_grid
PRINTER = str
