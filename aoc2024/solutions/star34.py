"""Solution for 2024 star 34.

Problem page:
    https://adventofcode.com/2024/day/17#part2

Solutions:
    1. Interpreter + brute force
        - O(kn) time, O(p) auxiliary space
            where k = minimum value for the program to output itself,
                  p = number of outputs
    2. Interpreter + backtracking
        - O(t^p * n) time, O(p) auxiliary space
            where t = number of trials per block
"""

from typing import Optional

from aoc2024.solutions import star33
from aoc2024.solutions.star33 import Executable
from aoclibs.executions import SolutionModule


def run(executable: Executable) -> int:
    """Find the lowest value of register A for the program to output itself."""
    [_, b, c], program = executable

    def outputs_match(outputs_buffer: list[int], lo: int) -> bool:
        for i, val in enumerate(outputs_buffer):
            if val != program[lo + i]:
                return False
        return True

    def backtrack(a: int, lo: int) -> Optional[int]:
        if lo == -1:
            return a

        for inc in range(32768):
            try_a = (a << 3) + inc
            outputs_buffer = star33.run(([try_a, b, c], program))

            if outputs_match(outputs_buffer, lo):
                answer = backtrack(try_a, lo - 1)
                if answer is not None:
                    return answer

        return None

    return backtrack(0, len(program) - 1)


solution = SolutionModule(run=run)
solution.parser = star33.solution.parser
