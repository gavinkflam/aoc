"""Solution for 2024 star 30.

Problem page:
    https://adventofcode.com/2024/day/15#part2

Solutions:
    1. Simulation, DFS + recursion
        - O(mn + pmn) time, O(mn) auxiliary space
            where m = height of map,
                  n = width of map,
                  p = number of actions
"""

from aoc2024.solutions import star29
from aoc2024.solutions.star29 import DIRECTIONS, LEFT, RIGHT, Coord, Grid
from aoclibs import inputs


def parse_input(lines: list[list[str]]) -> tuple[Grid, Coord, list[str]]:
    """Parse input into grid and actions."""
    grid, actions, robot = [], [], None
    n, cols, i = len(lines), len(lines[0]), 0

    # Construct grid
    while len(lines[i]) > 0:
        line = []

        for col in range(cols):
            if lines[i][col] == ".":
                line.extend([".", "."])
            elif lines[i][col] == "#":
                line.extend(["#", "#"])
            elif lines[i][col] == "O":
                line.extend(["[", "]"])
            elif lines[i][col] == "@":
                robot = (i, col * 2)
                line.extend(["@", "."])

        grid.append(line)
        i += 1
    i += 1

    # Construct actions
    while i < n:
        actions.extend(star29.ARROW_DIRECTIONS[arrow] for arrow in lines[i])
        i += 1

    return (grid, robot, actions)


def push_horizontally(
    grid: Grid, position: Coord, direction: Coord, dry_run: bool = False
) -> bool:
    """Push boxes horizontally."""
    (dr, dc), (pr, pc) = direction, position

    # Find ending space and determine ability to push
    space = star29.find_space(grid, pr, pc, dr, dc)
    if not space:
        return False
    if dry_run:
        return True

    # Push for real
    row, col = space
    while row != pr or col != pc:
        grid[row][col] = grid[row - dr][col - dc]
        row, col = row - dr, col - dc

    return True


def push_vertically(
    grid: Grid,
    position: Coord,
    direction: Coord,
    dry_run: bool = False,
    checked_sideway: bool = False,
) -> bool:
    """Push boxes vertically."""
    (pr, pc) = position

    # Base cases
    if grid[pr][pc] == "#":
        return False
    if grid[pr][pc] == ".":
        return True

    # Recursively check the entire box and any boxes in front of it
    (dr, dc) = direction
    nr, nc = pr + dr, pc + dc

    can_push = push_vertically(grid, (nr, nc), direction, dry_run)
    if can_push and not checked_sideway:
        hc = pc + 1 if grid[pr][pc] == "[" else pc - 1
        can_push = push_vertically(
            grid, (pr, hc), direction, dry_run, checked_sideway=True
        )

    if not can_push:
        return False
    if dry_run:
        return True

    # Push for real
    grid[nr][nc] = grid[pr][pc]
    grid[pr][pc] = "."
    return True


def run(lines: Grid) -> int:
    """Find the coordinates of boxes after the robot finished moving."""
    grid, (row, col), actions = parse_input(lines)

    for action in actions:
        dr, dc = DIRECTIONS[action]
        nr, nc = row + dr, col + dc

        # Wall
        if grid[nr][nc] == "#":
            continue
        # Box
        if grid[nr][nc] in ["[", "]"]:
            push = push_horizontally if action in [LEFT, RIGHT] else push_vertically
            if not push(grid, (nr, nc), (dr, dc), dry_run=True):
                continue

            push(grid, (nr, nc), (dr, dc))

        # Move
        grid[nr][nc], grid[row][col] = "@", "."
        row, col = nr, nc

    return star29.find_coordinate_sum(grid)


PARSER = inputs.parse_char_grid
PRINTER = str
