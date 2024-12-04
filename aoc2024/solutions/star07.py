"""Solution for 2024 star 7.

Problem page:
    https://adventofcode.com/2024/day/4

Solutions:
    1. Simple iteration - O(mn) time, O(1) auxiliary space
"""

from aoclibs import inputs


DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
TARGET = "XMAS"


def run(lines: list[str]) -> int:
    """Count the number of XMASes in every directions."""
    counts = 0
    rows, cols = len(lines), len(lines[0])

    def is_xmas(row: int, col: int, dr: int, dc: int) -> bool:
        end_row, end_col = row + dr * 3, col + dc * 3
        if not (0 <= end_row < rows and 0 <= end_col < cols):
            return False

        for i in range(1, 4):
            if lines[row + dr * i][col + dc * i] != TARGET[i]:
                return False

        return True

    for row in range(rows):
        for col in range(cols):
            if lines[row][col] != "X":
                continue

            for dr, dc in DIRECTIONS:
                if is_xmas(row, col, dr, dc):
                    counts += 1

    return counts


PARSER = inputs.parse_str_lines
PRINTER = str
