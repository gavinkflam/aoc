"""Solution for 2024 star 49.

Problem page:
    https://adventofcode.com/2024/day/25

Solutions:
    1. Brute force
        - O(mn) time, O(m + n) auxiliary space
            where m = number of locks,
                  n = number of keys
"""

from aoclibs import inputs


Pins = list[int]


def pin_height(lines: list[str], start_line: int, column: int) -> int:
    """Find the height of the required pin."""
    pounds = 0

    for i in range(7):
        if lines[start_line + i][column] == "#":
            pounds += 1

    return pounds - 1


def parse_inputs(lines: list[str]) -> tuple[list[Pins], list[Pins]]:
    """Parse the inputs into locks and keys."""
    locks, keys = [], []

    for i in range(0, len(lines), 8):
        pins = [pin_height(lines, i, column) for column in range(5)]

        if lines[i][0] == "#":
            locks.append(pins)
        else:
            keys.append(pins)

    return (locks, keys)


def have_overlaps(lock: Pins, key: Pins) -> bool:
    """Determine if the given lock and key have overlapping pins."""
    for pin in range(5):
        if lock[pin] + key[pin] > 5:
            return True

    return False


def run(lines: list[str]) -> int:
    """Find the number of lock and key pairs that fit together without overlaps."""
    locks, keys = parse_inputs(lines)
    fits = 0

    for lock in locks:
        for key in keys:
            if not have_overlaps(lock, key):
                fits += 1

    return fits


PARSER = inputs.parse_str_lines
PRINTER = str
