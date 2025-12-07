"""Solution for 2024 star 25.

Problem page:
    https://adventofcode.com/2024/day/13

Solutions:
    1. Brute force
        - O(m * max(px, py)) time, O(1) auxiliary space
"""

from aoclibs import inputs2, patterns


def run(machines: list[list[list[int]]]) -> int:
    """Find the lowest costs to win all winnable prizes."""
    total_costs = 0

    for machine in machines:
        [ax, ay], [bx, by], [px, py] = machine
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


PARSER = inputs2.compose(
    inputs2.mapf(
        inputs2.mapf(inputs2.re_mapf(patterns.UNSIGNED_INT, int)),
    ),
    inputs2.list_split(""),
    str.splitlines,
)
PRINTER = str
