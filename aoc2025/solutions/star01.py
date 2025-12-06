"""Solution for 2025 star 1.

Problem page:
    https://adventofcode.com/2025/day/1

Solutions:
    1. Simulation
        - O(n) time, O(1) auxiliary space,
            where n = number of lines
"""

from aoclibs import inputs2


DIRECTIONS = {"L": -1, "R": 1}


def run(instructions: list[tuple[str, int]]) -> int:
    """Simulate dial turning and count number of times the dial points at zero."""
    dial, zeros = 50, 0

    for direction, movement in instructions:
        dial = (dial + DIRECTIONS[direction] * movement) % 100

        if dial == 0:
            zeros += 1

    return zeros


PARSER = inputs2.compose(
    inputs2.mapf(
        inputs2.compose(tuple, inputs2.zip_applyf(str, int), inputs2.split_take_n(1))
    ),
    str.splitlines,
)
PRINTER = str
