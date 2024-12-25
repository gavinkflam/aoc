"""Solution for 2024 star 48.

Problem page:
    https://adventofcode.com/2024/day/24#part2

Solutions:
    1. Iteration
        - O(n + m) time, O(n + m) auxiliary space
            where n = number of gates,
                  m = number of wires
"""

import re

from aoc2024.solutions import star47
from aoc2024.solutions.star47 import Board
from aoclibs import inputs, outputs


INPUT_BITS = 45
IO_WIRE_REGEXP = re.compile(r"^[xyz]\d\d$")


def is_io_wire(wire: str) -> bool:
    """Return true if the given wire is an I/O wire."""
    return IO_WIRE_REGEXP.match(wire) is not None


def find_role(board: Board, wire: str) -> str:
    """Find the role of the given wire."""
    input0, _ = board.inputs_to[wire]

    if board.logics[wire] == "XOR" and is_io_wire(input0):
        return "XOR0"
    if board.logics[wire] == "XOR":
        return "XOR1"
    if board.logics[wire] == "AND" and is_io_wire(input0):
        return "AND0"
    if board.logics[wire] == "AND":
        return "AND1"
    if board.logics[wire] == "OR":
        return "OR0"

    return "Unsupported"


def validate_xor0(board: Board, wire: str) -> list[str]:
    """Validate the given XOR0 connected wire and return any bad wires found."""
    # Assume bit 0 gates are correct
    if board.inputs_to[wire][0] in ["x00", "y00"]:
        return []

    # XOR0 connects to XOR1 and AND1
    if is_io_wire(wire):
        return [wire]

    xor0_outs = board.adj_list[wire]
    if sorted([board.logics[out] for out in xor0_outs]) != ["AND", "XOR"]:
        return [wire]

    return []


def validate_and0(board: Board, wire: str) -> list[str]:
    """Validate the given AND0 connected wire and return any bad wires found."""
    # Assume bit 0 gates are correct
    if board.inputs_to[wire][0] in ["x00", "y00"]:
        return []

    # AND0 connects to OR0
    if is_io_wire(wire):
        return [wire]

    and0_outs = board.adj_list[wire]
    if sorted([board.logics[out] for out in and0_outs]) != ["OR"]:
        return [wire]

    return []


def validate_xor1(_: Board, wire: str) -> list[str]:
    """Validate the given XOR1 connected wire and return any bad wires found."""
    # XOR1 connects to a z-wire
    if not is_io_wire(wire):
        return [wire]
    return []


def validate_and1(_: Board, wire: str) -> list[str]:
    """Validate the given AND1 connected wire and return any bad wires found."""
    # AND1 connects to OR0
    if is_io_wire(wire):
        return [wire]
    return []


def validate_or0(board: Board, wire: str) -> list[str]:
    """Validate the given OR0 connected wire and return any bad wires found."""
    bad_wires = set()

    for or0_in in board.inputs_to[wire]:
        # OR0 inputs come from AND0 and AND1
        if board.logics[or0_in] != "AND":
            bad_wires.add(or0_in)

    return list(bad_wires)


VALIDATORS = {
    "XOR0": validate_xor0,
    "XOR1": validate_xor1,
    "AND0": validate_and0,
    "AND1": validate_and1,
    "OR0": validate_or0,
}


def find_bad_wires(board: Board) -> list[str]:
    """Find bad output wires on the board."""
    bad_wires = set()

    # Validate z-wire connections
    for bit in range(1, INPUT_BITS):
        z_wire = f"z{str(bit).rjust(2, "0")}"
        if board.logics[z_wire] != "XOR":
            bad_wires.add(z_wire)

    # Validate gate outputs by role
    for wire in board.inputs_to:
        role = find_role(board, wire)
        for wire in VALIDATORS[role](board, wire):
            bad_wires.add(wire)

    return list(bad_wires)


def run(lines: list[str]) -> list[str]:
    """Find the gates that have their outputs swapped."""
    board = star47.parse_inputs(lines)
    bad_wires = find_bad_wires(board)

    return sorted(bad_wires)


PARSER = inputs.parse_str_lines
PRINTER = outputs.stringify_list
