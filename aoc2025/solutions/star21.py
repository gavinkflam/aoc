"""Solution for 2025 star 21.

Problem page:
    https://adventofcode.com/2025/day/11

Solutions:
    1. Brute force, backtracking
        - O(n^n) time, O(n) auxiliary space,
            where n = number of devices
    2. BFS + topological sort
        - O(n + E) time, O(n + E) auxiliary space,
            where E = number of connections
"""

from typing import Optional
import re

from aoclibs.hofs import compose, mapf, re_splitf


def make_adjacency_list(devices: list[list[str]]) -> dict[str, list[int]]:
    """Make an adjacency list from the wirings."""
    adj_list = {}

    for wirings in devices:
        device, out_devices = wirings[0], wirings[1:]
        adj_list[device] = out_devices

    return adj_list


def find_in_degrees(
    adj_list: dict[str, list[int]], origin: str, excludes: Optional[set[str]] = None
) -> dict[str, int]:
    """Perform BFS to find the in-degrees of reachable devices, not in excludes, from origin."""
    queue = [origin]
    in_degrees = {}
    excludes = excludes if excludes is not None else {}

    while queue:
        new_queue = []

        for device in queue:
            if device not in adj_list:
                continue

            for out_device in adj_list[device]:
                if out_device in excludes:
                    continue

                in_degrees[out_device] = in_degrees.get(out_device, 0) + 1
                if in_degrees[out_device] > 1:
                    continue

                new_queue.append(out_device)

        queue = new_queue

    return in_degrees


def count_paths(
    adj_list: dict[str, list[str]], in_degrees: dict[str, int], origin: str, dest: str
) -> int:
    """Perform topological sort to count the number of paths from origin to dest."""
    queue, paths = [origin], {origin: 1}

    while queue:
        new_queue = []

        for device in queue:
            if device == dest:
                return paths[device]
            if device not in adj_list:
                continue

            for out_device in adj_list[device]:
                if out_device not in in_degrees:
                    continue

                in_degrees[out_device] -= 1
                paths[out_device] = paths.get(out_device, 0) + paths[device]

                if in_degrees[out_device] == 0:
                    new_queue.append(out_device)

        queue = new_queue

    return 0


def run(devices: list[list[str]]) -> int:
    """Find the number of paths from you to out."""
    adj_list = make_adjacency_list(devices)
    in_degrees = find_in_degrees(adj_list, "you")

    return count_paths(adj_list, in_degrees, "you", "out")


PARSER = compose(mapf(re_splitf(re.compile(r":?\s"))), str.splitlines)
PRINTER = str
