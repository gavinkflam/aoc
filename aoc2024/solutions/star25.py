"""Solution for 2024 star 25.

Problem page:
    https://adventofcode.com/2024/day/13

Solutions:
    1. Brute force
        - O(m * max(px, py)) time, O(1) auxiliary space
"""

from aoclibs import inputs


def parse_data(grid: list[list[int]], adjustment: int = 0) -> list[list[int]]:
    """Parse the given input into specifications of each machine."""
    n = len(grid)
    machines = []

    for i in range(0, n, 4):
        machine = [grid[i][0], grid[i][1], grid[i + 1][0], grid[i + 1][1]]
        machine += [adjustment + grid[i + 2][0], adjustment + grid[i + 2][1]]
        machines.append(machine)

    return machines


def run(grid: list[list[int]]) -> int:
    """Find the lowest costs to win all winnable prizes."""
    machines = parse_data(grid)
    total_costs = 0

    for ax, ay, bx, by, px, py in machines:
        cost = 0

        while px > 0 and py > 0:
            if px % bx == 0 and py % by == 0 and px // bx == py // by:
                cost += px // bx
                px, py = 0, 0
            else:
                px, py = px - ax, py - ay
                cost += 3

        if px == 0 and py == 0:
            total_costs += cost

    return total_costs


PARSER = inputs.parse_int_grid_regexp
PRINTER = str
