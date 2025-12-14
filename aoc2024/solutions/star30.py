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
from aoc2024.solutions.star29 import (
    ARROW_DIRECTIONS,
    DIRECTIONS,
    LEFT,
    RIGHT,
    Coord,
    Grid,
)
from aoclibs.executions import SolutionModule


def expand_grid(grid: Grid) -> Grid:
    """Expand the given grid to be twice as wide."""
    cols = len(grid[0])
    expanded_grid = []

    for line in grid:
        expanded_line = []

        for col in range(cols):
            if line[col] == ".":
                expanded_line.extend([".", "."])
            elif line[col] == "#":
                expanded_line.extend(["#", "#"])
            elif line[col] == "O":
                expanded_line.extend(["[", "]"])
            elif line[col] == "@":
                expanded_line.extend(["@", "."])

        expanded_grid.append(expanded_line)

    return expanded_grid


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


def run(info: tuple[Grid, str]) -> int:
    """Find the coordinates of boxes after the robot finished moving."""
    grid, action_strs = info
    grid = expand_grid(grid)

    row, col = star29.find_robot(grid)
    actions = [ARROW_DIRECTIONS[arrow] for arrow in action_strs]

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


solution = SolutionModule(run=run)
solution.parser = star29.solution.parser
