"""Solution for 2024 star 29.

Problem page:
    https://adventofcode.com/2024/day/15

Solutions:
    1. Simulation, DFS
        - O(mn + p * max(m, n)) time, O(mn) auxiliary space
            where m = height of map,
                  n = width of map,
                  p = number of actions
"""

from typing import Optional

from aoclibs import inputs2


LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3
ARROW_DIRECTIONS = {"<": LEFT, "^": UP, ">": RIGHT, "v": DOWN}
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


Grid = list[list[str]]
Coord = tuple[int, int]


def find_coordinate_sum(grid: Grid) -> int:
    """Calculate the sum of the coordinates of boxes."""
    rows, cols = len(grid), len(grid[0])
    coordinate_sum = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ["O", "["]:
                coordinate_sum += r * 100 + c

    return coordinate_sum


def find_robot(grid: Grid) -> Coord:
    """Find the coordinate of the robot."""
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "@":
                return (row, col)

    raise ValueError("Cannot find the coordinate of the robot.")


def find_space(grid: Grid, nr: int, nc: int, dr: int, dc: int) -> Optional[Coord]:
    """Find the next space in the given direction."""
    while grid[nr][nc] != "#":
        if grid[nr][nc] == ".":
            return (nr, nc)
        nr, nc = nr + dr, nc + dc

    return None


def run(info: tuple[Grid, str]) -> int:
    """Find the coordinates of boxes after the robot finished moving."""
    grid, action_strs = info
    row, col = find_robot(grid)
    actions = [ARROW_DIRECTIONS[arrow] for arrow in action_strs]

    # Simulation
    for action in actions:
        dr, dc = DIRECTIONS[action]
        nr, nc = row + dr, col + dc

        # Wall
        if grid[nr][nc] == "#":
            continue
        # Box
        if grid[nr][nc] == "O":
            # Find next space in front of the box(es)
            space = find_space(grid, nr, nc, dr, dc)
            if not space:
                continue

            sr, sc = space
            grid[sr][sc] = "O"

        # Move
        grid[nr][nc], grid[row][col] = "@", "."
        row, col = nr, nc

    return find_coordinate_sum(grid)


PARSER = inputs2.compose(
    tuple,
    inputs2.zip_applyf(
        inputs2.mapf(list),
        inputs2.str_joinf(),
    ),
    inputs2.list_split(""),
    str.splitlines,
)
PRINTER = str
