"""Solution for 2024 star 47.

Problem page:
    https://adventofcode.com/2024/day/24

Solutions:
    1. Brute force
        - O(n^2 + m) time, O(n + m) auxiliary space
            where n = number of gates,
                  m = number of wires
    2. Topological sort
        - O(n + m) time, O(n + m) auxiliary space
"""

from collections import defaultdict
from typing import NamedTuple

from aoclibs import inputs


Board = NamedTuple(
    "Board",
    [
        ("initial_values", dict[str, int]),
        ("logics", dict[str, str]),
        ("adj_list", dict[str, set[str]]),
        ("inputs_to", dict[str, list[str]]),
        ("in_degrees", dict[str, int]),
    ],
)


def and_gate(x: int, y: int) -> int:
    """Return 1 if both x and y are 1."""
    return 1 if x == y == 1 else 0


def or_gate(x: int, y: int) -> int:
    """Return 1 if x and y or 1."""
    return 1 if x == 1 or y == 1 else 0


def xor_gate(x: int, y: int) -> int:
    """Return 1 if x and y are different."""
    return 1 if x != y else 0


GATE_FUNCTIONS = {"AND": and_gate, "OR": or_gate, "XOR": xor_gate}


def parse_inputs(lines: list[str]) -> Board:
    """Parse inputs into initial value and configuration of wires."""
    initial_values, logics = {}, {}
    i = 0

    # Read initial values
    while lines[i]:
        line = lines[i]
        wire, value = line[:3], int(line[5])
        initial_values[wire] = value
        i += 1
    i += 1

    # Read logical gates
    adj_list, inputs_to = defaultdict(set), defaultdict(list)
    indegrees = defaultdict(int)

    while i < len(lines):
        input1, fn, input2, _, output = lines[i].split(" ")

        logics[output] = fn
        adj_list[input1].add(output)
        adj_list[input2].add(output)

        inputs_to[output].append(input1)
        inputs_to[output].append(input2)
        indegrees[output] += 2

        i += 1

    return Board(initial_values, logics, adj_list, inputs_to, indegrees)


def solve_values(board: Board) -> dict[str, int]:
    """Solve values of wires on the board."""
    values = board.initial_values.copy()
    queue = list(board.initial_values.keys())

    while queue:
        new_queue = []

        for wire in queue:
            # If the wire is an output of a logical gate, calculate its value
            if wire in board.logics:
                gate_fn = GATE_FUNCTIONS[board.logics[wire]]
                input1, input2 = board.inputs_to[wire]
                values[wire] = gate_fn(values[input1], values[input2])

            # Find downstream wires with all dependencies resolved
            removes = []

            for child in board.adj_list[wire]:
                board.in_degrees[child] -= 1
                removes.append(child)

                if board.in_degrees[child] == 0:
                    new_queue.append(child)

            for child in removes:
                board.adj_list[wire].remove(child)

        queue = new_queue

    return values


def construct_output_from_z_wires(values: dict[str, int]) -> int:
    """Construct the decimal number output from wires start with z."""
    output = 0
    next_wire = 0

    def wire_name(serial: int) -> str:
        return f"z{str(serial).rjust(2, "0")}"

    while wire_name(next_wire) in values:
        output ^= values[wire_name(next_wire)] << next_wire
        next_wire += 1

    return output


def run(lines: list[str]) -> int:
    """Find the decimal number represented by the wires starting with z."""
    board = parse_inputs(lines)
    values = solve_values(board)

    return construct_output_from_z_wires(values)


PARSER = inputs.parse_str_lines
PRINTER = str
