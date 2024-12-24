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


WireValues = dict[str, int]
AdjacencyList = dict[str, set[str]]
Degrees = dict[str, int]
Gate = NamedTuple(
    "Gate", [("input1", str), ("input2", str), ("fn", str), ("output", str)]
)
Board = NamedTuple(
    "InitialState", [("initial_values", WireValues), ("gates", dict[str, Gate])]
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
    """Parse inputs into initial value of wires and configuration of gates."""
    initial_values, gates = {}, {}
    i = 0

    # Read initial values
    while lines[i]:
        line = lines[i]
        wire, value = line[:3], int(line[5])
        initial_values[wire] = value
        i += 1

    i += 1

    # Read gates
    next_gate = 0

    while i + next_gate < len(lines):
        input1, fn, input2, _, output = lines[i + next_gate].split(" ")
        node_name = f"gate{str(next_gate).rjust(3, "0")}"
        gates[node_name] = Gate(input1, input2, fn, output)

        next_gate += 1

    return Board(initial_values, gates)


def build_adj_list(board: Board) -> tuple[AdjacencyList, Degrees]:
    """Construct adjacency list from the given board and count the in-degree of each node."""
    adj_list, in_degrees = defaultdict(set), defaultdict(int)

    for gate_name, gate in board.gates.items():
        adj_list[gate.input1].add(gate_name)
        adj_list[gate.input2].add(gate_name)
        adj_list[gate_name].add(gate.output)

        in_degrees[gate_name] = 2
        in_degrees[gate.output] += 1

    return (adj_list, in_degrees)


def find_values(board: Board) -> dict[str, int]:
    """Find values of wires on the board."""
    adj_list, in_degrees = build_adj_list(board)
    values = board.initial_values.copy()
    sources = list(board.initial_values.keys())

    while sources:
        new_sources = []

        for source in sources:
            # If source is a gate, calculate value for the output wire
            if source.startswith("gate"):
                gate = board.gates[source]
                gate_fn = GATE_FUNCTIONS[gate.fn]
                values[gate.output] = gate_fn(values[gate.input1], values[gate.input2])

            # Find downstream nodes with all dependencies resolved
            marked_for_removal = []

            for node in adj_list[source]:
                in_degrees[node] -= 1
                marked_for_removal.append(node)

                if in_degrees[node] == 0:
                    new_sources.append(node)

            for node in marked_for_removal:
                adj_list[source].remove(node)

        sources = new_sources

    return values


def construct_output_from_z_wires(values: WireValues) -> int:
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
    values = find_values(board)

    return construct_output_from_z_wires(values)


PARSER = inputs.parse_str_lines
PRINTER = str
