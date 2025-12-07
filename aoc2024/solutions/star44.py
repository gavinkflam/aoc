"""Solution for 2024 star 44.

Problem page:
    https://adventofcode.com/2024/day/22#part2

Solutions:
    1. Brute force, backtracking
        - O(19^4 * nk) time, O(1) auxiliary space
            where n = number of secrets,
                  k = number of generations
    2. Hash map + hash set
        - O(nk), O(nk) auxiliary space
"""

from collections import defaultdict, deque

from aoc2024.solutions import star43


def hash_key(sequence: list[int]) -> int:
    """Generate a hash key for the given sequence."""
    hkey = 0
    for diff in sequence:
        hkey = (hkey << 5) + (diff + 9)
    return hkey


def run(secrets: list[int]) -> int:
    """Find the most bananas that is possible to get."""
    bananas = defaultdict(int)
    max_bananas = 0

    for secret in secrets:
        sequence, seen = deque([]), set()
        prev = secret

        for _ in range(2000):
            curr = star43.evolve(prev)
            sequence.append(curr % 10 - prev % 10)

            if len(sequence) == 5:
                sequence.popleft()

            if len(sequence) == 4:
                hkey = hash_key(sequence)
                if hkey not in seen:
                    seen.add(hkey)
                    bananas[hkey] += curr % 10
                    max_bananas = max(max_bananas, bananas[hkey])

            prev = curr

    return max_bananas


PARSER = star43.PARSER
PRINTER = str
