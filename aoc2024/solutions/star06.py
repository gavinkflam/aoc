"""Solution for 2024 star 6.

Problem page:
    https://adventofcode.com/2024/day/3#part2

Solutions:
    1. Brute force
        - O(n * k * m) time, O(1) auxiliary space
            where m = types of instructions, k = maximum length of valid instruction
    2. Regular expression
        complexity depends on implementation and pattern complexity
    3. State machine, DFA / NFA
        - O(n) time, O(n) auxiliary space
            probably a fun challenge - may revisit and implement in the future
"""

import re

from aoclibs import inputs


PATTERN = re.compile(r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")


def run(lines: list[str]) -> int:
    """Sum the results of valid and enabled muplications."""
    answer = 0
    enabled = True

    for line in lines:
        for match in PATTERN.finditer(line):
            mul, x, y, do, dont = match.groups()

            if do:
                enabled = True
            elif dont:
                enabled = False
            elif mul and enabled:
                answer += int(x) * int(y)

    return answer


PARSER = inputs.parse_str_lines
PRINTER = str
