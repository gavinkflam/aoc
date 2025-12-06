"""Version 2 composable helper functions to parse input files."""

from functools import reduce
from typing import Any, Callable, Pattern, Type


def compose(*functions: Callable) -> Callable[[str], Any]:
    """Compose the provided functions into a single function."""
    return lambda arg: reduce(lambda acc, f: f(acc), reversed(functions), arg)


def new_from_args(klass: Type) -> Callable[[list[Any]], Any]:
    """Return a function that accept a list, to make a new instance of klass."""
    return lambda arg: klass(*arg)


def mapf(fn: Callable) -> Callable[[Any], list[Any]]:
    """Return a function that accept a list, to apply fn to each element."""
    return lambda ls: [fn(x) for x in ls]


def splitf(sep: str, fn: Callable = str) -> Callable[[str], list[Any]]:
    """Return a function that accept a string, to split the string by sep and apply fn."""
    return lambda s: [fn(x) for x in s.split(sep)]


def re_splitf(
    pattern: Pattern, fn: Callable = str, remove_empty_elements=False
) -> Callable[[str], list[Any]]:
    """Return a function that accept a string, to split the string using pattern and apply fn."""
    return lambda s: [
        fn(x) for x in pattern.split(s) if not (remove_empty_elements and x == "")
    ]


def list_split(sep: Any) -> Callable[[Any], list[list[Any]]]:
    """Return a function that accept a list, to split it by sep."""

    def inner(ls: list[Any]) -> list[list[Any]]:
        parts, part = [[]], 0

        for e in ls:
            if e == sep:
                parts.append([])
                part += 1
            else:
                parts[-1].append(e)

        return parts

    return inner


def list_split_but_n(n: int) -> Callable[[Any], list[list[Any]]]:
    """Return a function that accept a list,
    to split it into two parts with the second part of length n."""
    return lambda ls: [ls[: len(ls) - n], ls[len(ls) - n :]]


def zip_applyf(*functions: Callable) -> Callable[[Any], list[list[Any]]]:
    """Return a function that accept a list,
    apply functions of the corresponding index to each element."""
    return lambda ls: [functions[i](x) for i, x in enumerate(ls)]
