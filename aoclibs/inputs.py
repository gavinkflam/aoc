"""Helper functions to parse input file."""

import re


INT_PATTERN = re.compile(r"-?\d+")


def parse_int_grid(content: str) -> list[list[int]]:
    """Parse the file content as a grid of integer values."""
    return [[int(s) for s in l.split()] for l in content.splitlines()]


def parse_int_grid_regexp(content: str) -> list[list[int]]:
    """Parse the file content as a grid of integer values using regular expression."""
    return [[int(s) for s in INT_PATTERN.findall(l)] for l in content.splitlines()]


def parse_int_line(content: str) -> list[int]:
    """Parse the file content as a line of integer values."""
    return [int(s) for s in content.split()]


def parse_digit_grid(content: str) -> list[list[int]]:
    """Parse the file content as a grid of digits."""
    return [[int(ch) for ch in l] for l in content.splitlines()]


def parse_digit_list(content: str) -> list[int]:
    """Parse the file content as a list of digits."""
    return [int(ch) for ch in content]


def parse_str_line(content: str, sep: str = ",") -> list[str]:
    """Parse the file content as a single line of string separated by the provided separator."""
    return content.split(sep)


def parse_str_lines(content: str) -> list[str]:
    """Parse the file content as lines of string."""
    return content.splitlines()


def parse_char_grid(content: str) -> list[list[str]]:
    """Parse the file content as a grid of character values."""
    return [list(l) for l in content.splitlines()]
