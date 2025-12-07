"""Solution for 2024 star 42.

Problem page:
    https://adventofcode.com/2024/day/21#part2

Solutions:
    1. Simulation
        - O(nk^m) time, O(k^m) auxiliary space
            where n = number of codes,
                  k = maximum length of code,
                  m = number of robots
    2. DP
        - O(m * p^2 + nk) time, O(m * p^2) auxiliary space
            where p = number of keys
    3. DP, optimized space
        - O(m * p^2 + nk) time, O(p^2) auxiliary space
"""

from collections import defaultdict

from aoc2024.solutions import star41


KEYS = star41.DPAD_COORDS.keys()
LAYERS = 25


def run(codes: list[str]) -> int:
    """Find the sum of complexity to enter each of the code."""
    sequences = defaultdict(dict)
    dp0, dp1 = defaultdict(dict), defaultdict(dict)

    # Find the move sequence between each key and initialize dp dictionaries
    for start in KEYS:
        for end in KEYS:
            sequence = star41.dpad_to_dpad(start, end)
            sequences[start][end] = sequence
            dp0[start][end] = 1
            dp1[start][end] = len(sequence)

    # Find number of key presses in each layer
    for _ in range(LAYERS - 1):
        dp2 = defaultdict(dict)

        for start in KEYS:
            for end in KEYS:
                dp2[start][end], prev = 0, "A"

                for curr in sequences[start][end]:
                    dp2[start][end] += dp1[prev][curr]
                    prev = curr

        dp0, dp1 = dp1, dp2

    # Find sum of code complexities
    complexity_sum = 0

    for code in codes:
        numeric_part = int(code[:-1])
        sequence_length, prev = 0, "A"

        for curr in star41.wrap_sequence(list(code), star41.numpad_to_dpad):
            sequence_length += dp2[prev][curr]
            prev = curr

        complexity_sum += numeric_part * sequence_length

    return complexity_sum


PARSER = str.splitlines
PRINTER = str
