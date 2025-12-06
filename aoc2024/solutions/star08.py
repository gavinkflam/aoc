"""Solution for 2024 star 8.

Problem page:
    https://adventofcode.com/2024/day/4#part2

Solutions:
    1. Simple iteration
        - O(mn) time, O(1) auxiliary space
"""

DIAGONAL_1 = [(-1, -1), (1, 1)]
DIAGONAL_2 = [(-1, 1), (1, -1)]
TARGETS = ["MS", "SM"]


def run(lines: list[str]) -> int:
    """Count the number of MASes in the shape of an X."""
    counts = 0
    rows, cols = len(lines), len(lines[0])

    def is_mas(diagonal: list[tuple[int]], row: int, col: int) -> bool:
        for target in TARGETS:
            matched = True

            for i, (dr, dc) in enumerate(diagonal):
                if lines[row + dr][col + dc] != target[i]:
                    matched = False
                    break
            if matched:
                return True

        return False

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if lines[row][col] != "A":
                continue

            if not is_mas(DIAGONAL_1, row, col):
                continue
            if not is_mas(DIAGONAL_2, row, col):
                continue

            counts += 1

    return counts


PARSER = str.splitlines
PRINTER = str
