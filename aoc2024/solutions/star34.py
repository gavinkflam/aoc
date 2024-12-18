"""Solution for 2024 star 34.

Problem page:
    https://adventofcode.com/2024/day/17#part2

Solutions:
    1. Interpreter + brute force
        - O(kn) time, O(n) auxiliary space
            where k = minimum value for the program to output itself
    2. Todo
"""

from aoclibs import inputs


def run(_: list[list[int]]) -> int:
    """Find the lowest value of register A for the program to output itself."""
    return 0


PARSER = inputs.parse_int_grid_regexp
PRINTER = str
