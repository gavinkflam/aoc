"""Solution for 2024 star 26.

Problem page:
    https://adventofcode.com/2024/day/13#part2

Solutions:
    1. Brute force
        - O(m * max(px, py)) time, O(1) auxiliary space
    2. Algebra
        - O(m) time, O(1) auxiliary space
"""

from fractions import Fraction
from typing import Optional

from aoc2024.solutions import star25
from aoclibs import inputs


ADJUSTMENT = 10000000000000


def solve(formula: tuple[int, int, int, int, int, int]) -> Optional[tuple[int, int]]:
    """Return a solution if a and b are both positive integers."""
    ax, ay, bx, by, px, py = formula

    ratio = Fraction(-(bx * py - by * px), (ax * py - ay * px))
    b = Fraction(px, (ax * ratio + bx))
    a = b * ratio

    if not (a.is_integer() and b.is_integer() and a >= 0 and b >= 0):
        return None
    return (int(a), int(b))


def run(grid: list[list[int]]) -> int:
    """Find the lowest costs to win all winnable prizes."""
    machines = star25.parse_data(grid, adjustment=ADJUSTMENT)
    total_costs = 0

    for machine in machines:
        solution = solve(machine)

        if solution:
            a, b = solution
            total_costs += 3 * a + b

    return total_costs


PARSER = inputs.parse_int_grid_regexp
PRINTER = str
