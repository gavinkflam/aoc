"""Helper functions related to input manipulation."""


def parse_int_grid(content: str) -> list[list[int]]:
    """Parse the file content as a grid of integer values."""
    return [[int(s) for s in l.split()] for l in content.splitlines()]


def parse_str_lines(content: str) -> list[str]:
    """Parse the file content as lines of string."""
    return content.splitlines()
