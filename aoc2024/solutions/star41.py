"""Solution for 2024 star 41.

Problem page:
    https://adventofcode.com/2024/day/21

Solutions:
    1. Simulation
        - O(nk) time, O(1) auxiliary space
            where k = maximum length of code
"""

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
ARROW_COORDS = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}
NUMPAD_LAYOUT = ["789", "456", "123", " 0A"]
ARROW_LAYOUT = [" ^A", "<v>"]


Keymap = dict[str, tuple[int, int]]
MoveFn = Callable[[str, str], list[str]]


def horizontal_sequence(magnitude: int) -> list[str]:
    """Generate a horizontal move sequence of the given magnitude."""
    if magnitude < 0:
        return ["<"] * -magnitude
    if magnitude > 0:
        return [">"] * magnitude
    return []


def vertical_sequence(magnitude: int) -> list[str]:
    """Generate a vertical move sequence of the given magnitude."""
    if magnitude < 0:
        return ["^"] * -magnitude
    if magnitude > 0:
        return ["v"] * magnitude
    return []


def numpad_move_sequence(start: str, end: str) -> list[str]:
    """Find the shortest input to move from start to end on the numpad."""
    sequence = []
    (sr, sc), (er, ec) = NUMPAD_COORDS[start], NUMPAD_COORDS[end]

    horizontal_first = (
        # Left first can save and not passing through gap
        (ec < sc and NUMPAD_LAYOUT[sr][ec] != " ")
        # Down first can save but passing through gap. Go horizontal first
        or (er > sr and NUMPAD_LAYOUT[er][sc] == " ")
    )

    if horizontal_first:
        sequence.extend(horizontal_sequence(ec - sc))
        sequence.extend(vertical_sequence(er - sr))
    else:
        sequence.extend(vertical_sequence(er - sr))
        sequence.extend(horizontal_sequence(ec - sc))

    return sequence


def arrow_keypad_move_sequence(start: str, end: str) -> list[str]:
    """Find the shortest input to move from start to end on the arrow keypad."""
    sequence = []
    (sr, sc), (er, ec) = ARROW_COORDS[start], ARROW_COORDS[end]

    if er > sr:
        sequence.extend(vertical_sequence(er - sr))
        sequence.extend(horizontal_sequence(ec - sc))
    else:
        sequence.extend(horizontal_sequence(ec - sc))
        sequence.extend(vertical_sequence(er - sr))

    return sequence


def type_sequence(sequence: list[str], move_fn: MoveFn) -> list[str]:
    """Find the shortest input to type the given sequence."""
    result = []
    prev = "A"

    for curr in sequence:
        result.extend(move_fn(prev, curr))
        result.append("A")
        prev = curr

    return result


def button_sequence(code: str) -> list[str]:
    """Find the final button sequence to input the given code."""
    sequence = type_sequence(list(code), numpad_move_sequence)
    sequence = type_sequence(sequence, arrow_keypad_move_sequence)
    sequence = type_sequence(sequence, arrow_keypad_move_sequence)
    return sequence


def run(codes: list[str]) -> int:
    """Find the sum of complexity to enter each of the code."""
    complexity_sum = 0

    for code in codes:
        numeric_part = int(code[:-1])
        sequence = button_sequence(code)
        complexity_sum += numeric_part * len(sequence)

    return complexity_sum


PARSER = inputs.parse_str_lines
PRINTER = str
