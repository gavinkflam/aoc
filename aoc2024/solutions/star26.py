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

from aoclibs.executions import SolutionModule
from aoc2024.solutions import star25


ADJUSTMENT = 10000000000000


def solve(formula: list[int]) -> Optional[tuple[int, int]]:
    """Return a solution if a and b are both positive integers."""
    ax, ay, bx, by, px, py = formula
    ratio = Fraction(-(bx * py - by * px), (ax * py - ay * px))
    b = Fraction(px, (ax * ratio + bx))
    a = b * ratio

    if not (a.is_integer() and b.is_integer() and a >= 0 and b >= 0):
        return None
    return (int(a), int(b))


def run(machines: list[list[list[int]]]) -> int:
    """Find the lowest costs to win all winnable prizes."""
    total_costs = 0

    for machine in machines:
        [ax, ay], [bx, by], [px, py] = machine
        maybe_solution = solve([ax, ay, bx, by, px + ADJUSTMENT, py + ADJUSTMENT])

        if maybe_solution:
            a, b = maybe_solution
            total_costs += 3 * a + b

    return total_costs


solution = SolutionModule(run=run)
solution.parser = star25.solution.parser
