"""Solution for 2024 star 5.

Problem page:
    https://adventofcode.com/2024/day/3

Solutions:
    1. Brute force
        - O(n * k) time, O(1) auxiliary space
            where k = maximum length of valid instruction
    2. Regular expression
        - Remarks:
            Complexity depends on pattern and library implementation.
    3. State machine, DFA / NFA
        - O(n) time, O(n) auxiliary space
        - Remarks:
            Maybe later.
"""

import re

from aoclibs.executions import SolutionModule


PATTERN = re.compile(r"(mul)\((\d{1,3}),(\d{1,3})\)")


def run(lines: list[str]) -> int:
    """Sum the results of valid muplications."""
    answer = 0

    for line in lines:
        for match in PATTERN.finditer(line):
            _, x, y = match.groups()
            answer += int(x) * int(y)

    return answer


solution = SolutionModule(run=run)
solution.parser = str.splitlines
