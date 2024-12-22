"""Solution for 2024 star 41.

Problem page:
    https://adventofcode.com/2024/day/21

Solutions:
    1. Simulation
        - O(nk) time, O(k) auxiliary space
            where n = number of codes,
                  k = maximum length of code
"""

from functools import partial
from typing import Callable

from aoclibs import inputs


NUMPAD_COORDS = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}
DPAD_COORDS = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}
NUMPAD_LAYOUT = ["789", "456", "123", " 0A"]
DPAD_LAYOUT = [" ^A", "<v>"]


KeyCoords = dict[str, tuple[int, int]]
Layout = list[str]
InputFn = Callable[[str, str], list[str]]


def horizontal_sequence(magnitude: int) -> list[str]:
    """Generate a horizontal move sequence of the given magnitude."""
    if magnitude < 0:
        return ["<"] * -magnitude
    return [">"] * magnitude


def vertical_sequence(magnitude: int) -> list[str]:
    """Generate a vertical move sequence of the given magnitude."""
    if magnitude < 0:
        return ["^"] * -magnitude
    return ["v"] * magnitude


def input_sequence(
    coords: KeyCoords, layout: Layout, start: str, end: str
) -> list[str]:
    """Find the shortest input sequence to move to the end key and press it."""
    sequence = []
    (sr, sc), (er, ec) = coords[start], coords[end]

    if (
        # Prioritize moving left first
        (ec < sc and layout[sr][ec] != " ")
        # Moving vertically first would go out of boundary
        or (layout[er][0] == " " and sc == 0)
    ):
        sequence.extend(horizontal_sequence(ec - sc))
        sequence.extend(vertical_sequence(er - sr))
    else:
        sequence.extend(vertical_sequence(er - sr))
        sequence.extend(horizontal_sequence(ec - sc))

    sequence.append("A")
    return sequence


numpad_to_dpad = partial(input_sequence, NUMPAD_COORDS, NUMPAD_LAYOUT)
dpad_to_dpad = partial(input_sequence, DPAD_COORDS, DPAD_LAYOUT)


def wrap_sequence(sequence: list[str], input_fn: InputFn) -> list[str]:
    """Find the input sequence for the next level of keypad."""
    result, prev = [], "A"

    for curr in sequence:
        result.extend(input_fn(prev, curr))
        prev = curr

    return result


def run(codes: list[str]) -> int:
    """Find the sum of complexity to enter each of the code."""
    complexity_sum = 0

    for code in codes:
        numeric_part = int(code[:-1])
        sequence = wrap_sequence(list(code), numpad_to_dpad)
        sequence = wrap_sequence(sequence, dpad_to_dpad)
        sequence = wrap_sequence(sequence, dpad_to_dpad)
        complexity_sum += numeric_part * len(sequence)

    return complexity_sum


PARSER = inputs.parse_str_lines
PRINTER = str
