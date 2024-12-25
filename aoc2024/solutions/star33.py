"""Solution for 2024 star 33.

Problem page:
    https://adventofcode.com/2024/day/17

Solutions:
    1. Interpreter
        - O(n) time, O(1) auxiliary space
"""

from aoclibs import inputs, outputs


Executable = tuple[int, int, int, list[int]]
ADV, BXL, BST, JNZ, BXC, OUT, BDV, CDV = range(8)
LITERAL_0, LITERAL_1, LITERAL_2, LITERAL_3 = range(4)
COMBO_REG_A, COMBO_REG_B, COMBO_REG_C, RESERVED = range(4, 8)


def parse_input(lists: list[list[int]]) -> Executable:
    """Extract register values and program from the inputs."""
    a, b, c = lists[0][0], lists[1][0], lists[2][0]
    program = lists[4]
    return (a, b, c, program)


def interpret_program(executable: Executable) -> list[str]:
    """Interpret the given program and derive its outputs."""
    a, b, c, program = executable
    ip, n, outputs_buffer = 0, len(program), []

    def combo_value(operand: int) -> int:
        if LITERAL_0 <= operand <= LITERAL_3:
            return operand
        if operand == COMBO_REG_A:
            return a
        if operand == COMBO_REG_B:
            return b
        if operand == COMBO_REG_C:
            return c

        raise ValueError(f"Combo operand {operand} is not valid")

    while ip < n:
        if program[ip] == ADV:
            a = a // (1 << combo_value(program[ip + 1]))
        elif program[ip] == BXL:
            b = b ^ program[ip + 1]
        elif program[ip] == BST:
            b = combo_value(program[ip + 1]) % 8
        elif program[ip] == JNZ:
            if a != 0:
                ip = program[ip + 1]
                continue
        elif program[ip] == BXC:
            b = b ^ c
        elif program[ip] == OUT:
            outputs_buffer.append(combo_value(program[ip + 1]) % 8)
        elif program[ip] == BDV:
            b = a // (1 << combo_value(program[ip + 1]))
        elif program[ip] == CDV:
            c = a // (1 << combo_value(program[ip + 1]))

        ip += 2

    return outputs_buffer


def run(lists: list[list[int]]) -> list[str]:
    """Interpret the given program and derive its outputs."""
    executable = parse_input(lists)
    return interpret_program(executable)


PARSER = inputs.parse_int_grid_regexp
PRINTER = outputs.stringify_list
