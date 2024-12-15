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

from aoclibs import inputs


LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3
ARROW_DIRECTIONS = {"<": LEFT, "^": UP, ">": RIGHT, "v": DOWN}
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


Grid = list[list[str]]
Coord = tuple[int, int]


def parse_input(lines: Grid) -> tuple[Grid, Coord, list[str]]:
    """Parse input into grid and actions."""
    grid, actions, robot = [], [], None
    n, i = len(lines), 0

    # Construct grid
    while len(lines[i]) > 0:
        try:
            robot = (i, lines[i].index("@"))
        except ValueError:
            pass

        grid.append(lines[i])
        i += 1
    i += 1

    # Construct actions
    while i < n:
        actions.extend(ARROW_DIRECTIONS[arrow] for arrow in lines[i])
        i += 1

    return (grid, robot, actions)


def find_coordinate_sum(grid: Grid) -> int:
    """Calculate the sum of the coordinates of boxes."""
    rows, cols = len(grid), len(grid[0])
    coordinate_sum = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ["O", "["]:
                coordinate_sum += r * 100 + c

    return coordinate_sum


def find_space(grid: Grid, nr: int, nc: int, dr: int, dc: int) -> Optional[Coord]:
    """Find the next space in the given direction."""
    while grid[nr][nc] != "#":
        if grid[nr][nc] == ".":
            return (nr, nc)
        nr, nc = nr + dr, nc + dc

    return None


def run(lines: Grid) -> int:
    """Find the coordinates of boxes after the robot finished moving."""
    grid, (row, col), actions = parse_input(lines)

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


PARSER = inputs.parse_char_grid
PRINTER = str
