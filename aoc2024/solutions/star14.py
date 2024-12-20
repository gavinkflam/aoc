"""Solution for 2024 star 14.

Problem page:
    https://adventofcode.com/2024/day/7#part2

Solutions:
    1. Backtracking
        - worst: O(n * 2^m) time, best: O(nm) time, O(m) auxiliary space
            where m = maximum number of numbers in an equation
"""

from aoclibs import inputs


def is_concat(x: int, y: int) -> bool:
    """Determine if x is a concatenation of an integer and y."""
    return x > y and str(x).endswith(str(y))


def deconcat(x: int, suffix: int) -> int:
    """Remove suffix from x and return the prefix as an integer."""
    return int(str(x).removesuffix(str(suffix)))


def is_valid_equation(equation: list[int], curr: int, i: int) -> bool:
    """Determine if the equation is valid."""
    val = equation[i]

    if i == 1:
        return curr == val
    if curr % val == 0 and is_valid_equation(equation, curr // val, i - 1):
        return True
    if is_concat(curr, val) and is_valid_equation(equation, deconcat(curr, val), i - 1):
        return True
    return is_valid_equation(equation, curr - val, i - 1)


def run(grid: list[list[int]]) -> int:
    """Find the sum of the valid equations."""
    valid_equations_sum = 0

    for equation in grid:
        if is_valid_equation(equation, equation[0], len(equation) - 1):
            valid_equations_sum += equation[0]

    return valid_equations_sum


PARSER = inputs.parse_int_grid_regexp
PRINTER = str
