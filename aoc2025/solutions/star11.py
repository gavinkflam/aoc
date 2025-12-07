"""Solution for 2025 star 11.

Problem page:
    https://adventofcode.com/2025/day/6

Solutions:
    1. Simple iteration
        - O(mn) time, O(1) auxiliary space,
            where m = number of formulas,
                  n = number of operands for each formula
"""

from dataclasses import dataclass
from functools import reduce

from aoclibs import patterns
from aoclibs.hofs import applyf, compose, mapf, re_splitf, split_but_n, zip_applyf


@dataclass
class Worksheet:
    """Data class to represent the parsed worksheet."""

    numbers: list[list[int]]
    operators: list[list[str]]


def apply_operator(operator: str, operands: list[int]) -> int:
    """Apply operator to operands."""
    if operator == "+":
        return reduce(lambda x, y: x + y, operands)
    if operator == "*":
        return reduce(lambda x, y: x * y, operands)

    raise ValueError(f"Unknown operator {operator}")


def run(worksheet: Worksheet) -> int:
    """Calculate the sum of worksheet formulas."""
    ans = 0
    operators = worksheet.operators[0]
    formulas, operands = len(worksheet.numbers[0]), len(worksheet.numbers)

    for f in range(formulas):
        operator = operators[f]
        ans += apply_operator(
            operator, (worksheet.numbers[o][f] for o in range(operands))
        )

    return ans


PARSER = compose(
    applyf(Worksheet),
    zip_applyf(
        mapf(re_splitf(patterns.WHITESPACES, int, remove_empty_elements=True)),
        mapf(re_splitf(patterns.WHITESPACES, remove_empty_elements=True)),
    ),
    split_but_n(1),
    str.splitlines,
)
PRINTER = str
