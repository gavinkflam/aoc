"""Solution for 2024 star 38.

Problem page:
    https://adventofcode.com/2024/day/19#part2

Solutions:
    1. Brute force, backtracking
        - O(nmk) time, O(k) auxiliary space
            where n = number of designs to display
                  m = number of available towel patterns
                  k = maximum number of stripes in a design
    2. Trie + backtracking
        - O(mk + n * 2^k) time, O(mk) auxiliary space
    3. Trie + DP / memo
        - O(mk + n * k^2) time, O(mk + k) auxiliary space
"""

from aoc2024.solutions import star37
from aoclibs import inputs


def run(lines: list[str]) -> int:
    """Find the sum of the number of possible towel arrangements."""
    trie, designs = star37.parse_inputs(lines)
    arrangements = 0

    for design in designs:
        k = len(design)
        dp = [0] * (k + 1)
        dp[-1] = 1

        for left in range(k - 1, -1, -1):
            node = trie.root

            for right in range(left, k):
                ch = design[right]
                if ch not in node.children:
                    break

                node = node.children[ch]
                if node.is_word:
                    dp[left] += dp[right + 1]

        arrangements += dp[0]

    return arrangements


PARSER = inputs.parse_str_lines
PRINTER = str
