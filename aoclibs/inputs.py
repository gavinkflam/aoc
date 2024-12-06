"""Helper functions related to input manipulation."""

import re


INT_PATTERN = re.compile(r"\d+")


def parse_int_grid(content: str) -> list[list[int]]:
    """Parse the file content as a grid of integer values."""
    return [[int(s) for s in l.split()] for l in content.splitlines()]


def parse_int_grid_regexp(content: str) -> list[list[int]]:
    """Parse the file content as a grid of integer values using regular expression."""
    return [[int(s) for s in INT_PATTERN.findall(l)] for l in content.splitlines()]


def parse_str_lines(content: str) -> list[str]:
    """Parse the file content as lines of string."""
    return content.splitlines()
