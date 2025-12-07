"""Solution for 2024 star 49.

Problem page:
    https://adventofcode.com/2024/day/25

Solutions:
    1. Brute force
        - O(mn) time, O(m + n) auxiliary space
            where m = number of locks,
                  n = number of keys
"""

from aoclibs import inputs2


Pins = list[int]


def parse_blocks(blocks: list[list[str]]) -> tuple[list[Pins], list[Pins]]:
    """Parse the blocks into locks and keys."""
    locks, keys = [], []
    columns = len(blocks[0][0])

    for block in blocks:
        pins = [[s[col] for s in block].count("#") - 1 for col in range(columns)]

        if block[0][0] == "#":
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


def run(blocks: list[list[str]]) -> int:
    """Find the number of lock and key pairs that fit together without overlaps."""
    locks, keys = parse_blocks(blocks)
    fits = 0

    for lock in locks:
        for key in keys:
            if not have_overlaps(lock, key):
                fits += 1

    return fits


PARSER = inputs2.compose(inputs2.list_split(""), str.splitlines)
PRINTER = str
