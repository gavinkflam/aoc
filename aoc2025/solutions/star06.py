"""Solution for 2025 star 6.

Problem page:
    https://adventofcode.com/2025/day/3#part2

Solutions:
    1. Brute force
        - O(m * n^k) time, O(1) auxiliary space,
            where m = number of lines,
                  n = length of each line,
                  k = length of selection
    2. Better brute force
        - O(m * k^2 * n) time, O(k) auxiliary space
    3. Linked list
        - O(mkn) time, O(k) auxiliary space
"""

from dataclasses import dataclass
from typing import Optional

from aoc2025.solutions import star05
from aoclibs.executions import SolutionModule


@dataclass
class ListNode:
    """A dataclass to represent a node of a singly linked list."""

    digit: int
    next: Optional["ListNode"] = None


def run(banks: list[list[int]]) -> int:
    """Find the sum of the maximum joltage possible from each bank."""
    ans = 0

    for bank in banks:
        n = len(bank)

        # Construct linked list
        pre_head = ListNode(-1)
        curr = pre_head

        for i in range(12):
            curr.next = ListNode(bank[i], None)
            curr = curr.next

        # Process the rest of the batteries and try to improve joltage
        tail = curr

        for i in range(12, n):
            curr, prev = pre_head.next, pre_head

            while curr:
                if curr.next and curr.digit < curr.next.digit:
                    prev.next = curr.next
                    tail.next = ListNode(bank[i], None)
                    tail = tail.next
                    break
                if not curr.next and curr.digit < bank[i]:
                    prev.next = tail = ListNode(bank[i], None)
                    break

                curr, prev = curr.next, curr

        # Calculate jolt of the selected batteries
        jolt = 0
        curr = pre_head.next

        while curr:
            jolt = jolt * 10 + curr.digit
            curr = curr.next

        ans += jolt

    return ans


solution = SolutionModule(run=run)
solution.parser = star05.solution.parser
