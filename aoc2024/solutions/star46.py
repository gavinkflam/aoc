"""Solution for 2024 star 46.

Problem page:
    https://adventofcode.com/2024/day/23#part2

Solutions:
    1. Backtracking
        - O(2^n * n^2) time, O(n + m) auxiliary space
            where n = number of computers,
                  m = number of pairs
    2. Better backtracking
        - O(n * 2^p * p^2) time, O(n + m) auxiliary space
            where p = maximum number of neighbors of a computer
    3. Growing groups
        - O(m * p^k * klogk) time, O(n + m) auxiliary space
            where k = number of computers in the largest interconnected group

Further research:
    This is the problem of finding the maximum clique, which is a NP-complete problem.
"""

from typing import NamedTuple

from aoc2024.solutions import star45
from aoc2024.solutions.star45 import AdjacencyList
from aoclibs.executions import SolutionModule


Group = NamedTuple("Group", [("leader", str), ("members", set[str])])


def build_group(adj_list: AdjacencyList, *members: str) -> tuple[str, Group]:
    """Build a group and designate the member with the least neighbors as the leader."""
    leader = None
    signature = ",".join(sorted(members))

    for member in members:
        if not leader or len(adj_list[member]) < len(adj_list[leader]):
            leader = member

    return (signature, Group(leader, set(members)))


def run(pairs: list[tuple[str, str]]) -> str:
    """Find the members of the largest interconnected group of computers."""
    adj_list = star45.build_adjacency_list(pairs)
    n = len(adj_list)

    # Find the largest group by growing the current largest groups by one member
    groups = dict(build_group(adj_list, *pair) for pair in pairs)

    for _ in range(3, n + 1):
        new_groups = {}

        for leader, members in groups.values():
            for candidate in adj_list[leader]:
                if candidate in members:
                    continue

                # A new member needs to be connected to all members of the group
                if all(candidate in adj_list[member] for member in members):
                    signature, new_group = build_group(adj_list, *members, candidate)
                    if signature not in new_groups:
                        new_groups[signature] = new_group

        # No larger groups can be found
        if not new_groups:
            break
        groups = new_groups

    return next(iter(groups))


solution = SolutionModule(run=run)
solution.parser = star45.solution.parser
