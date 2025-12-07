"""Solution for 2024 star 11.

Problem page:
    https://adventofcode.com/2024/day/6

Solutions:
    1. DFS
        - O(mn) time, O(mn) auxiliary space
    2. DFS, in-place
        - O(mn) time, O(1) auxiliary space
"""

from aoclibs.hofs import compose, mapf


FACINGS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def find_guard_location(grid: list[list[str]]) -> tuple[int, int]:
    """Find the initial location of the guard."""
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "^":
                return (row, col)

    return None


def run(grid: list[list[str]]) -> int:
    """Run DFS to find how many distinct cells the guard visits."""
    rows, cols = len(grid), len(grid[0])

    # Run DFS
    row, col = find_guard_location(grid)
    facing, visited_cells = 0, 0
    grid[row][col] = "."

    while 0 <= row < rows and 0 <= col < cols:
        if grid[row][col] == ".":
            visited_cells += 1
            grid[row][col] = "X"

        # Check the next cell for obstacles
        nr, nc = row + FACINGS[facing][0], col + FACINGS[facing][1]
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "#":
            facing = (facing + 1) % 4
        else:
            row, col = nr, nc

    return visited_cells


PARSER = compose(mapf(list), str.splitlines)
PRINTER = str
