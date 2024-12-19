"""Solution for 2024 star 37.

Problem page:
    https://adventofcode.com/2024/day/19

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

from dataclasses import dataclass, field

from aoclibs import inputs


@dataclass
class TrieNode:
    """A node in the trie to represent a substring and/or a word."""

    is_word: bool = False
    children: dict[str, "TrieNode"] = field(default_factory=dict)


@dataclass
class Trie:
    """A trie to store and search words efficiently."""

    root: TrieNode = field(default_factory=TrieNode)

    @classmethod
    def from_words(cls, words: list[str]) -> "Trie":
        """Construct a trie from a list of words."""
        trie = Trie()
        for towel in words:
            trie.add(towel)
        return trie

    def add(self, word: str) -> None:
        """Add the given word to the trie."""
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_word = True


def parse_inputs(lines: list[str]) -> tuple[Trie, list[str]]:
    """Return available towels in as a trie and the list of desired designs."""
    trie = Trie.from_words(lines[0].split(", "))
    designs = lines[2:]
    return (trie, designs)


def is_possible(trie: Trie, design: str) -> bool:
    """Determine is the design possible with the available towels."""
    k = len(design)
    dp = [True] * (k + 1)

    def is_possible_from(left: int) -> bool:
        node = trie.root

        for right in range(left, k):
            ch = design[right]
            if ch not in node.children:
                return False

            node = node.children[ch]
            if node.is_word and dp[right + 1]:
                return True

        return False

    for left in range(k - 1, -1, -1):
        dp[left] = is_possible_from(left)

    return dp[0]


def run(lines: list[str]) -> int:
    """Find the number of possible designs."""
    trie, designs = parse_inputs(lines)
    possible_designs = 0

    for design in designs:
        if is_possible(trie, design):
            possible_designs += 1

    return possible_designs


PARSER = inputs.parse_str_lines
PRINTER = str
