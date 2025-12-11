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

import re

from aoclibs.hofs import compose, mapf, re_splitf


def make_adjacency_list(devices: list[list[str]]) -> dict[str, list[int]]:
    """Make an adjacency list from the wirings."""
    adj_list = {}

    for wirings in devices:
        device, out_devices = wirings[0], wirings[1:]
        adj_list[device] = out_devices

    return adj_list


def find_in_degrees(adj_list: dict[str, list[int]], origin: str) -> dict[str, int]:
    """Perform BFS to find all the reachable devices from origin and their in-degrees."""
    queue = [origin]
    in_degrees = {}

    while queue:
        new_queue = []

        for device in queue:
            for out_device in adj_list.get(device, []):
                in_degrees[out_device] = in_degrees.get(out_device, 0) + 1

                if in_degrees[out_device] > 1:
                    continue
                new_queue.append(out_device)

        queue = new_queue

    return in_degrees


def run(devices: list[list[str]]) -> int:
    """Find the number of paths from you to out."""
    adj_list = make_adjacency_list(devices)
    in_degrees = find_in_degrees(adj_list, "you")

    # Topological sort
    queue, paths = ["you"], {"you": 1}

    while queue:
        new_queue = []

        for device in queue:
            if device == "out":
                return paths[device]

            for out_device in adj_list[device]:
                if out_device not in in_degrees:
                    continue

                in_degrees[out_device] -= 1
                paths[out_device] = paths.get(out_device, 0) + paths[device]

                if in_degrees[out_device] == 0:
                    new_queue.append(out_device)

        queue = new_queue

    return 0


PARSER = compose(mapf(re_splitf(re.compile(r":?\s"))), str.splitlines)
PRINTER = str
