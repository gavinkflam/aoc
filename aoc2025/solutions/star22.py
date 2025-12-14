"""Solution for 2025 star 22.

Problem page:
    https://adventofcode.com/2025/day/11#part2

Solutions:
    1. Brute force, backtracking
        - O(n^n) time, O(n) auxiliary space,
            where n = number of devices
    2. BFS + topological sort
        - O(n + E) time, O(n + E) auxiliary space,
            where E = number of connections
"""

from aoc2025.solutions import star21


def run(devices: list[list[str]]) -> int:
    """Find the number of paths from svr to out via both fft and dac."""
    adj_list = star21.make_adjacency_list(devices)

    def count_paths_exclude_devices(excludes: set[str]) -> int:
        in_degrees = star21.find_in_degrees(adj_list, "svr", excludes=excludes)
        return star21.count_paths(adj_list, in_degrees, "svr", "out")

    return (
        count_paths_exclude_devices({})
        - count_paths_exclude_devices({"fft"})
        - count_paths_exclude_devices({"dac"})
        + count_paths_exclude_devices({"fft", "dac"})
    )


PARSER = star21.PARSER
PRINTER = str
