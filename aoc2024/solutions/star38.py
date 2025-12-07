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
from aoc2024.solutions.star37 import Trie


def run(info: tuple[list[str], list[str]]) -> int:
    """Find the sum of the number of possible towel arrangements."""
    words, designs = info
    trie = Trie.from_words(words)

    # Count arrangements
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


PARSER = star37.PARSER
PRINTER = str
