"""Solution for 2025 star 12.

Problem page:
    https://adventofcode.com/2025/day/6#part2

Solutions:
    1. Simple iteration
        - O(mn) time, O(1) auxiliary space,
            where m = number of lines,
                  n = max length of line
"""

from aoc2025.solutions import star11


def read_operator(worksheet: list[str], col: int) -> tuple[str, int]:
    """Read the next operator from col and seek to the column of the next operator."""
    cols = len(worksheet[0])
    operator = worksheet[-1][col]
    col += 1

    while col < cols and worksheet[-1][col] == " ":
        col += 1

    return (operator, col)


def read_operands(worksheet: list[str], left: int, right: int) -> list[int]:
    """Read the operands of the current formula from right-to-left and top-to-bottom."""
    rows = len(worksheet)
    operands = []

    for col in range(right, left - 1, -1):
        operand = 0

        for row in range(0, rows - 1):
            if worksheet[row][col] != " ":
                operand = operand * 10 + int(worksheet[row][col])

        operands.append(operand)

    return operands


def run(worksheet: list[str]) -> int:
    """Calculate the sum of worksheet formulas."""
    cols = len(worksheet[0])
    ans, col = 0, 0

    while col < cols:
        operator, next_col = read_operator(worksheet, col)
        right = next_col - (2 if next_col < cols else 1)
        operands = read_operands(worksheet, col, right)

        ans += star11.apply_operator(operator, operands)
        col = next_col

    return ans


PARSER = str.splitlines
PRINTER = str
