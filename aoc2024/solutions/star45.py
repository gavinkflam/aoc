"""Solution for 2024 star 45.

Problem page:
    https://adventofcode.com/2024/day/23

Solutions:
    1. Brute force
        - O(n * p^2 + m) time, O(n + m) auxiliary space
            where n = number of computers,
                  m = number of pairs,
                  p = maximum number of neighbors of a computer
"""

from collections import defaultdict

from aoclibs import inputs


def split_pairs(lines: list[str]) -> list[tuple[str, str]]:
    """Split each line into a pair of computer."""
    return [tuple(line.split("-")) for line in lines]


def run(lines: list[str]) -> int:
    """Find the number of three-computer groups with a member's name starting with t."""
    pairs = split_pairs(lines)

    # Construct adjacency list
    adj_list = defaultdict(set)

    for u, v in pairs:
        adj_list[u].add(v)
        adj_list[v].add(u)

    # Find groups satisfying the requirements
    good_groups = 0

    for u, neighbors in adj_list.items():
        neighbors_list = list(neighbors)

        for i in range(len(neighbors_list) - 1):
            v = neighbors_list[i]

            for j in range(i + 1, len(neighbors_list)):
                w = neighbors_list[j]
                if w in adj_list[v] and any(c[0] == "t" for c in [u, v, w]):
                    good_groups += 1

            neighbors.remove(v)
            adj_list[v].remove(u)

    return good_groups


PARSER = inputs.parse_str_lines
PRINTER = str
