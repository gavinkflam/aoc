"""Version 2 composable helper functions to parse input files."""

from functools import reduce
from typing import Any, Callable, Type


def compose(*functions: Callable) -> Callable[[str], Any]:
    """Compose the provided functions into a single function."""
    return lambda arg: reduce(lambda acc, f: f(acc), reversed(functions), arg)


def new_from_args(klass: Type) -> Callable[[list[Any]], Any]:
    """Make a new instance of the provided class from a list of arguments."""
    return lambda arg: klass(*arg)


def mapf(function: Callable) -> Callable[[Any], list[Any]]:
    """Process each element with the provided function."""
    return lambda elements: [function(element) for element in elements]


def splitf(
    delimiter: str = ",", function: Callable = str
) -> Callable[[str], list[Any]]:
    """Process each part separated by a delimiter using the provided function."""

    def inner(s: str) -> list[Any]:
        return [function(p) for p in s.split(delimiter)]

    return inner


def split_zip_applyf(
    delimiter: Any, *functions: Callable
) -> Callable[[Any], list[list[Any]]]:
    """Parse a multi-part list separated by the specified delimiter using the provided functions."""

    def inner(elements: list[Any]) -> list[list[Any]]:
        parts, part = [[]], 0

        for element in elements:
            if element == delimiter:
                parts.append([])
                part += 1
            else:
                parts[-1].append(functions[part](element))

        return parts

    return inner
